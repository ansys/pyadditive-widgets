:orphan:

.. _ref_getting_started:

###############
Getting started
###############

This section describes how to install PyAdditive-Widgets in user mode and quickly begin
using it. If you are interested in contributing to PyAdditive-Widgets, see :ref:`contribute`
for information on installing in developer mode.

.. _prerequisites:

Prerequisites
=============

The use of PyAdditive-Widgets requires the installation of a licensed copy of Ansys 2024 R1
or later and PyAdditive 0.17.2 or later.

The `PyAdditive`_ simulations described in this documentation also require a license for the
`Ansys Additive Suite <https://www.ansys.com/products/additive/ansys-additive-suite>`_.
To obtain a license, contact your Ansys sales representative or complete this
`inquiry form <https://www.ansys.com/contact-us>`_.

.. _package_dependencies:

Package dependencies
====================

PyAdditive-Widgets is supported on Python version 3.9 and later. Previous versions of Python are
no longer supported as outlined on the `History <https://python3statement.github.io/>`_ page
describing the transition from Python 2 to Python 3.

PyAdditive-Widgets dependencies are automatically checked when packages are installed. Included
in these dependencies are these projects:

* `ansys-additive-core <https://pypi.org/project/ansys-additive-core/>`_: PyAdditive is a Python
  client library for the `Ansys Additive`_ service.
* `Panel <https://panel.holoviz.org/>`_: A web app framework for Python that is used for interactive
   visualization of PyAdditive results.

Install the package
===================

#. Before installing PyAdditive-Widgets, make sure that you
   have the latest version of `pip`_ by running this command::

   .. code:: bash

       python -m pip install -U pip

#. Install PyAdditive-Widgets by running this command:

   .. code:: bash

       python -m pip install ansys-additive-widgets


Start a session
===============

You can start a session with the PyAdditive client in multiple ways. For example,
you can start a local session or a remote session. Also, before you can visualize
the results of a parametric additive simulation, you must instantiate a parametric study.

.. _ref_starting_a_local_session:

Start a local session
---------------------

Instantiating an ``Additive`` object starts the local installation of the Additive server:

.. code:: python

   import ansys.additive.core as pyadditive
   from ansys.additive.core.parametric_study import ParametricStudy
   from ansys.additive.widgets import display

   study = ParametricStudy("demo-study")

   # Display the empty study as a table
   display.show_table(study)

Start a remote session
----------------------

You start a remote session by specifying the host name and port of the server:

.. code:: python

   import ansys.additive.core as pyadditive
   from ansys.additive.core.parametric_study import ParametricStudy
   from ansys.additive.widgets import display

   additive = pyadditive.Additive(host="additiveserver.mydomain.com", port=12345)
   study = ParametricStudy("demo-study")

   # Display the empty study as a table
   display.show_table(study)


Use alternative startup methods
-------------------------------

The ``Additive`` class in the PyAdditive API provides additional session
startup methods that you can use. For more information, see
`Additive <https://additive.docs.pyansys.com/version/stable/api/ansys/additive/core/additive/Additive.html>`_
in the PyAdditive documentation.


Run simulations
===============
Once a session is started, you can run simulations.

Basic usage
-----------

This code shows how to import PyAdditive-Widgets and use some basic capabilities
to visualize the `PyAdditive`_-generated results of a parametric study as a table:

.. code:: python

   from ansys.additive.core.parametric_study import ParametricStudy
   from ansys.additive.widgets import display

   study = ParametricStudy("demo-study")

   bead_length = 0.005
   powers = [50, 250, 700]
   scan_speeds = [0.35, 1, 2.4]
   layer_thicknesses = [30e-6, 50e-6]
   heater_temperatures = [80, 100]
   beam_diameters = [2e-5]

   study.generate_single_bead_permutations(
      "material",
      powers,
      scan_speeds,
      bead_length=bead_length,
      layer_thicknesses=layer_thicknesses,
      heater_temperatures=heater_temperatures,
      beam_diameters=beam_diameters,
   )

   # Display the study as a table with the generated single bead simulations
   display.show_table(study)

Advanced usage
--------------

The `Examples`_ section provides comprehensive usage information.
For information on how to use PyAdditive for the `Ansys Additive`_ service,
see the `PyAdditive documentation`_.

.. LINKS AND REFERENCES
.. _black: https://github.com/psf/black
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _isort: https://github.com/PyCQA/isort
.. _pip: https://pypi.org/project/pip/
.. _pre-commit: https://pre-commit.com/
.. _PyAnsys Developer's guide: https://dev.docs.pyansys.com/
.. _pytest: https://docs.pytest.org/en/stable/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _tox: https://tox.wiki/
.. _Ansys Additive: https://www.ansys.com/products/additive
.. _PyAdditive: https://additive.docs.pyansys.com/version/stable/index.html
.. _PyAdditive documentation: https://additive.docs.pyansys.com/version/stable/index.html
.. _PyAdditive Getting Started: https://additive.docs.pyansys.com/version/stable/getting_started/index.html
.. _PyAdditive-Widgets documentation: https://widgets.additive.docs.pyansys.com/version/stable/index.html
.. _Contributing to PyAdditive-Widgets: https://widgets.additive.docs.pyansys.com/version/stable/contributing.html
.. _Examples: https://widgets.additive.docs.pyansys.com/version/stable/examples/gallery_examples/index.html