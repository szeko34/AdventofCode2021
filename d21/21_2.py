import copy

s=open("21.txt","w")

p1 = 5
p2 = 8

s1 = 0
s2 = 0

moz = {3:1,4:3,5:6,6:7,7:6,8:3,9:1}

stavy=[]
for i in range(10):
    tmp=[]
    for j in range(10):
        tmpp=[]
        for a in range(31):
            tmppp=[]
            for b in range(31):
                tmppp.append([0,0])
            tmpp.append(tmppp)
        tmp.append(tmpp)
    stavy.append(tmp)

stavy[p1][p2][s1][s2][0] = 1

kto = 1
treba = True
while treba:
    treba = False
    nstavy=[]
    for i in range(10):
        tmp=[]
        for j in range(10):
            tmpp=[]
            for a in range(31):
                tmppp=[]
                for b in range(31):
                    tmppp.append(stavy[i][j][a][b])
                tmpp.append(tmppp)
            tmp.append(tmpp)
        nstavy.append(tmp)
    for i in range(10):
        for j in range(10):
            for k in range(21):
                for l in range(21):
                    if stavy[i][j][k][l][abs(kto-1)] > 0:
                        #print("p",i,j,k,l,kto,stavy[i][j][k][l][abs(kto-1)],file=s)
                        treba = True
                        if kto == 1:
                            for a in moz.keys():

                                nstavy[(i + 1 + a -1) % 10 ][j][k+(i+1 + a - 1) % 10 +1][l][kto]+=stavy[i][j][k][l][abs(kto-1)]*moz[a]

                        else:
                            for a in moz.keys():
                                nstavy[i][(j + 1 + a -1) % 10 ][k][l+(j+1 + a -1) % 10 +1][kto]+=stavy[i][j][k][l][abs(kto-1)]*moz[a]


                        nstavy[i][j][k][l][abs(kto-1)] = 0

    kto = abs(kto-1)
    stavy = copy.deepcopy(nstavy)


a=0
b=0

for i in range(10):
    for j in range(10):
        for k in range(31):
            for l in range(31):
                if k>=21 or l >=21:
                    a+=stavy[i][j][k][l][0]
                    b+=stavy[i][j][k][l][1]

print(a,b)
