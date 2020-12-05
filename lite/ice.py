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
        r = requests.get(f"http://127.0.0.1:5000/get-module/{filename}.py")
        open(f"lite\external_modules\{filename}.py", "w").write(r.text)
    except FileNotFoundError:
        print(f"No module name {filename}")
    except Exception as e:
        print(f"The command raised the following exception: {e}")



if __name__ == '__main__':
    ice_cli(prog_name="ice")