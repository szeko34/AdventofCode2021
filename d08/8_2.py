# Tu napíšte svoj kód :-)
subor=open("8.txt","r")
predpis= [x.split("|") for x in subor]

sucet=0
dlzky={}

#vrati cislo, ktore sa skryva za retazcom
def vymen(x):
    for k,v in c.items():
        if v==set(x):
            return str(k)


for x in predpis:
    c = {}
    cislice = x[0].split()
    cislice = [set(x) for x in cislice]
    cislice = sorted(cislice, key=len)
    #ziskavam hodnoty na zaklade dlzky
    c[1] = cislice[0]
    c[7] = cislice[1]
    c[4] = cislice[2]
    c[8] = cislice[9]
    #odstranujem hodnoty zo zoznamu prehladavanych moznosti
    cislice.pop(9)
    cislice.pop(2)
    cislice.pop(1)
    cislice.pop(0)

    #horny segment ako rozdiel 7 a 1
    H=c[7]-c[1]

    #identifikovanie 9ky, ako toho, co mam vsetky body so 4kou a este dolny segment navyse, identifikovanie dolneho
    for i in range(len(cislice)):
        if (c[4] == c[4] & cislice[i]) and len(cislice[i]-c[4]) == 2:
            c[9] = cislice[i]
            D = c[9]-c[4]-H
            cislice.pop(i)
            break


    #6ka a pravy horny segment
    for i in range(len(cislice)):
        if len (c[8]-cislice[i])==1 and len(c[7]-cislice[i]) > 0:
            c[6] = cislice[i]
            PH = c[8]-c[6]
            cislice.pop(i)
            break

    #5ka a lavy dolny segment
    c[5]=c[9]-PH
    LD = c[6]-c[5]

    #O ako jediny zostavajuci so 6 znakmi
    for i in range(len(cislice)):
        if len (cislice[i])==6 :
            c[0] = cislice[i]
            cislice.pop(i)
            break

    #zvysok vyskladany zo segmentov
    S=c[8]-c[0]
    c[2]=H | D | S | PH | LD
    c[3]=H | D | c[1] | S

    #dopocitanie cisla do suctu
    sucet+=int("".join([vymen(a) for a in x[1].split()]))


print(sucet)
