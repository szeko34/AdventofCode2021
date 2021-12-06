# Tu napíšte svoj kód :-)
subor=open("6.txt","r")

cisla=[int(x)for x in subor.readline().split(",")]

dni=[0]*9

for x in cisla:
    dni[x]+=1

#for i in range(80): part 1
for i in range(256):
    pom=dni[0]
    for j in range(8):
        dni[j]=dni[j+1]
    dni[8]=pom
    dni[6]+=pom

print(sum(dni))





