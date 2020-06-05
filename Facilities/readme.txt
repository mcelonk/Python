Master:
Skript je naps�n v pythonu 3.6. Vyb�r� ze vstupn� mno�iny bod� facilities podle (Dimitris Fotakis: Memoryless Facility Location in One Pass).
T��da Facility vytv��� objekty s informac� o centroidu [x,y,z] a radiusu.
Vstupn� testovac� body ve form�tu xyz jsou na�teny do 2D pole, kter� je proch�zeno a vznik� podmno�ina facilities na z�klad� pravd�podobnosti a vzd�lenosti od ji� existuj�c�ch facilities.
Input: test_15k_bez_duplicit.xyz
Output: *Input*_test.csv

Verze: 0.2
Ve slo�ce je tak� soubor test_15k_bez_duplicit.csv ten slou�� jako kontroln� pro na�ten� do GISu (ArcMap).
Soubor BILO48_5g.xyz p�edstavuje bodov� mra�no v oblasti mapov�ho listu BILO48, obsahuje p�ibli�n� 450 000 bod�.
Skript testov�n na datech se 40 000 body, doba zpracov�n� v ��du minut.

Verze: 0.3
Byl p�id�n matlab skript normals.m pro v�po�et norm�l jednotliv�ch bod� v bodov�m mra�nu. V�po�et je prov�d�n ze 6 nejbli���ch bod�. 
Dojde k vytvo�en� Normaly.txt souboru, kter� slou�� jako vstup pro python skript Facilities.py.
!!! D�le�it� je nastaven� stejn�ho vstupn�ho bodov�ho mra�na v matlabu i python skriptu.

Verze: 0.4
Jedn� se o verzi 0.2, pokus o p�id�n� po�tu bod� pro jednotliv� facility

Dal�� mo�nosti vylep�en�:
P�ed�v�n� informace o vstupn�m bodov�m mra�nu z matlabu do pythonu
Vytv��en� souboru s norm�lami pouze do�asn�
P�eveden� do jednoho programu