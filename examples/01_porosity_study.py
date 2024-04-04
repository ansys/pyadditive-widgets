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
Porosity parametric study
=========================

This example shows how you can use PyAdditive-Wdigets to visualize the results
of a parametric study containing porosity simulations.
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

study = ParametricStudy("porosity-study")

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
# Create a porosity evaluation
# ----------------------------
# You can generate a set of porosity simulations using the
# :meth:`~ParametricStudy.generate_porosity_permutations` method. The parameters
# for the :meth:`~ParametricStudy.generate_porosity_permutations` method allow you to
# specify the material and machine parameters for the simulations. Not all
# parameters are required. Optional parameters that are not specified use default
# values defined in the :class:`MachineConstants` class.

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
min_build_rate = 5e-9

study.generate_porosity_permutations(
    material_name=material,
    laser_powers=laser_powers,
    scan_speeds=scan_speeds,
    size_x=1e-3,
    size_y=1e-3,
    size_z=1e-3,
    layer_thicknesses=layer_thicknesses,
    heater_temperatures=heater_temperatures,
    beam_diameters=beam_diameters,
    start_angles=start_angles,
    rotation_angles=rotation_angles,
    hatch_spacings=hatch_spacings,
    min_build_rate=min_build_rate,
    iteration=1,
)

###############################################################################
# Show the simulations as a table
# -------------------------------
# You can use the :obj:`display <ansys.additive.widgets.display>`
# package to list the simulations as a table.

display.show_table(study)

################################################################################
# Run porosity simulations
# ------------------------
# Run the simulations using the :meth:`~ParametricStudy.run_simulations` method.

study.run_simulations(additive)

###############################################################################
# Plot porosity results
# ---------------------
# Visualize porosity simulation results for relative density and build rate
# as a contour plot using the
# :func:`~ansys.additive.widgets.display.porosity_contour_plot` method.

display.porosity_contour_plot(study)

###############################################################################
# Visualize a heat map plot of porosity results to determine parametric regions
# with desirable relative density statistics using the
# :func:`~ansys.additive.widgets.display.porosity_eval_plot` method.

display.porosity_eval_plot(study)
