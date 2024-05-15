import socket

class NumberGuessingGameClient:
    def __init__(self, host='127.0.0.1', port=7777):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

    def play_game(self):
        while True:
            data = self.client_socket.recv(1024).decode()
            print(data.strip())
            if "Do you want to play again? (yes/no):" in data:
                play_again = input().strip().lower()
                self.client_socket.sendall(play_again.encode())
                if play_again != "yes":
                    break
            elif "Leaderboard" in data:
                continue
            else:
                user_input = input().strip()
                self.client_socket.sendall(user_input.encode())

    def close_connection(self):
        self.client_socket.close()

if __name__ == "__main__":
    client = NumberGuessingGameClient()
    client.play_game()
    client.close_connection()
