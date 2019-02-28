import urllib.request
import json
from storage.table_holdings import TableHoldings
from utils.date_util import getToday

class Magnate:
    def __init__(self):
        self.table = TableHoldings()

    def getData(self):
        url = r'https://eospark.com/api/tokens/magnate_rank?symbol=eos&account=eosio.token&size=500&amount_type=eosTotalBalance'
        res = urllib.request.urlopen(url)
        html = res.read().decode('utf-8')
        data = json.loads(html)
        return data['data']['rankings']

    def storeData(self, data):
        if self.dataReady():
            return
        today = getToday()
        print(today)
        for item in data:
            self.table.insertOne(item['holding_account'], item['amount'], item['ranking'], today)
        self.table.commitDB()

    def dataReady(self):
        today = getToday()
        today_data = self.table.getLastRank(today)
        print("xxxxx1----" + str(len(today_data)))
        if len(today_data) == 0:
            return False
        else:
            return True

    def getAndStoreData(self):
        data = self.getData()
        self.storeData(data)

    def printData(self):
        today = getToday()
        list = self.table.getLastRank(today)
        print("xxxxx2----"+str(len(list)))
        for row in list:
            print(row[0] + "    " + str(row[1]) + "    " + str(row[2]) + "    " + str(row[3]))

if __name__ == "__main__":
    print("main run")
    magnate1 = Magnate()
    magnate1.getAndStoreData()
    magnate1.printData()
    magnate1.table.closeDB()