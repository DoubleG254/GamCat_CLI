import click
from Game_Catalogue.Commands.developer import developer
from Game_Catalogue.Commands.game import game
from Game_Catalogue.Commands.genre import genre

@click.group()
def cli():
    """Game Catalogue CLI"""

cli.add_command(game)
cli.add_command(developer)
cli.add_command(genre)

if __name__ =='__main__':
    cli()