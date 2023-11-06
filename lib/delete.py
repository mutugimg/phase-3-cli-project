import click
from main import remove_property

@click.command()

@click.option("--choice", prompt="Would you like to proceed? [y/n]")

def delete_property(choice):
    if choice == "y":
        property_name = input("Enter name of property you would like to delete: ")
        remove_property(property_name)
    elif choice == "n":
        click.echo(click.style(("Aborted"),fg="red"))
    else:
        print("Please enter a valid response")

delete_property()
