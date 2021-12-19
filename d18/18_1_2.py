subor=open("18.txt","r")

cisla=[x.strip() for x in subor.readlines()]

scitani = len(cisla)-1
cis=[]

for x in cisla:
    vnorenie=0
    nc=[]
    for i in range(len(x)):
        if x[i]=="[":
            vnorenie+=1
        elif x[i] == "]":
            vnorenie -= 1
        elif x[i] == ",":
            pass
        else:
            nc.append([int(x[i]),vnorenie])
    cis.append(nc)

import copy
odloz=copy.deepcopy(cis)


def expl(tc,i):
    c=list(tc)
    l,p=c[i][0],c[i+1][0]
    if i-1>=0:
        c[i-1][0] += l
    if i+2 < len(c):
        c[i+2][0] += p
    c[i:i+2] = [[0,c[i][1]-1]]
    return(c)

def rozdel(tc,i):
    c=list(tc)
    c[i:i+1]=[[c[i][0]//2,c[i][1]+1],[c[i][0]-c[i][0]//2,c[i][1]+1]]
    return(c)

def pripocitaj(tc,b):
    c=list(tc)
    tmp=[]
    for x in c:
        tmp.append(x)
    for x in b:
        tmp.append(x)
    c = tmp.copy()

    for i in range(len(c)):
        c[i][1] += 1
    return(c)


def redukuj(tc):
    c=list(tc)
    i=0
    while i<len(c):
        while i<len(c):
            if c[i][1] == 5:
                c=list(expl(c,i))
                i = -1
            i += 1
        i=0
        delil=False
        while i<len(c) and not delil:
            if c[i][0]>=10:
                c=list(rozdel(c,i))
                delil = True
                i = -1
            i += 1
    return(c)

c=list(cis[0])
for i in range (scitani):

    c=list(pripocitaj(c,cis[i+1]))
    c=list(redukuj(c))


def vyries(tc):
    c=list(tc)
    vnorenie = max([j[1] for j in c])+1

    while len(c)>1:
        vnorenie -=1
        i=0
        while i<len(c):
            if c[i][1] == vnorenie:

                c[i:i+2]=[[c[i][0]*3+c[i+1][0]*2,c[i][1]-1]]

                i= -1
            i+=1
    return(c)

res = vyries(c)[0][0]
print(res)                  #uloha 1

ans = 0
for a in odloz:
    for b in odloz:
        ta=copy.deepcopy(a)
        tb=copy.deepcopy(b)
        r = vyries(redukuj(pripocitaj(ta,tb)))[0][0]
        if r > ans:
            ans = r

print(ans)                  #uloha 2
