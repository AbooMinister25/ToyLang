"""
Hey guys, this is the in development code for the Lite package manager, something I am trying to finish up soon, so don't bother trying to run this, it'll raise an error, since my API
isn't activated yet. 
"""


import click
import requests
import os


@click.group()
def ice_cli():
    """ Package Manager for the Lite programming language """



@ice_cli.command()
@click.argument('filename')
def install(filename):
    try:
        r = requests.get(fr"https://rcyclegar.pythonanywhere.com/get-module/{filename}.py")
        open(f"lite\external_modules\{filename}.py", "w").write(r.text)
        print(f"Module {filename} installed successfully")
    except FileNotFoundError:
        print(f"No module named {filename}")
    except Exception as e:
        print(f"The command raised the following exception: {e}")


@ice_cli.command()
@click.argument('filename')
def installfromfile(filename):
    try:
        modules = open(f"{filename}.txt", "r").readlines()
        for module in modules:
            r = requests.get(fr"https://rcyclegar.pythonanywhere.com/get-module/{module}.py")
            open(f"lite\external_modules\{module}.py", "w").write(r.text)
        print("Modules successfully installed")
    except FileNotFoundError:
        print(f"No file named {filename}")
    except Exception as e:
        print(f"The command raised the following exception: {e}")


@ice_cli.command()
@click.argument('filename')
def delete(filename):
    try:
        os.remove(f"lite\external_modules\{filename}.py")
    except FileNotFoundError:
        print(f"No module name {filename}")
    except Exception as e:
        print(f"The command raised the following exception: {e}")



if __name__ == '__main__':
    ice_cli(prog_name="ice")