Skript je naps�n v pythonu 3.6. Vyb�r� ze vstupn� mno�iny bod� facilities podle (Dimitris Fotakis: Memoryless Facility Location in One Pass).
T��da Facility vytv��� objekty s informac� o centroidu [x,y,z] a radiusu.
Vstupn� testovac� body ve form�tu xyz jsou na�teny do 2D pole, kter� je proch�zeno a vznik� podmno�ina facilities na z�klad� pravd�podobnosti a vzd�lenosti od ji� existuj�c�ch facilities.
Input: test_15k_bez_duplicit.xyz
Output: *Input*_test.csv

Ve slo�ce je tak� soubor test_15k_bez_duplicit.csv ten slou�� jako kontroln� pro na�ten� do GISu (ArcMap).
Soubor BILO48_5g.xyz p�edstavuje bodov� mra�no v oblasti mapov�ho listu BILO48, obsahuje p�ibli�n� 450 000 bod�.
Skript testov�n na datech se 40 000 body, doba zpracov�n� v ��du minut.