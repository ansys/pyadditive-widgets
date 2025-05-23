# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
Parametric study
================

This example shows how to use PyAdditive to perform a parametric study.
You perform a parametric study if you want to optimize additive machine parameters
to achieve a specific result. This examples first uses the :class:`ParametricStudy`
class to perform the parametric study. It then uses the :obj:`display <ansys.additive.widgets.display>`
package in PyAdditive-Widgets to visualize the results of the study.

Units are SI (m, kg, s, K) unless otherwise noted.
"""

###############################################################################
# Perform required imports and create study
# -----------------------------------------
# Perform the required imports and create a :class:`ParametricStudy` instance.

from ansys.additive.core import Additive, SimulationType
from ansys.additive.core.parametric_study import ColumnNames, ParametricStudy
import numpy as np

from ansys.additive.widgets import display

###############################################################################
# Select material for study
# -------------------------
# Select a material to use in the study. The material name must be known by
# the Additive service. You can connect to the Additive service
# and print a list of available materials prior to selecting one.

additive = Additive()
print("Available material names: {}".format(additive.materials_list()))
material = "IN718"

###############################################################################
# Create parametric study
# -----------------------
# Create a parametric study object using the :class:`Parametric
# Study <ansys.additive.core.parametric_study.ParametricStudy>` class.

study = ParametricStudy("demo-study", material)

###############################################################################
# Get name of study file
# ----------------------
# The current state of the parametric study is saved to a file upon each
# update. This code retrieves the name of the file. This file
# uses a binary format and is not human readable.

print(study.file_name)

###############################################################################
# Create single bead evaluation
# -----------------------------
# Parametric studies often start with single bead simulations to determine melt
# pool statistics. The following code uses the :meth:`~ParametricStudy.generate_single_bead_permutations`
# method to generate single bead simulation permutations. This method's parameters
# allow you to specify a range of machine parameters and filter them by energy density.
# Not all of the parameters listed are required. Optional parameters that are not specified
# use the default values defined in the :class:`MachineConstants` class.

# Specify a range of laser powers. Valid values are 50 to 700 W.
initial_powers = np.linspace(50, 700, 7)
# Specify a range of laser scan speeds. Valid values are 0.35 to 2.5 m/s.
initial_scan_speeds = np.linspace(0.35, 2.5, 5)
# Specify powder layer thicknesses. Valid values are 10e-6 to 100e-6 m.
initial_layer_thicknesses = [40e-6, 50e-6]
# Specify laser beam diameters. Valid values are 20e-6 to 140e-6 m.
initial_beam_diameters = [80e-6]
# Specify heater temperatures. Valid values are 20 - 500 C.
initial_heater_temps = [80]
# Restrict the permutations within a range of laser power/velocity
# (a.k.a. scan speed) ratios.
min_pv_ratio = 200
max_pv_ratio = 1000
# Specify a bead length in meters.
bead_length = 0.001

study.generate_single_bead_permutations(
    bead_length=bead_length,
    laser_powers=initial_powers,
    scan_speeds=initial_scan_speeds,
    layer_thicknesses=initial_layer_thicknesses,
    beam_diameters=initial_beam_diameters,
    heater_temperatures=initial_heater_temps,
    min_pv_ratio=min_pv_ratio,
    max_pv_ratio=max_pv_ratio,
)

###############################################################################
# Show simulations as a table
# ---------------------------
# You can use the :obj:`display <ansys.additive.core.parametric_study.display>`
# package to list the simulations as a table.

display.show_table(study)

###############################################################################
# Run study
# ---------
# Run the simulations using the :meth:`~Additive.simulate_study` method.
# All simulations with a :obj:`SimulationStatus.PENDING` status are executed.

additive.simulate_study(study)

###############################################################################
# Save study to CSV file
# ----------------------
# The parametric study is saved with each update in a binary format.
# For other formats, use the ``to_*`` methods provided by the :class:`~pandas.DataFrame` class.

study.data_frame().to_csv("demo-study.csv")

###############################################################################
# Plot single bead results
# ------------------------
# Plot the single bead results using the
# :func:`~ansys.additive.widgets.display.single_bead_eval_plot` function.

display.single_bead_eval_plot(study)

###############################################################################
# Create porosity evaluation
# --------------------------
# You can use the insights gained from the single bead evaluation to
# generate parameters for a porosity evaluation. Alternatively, you can
# perform a porosity evaluation without a previous single bead evaluation.
# The following code determines the laser power and scan speeds by filtering the
# single bead results, where the ratio of the melt pool reference depth
# to reference width is within a specified range. Then, it uses the
# :meth:`~ParametricStudy.generate_porosity_permutations` method to
# add porosity simulations to the study, further restricting the permutations
# by specifying the minimum build rate, which is equal to the layer thickness
# times the scan speed times the hatch spacing in m^3/s.

df = study.data_frame()
df = df[
    (df[ColumnNames.MELT_POOL_REFERENCE_DEPTH_OVER_WIDTH] >= 0.6)
    & (df[ColumnNames.MELT_POOL_REFERENCE_DEPTH_OVER_WIDTH] <= 1.0)
]

study.generate_porosity_permutations(
    laser_powers=df[ColumnNames.LASER_POWER].unique(),
    scan_speeds=df[ColumnNames.SCAN_SPEED].unique(),
    size_x=1e-3,
    size_y=1e-3,
    size_z=1e-3,
    layer_thicknesses=[40e-6],
    heater_temperatures=[80],
    beam_diameters=[80e-6],
    start_angles=[45],
    rotation_angles=[67.5],
    hatch_spacings=[100e-6],
    min_build_rate=4e-9,
    iteration=1,
)

###############################################################################
# Run study
# ---------
# Run the simulations using the :meth:`~Additive.simulate_study` method.
# All simulations with a :obj:`SimulationStatus.PENDING` status are executed.

additive.simulate_study(study)

###############################################################################
# Plot porosity results
# ---------------------
# Plot the porosity simulation results using the
# :func:`~ansys.additive.widgets.display.porosity_contour_plot` method.

display.porosity_contour_plot(study)

###############################################################################
# Create microstructure evaluation
# --------------------------------
# The following code generates a set of microstructure simulations using many of the same
# parameters used for the porosity simulations. The code then uses the
# :meth:`~ParametricStudy.generate_microstructure_permutations` method to add
# microstructure simulations to the study. Because the ``cooling_rate``,
# ``thermal_gradient``, ``melt_pool_width``, and ``melt_pool_depth`` parameters
# are not specified, they are calculated when the simulations are run.

df = study.data_frame()
df = df[(df[ColumnNames.TYPE] == SimulationType.POROSITY)]

study.generate_microstructure_permutations(
    laser_powers=df[ColumnNames.LASER_POWER].unique(),
    scan_speeds=df[ColumnNames.SCAN_SPEED].unique(),
    size_x=1e-3,
    size_y=1e-3,
    size_z=1.1e-3,
    sensor_dimension=1e-4,
    layer_thicknesses=[40e-6],
    heater_temperatures=df[ColumnNames.HEATER_TEMPERATURE].unique(),
    beam_diameters=df[ColumnNames.BEAM_DIAMETER].unique(),
    start_angles=df[ColumnNames.START_ANGLE].unique(),
    rotation_angles=df[ColumnNames.ROTATION_ANGLE].unique(),
    hatch_spacings=df[ColumnNames.HATCH_SPACING].unique(),
    iteration=2,
)

###############################################################################
# Run study
# ---------
# Run the simulations using the :meth:`~Additive.simulate_study` method.
# All simulations with a :obj:`SimulationStatus.PENDING` status are executed.

additive.simulate_study(study)

###############################################################################
# Plot microstructure results
# ---------------------------
# Plot and compare the average grain sizes from the microstructure simulations
# using the :func:`~ansys.additive.widgets.display.ave_grain_size_plot`
# function.

display.ave_grain_size_plot(study)
