from IqAir import IqAir
import IpBase


class Controller():
    def __init__(self):
        self.ip = IpBase.IpBase()
        self.air = IqAir()

    def __str__(self):
        return f'Controller({self.ip}, {self.air})'

    def main(self):
        cords = self.ip.get()
        latlong = self.ip.latlong(cords)
        lat = latlong[0]
        long = latlong[1]
        response = self.air.get(lat, long)
        self.air.windcity(response)


