# -*- coding: cp1250 -*-

#Przepraszam, �e wrzucam zadanie po czasie, ale nie zauwa�y�am wcze�niej,
#�e doda�am pusty plik zamiast pliku z rozwi�zaniem tego zadania.

class Pisarz (object):
    def __init__(self, imie, nazwisko, tytul):
        self.imie = imie
        self.nazwisko = nazwisko
        self.tytul = tytul

    def get_imie(self):
        return self.imie
    def set_imie(self, imie):
        self._imie = imie
    def get_nazwisko(self):
        return self.nazwisko
    def set_nazwisko(self, nazwisko):
        self._nazwisko = nazwisko
    def get_tytul(self):
        return self.tytul
    def set_tytul(self, tytul):
        self._tytul = tytul
        
    def piszKsiazke(self):
        print "Nazywam si� " + str(self.imie) + " " + str(self.nazwisko) + " i pisz� ksi��k� pod tytu�em '" + str(self.tytul) + "'."


class Ksiazka (Pisarz):
    def __init__(self, imie, nazwisko, tytul, liczbaStron, okladka):
        Pisarz.__init__(self, imie, nazwisko, tytul)
        self.liczbaStron = liczbaStron
        self.okladka = okladka


    def get_liczbaStron(self):
        return self.liczbaStron
    def set_liczbaStron(self, liczbaStron):
        self._liczbaStron = liczbaStron
    def get_okladka(self):
        return self.okladka
    def set_okladka(self, okladka):
        self._okladka = okladka

    def nazwaKsiazki(self):
        print "Ta ksi��ka nosi tytu�: " + str(self.tytul) + ", ma " + str(self.liczbaStron) + " stron i ma " + str(self.okladka) + " ok�adk�."

    def czyDluga(self):
        if self.liczbaStron < 50:
            print "Kr�ciutka ta ksi��ka... tylko " + str(self.liczbaStron) + " strony."
        else:
            print "Ta ksi��ka jest bardzo d�uga. Ma " + str(self.liczbaStron)  + " stron."

    def doTorebki(self):
        if self.liczbaStron > 200 and self.okladka == "twarda":
            print "Ksi��ka jest zbyt du�a i ci�ka �eby j� nosi� w torebce."
        elif self.liczbaStron > 200 and self.okladka == "miekka":
            print "W sumie mo�na j� wsadzi� do torebki i poczyta� w tramwaju."
        else:
            print "Idealna ksi��ka do noszenia w torbie!"



class KsiazkaDlaDzieci(Ksiazka):
    def __init__(self, imie, nazwisko, tytul, liczbaStron, okladka, koloroweObrazki):
        Ksiazka.__init__(self, imie, nazwisko, tytul, liczbaStron, okladka)
        self.koloroweObrazki = koloroweObrazki
        
    def get_koloroweObrazki(self):
        return self.koloroweObrazki
    def set_koloroweObrazki(self, koloroweObrazki):
        self._koloroweObrazki = koloroweObrazki


    def maleDzieci(self):
        if self.koloroweObrazki == True:
            print "Ta ksi�zka spodoba si� dzieciakom!"
        else:
            print "Bez obrazk�w ksi��ka jest smutna..."


class Ksiegarnia(KsiazkaDlaDzieci, Ksiazka):
    def __init__(self, imie, nazwisko, tytul, liczbaStron, okladka, koloroweObrazki, nazwa, miasto):
        Ksiazka.__init__(self, imie, nazwisko, tytul, liczbaStron, okladka)
        KsiazkaDlaDzieci.__init__(self, imie, nazwisko, tytul, liczbaStron, okladka, koloroweObrazki)
        self.nazwa = nazwa
        self.miasto = miasto

    def get_nazwa(self):
        return self.nazwa
    def set_nazwa(self,nazwa):
        self.nazwa = nazwa
    def get_miasto(self):
        return self.miasto
    def set_miasto(self,miasto):
        self.miasto = miasto
        
    def nazwaKsiegarni(self):
        print "Witamy w ksi�garni " + self.nazwa + ". Nasz sklep znajduje si� w mie�cie " + self.miasto + "." 

    def sprzedaj(self, KsiazkaDlaDzieci):
        print "W sprzeda�y jest ksi��ka dla dzieci pt: " + KsiazkaDlaDzieci.tytul + ", autor: " + KsiazkaDlaDzieci.imie + " "+  KsiazkaDlaDzieci.nazwisko 





Pasek = Pisarz('Adam', 'Pasek', 'Za gorami za lasami')
Pasek.piszKsiazke()

powiesc = Ksiazka('Karol', 'Robak','Krol Lew', 22, 'twarda')
powiesc.nazwaKsiazki()
powiesc.czyDluga()
powiesc.doTorebki()
powiesc.doTorebki()

bajka = KsiazkaDlaDzieci('Tove', 'Jansson','Muminki', 23, 'miekka', True)
bajka.maleDzieci()

Matras = Ksiegarnia('Tove', 'Jansson','Muminki', 23, 'miekka', True, 'Book4U' , 'Wroclaw')
Matras.nazwaKsiegarni()
Matras.sprzedaj(bajka)
