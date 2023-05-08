import ipbase

class IpBase():

    def __init__(self):
        self.url = "https://api.ipbase.com/v2/info?apikey=euAa9RLA1fIslgRXQj5EM8pHCihQVN40iPSedzca&ip=1.1.1.1"
        # API KEY (IP Location): euAa9RLA1fIslgRXQj5EM8pHCihQVN40iPSedzca

    def __str__(self):
        return f'IpBase({self.url})'
        
    def get(self):
        client = ipbase.Client('euAa9RLA1fIslgRXQj5EM8pHCihQVN40iPSedzca')
        result = client.info()
        return(result)

    def latlong(self, result):
        latdata = result['data']
        latlocation = latdata['location']
        lat = latlocation['latitude']
        # unwrapping the json dictionary to find the latitude

        longdata = result['data']
        longlocation = longdata['location']
        long = longlocation['longitude']
        # unwrapping the json dictionary to find the latitude

        print("Latitude: " + str(lat))
        print("Longitude: " + str(long))
        return[lat, long]
        