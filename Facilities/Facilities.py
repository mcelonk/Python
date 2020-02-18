import numpy as np
import math


class Facility:
    def __init__(self, c, m):
        self.c = c  # centroid
        self.m = m  # radius


# nacteni do 2d pole
def readXYZ(fil):
    p_list = []
    XYZ = open(fil)
    for line in XYZ:
        l = line.split()
        float_l = [float(x) for x in l]

        p_list.append(float_l)

    return p_list


# funkce square distance, jeste nefunguje, problem s datovym typem
def countDist(p1, p2):
    distance = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2)
    return distance


def nearestFacility(p1, facility_list):
    min = countDist(p1, facility_list[0].c)
    min = min + 2 * facility_list[0].m
    for z in facility_list:
        distance = countDist(p1, z.c)
        distance = distance + 2 * z.m
        if distance < min:
            min = distance
    return min

filename = "BILO48_5g.xyz"
xyz = readXYZ(filename)
tresh = 5  # cena (cost, hranicni hodnota)
alpha = 9.5  # koeficient
f_list = []
f = Facility(xyz[0], 0)  # vlozeni prvni facility do listu
f_list.append(f)

for i in xyz:
    #tiskne kazdy 1000 zpracovanych bodu
    if xyz.index(i) % 1000 == 0:
        print(xyz.index(i))
        
    # vypocet vzdalenosti s kazdou existujici facilitou
    # index_dist_min = dis_list.index(min(dis_list)) index pro nejblizsi facility, zatim se nevyuziva
    g = nearestFacility(i, f_list)
    p = np.random.uniform()  # vygenerovani pravdepodobnosti

    # rozhodnuti zda ma byt vytvorena nova facility
    if p < g / (tresh * alpha):
        m = (g / (tresh * alpha)) / 6
        f = Facility(i, m)

        # pokud je nejaka facility prilis blizko, bude odstranena
        for facility in f_list:
            dist = countDist(i, facility.c)
            if dist < facility.m:
                f_list.remove(facility)

        f_list.append(f)  # pridani facility do listu



# vytvoreni csv souboru
out = open(filename[:-4] + "_test.csv", "w")
out.write("X")
out.write(" ")
out.write("Y")
out.write(" ")
out.write("Z")
out.write("\n")
for k in f_list:
    out.write(str(k.c[0]))
    out.write(" ")
    out.write(str(k.c[1]))
    out.write(" ")
    out.write(str(k.c[2]))
    out.write("\n")
