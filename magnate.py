import urllib.request
import json
from storage.table_holdings import TableHoldings

def getData():
    url = r'https://eospark.com/api/tokens/magnate_rank?symbol=eos&account=eosio.token&size=500&amount_type=eosTotalBalance'
    res = urllib.request.urlopen(url)
    html = res.read().decode('utf-8')
    data = json.loads(html)
    return data['data']['rankings']

def storeData(data):
    table = TableHoldings()
    for item in data:
        table.insertOne(item['holding_account'], item['amount'], item['ranking'], 0)

def getAndStoreData():
    data = getData()
    storeData(data)

def printData():
    table = TableHoldings()
    list = table.getLastRank()
    for row in list:
        print(row[0] + "    " + row[1].decode('utf-8') + "    " + row[2].decode('utf-8'))


if __name__ == "__main__":
    print("main run")
    getAndStoreData()
    printData()
    table = TableHoldings()
    table.closeDB()