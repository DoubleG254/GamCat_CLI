import click
from Game_Catalogue.tables_module import Game,Developer,Session

@click.group()
def developer():
    pass
@developer.command()
@click.option('--id',prompt = 'ID', help = 'Id of the Developer')
@click.option('--name', prompt= "Name", help = 'Name of Developer')
def add(id,name):
    """Add new developer"""
    session = Session()
   
    existing_developer = session.query(Developer).filter_by(id=id).first()

    if existing_developer:
        click.echo(f"Developer with ID {id} already exists.")
    else:
        developer = Developer(id=id,name=name)
        session.add(developer)
        session.commit()
        click.echo(f"{name} added as Developer")
@developer.command()
def list():
    """List all Developers"""
    session = Session()
    developers = session.query(Developer).all()
    if not developers:
        click.echo("No Developers in contract")
    else:
        click.echo("Developers:")
        for developer in developers:
            click.echo(f"ID:{developer.id} Name:{developer.name}")


