import re 
from Controller import *
from Student import *

control = Controller()

def valDni(dni):
    code = "TRWAGMYFPDXBNIZSQVHLCKE"
    dniNum = dni[:-1]

    if dni[:-1].isdigit() and len(dni) == 9:

        dniNum = int(dniNum)

        num = dniNum % 23
        if dni[-1] == code[num]:
            return True
        else:
            return False
    else:
        return False

def valName(name):
    if len(name) > 0:
        return True
    else:
        return False

def valSurnames(surname):
    if len(surname) > 0:
        return True
    else:
        return False

def valAge(age):
    try:
        age = int(age)
        return True
    except:
        return False


def valCity(city):
    if len(city) > 0:
        return True
    else:
        return False

def valProvince(province):
    if len(province) > 0:
        return True
    else:
        return False

def valEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

while True:
    print("\nSTUDENT CRUD")
    print("----------------------------")
    print("1.- Add a student")
    print("2.- Delete a student")
    print("3.- Modify a student")
    print("4.- Search a student")
    print("5.- Exit")
    user = input("Choose option: ")

    if user == "1":

        print("\nCreate an student:")

        while True:
            dni = input("1.- Insert DNI: ")
            if valDni(dni):
                break
            else:
                print("Incorrect DNI")

        while True:
            name = input("2.- Insert Name: ")
            if valName(name):
                break
            else:
                print("Incorrect Name")

        while True:
            surnames = input("3.- Insert Surname: ")
            if valSurnames(surnames):
                break
            else:
                print("Incorrect Surname")

        while True:
            age = input("4.- Insert Age: ")
            if valAge(age):
                age = int(age)
                break
            else:
                print("Incorrect Age")

        while True:
            city = input("5.- Insert City: ")
            if valCity(city):
                break
            else:
                print("Incorrect City")

        while True:
            province = input("6.- Insert Province: ")
            if valProvince(province):
                break
            else:
                print("Incorrect Province")
        
        while True:
            email = input("7.- Insert Email: ")
            if valEmail(email):
                break
            else:
                print("Incorrect Email")

        if control.addStudent(dni, name, surnames, age,city, province, email):
            print("The student was added succesfully.")
        else:
            print("The student wasn't added :(")

    elif user == "2":

        dni = input("\nInsert a DNI: ")

        if control.deleteStudent(dni):
            print("The student with DNI " + dni + " was deleted succesfully")
        else:
            print("There is no student with this DNI")

    elif user == "3":

        dni = input("\nInsert a DNI: ")
        student = control.getStudent(dni)

        if student != None:
            print("Modification of student with DNI: " + dni)
            print("1.- Modify Name")
            print("2.- Modify Surname")
            print("3.- Modify Age")
            print("4.- Modify City")
            print("5.- Modify Province")
            print("6.- Modify Email")
            user = input("What do you want to modify: ")

            if user == "1":

                while True:
                    name = input("Insert Name: ")
                    if valName(name):
                        break
                    else:
                        print("Incorrect Name")
                student.setName(name)

            elif user == "2":

                while True:
                    surnames = input("Insert Surname: ")
                    if valSurnames(surnames):
                        break
                    else:
                        print("Incorrect Surname")
                student.setSurname(surnames)

            elif user == "3":

                while True:
                    age = input("Insert Age: ")
                    if valAge(age):
                        age = int(age)
                        break
                    else:
                        print("Incorrect Age")
                student.setAge(age)
                
            elif user == "4":

                while True:
                    city = input("Insert City: ")
                    if valCity(city):
                        break
                    else:
                        print("Incorrect City")
                student.setCity(city)

            elif user == "5":

                while True:
                    province = input("Insert Province: ")
                    if valProvince(province):
                        break
                    else:
                        print("Incorrect Province")
                student.setProvince(province)

            elif user == "6":

                while True:
                    email = input("Insert Email: ")
                    if valEmail(email):
                        break
                    else:
                        print("Incorrect Email")
                student.setEmail(email)
            
            control.modifyStudent(student)

        else:
            print("\nThere is no student with this DNI")
    

    elif user == "4":

        dni = input("\nInsert a DNI: ")
        student = control.getStudent(dni)
        if student != None:
            print("Information of student with DNI: " + dni)
            print("1.- Name: " + student.getName())
            print("2.- Surname: " + student.getSurnames())
            print("3.- Age: " + str(student.getAge()))
            print("4.- City: " + student.getCity())
            print("5.- Province: " + student.getProvince())
            print("6.- Email: " + student.getEmail())

        else:
            print("\nThere is no student with this DNI")
    
    elif user == "5":
        print("\nThat's all folks!!")
        break