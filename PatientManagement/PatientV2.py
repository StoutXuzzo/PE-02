from Patient import *

class PatientV2(Patient):
    def __init__(self, dni, name, surname, born, phone, mail, age, height, weight, health):
        super().__init__(dni, name, surname, born, phone, mail)
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__health = health

    def getAge(self):
        return self.__age

    def getHeight(self):
        return self.__height

    def getWeight(self):
        return self.__weight

    def getHealth(self):
        return self.__health