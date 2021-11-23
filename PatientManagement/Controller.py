class Controller():
    def __init__(self):
        self.__data = {}

    def addPatient(self, patient):
        if not patient.getDni() in self.__data:
            self.__data[patient.getDni()] = patient
            return True
        return False

    def deletePatient(self, dni):
        if dni in self.__data:
            self.__data.pop(dni)
            return True
        return False

    def getAllPatients(self):
        return self.__data

    def getPatient(self, dni):
        return self.__data[dni]

    def getTotal(self):
        return len(self.__data)

    def addVisit(self, dni, info):
        self.__data[dni].addVisit(info)