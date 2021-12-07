# Tu napíšte svoj kód :-)
subor=open("7.txt","r")

cisla=[int(x)for x in subor.readline().split(",")]

m=1000000000000000000000
for i in range(min(cisla),max(cisla)+1):
    pm=0
    for x in cisla:
        pm+=abs(x-i)*((abs(x-i)+1)/2)
    if pm<m:
        m=pm
print(m)





