# Rock, Paper, Scissors Application in Python
##### Using Tozny Services

## Features

- A simple 2 player game of rock, paper, scissors.
- One judge named Clarence
- The players have 3 rounds per game.
- The players have 3 chances to correctly type their move or they will automatically lose.
- play.py script lets the players play and encrypt the moves they made.
- Only the player that made the move and the judge can read the move.
- judge.py script lets the judge decrypt the players moves, determine the winner, and encrypt the winner list.
- winner.py script lets the players see who won.

## Software
- VScode from https://code.visualstudio.com/Download
- Firefox or Chrome Browsers
- Account at https://tozny.com/
- Tozny SDK from https://github.com/tozny/e3db-python

## Installation

Download and install the necessary Software listed above. Clone this repository.

Open VScode, and navigate to the location of the cloned directory. Create a virtual environment using the environment.yaml file.

```sh
~$ conda env create -f environment.yaml <newEnvNameHere>
```
Create your new clients and register them per the Tozny documentation. Use the registrationA.py file as example on how to register them. Make sure your new client config files have the same names as alicia, bruce, clarence (Notice all lowercase letters). Run the scripts in the following order.
```sh
~$ python play.py
~$ python judge.py
~$ python winner.py
```

## Sources
- https://tozny.com/
- https://github.com/tozny/e3db-python
- https://github.com/tozny/e3db-python/blob/master/examples/simple.py
- https://www.youtube.com/watch?v=8dMUxKNjNgw
- https://stackoverflow.com/questions/33686747/save-a-list-to-a-txt-file


## License

MIT