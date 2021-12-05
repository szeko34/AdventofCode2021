# Tu napíšte svoj kód :-)
subor = open("5.txt", "r")

ciary = [x.strip().replace(" -> ", ",").split(",") for x in subor]

for i in range(len(ciary)):
    for j in range(len(ciary[i])):
        ciary[i][j] = int(ciary[i][j])

miesta = {}

for r in ciary:
    if r[0] == r[2]:
        zac = min(r[1], r[3])
        for i in range(zac, zac+abs(r[1]-r[3])+1):
            if (r[0], i) in miesta:
                miesta[(r[0], i)] += 1
            else:
                miesta[(r[0], i)] = 1
    if r[1] == r[3]:
        zac = min(r[0], r[2])
        for i in range(zac, zac+abs(r[0]-r[2])+1):
            if (i, r[1]) in miesta:
                miesta[(i, r[1])] += 1
            else:
                miesta[(i, r[1])] = 1

print(sum(v > 1 for v in miesta.values()))


