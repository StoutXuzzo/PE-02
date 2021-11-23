import random

class Event():
    def __init__(self, name, date, location, province, price):
        self.__name = name
        self.__date = date
        self.__location = location
        self.__province = province
        self.__price = float(price)
        self.__total = 0.0
        self.__participants = []
        self.__finished = False
        self.__podium = {"FIRST":"", "SECOND":"", "THIRD":""}

    def getName(self):
        return self.__name

    def getDate(self):
        return self.__date

    def getLocation(self):
        return self.__location

    def getProvince(self):
        return self.__province

    def getPrice(self):
        return self.__price

    def getTotal(self):
        return self.__total

    def getParticipants(self):
        return self.__participants

    def getState(self):
        return self.__finished

    def getPodium(self):
        return self.__podium

    def __str__(self):
        return self.__name + " - " + str(self.__date) + " - " + self.__province + " " + self.__location

    def addParticipant(self, participant):
        self.__participants.append(participant)
        self.__total += self.__price

    def endEvent(self):
        self.__finished = True
        participants = self.__participants[:]
        if len(self.__participants) >= 3:
            self.__podium["FIRST"] = participants.pop(random.randint(0, len(participants)) - 1)
            self.__podium["SECOND"] = participants.pop(random.randint(0, len(participants)) - 1)
            self.__podium["THIRD"] = participants[random.randint(0, len(participants)) - 1]
            return self.__podium
        return False