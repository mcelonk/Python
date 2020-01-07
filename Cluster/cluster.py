import math, numpy


class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z



# nacteni bodu
def readXYZ(fil):
    p_list = []
    XYZ = open(fil)
    for line in XYZ:
        l = line.split()
        bod = point(l[0], l[1], l[2])
        p_list.append(bod)
    return p_list

#vytvoreni matice vzdalenosti
def dist_table(body):
    test_count = 0 #pokud je == 1 dochazi k zapisu do noveho radku v matici
    final = numpy.zeros(len(body))
    for bod_i in body:
        # vypocita a ulozi do matice
        temp_a = numpy.zeros(len(body))
        i = 0
        i_x = float(bod_i.x)
        i_y = float(bod_i.y)
        for bod_j in body:
            j_x = float(bod_j.x)
            j_y = float(bod_j.y)
            distance = abs(math.sqrt(pow(i_x - j_x, 2) + pow(i_y - j_y, 2)))
            temp_a[i] = distance
            i += 1

        if test_count == 0:
            final = temp_a
        else:
            final = numpy.vstack([final, temp_a])
        test_count = 1
    return final

#nastaveni hranicni hodnoty
tresh = 25

body = readXYZ("test_15k_bez_duplict.xyz") #nacte body
matice = dist_table(body) #vypocita vzdalenosti
clusters = [] #priprava pole pro cluster
pouzite = [] #jiz zarazene body

for i in range(len(body)):
    #preskoci jiz zarazene body
    if body[i] not in pouzite:
        current_cluster = []
    else:
        continue

    #vytvoreni prvniho clusteru
    if not clusters:
        current_cluster.append(body[i])
        pouzite.append(body[i])
        clusters.append(current_cluster)
        current_cluster = []

    for j in (len(body)):
        #preskoci jiz zarazene body
        if body[j] in pouzite:
            continue
        k_minima = []
        for k in clusters: #kontrola jiz vytvorenych clusteru
            minima = []
            for l in k:
                ind = body.index(l)
                minima.append(matice[j][ind])
            k_minima.append(min(minima)) #zjisteni vsech minimalnich vzdalenosti pocitaneho bodu a vytvorenych clusteru

        if min(k_minima) < tresh: #kontrola zda bude bod pridan do existujiciho clusteru
            min_ind = k_minima.index(min(k_minima))
            temp_cluster = clusters[min_ind]
            temp_cluster.append(body[j])
            clusters[min_ind] = temp_cluster
            pouzite.append(body[j])
        elif matice[i][j] < tresh: #... soucasneho clusteru
            current_cluster.append(body[j])
            pouzite.append(body[j])
        else:
            current_cluster.append(body[j]) #... noveho clusteru
            pouzite.append(body[j])
            break

    if current_cluster:
        clusters.append(current_cluster) #prida cluster do listu clusteru

print len(clusters)

#vypise body ve formatu .csv, 4 sloupec je cislo clusteru
f = open("cluster_done.csv", "w")
for k in clusters:
    for i in k:
        f.write(i.x)
        f.write(" ")
        f.write(i.y)
        f.write(" ")
        f.write(i.z)
        f.write(" ")
        f.write(str(clusters.index(k)))
        f.write("\n")



