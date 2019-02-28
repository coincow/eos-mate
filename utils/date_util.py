import datetime
import time

def getToday():
    today = datetime.date.today()
    st = time.strptime(str(today.year)+str(today.month)+str(today.day), "%Y%m%d")
    return time.mktime(st)