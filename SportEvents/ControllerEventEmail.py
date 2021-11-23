from ControllerEvent import *
import requests

class ControllerEventEmail(ControllerEvent):

    def __init__(self):
        super().__init__()  

    def addParticipant(self, id, participant):
        if super().addParticipant(id, participant):

            url = "https://email-sender1.p.rapidapi.com/"

            payload = {}

            headers = {
                'content-type': "application/json",
                'x-rapidapi-host': "email-sender1.p.rapidapi.com",
                'x-rapidapi-key': "12a7bee204mshec6c495a21d90adp18d50ejsnbf40077fc112"
                }

            querystring = {"txt_msg":"You have been succesfully subscribed to an event!","to":participant[-1],
            "from":"Auto email sender","subject":"test of the subject","bcc":"bcc-mail@gmail.com",
            "reply_to":"reply-to@gmail.com"}

            response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
            return True
        return False

