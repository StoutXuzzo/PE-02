from Event import *

class ControllerEvent():
    def __init__(self):
        self.__events = []

    def addEvent(self, name, date, location, province, price):
        try:
            event = Event(name, date, location, province, price)
            self.__events.append(event)
            return True
        except:
            return False

    def getEvents(self):
        result = []
        for event in self.__events:
            if not event.getState():
                result.append(event)
        return result

    #def getEvents(self, semaf):
    #    result = []
    #    for event in self.__events:
    #        if event.getState() == semaf:
    #            if not semaf and len(event.getParticipants) > 0:
    #                result.append(event)
    #            elif semaf and event.getPodium()["FIRST"] == "":
    #                result.append(event)

    def getFinishEvents(self):
        result = []
        for event in self.__events:
            if event.getState() and event.getPodium()["FIRST"] != "":
                result.append(event)
        return result

    def getNoFinishEvents(self):
        result = []
        for event in self.__events:
            participants = event.getParticipants()
            if event.getState() == False and len(participants) > 0:
                    result.append(event)
        return result

    def addParticipant(self, id, participant):
        try:
            self.__events[id].addParticipant(participant)
            return True
        except:
            return False

    def finishEvent(self, id):
            return self.__events[id].endEvent()
