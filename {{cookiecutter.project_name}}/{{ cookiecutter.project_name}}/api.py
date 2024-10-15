from ninja import NinjaAPI
from django.conf import settings

api = NinjaAPI(version=settings.VERSION, title="{{cookiecutter.project_cookbook}}_sdk")

api.add_router("/{{cookiecutter.project_name}}/", "{{cookiecutter.project_name}}.{{cookiecutter.project_cookbook}}.kitchen.router")  #   or by Python path

