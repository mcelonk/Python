Master:
Skript je napsán v pythonu 3.6. Vybírá ze vstupní množiny bodù facilities podle (Dimitris Fotakis: Memoryless Facility Location in One Pass).
Tøída Facility vytváøí objekty s informací o centroidu [x,y,z] a radiusu.
Vstupní testovací body ve formátu xyz jsou naèteny do 2D pole, které je procházeno a vzniká podmnožina facilities na základì pravdìpodobnosti a vzdálenosti od již existujících facilities.
Input: test_15k_bez_duplicit.xyz
Output: *Input*_test.csv

Verze: 0.2
Ve složce je také soubor test_15k_bez_duplicit.csv ten slouží jako kontrolní pro naètení do GISu (ArcMap).
Soubor BILO48_5g.xyz pøedstavuje bodové mraèno v oblasti mapového listu BILO48, obsahuje pøibližnì 450 000 bodù.
Skript testován na datech se 40 000 body, doba zpracování v øádu minut.

Verze: 0.3
Byl pøidán matlab skript normals.m pro výpoèet normál jednotlivých bodù v bodovém mraènu. Výpoèet je provádìn ze 6 nejbližších bodù. 
Dojde k vytvoøení Normaly.txt souboru, který slouží jako vstup pro python skript Facilities.py.
!!! Dùležité je nastavení stejného vstupního bodového mraèna v matlabu i python skriptu.

Verze: 0.4
Jedná se o verzi 0.2, pokus o pøidání poètu bodù pro jednotlivé facility

Další možnosti vylepšení:
Pøedávání informace o vstupním bodovém mraènu z matlabu do pythonu
Vytváøení souboru s normálami pouze doèasnì
Pøevedení do jednoho programu