# Number Guessing Game

This is a client-server based number guessing game. The server generates a random number, and the client tries to guess it. The game supports multiple difficulty levels and maintains a leaderboard to track player scores.

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Files

- `server.py`: Contains the server-side code
- `client.py`: Contains the client-side code
- `leaderboard.json`: A JSON file to store the leaderboard data

### Installation

1. Clone the repository or download the code files.
2. Ensure you have Python 3.x installed.

### Running the Server

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `server.py` file.
3. Run the server using the following command:

   ```bash
   python server.py


The server will start listening on 0.0.0.0:7777.

Running the Client
Open a new terminal or command prompt.

Navigate to the directory containing the client.py file.

Run the client using the following command:

How to Play
After starting the client, you will be prompted to enter your name.
Choose a difficulty level (easy, medium, hard).
Guess the number within the range specified by the chosen difficulty level.
If you guess the number correctly, your score (number of attempts) will be recorded on the leaderboard.
After winning, you will be asked if you want to play again. Enter yes to play another round, or no to exit.
Leaderboard
The leaderboard shows the names, scores, and difficulty levels of all players.
The leaderboard is stored in the leaderboard.json file and is updated after each game.
Code Explanation
Server Code (server.py)
Imports: The code imports necessary modules: socket, random, and json.
NumberGuessingGameServer Class:
__init__(self, host='0.0.0.0', port=7777): Initializes the server with the specified host and port, loads the leaderboard, and sets up the server socket.
load_leaderboard(self): Loads the leaderboard from the leaderboard.json file.
save_leaderboard(self): Saves the leaderboard to the leaderboard.json file.
display_leaderboard(self): Prints the leaderboard to the console.
generate_random_number(self, difficulty): Generates a random number based on the selected difficulty level.
handle_client(self, conn, addr): Handles the client's game session.
update_leaderboard(self, username, score, difficulty): Updates the leaderboard with the player's score and saves it.
send_leaderboard(self, conn): Sends the leaderboard to the client.
start(self): Starts the server and listens for incoming connections.
Client Code (client.py)
Imports: The code imports the socket module.
NumberGuessingGameClient Class:
__init__(self, host='127.0.0.1', port=7777): Initializes the client and connects to the server.
play_game(self): Handles the gameplay, including receiving prompts from the server, sending user inputs, and handling the end-of-game loop.
close_connection(self): Closes the connection to the server.
License
This project is licensed under the MIT License.

Acknowledgments
This project is created for learning purposes and demonstrates a simple client-server application in Python.
