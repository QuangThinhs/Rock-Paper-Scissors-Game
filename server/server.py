import socket, threading, json
from database import Database
from auth import login
from game_manager import determine_winner

class GameServer:
    def __init__(self):
        self.db = Database()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}

    def handle_client(self, sock, addr):
        while True:
            data = json.loads(sock.recv(4096).decode())
            if data['action'] == 'login':
                user = login(self.db, data['username'], data['password'])
                sock.send(json.dumps({
                    'action': 'login_response',
                    'success': bool(user),
                    'user': user
                }).encode())

    def start(self):
        self.server.bind(('0.0.0.0', 5555))
        self.server.listen()
        while True:
            c, a = self.server.accept()
            threading.Thread(target=self.handle_client, args=(c,a)).start()
