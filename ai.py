
from random import randrange

def tah_pocitace(retezec1D, znak_pocitace, znak_hrace):
    """Funkce tah_pocitace vygeneruje náhodnou pozici a ověří, zda už není obsazena.
    Pokud není zavolá funkci tah """
    if len(retezec1D) == 0:
        raise ValueError("Hrací pole má délku nula")
    if "-" not in retezec1D:
        raise ValueError("Hrací pole je už obsazené")
    utok = retezec1D.find(znak_pocitace + znak_pocitace + "-")
    if utok != -1:
        return utok+2
    utok = retezec1D.find(znak_pocitace + "-" + znak_pocitace)
    if utok != -1:
        return utok+1
    utok = retezec1D.find("-" + znak_pocitace + znak_pocitace)
    if utok != -1:
        return utok

    obrana = retezec1D.find(znak_hrace + znak_hrace + "-")
    if obrana != -1:
        return obrana+2
    obrana = retezec1D.find(znak_hrace + "-" + znak_hrace)
    if obrana != -1:
        return obrana+1
    obrana = retezec1D.find("-" + znak_hrace + znak_hrace)
    if obrana != -1:
        return obrana
    obrana = retezec1D.find("-" + znak_hrace + "-")
    if obrana != -1:
        return obrana + 2

    utok2 = retezec1D.find(znak_pocitace + "--")
    if utok2 != -1:
        return utok2+1
    utok2 = retezec1D.find("--" + znak_pocitace)
    if utok2 != -1:
        return utok2+1

    while True:
        cisloPolickaPocitace = randrange(0, len(retezec1D))
        if retezec1D[cisloPolickaPocitace] != "-":
            continue
        else:
            return cisloPolickaPocitace

#print(tah_pocitace("-----xxoo---xx--oo--"))
