class Invoice():
    def __init__(self, id, date, nif, paid, lines):
        self.__id = id
        self.__date = date
        self.__nif = nif
        self.__paid = paid
        self.__lines = lines[:]
        self.__base = 0
        for elem in self.__lines:
            self.__base += elem[2]
        VAT = 0.21
        self.__total = self.__base - (self.__base * VAT) 
        

    def getId(self):
        return self.__id
    
    def getDate(self):
        return self.__date

    def getNif(self):
        return self.__nif

    def getPaid(self):
        return self.__paid
    
    def setAsPaid(self):
        self.__paid = True

    def getBase(self):
        return self.__base

    def getTotal(self):
        return self.__total

    def getLines(self):
        return self.__lines