# Tu napíšte svoj kód :-)
subor=open("3.txt","r")
cisla = subor.readlines()

for i in range(len(cisla[0])-1):
    l=[x[i] for x in cisla]
    if l.count("1")>=l.count("0"):
        ncisla=[]
        for j in range(len(cisla)):
            if cisla[j][i]=="1":
                ncisla.append(cisla[j])
        cisla = ncisla
    else:
        ncisla=[]
        for j in range(len(cisla)):
            if cisla[j][i]=="0":
                ncisla.append(cisla[j])
        cisla = ncisla

ogr = int(cisla[0],2)
subor.close()

#hladam csr
subor=open("3.txt","r")
cisla = subor.readlines()

for i in range(len(cisla[0])-1):
    l=[x[i] for x in cisla]
    if l.count("1")>=l.count("0"):
        ncisla=[]
        if len(cisla)>1:
            for j in range(len(cisla)):
                if cisla[j][i]=="0":
                    ncisla.append(cisla[j])
            cisla = ncisla
    else:
        ncisla=[]
        if len(cisla)>1:
            for j in range(len(cisla)):
                if cisla[j][i]=="1":
                    ncisla.append(cisla[j])
            cisla = ncisla

csr = int(cisla[0],2)

print(ogr*csr)
