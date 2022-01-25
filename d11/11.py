subor = open("11.txt", "r")

pole = []

riadky = [x.strip() for x in subor.readlines()]
n = len(riadky[0])
v = len(riadky)

for i in riadky:
    pole.append([int(x) for x in i])

I = [0, 0, 1, -1, 1, 1, -1, -1]
J = [1, -1, 0, 0, -1, 1, -1, 1]
f = 0

def buchni(i, j,k):
    global f
    if 0 <= i < 10 and 0 <= j < 10:
        pole[i][j] += 1
        if pole[i][j] == 10:
            f += 1
            for k in range(8):
                buchni(i+I[k], j+J[k])
a = 1
while True:

    for i in range(10):
        for j in range(10):
            buchni(i, j)
    for i in range(10):
        for j in range(10):
            if pole[i][j] > 9:
                pole[i][j] = 0
    if a == 100: print(f)                       #uloha 1
    if(sum([sum(x) for x in pole])) == 0:       #uloha 2
        print(a)
        break
    a += 1

