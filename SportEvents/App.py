from ControllerEventEmail import *
from Event import *
import Validations as val

ctrl = ControllerEventEmail()

ctrl.addEvent("Pachanga", "1995-12-12", "Alzira", "Valencia", "25.6")
participant = ("20845437P", "Josep", "26", "josepteleco@gmail.com")
ctrl.addParticipant(0, participant)
participant = ("20845437P", "Juan", "26", "asd@asd.asd")
ctrl.addParticipant(0, participant)
participant = ("20845437P", "Lopez", "26", "asd@asd.asd")
ctrl.addParticipant(0, participant)

while True:
    print("\n1.- Add Event")
    print("2.- Add participant to an event")
    print("3.- List pending events with participants")
    print("4.- List events finished with podium")
    print("5.- Finish an event")
    print("6.- Exit")
    user = input("Select an option: ")

    if user == "1":
        print("\n1.- Add Event:")
        name = val.valString("Event Name")
        date = val.valDate()
        location = val.valString("Location")
        province = val.valString("Province")
        price = val.valDouble("Registration Price")

        if ctrl.addEvent(name, date, location, province, price):
            print("Event succesfully added")
        else:
            print("Error adding Event")

    elif user == "2":
        print("\n2.- Add participant to an event")
        events = ctrl.getEvents()

        cont = 1
        for event in events:
            print("\t" + str(cont) + ".- " + str(event))
            cont += 1

        while True:
            try:
                user = int(input("Select an event: ")) - 1
                event = events[user]
                break
            except:
                print("Event not valid")

        print("\nCreate participant: ")
        dni = val.valDni()
        name = val.valString("Name")
        age = val.valInt("Age")
        email = val.valEmail()

        participant = (dni, name, age, email)
        
        if ctrl.addParticipant(user, participant):
            print("Participant succesfully added")
        else:
            print("Error adding the new participant")

    elif user == "3":
        print("\n3.- List pending events with participants")
        for event in ctrl.getNoFinishEvents():
            print(event)
    
    elif user == "4":
        print("\n4.- List events finished with podium")
        for event in ctrl.getFinishEvents():
            print(event)
    
    elif user == "5":
        print("\n5.- Finish an event")
        events = ctrl.getEvents()

        cont = 1
        for event in events:
            if not event.getState():
                print("\t" + str(cont) + ".- " + str(event))
            cont += 1

        while True:
            try:
                user = int(input("Select an event: ")) - 1
                event = events[user]
                break
            except:
                print("Event not valid")

        finished = ctrl.finishEvent(user)

        if finished != False:
            print("Event finished succesfully:")
            print(str(finished))
        else:
            print("The event was canceled")

    elif user == "6":
        break