"""Tento program je zjednodušenou verzí 1D piškvorek"""

from ai import tah_pocitace

def vyhodnot(retezec1D):
    """Funkce vyhodnot zjistí zda vyhrály kolečka nebo křížky"""
    if "ooo" in retezec1D:
        return "o"
    elif "xxx" in retezec1D:
        return "x"
    elif "-" not in retezec1D:
        return "!"
    else:
        return "-"

def pozice_od_hrace():
    """Fuknce pozice od hrace se zeptá uživatele kam chce umístít svůj znak,
    ověří, že se jedná o číslo a pozici vrátí"""
    while True:
        try:
            cisloPolickaHrace = int(input("Na kolikáté místo v herním poli chceš umístit tvůj znak \"x\"? "))-1
        except ValueError:
            print("To není číslo")
        else:
            return cisloPolickaHrace

def overeni_tahu_hrace(retezec1D, cisloPolickaHrace):
    """Funkce overeni tahu hrace zjistí, zda je možné na zvolenou pozici hrát a
     pokud ne vratí řetězec s chybovou hláškou. Pokud lze tah provést, vrátí None """
    if  cisloPolickaHrace + 1 == 0:
        return "Nelze hrát na nultou pozici"
    elif cisloPolickaHrace + 1 < 0:
        return "Nelze hrát na zápornou pozici"
    elif len(retezec1D) < cisloPolickaHrace:
        return "Taková pozice v herním poli není"
    elif retezec1D[cisloPolickaHrace] != "-":
        return "Zadaná pozice je obsazená zkus to znovu "
    else:
        return None

def tah(retezec1D, cisloPolicka, symbolXO):
    """Funkce tah doplní do retezce1D symbol x nebo o na pozici číslo políčka"""
    return retezec1D[:cisloPolicka] + symbolXO + retezec1D[cisloPolicka + 1:]

def vrat_znak_hrace():
    """Funkce vrat_znak_hrace se zeptá uživatele za jáký symbol chce hrát a ověří zda jde
     o povolený znak. Na závěr vybraný validní znak vrátí """
    while True:
        znak_hrace = input("Chceš hrát za \"x\" nebo za \"o\"? ")
        if znak_hrace != "x" and znak_hrace != "o":
            print("Vybral si nepovolený znak")
            continue
        else:
            print("Hraješ za: " + znak_hrace)
            return znak_hrace

def vrat_herni_pole():
    """Funkce vrat_herni_pole se zeptá uživatele jak velké chce herní pole,
     toto pole vytvoří a následně vrátí """
    while True:
        try:
            delkaPole = int(input("Zadej velikost herního pole: "))
        except ValueError:
            print("To není číslo")
        else:
            retezec1D = "-"*delkaPole
            return retezec1D

def piskvorky1d():
    """Fukce piskovorky1d nejprve zavolá funkce vrat_znak_hrace a vrat_herni_pole,
    následně začne opakovaně volat pozice_od_hrace a overeni_tahu_hrace, dokud nezíská
    od uživatele validní odpověd a zavolá tah. Poté zavolá tah počítače a opět funkci tah.
    Tak pokračuje dokud není hra u konce. U konce je pokud někdo vyhraje nebo dojde k remíze """
    print("HRA PIŠKVORKY 1D")
    znak_hrace = vrat_znak_hrace()
    if znak_hrace == "x":
        znak_pocitace = "o"
    else:
        znak_pocitace = "x"
    retezec1D = vrat_herni_pole()
    print(retezec1D)
    while True:
        cisloPolickaHrace = pozice_od_hrace()
        overeni = overeni_tahu_hrace(retezec1D, cisloPolickaHrace)
        if overeni != None:
            print(overeni)
            continue
        print("Tvůj tah: ")
        retezec1D = tah(retezec1D, cisloPolickaHrace, znak_hrace)
        print(retezec1D)
        vysledek_hry = vyhodnot(retezec1D)
        if vysledek_hry != "-":
            break
        cisloPolickaPocitace = tah_pocitace(retezec1D, znak_pocitace, znak_hrace)
        print("Tah počítače: ")
        retezec1D = tah(retezec1D, cisloPolickaPocitace, znak_pocitace)
        print(retezec1D)
        vysledek_hry = vyhodnot(retezec1D)
        if vysledek_hry != "-":
            break
    if vysledek_hry == "!":
        print(retezec1D)
        print("Hra skončila remízou" + vysledek_hry)
    else:
        print(retezec1D)
        print("Hra je u konce. Vyhrál hráč s " + vysledek_hry + ".")
