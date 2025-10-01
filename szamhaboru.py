"""Követelmények:
Bevezetés


A program üdvözölje a játékost, pl.:
 "Üdv a Számháború játékban!"


Játékos választása


A felhasználó írjon be egy számot 1–6 között.
Ha nem megfelelő számot ad meg (pl. 0 vagy 9), figyelmeztesse: "Csak 1 és 6 közötti számot adhatsz meg!"


Gép választása


A számot a gép véletlenszerűen válassza 1-6 között.


Győztes eldöntése (if/elif/else)


Ha a játékos száma > gép száma → "Nyertél!"
Ha a játékos száma < gép száma → "Vesztettél!"
Ha a kettő egyenlő → "Döntetlen!"


Pontszám nyilvántartása


A játék folyamán tárolni kell, hogy hányat nyert, vesztett és döntetlenezett a játékos.


Újra játszás


Minden kör után kérdés: "Szeretnél újra játszani? (i/n)"
Ha n, a program írja ki az összesített eredményt, pl.:
 "Végső eredmény: 3 nyerés, 2 vereség, 1 döntetlen."



Példa a program futtatására:
Üdv a Számháború játékban!

Adj meg egy számot 1 és 6 között: 4
A gép száma: 2
Nyertél!
Eddigi eredmény: 1 nyerés, 0 vereség, 0 döntetlen

Szeretnél újra játszani? (i/n) i
Adj meg egy számot 1 és 6 között: 6
A gép száma: 6
Döntetlen!
Eddigi eredmény: 1 nyerés, 0 vereség, 1 döntetlen

Szeretnél újra játszani? (i/n) n
Végső eredmény: 1 nyerés, 0 vereség, 1 döntetlen
Köszi a játékot!

"""
import random
print("Üdv a Számháború játékban!")
nyereseg = 0
vereseg = 0
dontetlen = 0
while True:
    while True:
        szam = int(input("Adj meg egy számot 1 és 6 között: "))
        if 1 <= szam <= 6:
            break
        print("Csak 1 és 6 közötti számot adhatsz meg!")
    gep_szam = random.randint(1, 6)
    print(f"A gép száma: {gep_szam}")
    if szam > gep_szam:
        print("Nyertél!")
        nyereseg += 1
    elif szam < gep_szam:
        print("Vesztettél!")
        vereseg += 1
    else:
        print("Döntetlen!")
        dontetlen += 1
    print(f"Eddigi eredmény: {nyereseg} nyerés, {vereseg} vereség, {dontetlen} döntetlen")
    ujra = input("Szeretnél újra játszani? (i/n) ")
    if ujra.lower() != 'i':
        break
print(f"Végső eredmény: {nyereseg} nyerés, {vereseg} vereség, {dontetlen} döntetlen")
print("Köszi a játékot!")
