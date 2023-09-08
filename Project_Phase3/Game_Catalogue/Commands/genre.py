import click
from Game_Catalogue.tables_module import Genre,Session

@click.group()
def genre():
    pass

@genre.command()
@click.option("--id",prompt = "ID",help = "ID of the genre")
@click.option("--name",prompt = "Genre",help = "Name of genre")
def add(id,name):
    """Add Genre"""
    genre = Genre(id=id,name=name)
    session = Session()
    session.add(genre)
    session.commit()
    click.echo(f"{name} added to genres")
@genre.command()
def list():
    session = Session()
    genres=session.query(Genre).all()
    if not genres:
        click.echo("No Genres created")
    else:
        click.echo("Genres:")
        for genre in genres:
            click.echo(f"ID:{genre.id} Genre:{genre.name}")
        
