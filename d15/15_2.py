subor = open("15.txt", "r")

pole = [[int(a) for a in x.strip()] for x in subor.readlines()]
n = len(pole)

npole=[[0 for j in range(n*5)] for i in range(n*5)]
for i in range(n*5):
        for j in range(n*5):
            npole[i][j]=(pole[i%n][j%n]+i//n+j//n)
            if npole[i][j]>9:
                npole[i][j]-=9

n=n*5
pole=[[0 for j in range(n)] for i in range(n)]
vysky=[[0 for j in range(n)] for i in range(n)]
for i in range(n):
        for j in range(n):
            pole[i][j]=npole[i][j]
            vysky[i][j]=pole[i][j]

def susedia(a,b):
    co=[]
    if n> a-1 >= 0:
        co.append(pole[a-1][b]+vysky[a][b])
    if n> a+1 >= 0:
        co.append(pole[a+1][b]+vysky[a][b])
    if n> b-1 >= 0:
        co.append(pole[a][b-1]+vysky[a][b])
    if n> b+1 >= 0:
        co.append(pole[a][b+1]+vysky[a][b])
    return(min(co))

npole=[[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        npole[i][j]=pole[i][j]
        for a in range(i):
            npole[i][j]+=pole[a][j]
        for a in range(j):
            npole[i][j]+=pole[0][a]



for i in range(n):
        for j in range(n):
            pole[i][j] = npole[i][j]


def zmensi():
    global pole
    bolo = False
    npole=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if susedia(i,j) < pole[i][j]:
                npole[i][j] = susedia(i,j)
                bolo = True
            else:
                npole[i][j] = pole[i][j]
    for i in range(n):
        for j in range(n):
            pole[i][j] = npole[i][j]
    return(bolo)

bolo=True
while bolo:
    bolo=zmensi()
print(pole[n-1][n-1]-pole[0][0])
