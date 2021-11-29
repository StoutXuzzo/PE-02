class Patient():
    def __init__(self, dni, name, surname, born, phone, mail):
        self.__dni = dni
        self.__name = name
        self.__surname = surname
        self.__born = born
        self.__phone = phone
        self.__mail = mail
        self.__visits = []
        self.__nVisits = len(self.__visits)

    def getDni(self):
        return self.__dni

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname

    def getBorn(self):
        return self.__born

    def getPhone(self):
        return self.__phone

    def getMail(self):
        return self.__mail

    def getVisits(self):
        return self.__visits

    def getNumVisits(self):
        return self.__nVisits

    def addVisit(self, appointment):
        self.__visits.append(appointment)
        self.__nVisits = len(self.__visits)