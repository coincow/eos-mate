from storage.db import DataBase

class TableHoldings:

    def __init__(self):
        self.db = DataBase().getDB()
        try:
            create_table_cmd = "CREATE TABLE IF NOT EXISTS HOLDINGS (ACCOUNT TEXT PRIMARY KEY, AMOUNT REAL, RANKING INTEGER, DATE INTEGER)"
            self.db.execute(create_table_cmd)
        except Exception as e:
            print(e)

    def insertOne(self, account, amount, ranking, date):
        sqlString = "INSERT INTO HOLDINGS (ACCOUNT, AMOUNT, RANKING, DATE) VALUES(?,?,?,?)"
        v = (account, amount, ranking, date)
        cursor = self.db.cursor()
        cursor.execute(sqlString, v)
        return

    def getLastRank(self):
        list = []
        sqlString = "SELECT * FROM HOLDINGS"
        # sqlString = "SELECT * FROM HOLDINGS where DATE=?"
        v = (0,)
        cursor = self.db.cursor()
        hint = cursor.execute(sqlString)
        hit_all = hint.fetchall()
        for row in hit_all:
            list.append(row[0])
        print('print item end!')
        return list

    def closeDB(self):
        self.db.close()






