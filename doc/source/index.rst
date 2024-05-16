PyAdditive-Widgets documentation |version|
==========================================

PyAdditive-Widgets is a widget toolkit for `PyAdditive`_ simulations. It provides
methods for visualizing the results of parametric additive simulations. Some examples
include viewing the study as a table, viewing the single bead simulation results as
a heat map, and viewing the porosity relative density results as a contour plot.


.. grid:: 1 2 2 2


    .. grid-item-card:: Getting started :material-regular:`directions_run`
        :padding: 2 2 2 2
        :link: getting_started/index
        :link-type: doc

        Learn how to install PyAdditive-Widgets in user mode and quickly
        begin using it.

    .. jinja:: main_toctree

        {% if build_api %}
        .. grid-item-card:: API reference :material-regular:`bookmark`
            :padding: 2 2 2 2
            :link: api/index
            :link-type: doc

            Understand how to use Python to interact programmatically with
            PyAdditive-Widgets.
        {% endif %}

        {% if build_examples %}
        .. grid-item-card:: Examples :material-regular:`play_arrow`
            :padding: 2 2 2 2
            :link: examples/gallery_examples/index
            :link-type: doc

            Explore examples that show how to use PyAdditive-Widgets to
            perform many different types of operations.
        {% endif %}

        .. grid-item-card:: Contribute :material-regular:`group`
            :padding: 2 2 2 2
            :link: contributing
            :link-type: doc

            Learn how to contribute to the PyAdditive-Widgets codebase or documentation.


.. jinja:: main_toctree

    .. toctree::
       :hidden:
       :maxdepth: 3

       getting_started/index
       {% if build_api %}
       api/index
       {% endif %}
       {% if build_examples %}
       examples/gallery_examples/index
       {% endif %}
       contributing
