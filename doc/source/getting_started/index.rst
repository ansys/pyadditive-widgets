:orphan:

.. _ref_getting_started:

###############
Getting started
###############

PyAdditive-Widgets is a widget toolkit for PyAdditive Simulations.
The widget provides methods to visualize the results of parametric additive simulations.
You can view the study as a table, view the single bead simulation results as a heat map or
view the porosity relative density results as a contour plot and so on.

.. note::
   Requires Ansys 2024 R1 or later.
   Requires PyAdditive 0.17.2 or later.

.. warning::
   The simulations described in this documentation require an Additive Suite license. To obtain a license,
   contact your Ansys sales representative or see https://www.ansys.com/contact-us.



Installation
============

.. include:: ../../../INSTALLATION.rst
   :start-after: .. installation_start

For testing
-----------

This project takes advantage of `tox`_. This tool allows to automate common
development tasks (similar to Makefile) but it is oriented towards Python
development.

Using tox
---------

As Makefile has rules, `tox`_ has environments. In fact, the tool creates its
own virtual environment so anything being tested is isolated from the project in
order to guarantee project's integrity. The following environments commands are provided:

- **tox -e style**: checks for coding style quality.
- **tox -e py**: checks for unit tests.
- **tox -e py-coverage**: checks for unit testing and code coverage.
- **tox -e doc**: checks for documentation building process.


Raw testing
-----------

If required, you can always call the style commands (`black`_, `isort`_,
`flake8`_...) or unit testing ones (`pytest`_) from the command line. However,
this does not guarantee that your project is being tested in an isolated
environment, which is the reason why tools like `tox`_ exist.


A note on pre-commit
--------------------

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
.. _Examples: https://widgets.additive.docs.pyansys.com/version/stable/examples/gallery_examples/index.html
.. _PyAdditive: https://additive.docs.pyansys.com/version/stable/index.html
.. _PyAdditive documentation: https://additive.docs.pyansys.com/version/stable/index.html
.. _PyAdditive Getting Started: https://additive.docs.pyansys.com/version/stable/getting_started/index.html
.. _PyAdditive-Widgets documentation: https://widgets.additive.docs.pyansys.com/version/stable/index.html