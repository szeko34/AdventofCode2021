# Tu napíšte svoj kód :-)
subor=open("7.txt","r")

cisla=[int(x)for x in subor.readline().split(",")]

import statistics

vzd=sum([abs(statistics.median(cisla)-x) for x in cisla])

print(vzd)





