# Tu napíšte svoj kód :-)
subor = open("10.txt", "r")

o = ["(","[","<","{"]
c = [")","]",">","}"]
cena = {")":3,"]":57,">":25137,"}":1197}

r = [x.strip() for x in subor.readlines()]

suc = 0
for x in r:
    z = []
    for i in range(len(x)):
        if x[i] in o:
            z.append(x[i])
        elif z != [] and c.index(x[i]) == o.index(z[-1]):
            z.pop()
        else:
            suc += cena[x[i]]
            break

print(suc)
