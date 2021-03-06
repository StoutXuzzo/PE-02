import requests, json
from SentimentAnalisis import valorarFrase
#import matplotlib.pyplot as plt

headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': "12a7bee204mshec6c495a21d90adp18d50ejsnbf40077fc112"
        }

def getCity(city):

    url = "https://hotels4.p.rapidapi.com/locations/v2/search"

    querystring = {"query":city ,"locale":"en_US","currency":"USD"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = dict(json.loads(response.content))

    return response["suggestions"][0]["entities"]

def getCloserHotels(cityId):

    url = "https://hotels4.p.rapidapi.com/properties/list"
    
    querystring = {"destinationId":cityId ,"pageNumber":"1","pageSize":"25","checkIn":"2020-01-08","checkOut":"2020-01-15","adults1":"1","sortOrder":"PRICE","locale":"en_US","currency":"USD"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = dict(json.loads(response.text))

    return response["data"]["body"]["searchResults"]["results"]
    
def getReviewData(hotelId):

    url = "https://hotels4.p.rapidapi.com/reviews/list"

    querystring = {"id": hotelId,"page":"1","loc":"en_US"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = dict(json.loads(response.content))

    return response["reviewData"]["guestReviewGroups"]["guestReviews"]

city = input("Insert the name of the city you want to go: ")

cities = getCity(city)

if len(cities) > 0:
    print("\nFound cities:")
    for i in range(len(cities)):
        print("    " + str(i + 1) + ".- " + cities[i]["name"])
    num = int(input("\nSelect an option: ")) - 1

    cityId = cities[num]["destinationId"]
    city = cities[num]["name"]
    hotels = getCloserHotels(cityId)

    print("\nThis are the 25 closest hotels to " + city + ":")
    for i in range(len(hotels)):
        print("    " + str(i+1)  + ".- " + hotels[i]["name"] + " in " + hotels[i]["neighbourhood"])
    num = int(input("\nSelect an option: ")) - 1

    hotelId = hotels[num]["id"]
    hotelName = hotels[num]["name"]

    reviews = getReviewData(hotelId)
    result = {"P+": 0, "P":0, "NEU":0 ,"N":0 ,"N+":0 ,"NONE":0}

    print()

    try:

        for e in reviews[0]["reviews"]:
            tmp = valorarFrase(e["summary"])

            if tmp == "P+":
                result["P+"] += 1
            elif tmp == "P":
                result["P"] +=1
            elif tmp == "NEU":
                result["NEU"] += 1
            elif tmp == "N":
                result["N"] += 1
            elif tmp == "N+":
                result["N+"] += 1
            else:
                result["NONE"] += 1
        
        print(result)
        
    except:
        print("The hotel don't have reviews")
        
else:
    print("No se han encontrado ciudades con ese nombre.")

