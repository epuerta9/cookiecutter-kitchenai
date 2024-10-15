import djp

@djp.hookimpl
def settings(current_settings):
    current_settings["KITCHENAI"]["{{ cookiecutter.project_cookbook }}"] = "{{cookiecutter.project_name}}.{{cookiecutter.project_cookbook}}.kitchen.router"