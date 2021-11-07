import http.client

conn = http.client.HTTPSConnection("hotels4.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "hotels4.p.rapidapi.com",
    'x-rapidapi-key': "12a7bee204mshec6c495a21d90adp18d50ejsnbf40077fc112"
    }

conn.request("GET", "/properties/list?destinationId=1506246&pageNumber=1&pageSize=25&checkIn=2020-01-08&checkOut=2020-01-15&adults1=1&sortOrder=PRICE&locale=en_US&currency=USD", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))