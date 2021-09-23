{%- macro heading(text) -%}
{{text}}
{% for _ in text %}-{% endfor %}
{%- endmacro -%}

{{ heading("Documentation for " + cookiecutter.package_name) }}

.. toctree::
   :hidden:
   :maxdepth: 1

   usage
   reference_material/index
   code_reference
