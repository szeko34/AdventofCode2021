# Tu napíšte svoj kód :-)
subor=open("2.txt","r")

inst=[x.split() for x in subor]

v = 0
z = 0
a = 0
for x in inst:
    if x[0] == "forward":
        v += int(x[1])
    if x[0] == "down":
        z += int(x[1])
    if x[0] == "up":
        z -= int(x[1])

print(v*z)
