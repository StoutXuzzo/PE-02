from PatientV2 import *
from ControllerV2 import *
import Validations as val
import datetime, re

ctrl = ControllerV2()

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

        dni = val.valDni()
        name = val.valString("Name")
        surname = val.valString("Surname")
        born = val.valDate()
        phone = val.valInt("Phone")
        mail = val.valEmail()
        height = val.valDouble("Height")
        weight = val.valDouble("Weight")

        if ctrl.addPatient(dni, name, surname, born, phone, mail, height, weight):
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
        print("Age: " + str(patient.getAge()))
        print("Height: " + str(patient.getHeight()))
        print("Weight: " + str(patient.getWeight()))
        print("Health: " + patient.getHealth())
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

    elif user == "6":
        break