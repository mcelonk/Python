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

# funkce pro vypocet vektoroveho soucinu
def crossProd (u, v):
    u = u[len(u)//2:]
    v = v[len(v)//2:]
    w = np.cross(u, v)
    w = w.tolist()
    return w

# funkce pro vypocet velikosti normaly
def vectorSize(w):
    size = math.sqrt(w[0]**2 + w[1]**2 + w[2]**2)
    return size

# vypocet nejblizsi facility na zaklade vzdalenosti
def nearestFacility(p1, facility_list):
    min = countDist(p1, facility_list[0].c)
    min = min + 2 * facility_list[0].m
    for z in facility_list:
        distance = countDist(p1, z.c)
        distance = distance + 2 * z.m
        cross_normal = crossProd(p1, z.c) # vektorovy soucin normal
        cross_normal_size = vectorSize(cross_normal) # velikost vektoru vytvoreneho soucinem
        if distance < min:
            min = distance
    return min



filename = "Normaly.txt"
normals = readXYZ(filename) # nacteni vectoru normaly




filename = "test_15k_bez_duplict.xyz"
xyz = readXYZ(filename)
c = np.concatenate((xyz, normals), 1) # concatenate xyz list a list s vektory normal
c = c.tolist() # prevedeni do normalniho pole
tresh = 5  # cena (cost, hranicni hodnota)
alpha = 9.5  # koeficient
f_list = []
f = Facility(c[0], 0)  # vlozeni prvni facility do listu
f_list.append(f)

for i in c:
    #tiskne kazdy 1000 zpracovanych bodu
    if c.index(i) % 1000 == 0:
        print(c.index(i))

    # vypocet vzdalenosti s kazdou existujici facilitou
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



# vytvoreni csv souboru podle nazvu vstupniho souboru
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
