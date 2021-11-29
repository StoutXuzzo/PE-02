from Controller import *
from datetime import date
from PatientV2 import *
import requests
import json

class ControllerV2(Controller):
    def __init__(self):
        super().__init__()

    def addPatient(self, dni, name, surname, born, phone, mail, height, weight):
        today = date.today()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        url = "https://fitness-calculator.p.rapidapi.com/bmi"

        querystring = {"age":str(age),"weight":str(weight),"height":str(height)}

        headers = {
            'x-rapidapi-host': "fitness-calculator.p.rapidapi.com",
            'x-rapidapi-key': "12a7bee204mshec6c495a21d90adp18d50ejsnbf40077fc112"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        health = json.loads(response.text)

        try:
            health = health.json()["data"]["health"]
        except:
            health = "Error, height and weight are not valid"

        patient = PatientV2(dni, name, surname, born, phone, mail, age, height, weight, health)

        super().addPatient(patient)