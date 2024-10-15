from django.apps import AppConfig


class {{ cookiecutter.project_cookbook | replace('_', ' ') | title | replace(' ', '') }}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{ cookiecutter.project_name}}.{{cookiecutter.project_cookbook}}"
