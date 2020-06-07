import numpy as np
import math
import os, sys


class Facility:
    def __init__(self, c, m):
        self.c = c  # centroid
        self.m = m  # radius
        self.points = 0
        self.dist = 0

    def setPoints(self, df_points):
        self.points = df_points

    def getPoints(self):
        return self.points

    def setDist(self, df_dist):
        self.dist = df_dist

    def getDist(self):
        return self.dist

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
    min_facility = facility_list[0]
    for z in facility_list:
        distance = countDist(p1, z.c)
        distance = distance + 2 * z.m
        if distance < min:
            min = distance
            min_facility = z
    min_facility.setDist(min)
    return min_facility

for file in os.listdir("pointcloud"):
    print(file)
    filename = file
    xyz = readXYZ("pointcloud//"+filename)
    tresh = 3  # cena (cost, hranicni hodnota)
    alpha = 9.5  # koeficient
    f_list = []
    f = Facility(xyz[0], 0)  # vlozeni prvni facility do listu
    f_list.append(f)

    for i in xyz:
        #tiskne kazdy 1000 zpracovanych bodu
        if xyz.index(i) % 1000 == 0:
            print(xyz.index(i))

        # vypocet vzdalenosti s kazdou existujici facilitou
        n_facility = nearestFacility(i, f_list)
        g = n_facility.getDist() # dostane hodnotu vzdalenosti k nejblizsi facility
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
        # ke kazde facilite zjisti pocet bodu ze ktereho vznikl
            f.setPoints(f.getPoints() + 1)
        else:
            n_facility.setPoints(n_facility.getPoints()+1)



    # vytvoreni csv souboru podle nazvu vstupniho souboru
    out = open(filename[:-4] + "_test.csv", "w")
    out.write("X")
    out.write(" ")
    out.write("Y")
    out.write(" ")
    out.write("Z")
    out.write(" ")
    out.write("Points")
    out.write("\n")
    for k in f_list:
        out.write(str(k.c[0]))
        out.write(" ")
        out.write(str(k.c[1]))
        out.write(" ")
        out.write(str(k.c[2]))
        out.write(" ")
        out.write(str(k.points))
        out.write("\n")
