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
            
def valDate():
    while True:
        date = input("Input Date (dd/mm/yyyy): ")
        try:
            date = date.split("/")
            date = datetime.date(int(date[2]), int(date[1]), int(date[0]))
            return date
        except:
            print("Incorrect Date")

def valEmail():
    while True:
        email = input("Input Email: ")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return email
        else:
            print("Incorrect Email")

def valString(value):
    while True:
        string = input("Input " + value + ": ")
        if len(string) > 0:
            return string
        else:
            print("Incorrect " + value)

def valInt(value):
    while True:
        num = input("Input " + value + ": ")
        try:
            num = int(num)
            return str(num)
        except:
            print("Incorrect " + value)

def valDouble(value):
    while True:
        num = input("Input " + value + ": ")
        try:
            num = float(num)
            return str(num)
        except:
            print("Incorrect " + value)