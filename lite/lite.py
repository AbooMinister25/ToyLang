import click
from main import run_lite
import os

@click.group()
def lite_cli():
    """ CLI for the Lite programming language """


@click.option('-f', '--filename', help='Name of filename to run')
@lite_cli.command()
def run(filename: str):
    """ Command for running and interacting with Lite code"""
    
    if filename == None:
        run_lite()
    if os.path.exists(filename):
        run_lite(filename)
    else:
        print(f"InvalidFilenameError: Invalid filename {filename} given")


if __name__ == '__main__':
    lite_cli(prog_name="lite")