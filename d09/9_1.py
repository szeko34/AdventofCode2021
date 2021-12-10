# Tu napíšte svoj kód :-)
subor = open("9t.txt", "r")

pole = []

riadky = [x.strip() for x in subor.readlines()]
n = len(riadky[0])
v = len(riadky)

pole.append([10]*(n+2))
for i in riadky:
    pole.append([10] + [int(x) for x in i] + [10])
pole.append([10] * (n+2))

def sused(i, j):
    if pole[i][j] < pole[i-1][j] and pole[i][j] < pole[i+1][j] and pole[i][j] < pole[i][j+1] and pole[i][j] < pole[i][j-1]:
        return(pole[i][j] + 1)
    else:
        return 0

suc = 0
for i in range(1, v + 1):
    for j in range(1, n + 1):
        suc += sused(i, j)

print(suc)
