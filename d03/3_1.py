# Tu napíšte svoj kód :-)
subor=open("3.txt","r")

cisla = subor.readlines()

g=""
e=""

for i in range(len(cisla[0])-1):
    l=[x[i] for x in cisla]
    if l.count("1")>l.count("0"):
        g+="1"
        e+="0"
    else:
        g+="0"
        e+="1"

print(int(g,2)*int(e,2))
