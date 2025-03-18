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
Single bead evaluation plot
===========================

This example shows how to use PyAdditive-Widgets to visualize the results
of a parametric study containing single bead simulations.
It uses the :obj:`display <ansys.additive.widgets.display>` package to
visualize the results of the study.

Units are SI (m, kg, s, K) unless otherwise noted.
"""
###############################################################################
# Perform required imports
# ------------------------
# Perform the required imports.

from ansys.additive.core import Additive, SimulationStatus, SimulationType
from ansys.additive.core.parametric_study import ColumnNames, ParametricStudy
import numpy as np

from ansys.additive.widgets import display

###############################################################################
# Select material for study
# -------------------------
# Each parametric study uses a single material. The material name must be known
# by the Additive service. You can connect to the Additive service
# and print a list of available materials prior to selecting one.

additive = Additive(host="localhost")
additive.materials_list()
material = "IN718"

###############################################################################
# Create parametric study
# -----------------------
# Create a parametric study object using the :class:`Parametric
# Study <ansys.additive.core.parametric_study.ParametricStudy>` class.

study = ParametricStudy("single-bead-study", material)

###############################################################################
# Get name of study file
# ----------------------
# The current state of the parametric study is saved to a file on each
# update. The following code retrieves the name of the file. This file
# uses a binary format and is not human readable.

print(study.file_name)

###############################################################################
# Create single bead evaluation
# -----------------------------
# Generate single bead simulation permutations using the
# :meth:`~ParametricStudy.generate_single_bead_permutations` method. This method's
# parameters allow you to specify a range of machine parameters and filter them by
# energy density. Not all the parameters shown are required. Optional parameters
# that are not specified use the default values defined in the
# :class:`MachineConstants` class.

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
min_pv_ratio = 50
max_pv_ratio = 1500
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
# Use the :obj:`display <ansys.additive.widgets.display>`
# package to list the simulations as a table.

display.show_table(study)

###############################################################################
# Skip some simulations
# ---------------------
# If you are working with a large parametric study, you might want to skip some
# simulations to reduce processing time. To do so, set the simulation status,
# which is defined in the :class:`SimulationStatus` class, to :obj:`SimulationStatus.SKIP`.
# The following code obtains a :class:`~pandas.DataFrame` object, applies a filter to
# get a list of simulation IDs, and then updates the status on the simulations
# with those IDs.

df = study.data_frame()
# Get IDs for single bead simulations with laser power below 75 W.
ids = df.loc[
    (df[ColumnNames.LASER_POWER] < 75) & (df[ColumnNames.TYPE] == SimulationType.SINGLE_BEAD),
    ColumnNames.ID,
].tolist()
study.set_simulation_status(ids, SimulationStatus.SKIP)
display.show_table(study)

###############################################################################
# Run study
# ---------
# Run the simulations using the :meth:`~Additive.simulate_study` method.
# All simulations with a :obj:`SimulationStatus.PENDING` status are executed.

additive.simulate_study(study)

###############################################################################
# Plot single bead results
# ------------------------
# Plot the single bead results using the
# :func:`~ansys.additive.widgets.display.single_bead_eval_plot` function.

display.single_bead_eval_plot(study)
