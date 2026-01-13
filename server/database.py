import mysql.connector

class Database:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'locdeptrai12',
            'database': 'rps_game'
        }

    def connect(self):
        return mysql.connector.connect(**self.config)
