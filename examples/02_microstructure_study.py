# Copyright (C) 2024 ANSYS, Inc. and/or its affiliates.
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
Microstructure parametric study
===============================

This example shows how you can use PyAdditive-Wdigets to visualize the results
of a parametric study containing microstructure simulations.
Here, the :class:`ParametricStudy` class is used to conduct a parametric study.
While not essential, the :class:`ParametricStudy` class provides data management
and visualization features that make the work easier.
The :obj:`display <ansys.additive.widgets.display>` package is used to
visualize the results of the study.

Units are SI (m, kg, s, K) unless otherwise noted.
"""
###############################################################################
# Perform required imports and create a study
# -------------------------------------------
# Perform the required import and create a :class:`ParametricStudy` instance.
from ansys.additive.core import Additive
from ansys.additive.core.parametric_study import ParametricStudy

from ansys.additive.widgets import display

study = ParametricStudy("microstructure-study")

###############################################################################
# Get the study file name
# -----------------------
# The current state of the parametric study is saved to a file upon each
# update. You can retrieve the name of the file as shown below. This file
# uses a binary format and is not human readable.

print(study.file_name)

###############################################################################
# Select a material for the study
# -------------------------------
# Select a material to use in the study. The material name must be known by
# the Additive service. You can connect to the Additive service
# and print a list of available materials prior to selecting one.

additive = Additive()
additive.materials_list()
material = "IN718"

###############################################################################
# Create a microstructure evaluation
# ----------------------------------
# Here a set of microstructure simulations is generated using many of the same
# parameters used for the porosity simulations in the previous example.
# The parameters ``cooling_rate``, ``thermal_gradient``, ``melt_pool_width``,
# and ``melt_pool_depth`` are not specified so they are calculated. The
# :meth:`~ParametricStudy.generate_microstructure_permutations` method is used to add
# microstructure simulations to the study.

# Specify a range of laser powers. Valid values are 50 to 700 W.
laser_powers = [50, 150, 250, 350, 550]
# Specify a range of laser scan speeds. Valid values are 0.35 to 2.5 m/s.
scan_speeds = [0.35, 0.5, 0.7]
# Specify a range of layer thicknesses. Valid values are 10-6 to 100e-6 m.
layer_thicknesses = [40e-6]
# Specify a range of heater temperatures. Valid values 20 - 500 C.
heater_temperatures = [80]
# Specify laser beam diameters. Valid values are 20e-6 to 140e-6 m.
beam_diameters = [80e-6]
# Specify the machine parameters for the simulations.
start_angles = [45]
rotation_angles = [67.5]
hatch_spacings = [100e-6]

study.generate_microstructure_permutations(
    material_name=material,
    laser_powers=laser_powers,
    scan_speeds=scan_speeds,
    size_x=1e-3,
    size_y=1e-3,
    size_z=1.1e-3,
    sensor_dimension=1e-4,
    layer_thicknesses=layer_thicknesses,
    heater_temperatures=heater_temperatures,
    beam_diameters=beam_diameters,
    start_angles=start_angles,
    rotation_angles=rotation_angles,
    hatch_spacings=hatch_spacings,
    iteration=2,
)

###############################################################################
# Show the simulations as a table
# -------------------------------
# You can use the :obj:`display <ansys.additive.widgets.display>`
# package to list the simulations as a table.

display.show_table(study)

###############################################################################
# Run microstructure simulations
# ------------------------------
# Run the simulations using the :meth:`~ParametricStudy.run_simulations` method.

study.run_simulations(additive)

###############################################################################
# Plot microstructure results
# ---------------------------
# Plot and compare the average grain sizes from the microstructure simulations
# using the :func:`~ansys.additive.widgets.display.ave_grain_size_plot`
# method.

display.ave_grain_size_plot(study)
