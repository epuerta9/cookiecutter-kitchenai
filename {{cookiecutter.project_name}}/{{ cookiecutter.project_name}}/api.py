from ninja import NinjaAPI
from django.conf import settings

api = NinjaAPI()

api.add_router("/{{cookiecutter.project_name}}/", "{{cookiecutter.project_name}}.{{cookiecutter.project_cookbook}}.kitchen.router")  #   or by Python path

