import sqlite3

class DataBase:
    def __init__(self):
        self.db = sqlite3.connect("./db")
        # self.db.set_trace_callback(print)

    def getDB(self):
        return self.db

