import click
from main import get_properties

@click.command()

@click.option("--view", prompt="Welcome to MMG properties. Would you like to view our listings? [y/n]")

def list_property(view):
    if view == "y":
        get_properties()
    elif view == "n":
        click.echo(click.style(("Aborted"),fg="red"))
    else:
        print("Please enter a valid response")




list_property()