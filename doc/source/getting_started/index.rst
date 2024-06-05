.. _ref_getting_started:

###############
Getting started
###############

This section describes how to install PyAdditive-Widgets in user mode and quickly begin
using it. If you are interested in contributing to PyAdditive-Widgets, see :ref:`ref_contribute`
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

Dependencies for PyAdditive-Widgets are automatically checked when packages are installed. Included
in these dependencies are these projects:

* `ansys-additive-core <https://pypi.org/project/ansys-additive-core/>`_: PyAdditive is a Python
  client library for the `Ansys Additive`_ service.
* `Panel <https://panel.holoviz.org/>`_: A web app framework for Python that is used for interactive
  visualization of PyAdditive results.

Install the package
===================

#. Before installing PyAdditive-Widgets, make sure that you
   have the latest version of `pip`_ with this command:

   .. code:: bash

       python -m pip install -U pip

#. Install PyAdditive-Widgets with this command:

   .. code:: bash

       python -m pip install ansys-additive-widgets

For information on starting a session and running simulations, see :ref:`ref_user_guide`.

.. LINKS AND REFERENCES
.. _Ansys Additive: https://www.ansys.com/products/additive
.. _PyAdditive: https://additive.docs.pyansys.com/version/stable/index.html
.. _Examples: https://widgets.additive.docs.pyansys.com/version/stable/examples/gallery_examples/index.html
.. _PyAdditive documentation: https://additive.docs.pyansys.com/version/stable/index.html
.. _pip: https://pypi.org/project/pip/
