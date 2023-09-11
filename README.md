## GamCat-CLI
A Command-Line Interface (CLI) application for managing games within game stores.The CLI tool utilizes CRUD(Create,Read,Update and Delete)operations to fulfil the users needs.

## Table of Contents
 [Installation](#installation)
 [Usage](#usage)
 [Technologies](#technologies)
 [License](#license)
 [Author](#author)

## Installation

 # clone the repository
 $ git clone <git@github.com:DoubleG254/GamCat_CLI.git>
 
 # navigate to directory
 $ cd </GamCat-CLI-project/Project_Phase3>
 # install dependencies and create virtual environment
 $ pipenv install & pipenv shell
 # run the applictaion
 $ python main.py

 ## Usage
   # list available commands
   $ python main.py --help
  ## Commands
   ```games management```
   # add new game
   $ python main.py game create-game
   # list available games
   $ python main.py game list-games
   # remove bought game
   $ python main.py game remove-game
   # search for a specific game
   $ python main.py game search-game

   ```developer management```
   # add new developer
   $ python main.py developer add
   # list developers
   $ python main.py developer list
   
    ```genre commands```
  # add new genre
  $ python main.py genre add
  # list genres
  $ python main.py genre list

## Technologies
1.Python
2.SQL Alchemy
3.Click library

## License
MIT
## Author
Glory Gweth






