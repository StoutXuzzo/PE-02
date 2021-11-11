from Student import Student

class Controller():

    def __init__(self):
        self.__students = {}

    def getStudents(self):
        return self.__students

    def addStudent(self, dni, name, surnames, age,city, province, email):
        student = Student(dni, name, surnames, age,city, province, email)
        if dni in self.__students:
            return False
        else:
            self.__students[dni] = student
            return True

    def deleteStudent(self, dni):
        if dni in self.__students:
            self.__students.pop(dni)
            return True
        else:
            return False

    def getStudent(self, dni):
        return self.__students.get(dni)

    def modifyStudent(self, student):
        pass
        #self.__students[student.getDni()] = student