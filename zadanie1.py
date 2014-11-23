# -*- coding: cp1250 -*-

plik = open('Mraz.txt', 'r')
tekst = plik.read()
print tekst
tekst = tekst.lower()

#Usunięcie znaków interpunkcyjnych
znakiInt = (',', '.', ':', ';', '-', '!', '?', '/', '!')
for i in znakiInt:
    tekst = tekst.replace(i, "")

liczbaWyr = {}
for wyraz in tekst.split():
    if wyraz not in liczbaWyr:
        liczbaWyr[wyraz] = 1
    else:
        liczbaWyr[wyraz] += 1
         
liczbaWyrLista = [(v,k) for k,v in liczbaWyr.items()]
#print liczbaWyrLista

liczbaWyrLista.sort(reverse=True)

zapis = open("statystyki.txt", "w")
zapis.writelines("Statystyki wyrazów danego pliku: \n")
for wyraz in liczbaWyrLista:
    stat = "%10s : %d" % (wyraz[1], wyraz[0]) + '\n'
#   print stat,
    zapis.writelines(stat)
zapis.close()



