import ipbase
import requests
import json

class IpBase():

    def __init__(self):
        self.url = "https://api.ipbase.com/v2/info?apikey=euAa9RLA1fIslgRXQj5EM8pHCihQVN40iPSedzca&ip=1.1.1.1"
        # API KEY (IP Location): euAa9RLA1fIslgRXQj5EM8pHCihQVN40iPSedzca

    def get(self):
        client = ipbase.Client('euAa9RLA1fIslgRXQj5EM8pHCihQVN40iPSedzca')
        result = client.info()
        return(result)

    def latlong(self, result):
        dictionary = json.dumps(result)
        Latitude = dictionary.data.location.latitude
        Longitude = dictionary.data.location.longitude
        print("Latitude: " + Latitude)
        print("Longitude: " + Longitude)

        