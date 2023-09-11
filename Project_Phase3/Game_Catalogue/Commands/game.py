import click
from Game_Catalogue.tables_module import Game, Developer, Session
from sqlalchemy.orm import sessionmaker

@click.group()
def game():
    pass

@game.command()
@click.option('--name', prompt='Name', help='Name of the game')
@click.option('--price', prompt='Price', type=int, help='Price of the game')
@click.option('--developer_id', prompt='Developer ID', help='ID of the developer')
@click.option('--genre_id', prompt='Genre ID', help='ID of the genre')
def create_game(name, price, developer_id, genre_id):
    """Create a new game."""
    session = Session()
    developer = session.query(Developer).filter_by(id=developer_id).first()
    if developer:
        game = Game(name=name, price=price, developer_id=developer_id, genre_id=genre_id)
        session.add(game)
        session.commit()
        click.echo(f"Game created: {name}")
    else:
        click.echo("Invalid or unknown game developer" )

@game.command()
def list_games():
    """List all games."""
    session = Session()
    games = session.query(Game).all()
    if not games:
        click.echo("No games found.")
    else:
        click.echo("Games:")
        for game in games:
            click.echo(f"ID: {game.id}, Name: {game.name}, Price: {game.price}")

@game.command()
@click.option('--game_id', prompt='Game ID', type=int, help='ID of the game to delete')
def remove_game(game_id):
    """Remove a bought game by ID."""
    session = Session()
    game = session.query(Game).filter_by(id=game_id).first()
    if game:
        session.delete(game)
        session.commit()
        click.echo(f"Game {game_id} deleted.")
    else:
        click.echo(f"Game with ID {game_id} not found.")

@game.command()
@click.option("--name",prompt = "Name",help = "Input game name")
def search_game(name):
    """Search game by name"""
    session = Session()
    games = session.query(Game).filter_by(name=name)
    if not games:
        click.echo("ERROR!!! Game does not exist")
    else:
        click.echo("Search result:")
        for game in games:
            click.echo(f" ID:{game.id} Name:{game.name} Price:{game.price}")
            


if __name__ == '__main__':
    game()