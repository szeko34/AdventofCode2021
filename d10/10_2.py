# Tu napíšte svoj kód :-)
subor = open("10.txt", "r")

o = ["(","[","<","{"]
c = [")","]",">","}"]

dopln = {"(":1,"[":2,"<":4,"{":3}

r = [x.strip() for x in subor.readlines()]
n = []

for x in r:
    z = []
    pokazeny = False
    for i in range(len(x)):
        if x[i] in o:
            z.append(x[i])
        elif z != [] and c.index(x[i]) == o.index(z[-1]):
            z.pop()
        else:
            pokazeny = True
            break
    if not pokazeny: n.append(z)

suc = []

for x in n:
    co =""
    for a in x:
        co+=str(dopln[a])
    suc.append(int(co[::-1],5))

suc.sort()

print(suc[len(suc)//2])
