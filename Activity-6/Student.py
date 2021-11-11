
class Student():
    def __init__(self, dni, name, surnames, age, city, province, email):
        self.__dni = dni
        self.__name = name
        self.__surnames = surnames
        self.__age = age
        self.__city = city
        self.__province = province
        self.__email = email
    
    def setDni(self, dni):
        self.__dni = dni

    def getDni(self):
        return self.__dni
    
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSurnames(self, surnames):
        self.__surnames = surnames

    def getSurnames(self):
        return self.__surnames

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setCity(self, city):
        self.__city = city

    def getCity(self):
        return self.__city

    def setProvince(self, province):
        self.__province = province

    def getProvince(self):
        return self.__province

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email
