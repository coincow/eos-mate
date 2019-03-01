from tkinter import *
from storage.table_holdings import TableHoldings

class AccountList:
    def __init__(self):
        self.root = Tk()
        self.root.title("eos富豪排名")
        self.list = Listbox(self.root, width=60, height=60)
        self.list.place(relx=1, rely=1)
        table = TableHoldings()
        data = table.getLastRank()
        for row in data:
            self.list.insert(END, [row[2], row[0], row[1]])
        self.list.grid(row=60, column=3)
        self.root.mainloop()

