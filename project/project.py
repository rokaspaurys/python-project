import json
import os
import datetime
import pyllist
from pyllist import dllist


clear = lambda: os.system('cls')

def choices():
    print('   Savaitės darbo planas')
    print('(1) Nuskaityti tvarkaraštį')
    print('(2) Rodyti tvarkaraštį')
    print('(3) Ištrinti treniruotę')
    print('(4) Pridėti treniruotę')
    print('(5) Pakeisti informaciją')
    print('(6) Surasti klientą')
    print('(7) Išsaugoti')
    print('(0) exit')


def nuskaitymas(x):
    lst = dllist([])
    with open(x+'.json', 'r') as file:
        temp = json.load(file)
        for ivedimas in temp:
            lst.append(ivedimas)
    print('Tvarkaraštis nuskaitytas')
    return lst


def rodymas(lst):
    i = 1
    print('                                 Treniruočių sąrašas')
    print("Nr. Data          Laikas        Vardas        Pavardė       Pratimai")
    print('----------------------------------------------------------------------------------------------------------')
    for item in lst:
        if i < 10:
            print(i, " ", item['Data'], " " * (12 - len(item['Data'])), item['Laikas'],
                " " * (12 - len(item['Laikas'])), item['Vardas'], " " * (12 - len(item['Vardas'])), item['Pavarde'],
                " " * (12 - len(item['Pavarde'])), item['Pratimai'], " " * (12 - len(item['Pratimai'])))
        elif i < 100:
            print(i, "", item['Data'], " " * (12 - len(item['Data'])), item['Laikas'],
                  " " * (12 - len(item['Laikas'])), item['Vardas'], " " * (12 - len(item['Vardas'])), item['Pavarde'],
                  " " * (12 - len(item['Pavarde'])), item['Pratimai'], " " * (12 - len(item['Pratimai'])))
        i = i + 1

def istrinti(lst, pos):
    if int(pos) > lst.size:
        print('Klaida! Bandykite darkart.')
    else:
        pos = int(pos)-int(1)
        node = lst.nodeat(int(pos))
        lst.remove(node)
    return lst


def prideti(lst, pos):
    if int(pos) - int(1) <= lst.size:
        info = {}
        info['Data'] = input('Įveskite datą:  ')
        info['Laikas'] = input('Įveskite laiką:  ')
        info['Vardas'] = input('Įveskite vardą:  ')
        info['Pavarde'] = input('Įveskite pavardę:  ')
        info['Pratimai'] = input('Įveskite pratimus:  ')
        if int(pos) <= lst.size:
            pos = int(pos) - int(1)
            lst.insert(info, lst.nodeat(int(pos)))
        elif int(pos)-int(1) == lst.size:
            lst.appendright(info)
    else:
        print('Klaida! Bandykite darkart.')
    return lst


def pakeisti(lst, pos):
    print('Duomenų redagavimas:')
    data = input('Nauja data:  ')
    laikas = input('Naujas laikas:  ')
    vardas = input('Naujas vardas:  ')
    pavarde = input('Nauja pavardė:  ')
    pratimai = input('Nauji pratimai:  ')
    temp = {'Data': data, 'Laikas': laikas, 'Vardas': vardas, 'Pavarde': pavarde, 'Pratimai': pratimai}
    pos = int(pos) - int(1)
    if int(pos) <= lst.size:
        lst.insert(temp, lst.nodeat(int(pos)))
        pos = int(pos)+int(2)
        istrinti(lst, pos)
    else:
        print('Klaida! Bandykite darkart.')
    return lst

def surasti(lst):
    print('     Kliento paieška')
    klientas = input('Įveskite vardą ir pavardę:  ')
    temp = []
    for item in lst:
        if item['Vardas'] + ' ' + item['Pavarde'] == klientas:
            data = item['Data']
            laikas = item['Laikas']
            pratimai = item['Pratimai']
            temp.append({'Data': data, 'Laikas': laikas, 'Pratimai': pratimai})
    print('(1) Išvesti į ekraną')
    print('(2) Išvesti į dokumentą')
    print('(3) Sugeneruoti pratimų ataskaitą')
    pas = input('Pasirinkite:  ')
    if pas == '1':
        print("Kliento", klientas, "treniruotės:")
        print("Nr. Data          Laikas        Pratimai")
        print('----------------------------------------------------------------------------------------------------------------------------------------')
        i = 1
        for item in temp:
            data = item['Data']
            laikas = item['Laikas']
            pratimai = item['Pratimai']
            print(i, " ", data, " " * (12 - len(data)), laikas, " " * (12 - len(laikas)), pratimai, " " * (12 - len(pratimai)))
            i = i + 1
    if pas == '2':
        x = input('Įveskite dokumento pavadinimą:   ')
        with open(x+'.json', 'w') as file:
            for item in temp:
                json.dump(item, file)
        print('Sėkmingai išvesta į', x+'.json', 'dokumentą.')
    if pas == '3':
        ats = []
        for item in lst:
            if item['Vardas'] + ' ' + item['Pavarde'] == klientas:
                pratimai = item['Pratimai']
                ats.append({'Pratimai': pratimai})
        with open(klientas+'Ataskaita.json', 'w') as file:
            json.dump(ats, file)
        print('Kliento', klientas, 'ataskaita išsaugota')
    else:
        print('Klaida! Bandykite darkart.')

def issaugoti(lst, x):
    temp = []
    for item in lst:
        temp.append(item)
    with open(x+'.json', 'w') as file:
        json.dump(temp, file, indent=4)
    print('Sėkmingai išsaugota.')
    del temp


choices()
print("Treniruočių nėra! Nuskaitykite treniruočių tvarkaraštį.")
while True:
    choice = input('Pasirinkite operaciją:   ')
    clear()
    choices()
    if choice == '1':
        x = input('Įveskite failo pavadinimą:  ')
        lst = nuskaitymas(x)
    elif choice == '2':
        rodymas(lst)
    elif choice == '3':
        rodymas(lst)
        pos = input('Pasirinkite treniruote, kurią norite ištrinti:  ')
        lst = istrinti(lst, pos)
    elif choice == '4':
        rodymas(lst)
        pos = input('Pasirinkite vietą, į kurią norite pridėti treniruotę:  ')
        lst = prideti(lst, pos)
    elif choice == '5':
        rodymas(lst)
        print('Kurios treniruotes duomenis norite pakeisti? ')
        pos = input('Pasirinkite numerį:  ')
        lst = pakeisti(lst, pos)
    elif choice == '6':
        rodymas(lst)
        surasti(lst)
    elif choice == '7':
        issaugoti(lst, x)
    elif choice == '0':
        issaugoti(lst, x)
        break
    else:
        print("Klaidingas numeris: bandykite darkart.")