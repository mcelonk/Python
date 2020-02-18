Skript je napsán v pythonu 3.6. Vybírá ze vstupní množiny bodù facilities podle (Dimitris Fotakis: Memoryless Facility Location in One Pass).
Tøída Facility vytváøí objekty s informací o centroidu [x,y,z] a radiusu.
Vstupní testovací body ve formátu xyz jsou naèteny do 2D pole, které je procházeno a vzniká podmnožina facilities na základì pravdìpodobnosti a vzdálenosti od již existujících facilities.
Input: test_15k_bez_duplicit.xyz
Output: *Input*_test.csv

Ve složce je také soubor test_15k_bez_duplicit.csv ten slouží jako kontrolní pro naètení do GISu (ArcMap).
Soubor BILO48_5g.xyz pøedstavuje bodové mraèno v oblasti mapového listu BILO48, obsahuje pøibližnì 450 000 bodù.
Skript testován na datech se 40 000 body, doba zpracování v øádu minut.