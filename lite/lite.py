import click
from main import run_lite, __version__
import os


@click.group()
def lite_cli(version=__version__):
    """ CLI for the Lite programming language """


@click.option('-f', '--filename', help='Name of filename to run')
@lite_cli.command()
def run(filename: str):
    """ Command for running and interacting with Lite code"""
    
    if filename == None:
        print("Welcome to the Lite v1.0.3 shell! Press CTRL + V to exit")
        run_lite()
    if os.path.exists(filename):
        run_lite(filename)
    else:
        print(f"InvalidFilenameError: Invalid filename {filename} given")


@lite_cli.command()
def version():
    print(__version__)


if __name__ == '__main__':
    lite_cli(prog_name="lite")