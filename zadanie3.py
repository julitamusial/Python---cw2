# -*- coding: cp1250 -*-
from math import sqrt

class LiczbaZespolona(object):
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im

    def get_Re(self):
        return self.__Re
    
    def set_Re(self, Re):
        return self.__Re
    
    def get_IM(self):
        return self.__Im

    def set_Im(self, Im):
        return self.__Im

    def dodajZespolone(self, LiczbaZespolona):
        suma = (self.Re + LiczbaZespolona.Re, self.Im + LiczbaZespolona.Im)
        print "Suma liczb zespolonych to: " + str(suma) + "i"
        return suma

    def odejmijZespolone(self, LiczbaZespolona):
        roznica = (self.Re - LiczbaZespolona.Re, self.Im - LiczbaZespolona.Im)
        print "Różnica liczb zespolonych to: " + str(roznica) + "i"
        return roznica
        

    def modulZespolona(self):
        modul = sqrt(self.Re**2 + self.Im**2)
        print "Moduł liczby zespolonej to: %s" % str(modul) + "i"
        return modul
        

    def podajLiczbe(self):
        if self.Im <0:
            znak = ""
        else:
            znak = "+"
        print "Liczba zespolona to: " + str(self.Re) + znak +  str(self.Im) + "i"
        



zespolona1 = LiczbaZespolona(2,-3)
zespolona2 = LiczbaZespolona(4,1)
zespolona1.dodajZespolone(zespolona2)
zespolona1.odejmijZespolone(zespolona2)
zespolona1.modulZespolona()
zespolona1.podajLiczbe()
zespolona2.podajLiczbe()
