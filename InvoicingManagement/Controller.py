from Invoice import *
import datetime

# nowstrftime("%d/%m/Y")

class Controller():
    def __init__(self):
        self.invList = []

    def newInvoice(self, nif, products):
        invoice = Invoice(len(self.invList) + 1, datetime.datetime.now(), nif, False, products)
        self.invList.append(invoice)
        #print(self.invList)
        return invoice

    def isPaid(self, semaf):
        res = []
        for elem in self.invList:
            if semaf != elem.getPaid():
                continue
            res.append(elem)

        return res

    def isPaidNif(self, semaf, nif):
        res = []
        for elem in self.invList:
            if elem.getPaid() == semaf and nif == elem.getNif():
                res.append(elem)

        return res

    def getInvoice(self, id):
        for elem in self.invList:
            if elem.getId() == id:
                return elem
            
        return None
