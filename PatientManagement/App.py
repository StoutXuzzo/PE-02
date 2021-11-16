from Patient import *
from Controller import *

ctrl = Controller()

while True:
    print("Matias Polyclinic")
    print("Currently there are 0 registered patients.")
    print("1.- Add Patient")
    print("2.- Delete Patient")
    print("3.- Get Patient History")
    print("4.- List patients")
    print("5.- Add appointment")
    print("6.- Exit")
    user = input("Choose option: ")

    if user == "1":
        print("Adding patient")
        dni = input("Input DNI: ")
        name = input("Input Name: ")
        surname = input("Input Surname: ")
        phone = input("Input phone: ")
        mail = input("Inout email: ")

        patient = Patient(dni, name, surname, phone, mail)

        print("Pacient added successfully!")
    elif user == "2":
        pass
    elif user == "3":
        pass
    elif user == "4":
        pass
    elif user == "5":
        pass
    elif user == "6":
        break