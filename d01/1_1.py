# Tu napíšte svoj kód :-)
subor=open("1.txt","r")


cisla=[int(x) for x in subor]
vacsie = 0
for i in range(3,len(cisla)):
    if cisla[i]>cisla[i-3]:
        vacsie+=1

print(vacsie)

