p1 = 6
p2 = 9

s1 = 0
s2 = 0

kocka = 100

tahy = 0

bol, kto = 1,2

while s1 <1000 and s2 <1000:
    bol, kto = kto, bol
    kolko = 0
    for i in range(3):
        tahy +=1
        kocka = (kocka) % 100 + 1
        kolko += kocka
    if kto == 1:
        p1 = (p1 + kolko - 1) % 10 + 1
        s1 += p1
    else:
        p2 = (p2 + kolko - 1) % 10 + 1
        s2 += p2
    print(kto,kocka,s1,p1,s2,p2)

print(s1,p1,s2,p2,tahy)
print(s1*tahy, s2*tahy)

