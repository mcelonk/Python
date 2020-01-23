import numpy as np

class Facility:
    def __init__(self ,c ,m):
        self.c = c #centroid
        self.m = m #radius


# nacteni do 2d pole
def readXYZ(fil):
    p_list = []
    XYZ = open(fil)
    for line in XYZ:
        l = line.split()
        p_list.append(l)
    return p_list

xyz = readXYZ("test_15k_bez_duplict.xyz")

tresh = 5 #cena (cost, hranicni hodnota)
alpha = 9.5 #koeficient
f_list = []
f = Facility(xyz[0], 0)  # vlozeni prvni facility do listu
f_list.append(f)


for i in xyz:
    p1 = np.array([i[0], i[1], i[2]])
    p1 = p1.astype(float)
    dis_list = [] #pole vzdalenosti bodu od facilities

    #vypocet vzdalenosti s kazdou existujici facilitou
    for z in f_list:
        p2 = np.array([z.c[0], z.c[1], z.c[2]])
        p2 = p2.astype(float)
        squared_dist = np.sum((p1 - p2) ** 2, axis=0)
        dist = np.sqrt(squared_dist) #vypocitani vzdalenosti
        dist = dist + 2*z.m #nasobeni 2m jako v clanku
        dis_list.append(dist) #pridat do listu vzdalenosti

    #index_dist_min = dis_list.index(min(dis_list)) index pro nejblizsi facility, zatim se nevyuziva
    g = min(dis_list)
    p = np.random.uniform() #vygenerovani pravdepodobnosti

    #rozhodnuti zda ma byt vytvorena nova facility
    if p > g/(tresh*alpha):
        g_u = g #zapamatuje si posledni hodnotu g, vyuziva se dale pro vypocet m(w)
        continue #nevytvari se nova facility, posun na dalsi bod

    #vytvoreni facility w
    m = (g/(tresh*alpha))/6
    f = Facility(i, m)

    #pokud je nejaka facility prilis blizko, bude odstranena
    for z in f_list:
        p2 = np.array([z.c[0], z.c[1], z.c[2]])
        p2 = p2.astype(float)
        squared_dist = np.sum((p1 - p2) ** 2, axis=0)
        dist = np.sqrt(squared_dist)  # vypocitani vzdalenosti
        if dist < z.m:
            f_list.remove(z)

    f_list.append(f) #pridani facility do listu

#vytvoreni csv souboru
out = open("facilities.csv", "w")
out.write("X")
out.write(" ")
out.write("Y")
out.write(" ")
out.write("Z")
out.write("\n")
for k in f_list:
    out.write(k.c[0])
    out.write(" ")
    out.write(k.c[1])
    out.write(" ")
    out.write(k.c[2])
    out.write("\n")



