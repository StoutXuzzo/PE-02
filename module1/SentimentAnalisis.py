from typing import Text
import requests, json

def valorarFrase(text):

    if len(text) == 0:
        return "NONE"

    url = "https://api.meaningcloud.com/sentiment-2.1"
    payload={
        'key': '73c7425b3a9fec1ba6b3dd4db4840442',
        'txt': text,
        'lang': 'en',
    }

    response = requests.post(url, data = payload)
    response = json.loads(response.content)
    return response["sentence_list"][0]["score_tag"]