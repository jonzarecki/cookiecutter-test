{%- macro heading(text) -%}
{{text}}
{% for _ in text %}-{% endfor %}
{%- endmacro -%}

{{ heading("Documentation for " cookiecutter.package_name) }}

.. toctree::
   :hidden:
   :maxdepth: 1

   usage
   reference
   Changelog <https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/releases>
