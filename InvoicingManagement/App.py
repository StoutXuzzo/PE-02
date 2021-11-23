from Controller import *
from Invoice import *
import matplotlib.pyplot as plt

def showInvoices(invoices):
    invo = []
    val = []
    for elem in invoices:
        invo.append(elem.getId())
        val.append(elem.getTotal())
    
    plt.bar(x=invo, height=val)
    plt.xlabel("Invoice ID: ")
    plt.ylabel("€")
    plt.show()

    print(elem.getId(), str(elem.getDate()), elem.getNif(), elem.getPaid(), elem.getBase(), elem.getTotal(), sep="\n")
    for pro in elem.getLines():
        print("      -" + pro[0], pro[1], pro[2])

ctrl = Controller()

while True:

    print("1.- Add invoice")
    print("2.- List not paid invoices: All and by Customer NIF ")
    print("3.- List paid invoices: All and by Customer NIF")
    print("4.- Pay invoice")
    print("5.- Exit")
    user = input("Select an option: ")

    if user == "1":
        nif = input("\nInsert the client NIF: ")
        print("Insert the products, the quantity and their total prices")

        products = []
        while True:
            name = input("Name: ")
            quantity = int(input("Quantity: "))
            price = int(input("Total Price: "))

            product = (name, quantity, price)
            products.append(product)

            user = input("You want to add more products? (0 to exit)")
            if user == "0":
                break

        invoice = ctrl.newInvoice(nif, products)
        
    elif user == "2":
        
        user = input("Insert a NIF or 0: ")
        if user == "0":
            invoices = ctrl.isPaid(False)
            
            showInvoices(invoices)
        else:
            invoices = ctrl.isPaidNif(False, user)
            showInvoices(invoices)

    elif user == "3":

        user = input("Insert a NIF or 0: ")
        if user == "0":
            invoices = ctrl.isPaid(True)
            
            showInvoices(invoices)
        else:
            invoices = ctrl.isPaidNif(True, user)
            showInvoices(invoices)

    elif user == "4":
        
        id = input("Insert the invoice ID: ")

        invoice = ctrl.getInvoice(int(id))
        if invoice != None:
            invoice.setAsPaid()
        else:
            print("This ID, doesn't exist")


    elif user == "5":
        break