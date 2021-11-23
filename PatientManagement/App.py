from Patient import *
from Controller import *
import datetime, re

def valDni():
    code = "TRWAGMYFPDXBNIZSQVHLCKE"

    while True:
        dni = input("Input DNI: ")

        dniNum = dni[:-1]

        if dni[:-1].isdigit() and len(dni) == 9:

            dniNum = int(dniNum)

            num = dniNum % 23
            if dni[-1] == code[num]:
                return dni
            else:
                print("Incorrect DNI")
        else:
            print("Incorrect DNI")
                

def valName():
    while True:
        name = input("Input Name: ")
        if len(name) > 0:
            return name
        else:
            print("Incorrect Name.")
                

def valSurnames():
    surname = input("Input Surname:")
    if len(surname) > 0:
        return surname
    else:
        print("Incoreect Surname")

def valDate():
    while True:
        date = input("Input birth date (dd/mm/yyyy): ")
        try:
            date = date.split("/")
            date = datetime.date(int(date[2]), int(date[1]), int(date[0]))
            return date
        except:
            print("Incorrect Date")

def valPhone():
    while True:
        num = input("Input Phone: ")
        try:
            num = int(num)
            return str(num)
        except:
            print("Incorrect Phone")

def valEmail():
    while True:
        email = input("Input Email: ")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return email
        else:
            print("Incorrect Email")

ctrl = Controller()

while True:
    print("\nMatias Polyclinic")
    print("Currently there are " + str(ctrl.getTotal()) + " registered patients.")
    print("1.- Add Patient")
    print("2.- Delete Patient")
    print("3.- Get Patient History")
    print("4.- List patients")
    print("5.- Add appointment")
    print("6.- Exit")
    user = input("Choose option: ")

    if user == "1":

        print("\nAdding patient")

        dni = valDni()
        name = valName()
        surname = valSurnames()
        born = valDate()
        phone = valPhone()
        mail = valEmail()

        patient = Patient(dni, name, surname,born, phone, mail)

        if ctrl.addPatient(patient):
            print("\nPacient added successfully!")
        else:
            print("\nThis pacient alreadi exist.")

    elif user == "2":

        print("\nDeleting patient")
        dni = input("Input DNI: ")   

        if ctrl.deletePatient(dni):
            print("\nPatient successfully deleted.")     
        else:
            print("\nThis pacient doesn't exist.")

    elif user == "3":

        print("\nShowing a patient:")
        dni = input("Input DNI: ")

        patient = ctrl.getPatient(dni)

        print("Name: " + patient.getName())
        print("Surname: " + patient.getSurname())
        print("Birth date: " + str(patient.getBorn()))
        print("Phone: " + patient.getPhone())
        print("email: " + patient.getMail())
        print("Number of visits:" + str(patient.getNumVisits()))
        print("History: ")

        for elem in patient.getVisits():
            print("\t -" + str(elem))

    elif user == "4":
        
        print("\nPatients: ")
        patients = ctrl.getAllPatients()

        for key in patients.keys():
            print("  -" + patients[key].getDni(), patients[key].getName(), patients[key].getSurname())

    elif user == "5":
        
        print("\nAdding Appointment")
        dni = input("Input DNI: ")

        patient = ctrl.getPatient(dni)

        print("Name: " + patient.getName())
        print("Surname: " + patient.getSurname())
        print("Birth date: " + str(patient.getBorn()))
        print("Phone: " + patient.getPhone())
        print("email: " + patient.getMail())
        print("Number of visits:" + str(patient.getNumVisits()))
        print("History: ")

        for elem in patient.getVisits():
            print("     -" + str(elem))

        description = input("Input Appointment: ")

        fecha = datetime.datetime.now()
        fecha = fecha.strftime("%d/%m/%Y %H:%M")

        info = str(fecha) + " - " + description

        ctrl.addVisit(dni, info)

        #patient.addVisit(str(fecha) + " - " + description)

    elif user == "6":
        break