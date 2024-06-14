.. _ref_user_guide:

##########
User guide
##########

This section describes how to start a session with the PyAdditive client and run simulations.

Start a session
===============

You can start a session with the PyAdditive client in multiple ways. For example,
you can start a local session or a remote session.

Before you can visualize the results of a parametric additive simulation, you must
instantiate a parametric study.

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

Start a remote session by specifying the host name and port of the server:

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
in the PyAdditive API reference documentation.


Run simulations
===============
Once a session is started, you can run simulations.

Basic usage
-----------

This code shows how to import PyAdditive-Widgets and use some basic capabilities
to visualize `PyAdditive`_-generated results of a parametric study as a table:

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

The `Examples`_ section provides comprehensive examples of how to use PyAdditive-Widgets.
For information on how to use PyAdditive for the `Ansys Additive`_ service,
see the `PyAdditive documentation`_.

.. LINKS AND REFERENCES
.. _Ansys Additive: https://www.ansys.com/products/additive
.. _PyAdditive: https://additive.docs.pyansys.com/version/stable/index.html
.. _Examples: https://widgets.additive.docs.pyansys.com/version/stable/examples/gallery_examples/index.html
.. _PyAdditive documentation: https://additive.docs.pyansys.com/version/stable/index.html

