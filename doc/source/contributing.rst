.. _ref_contribute:

##########
Contribute
##########

Overall guidance on contributing to a PyAnsys library appears in the
`Contributing <https://dev.docs.pyansys.com/how-to/contributing.html>`_ topic
in the *PyAnsys developer's guide*. Ensure that you are thoroughly familiar
with this guide before attempting to contribute to PyAdditive.

The following contribution information is specific to PyAdditive-Widgets.

Install in developer mode
=========================

Installing PyAdditive-Widgets in developer mode allows you to modify and enhance
the source.

.. note::
  For information on required Ansys products and Python packages, see
  :ref:`prerequisites` and :ref:`package_dependencies`.

Perform these steps to install PyAdditive-Widgets in developer mode:

#. Clone the repository:

   .. code:: bash

      git clone https://github.com/ansys/pyadditive-widgets

#. Create a fresh-clean Python `virtual environment <https://docs.python.org/3/library/venv.html>`_
   and activate it:

   .. code:: bash

      # Create a virtual environment
      python -m venv .venv

      # Activate it in a POSIX system
      source .venv/bin/activate

      # Activate it in Windows CMD environment
      .venv\Scripts\activate.bat

      # Activate it in Windows Powershell
      .venv\Scripts\Activate.ps1

#. Make sure that you have the latest required build system and documentation,
   testing, and CI tools:

   .. code:: bash

      python -m pip install -U pip flit tox
      python -m pip install -e .[doc,tests]

#. Install the project in editable mode:

   .. code:: bash

      python -m pip install --editable ansys-additive-widgets

#. Verify your development installation:

   .. code:: bash

      tox

Testing
=======

This project takes advantage of `tox`_. Similar to Makefile, this tool
allows you to automate common development tasks, but it is oriented towards
Python development.

Use ``tox``
-----------

While Makefile has rules, ``tox`` has environments. In fact, the tool creates its
own virtual environment so that anything being tested is isolated from the project
to guarantee the project's integrity.

The following environments commands are provided:

- **tox -e style**: Checks for coding style quality.
- **tox -e py**: Checks for unit tests.
- **tox -e py-coverage**: Checks for unit testing and code coverage.
- **tox -e doc**: Checks for the documentation-building process.

Perform raw testing
-------------------

If required, you can always call code style commands, such as `Black`_, `isort`_,
and `Flake8`_, or unit testing tools, such as `pytest`_, from the command line. However,
using these tools do not guarantee that your project is being tested in an isolated
environment, which is the reason why a tool like ``tox`` exists.


Run style checks
----------------

The style checks take advantage of `pre-commit`_. Developers are not forced but
encouraged to install this tool by running this command:

.. code:: bash

    python -m pip install pre-commit && pre-commit install


Adhere to code style
--------------------

PyAdditive follows the PEP8 standard as indicated in
`PEP 8 <https://dev.docs.pyansys.com/coding-style/pep8.html>`_ in
the *PyAnsys developer's guide*. It also implements style checking
using `pre-commit`_.

To ensure your code meets minimum code styling standards, run these commands::

  pip install pre-commit
  pre-commit run --all-files

You can also install this as a Git pre-commit hook by running this command::

  pre-commit install

This way, it's not possible for you to push code that fails the code style checks::

  $ pre-commit install
  $ git commit -am "added my cool feature"
  black....................................................................Passed
  blacken-docs.............................................................Passed
  isort....................................................................Passed
  flake8...................................................................Passed
  docformatter.............................................................Passed
  codespell................................................................Passed
  pydocstyle...............................................................Passed
  check for merge conflicts................................................Passed
  debug statements (python)................................................Passed
  check yaml...............................................................Passed
  trim trailing whitespace.................................................Passed
  Add License Headers......................................................Passed
  Validate GitHub Workflows................................................Passed

Documentation builds
====================

To build documentation, you can run the usual rules provided in the
`Sphinx`_ Makefile with a command like this:

.. code:: bash

    make -C doc/ html && open doc/html/index.html

However, the recommended way of checking documentation integrity is to use a ``tox``
command like this:

.. code:: bash

    tox -e doc && open .tox/doc_out/index.html

Distribution
============

If you would like to create either source or wheel files, run the following
commands to install the building requirements and execute the build module:

.. code:: bash

    python -m pip install -r requirements/requirements_build.txt
    python -m build
    python -m twine check dist/*

Post issues
===========

Use the `PyAdditive-Widgets Issues <https://github.com/ansys/pyadditive-widgets/issues>`_
page to report bugs and request new features. When possible, use the issue templates provided.
If your issue does not fit into one of these templates, click the link for opening a blank issue.

If you have general questions about the PyAnsys ecosystem, email
`pyansys.core@ansys.com <pyansys.core@ansys.com>`_. If your
question is specific to PyAdditive-Widgets, ask your question
in an issue as described in the previous paragraph.

.. LINKS AND REFERENCES
.. _tox: https://tox.wiki/
.. _Black: https://github.com/psf/black
.. _isort: https://github.com/PyCQA/isort
.. _Flake8: https://flake8.pycqa.org/en/latest/
.. _pytest: https://docs.pytest.org/en/stable/
.. _pre-commit: https://pre-commit.com/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
