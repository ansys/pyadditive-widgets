.. _ref_installation:

##################
PyAdditive-Widgets
##################

Installation
============

.. installation_start

Package dependencies
--------------------

PyAdditive-Wdigets is supported on Python version 3.9 and later. Previous versions of Python are
no longer supported as outlined in this `Moving to require Python 3 <https://python3statement.org/>`_
statement.

PyAdditive-Widgets dependencies are automatically checked when packages are installed. Included
in these dependencies are these projects:

* `ansys-additive-core <https://pypi.org/project/ansys-additive-core/>`_: PyAdditive is a Python client library
   for the `Ansys Additive`_: service.
* `Panel <https://panel.holoviz.org/>`_: Web app framework used for interactive visualization
  of PyAdditive results.

Install the package
-------------------

.. basic_installation_start

In order to install Pyadditive-Widgets, make sure you
have the latest version of `pip`_. To do so, run:

.. code:: bash

    python -m pip install -U pip

Then, you can simply execute:

.. code:: bash

    python -m pip install ansys-additive-widgets

.. basic_installation_end

.. _ref_install_in_developer_mode:

For developers
--------------

Installing PyAdditive-Widgets in developer mode allows
you to modify the source and enhance it.

Before contributing to the project, please refer to the `PyAnsys Developer's guide`_. You will
need to follow these steps:

#. Start by cloning this repository:

   .. code:: bash

      git clone https://github.com/ansys/pyadditive-widgets

#. Create a Python virtual environment and activate it:

   .. code:: bash

      # Create a virtual environment
      python -m venv .venv

      # Activate it in a POSIX system
      source .venv/bin/activate

      # Activate it in Windows CMD environment
      .venv\Scripts\activate.bat

      # Activate it in Windows Powershell
      .venv\Scripts\Activate.ps1

#. Make sure you have the latest required build system and doc, testing, and CI tools:

   .. code:: bash

      python -m pip install -U pip flit tox
      python -m pip install -r requirements/requirements_build.txt
      python -m pip install -r requirements/requirements_doc.txt
      python -m pip install -r requirements/requirements_tests.txt


#. Install the project in editable mode:

    .. code:: bash

      python -m pip install --editable ansys-additive-widgets

    #. Finally, verify your development installation by running:

   .. code:: bash

      tox

Consider using a virtual environment for the installation.

Starting a session
==================

There are multiple ways to start a session with the PyAdditive client. You can start a local session or a remote session.
A parametric study needs to be instantiated before visualizing the study or results.

.. _ref_starting_a_local_session:

Starting a local session
------------------------

Instantiating an ``Additive`` object starts the local installation of the Additive server.

.. code:: python

   import ansys.additive.core as pyadditive
   from ansys.additive.core.parametric_study import ParametricStudy
   from ansys.additive.widgets import display

   study = ParametricStudy("demo-study")

   # Display the empty study as a table
   display.show_table(study)

Starting a remote session
-------------------------

You can start a remote session by specifying the host name and port of the server.

.. code:: python

   import ansys.additive.core as pyadditive
   from ansys.additive.core.parametric_study import ParametricStudy
   from ansys.additive.widgets import display

   additive = pyadditive.Additive(host="additiveserver.mydomain.com", port=12345)
   study = ParametricStudy("demo-study")

   # Display the empty study as a table
   display.show_table(study)


Alternative startup methods
---------------------------

For additional session startup methods, see the documentation for the
`Additive class <https://additive.docs.pyansys.com/version/stable/api/ansys/additive/core/additive/Additive.html>`_.


Run simulations
===============

For comprehensive usage information, see `Examples`_ in the `PyAdditive-Widgets documentation`_.
For information on how to use the PyAdditive library for the `Ansys Additive`_ service,
refer to the documentation hosted at `PyAdditive documentation`_.

Basic usage
-----------

This code shows how to import PyAdditive-Widgets and use some basic capabilities
to show a the simulations of parametric study generated using the `PyAdditive`_ library
as a table:

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

For comprehensive usage information, see `Examples`_ in the `PyAdditive-Widgets documentation`_.
For information on how to use the PyAdditive library for the `Ansys Additive`_ service,
refer to the documentation hosted at `PyAdditive documentation`_.


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
.. _Examples: https://widgets.additive.docs.pyansys.com/version/stable/examples/gallery_examples/index.html
.. _PyAdditive: https://additive.docs.pyansys.com/version/stable/index.html
.. _PyAdditive documentation: https://additive.docs.pyansys.com/version/stable/index.html
.. _PyAdditive Getting Started: https://additive.docs.pyansys.com/version/stable/getting_started/index.html
.. _PyAdditive-Widgets documentation: https://widgets.additive.docs.pyansys.com/version/stable/index.html
