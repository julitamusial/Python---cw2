 #-*- coding: cp1250 -*-

menu = {}
karta= open("menu.txt", 'r')
for i in karta:
    item = i.split()
    k,v = item[0], item[1]
    menu[k] = float(v)
#print menu

def rachunek(order):
    bill = 0
    for i in order:
        if i in menu:
            bill = bill + menu[i]

    print "Warto�� zam�wienia wynosi: %s" % bill  + " z�"
    
    tip = (bill*0.15)
    print "Napiwek wynosi: %s" % tip  + " z�"
    
    print "Kwota ko�cowa rachunku: %s" % (bill+tip) + " z�"
    return

order1 = ["sushi", "zupa", "frytki"]

print "Zam�wienie: " + str(order1)
print rachunek(order1)

karta.close()

