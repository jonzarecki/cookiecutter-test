{%- macro heading(text) -%}
{{text}}
{% for _ in text %}-{% endfor %}
{%- endmacro -%}
Reference
=========

.. contents::
    :local:
    :backlinks: none


{{ heading(cookiecutter.package_name + ".main") }}

.. automodule:: {{cookiecutter.package_name}}.main
   :members:
