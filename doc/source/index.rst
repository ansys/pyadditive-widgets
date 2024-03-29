..
   Just reuse the root readme to avoid duplicating the documentation.
   Provide any documentation specific to your online documentation
   here.

PyAdditive-Widgets Documentation  |version|
===========================================

.. include:: ../../README.rst
   :start-after: .. readme_start

.. include:: ../../INSTALLATION.rst
   :start-after: .. installation_start

.. jinja:: main_toctree

   .. toctree::
      :hidden:
      :maxdepth: 2

      getting_started/index
      {% if build_examples %}
      examples/gallery_examples/index
      {% endif %}
      contributing
