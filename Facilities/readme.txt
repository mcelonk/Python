Skript je napsán v pythonu 3.6. Vybírá ze vstupní množiny bodù facilities podle (Dimitris Fotakis: Memoryless Facility Location in One Pass).
Tøída Facility vytváøí objekty s informací o centroidu [x,y,z] a radiusu.
Vstupní testovací body ve formátu xyz jsou naèteny do 2D pole, které je procházeno a vzniká podmnožina facilities na základì pravdìpodobnosti a vzdálenosti od již existujících facilities.
Input: test_15k_bez_duplicit.xyz
Output: facilities.csv

Ve složce je také soubor test_15k_bez_duplicit.csv ten slouží jako kontrolní pro naètení do GISu (ArcMap).