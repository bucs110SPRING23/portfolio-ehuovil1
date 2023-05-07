import pygame
import requests
#import IqAir
from IqAir import IqAir
import IpBase


class Controller():
    def __init__(self):
        self.ip = IpBase.IpBase()
        self.air = IqAir()


    def main(self):
        self.air.get()
        cords = self.ip.get()
        self.ip.latlong(cords)
    

