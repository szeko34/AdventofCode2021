# Tu napíšte svoj kód :-)
subor=open("4.txt","r")
cisla = [int(x) for x in subor.readline().split(",")]

dosky=[]

for i in range(100):
    subor.readline()
    d=[]
    for j in range(5):
        d.append([int(x) for x in subor.readline().split()])
    dosky.append(d)

def vyhral():
    for i in range(len(dosky)):
        for j in range(5):
            if len([x for x in dosky[i][j] if x>=0])==0:
                return i
            if len([x[j] for x in dosky[i] if x[j]>=0])==0:
                return i
    return -1

def vyskrtni(c):
    for i in range(len(dosky)):
        for j in range(5):
            for k in range(5):
                if dosky[i][j][k]==cisla[c]:
                    dosky[i][j][k]=-dosky[i][j][k]-1 #kvoli 0


c=0
skrtnutych = 0
while len(dosky)>1:
    vyskrtni(c)
    while vyhral()>-1:
        vyskrtni(c)
        ktora=vyhral()
        if ktora>-1: dosky.pop(ktora)
    c+=1

#hladanie konca pre poslednu
while vyhral()==-1:
    vyskrtni(c)
    c+=1

s=0
for i in range(5):
    for j in range(5):
        if dosky[0][i][j]>=0:
            s+=dosky[0][i][j]

print(s*cisla[c-1])

