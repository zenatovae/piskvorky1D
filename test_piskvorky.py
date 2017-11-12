from ai import tah_pocitace
from piskvorky1D import piskvorky1d, tah, vyhodnot, overeni_tahu_hrace

def test_vyhodnoceni_hry_x():
    assert vyhodnot("----xxx--oo-----x---") == "x"

def test_vyhodnoceni_hry_o():
    assert vyhodnot("----xx---ooo-----x---") == "o"

def test_vyhodnoceni_hry_plichta():
    assert vyhodnot("xxoxxooxoxoxxooxooxooxx") == "!"

def test_vyhodnoceni_hry_hra_neskoncila():
    assert vyhodnot("xxoxxooxoxoxxoo-ooxooxx") == "-"

def test_overeni_tahu_hrace_nula():
    assert overeni_tahu_hrace("----xx---ooo-----x---", -1) == "Nelze hrát na nultou pozici"

def test_overeni_tahu_hrace_zaporny():
    assert overeni_tahu_hrace("----xx---ooo-----x---", -2) == "Nelze hrát na zápornou pozici"

def test_overeni_tahu_hrace_mimo_pole():
    assert overeni_tahu_hrace("----xx---ooo-----x---", 25) == "Taková pozice v herním poli není"

def test_overeni_tahu_hrace_obsazeno():
    assert overeni_tahu_hrace("----xx---ooo-----x---", 5) == "Zadaná pozice je obsazená zkus to znovu "

def test_overeni_tahu_hrace_volno():
    assert overeni_tahu_hrace("----xx---ooo-----x---", 1) == None

def test_tah_na_prazdne_pole():
    retezec1D = tah("--------------------", 3, "o")
    assert len(retezec1D) == 20
    assert retezec1D.count('o') == 1
    assert retezec1D.count('-') == 19
    assert retezec1D.index("o") == 3

def test_tah_na_delsi_pole():
    retezec1D = tah("-------------------------", 23, "o")
    assert len(retezec1D) == 25
    assert retezec1D.count('o') == 1
    assert retezec1D.count('-') == 24
    assert retezec1D.index("o") == 23

def test_tah_pocitace_utok_xx_prazdno():
    assert tah_pocitace("----xx---oo------x---x", "x", "o") == 6

def test_tah_pocitace_obrana_prazdno_o_prazdno():
    assert tah_pocitace("----x----o---o---x----", "x", "o") == 10
