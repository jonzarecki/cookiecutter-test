{%- macro heading(text) -%}
{{text}}
{% for _ in text %}-{% endfor %}
{%- endmacro -%}
Code Reference
==============

.. contents::
    :local:
    :backlinks: none


{{ heading(cookiecutter.package_name) }}
{{cookiecutter.package_name}} package.

.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:

   {{cookiecutter.package_name}}


common
------
All non-project specific code.

.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:

   common
