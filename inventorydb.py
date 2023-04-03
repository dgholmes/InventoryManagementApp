import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(self, db)
