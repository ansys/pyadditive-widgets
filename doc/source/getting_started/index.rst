:orphan:

.. _ref_getting_started:

###############
Getting started
###############

PyAdditive-Widgets is a widget toolkit for PyAdditive Simulations. The `PyAdditive`_ library
will be automatically installed with this package.
The widget provides methods to visualize the results of parametric additive simulations.
You can view the study as a table, view the single bead simulation results as a heat map or
view the porosity relative density results as a contour plot and so on.

.. note::
   Requires Ansys 2024 R1 or later.
   Requires PyAdditive 0.17.2 or later.

.. warning::
   The simulations described in this documentation require an Additive Suite license. To obtain a license,
   contact your Ansys sales representative or see https://www.ansys.com/contact-us.


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



Installation
============

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

At least two installation modes are provided: user and developer.

For users
^^^^^^^^^

In order to install Pyadditive-Widgets, make sure you
have the latest version of `pip`_. To do so, run:

.. code:: bash

    python -m pip install -U pip

Then, you can simply execute:

.. code:: bash

    python -m pip install ansys-additive-widgets


.. _ref_install_in_developer_mode:

For developers
^^^^^^^^^^^^^^

Installing Pyadditive-Widgets in developer mode allows
you to modify the source and enhance it.

Before contributing to the project, please refer to the `PyAnsys Developer's guide`_. You will
need to follow these steps:

#. Start by cloning this repository:

   .. code:: bash

      git clone https://github.com/ansys/pyadditive-widgets

#. Create a fresh-clean Python environment and activate it:

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


Basic usage
^^^^^^^^^^^

For comprehensive usage information, see `Examples`_ in the `PyAdditive-Widgets Documentation`_.
For information on how to use the PyAdditive library for the `Ansys Additive`_ service,
refer to the documentation hosted at `PyAdditive documentation`_.

For testing
--------------

This project takes advantage of `tox`_. This tool allows to automate common
development tasks (similar to Makefile) but it is oriented towards Python
development.

Using tox
^^^^^^^^^

As Makefile has rules, `tox`_ has environments. In fact, the tool creates its
own virtual environment so anything being tested is isolated from the project in
order to guarantee project's integrity. The following environments commands are provided:

- **tox -e style**: will check for coding style quality.
- **tox -e py**: checks for unit tests.
- **tox -e py-coverage**: checks for unit testing and code coverage.
- **tox -e doc**: checs for documentation building process.


Raw testing
^^^^^^^^^^^

If required, you can always call the style commands (`black`_, `isort`_,
`flake8`_...) or unit testing ones (`pytest`_) from the command line. However,
this does not guarantee that your project is being tested in an isolated
environment, which is the reason why tools like `tox`_ exist.


A note on pre-commit
^^^^^^^^^^^^^^^^^^^^

The style checks take advantage of `pre-commit`_. Developers are not forced but
encouraged to install this tool via:

.. code:: bash

    python -m pip install pre-commit && pre-commit install


Documentation
-------------

For building documentation, you can either run the usual rules provided in the
`Sphinx`_ Makefile, such us:

.. code:: bash

    make -C doc/ html && open doc/html/index.html

However, the recommended way of checking documentation integrity is using:

.. code:: bash

    tox -e doc && open .tox/doc_out/index.html


Distributing
------------

If you would like to create either source or wheel files, start by installing
the building requirements and then executing the build module:

.. code:: bash

    python -m pip install -r requirements/requirements_build.txt
    python -m build
    python -m twine check dist/*

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
.. _Examples: https://additive-widgets.docs.pyansys.com/version/stable/examples/gallery_examples/index.html
.. _PyAdditive: https://additive.docs.pyansys.com/version/stable/index.html
.. _PyAdditive documentation: https://additive.docs.pyansys.com/version/stable/index.html
.. _PyAdditive Getting Started: https://additive.docs.pyansys.com/version/stable/getting_started/index.html
.. _PyAdditive-Widgets documentation: https://additive-widgets.docs.pyansys.com/version/stable/index.html