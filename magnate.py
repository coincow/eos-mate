import urllib.request
import json
from storage.table_holdings import TableHoldings

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
        for item in data:
            self.table.insertOne(item['holding_account'], item['amount'], item['ranking'], 0)

    def getAndStoreData(self):
        data = self.getData()
        self.storeData(data)

    def printData(self):
        list = self.table.getLastRank()
        for row in list:
            print(row[0] + "    " + str(row[1]) + "    " + str(row[2]))


if __name__ == "__main__":
    print("main run")
    magnate1 = Magnate()
    magnate1.getAndStoreData()
    magnate1.printData()
    magnate1.table.closeDB()