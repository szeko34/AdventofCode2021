from collections import defaultdict
subor=open("16.txt","r")
a={
"0" : "0000",
"1" : "0001",
"2" : "0010",
"3" : "0011",
"4" : "0100",
"5" : "0101",
"6" : "0110",
"7" : "0111",
"8" : "1000",
"9" : "1001",
"A" : "1010",
"B" : "1011",
"C" : "1100",
"D" : "1101",
"E" : "1110",
"F" : "1111"
}

ss=subor.read().strip()

s=""
for x in ss:
    s=s+a[x]


co_robim=""
ans=0

id=0

def parse(s):

    global ans,co_robim
    if "1" in s:

        v = s[:3]

        ans+=int(v,2)
        t = s[3:6]

        if t!="100":

            if int(t,2) == 0:
                co_robim+="\"sum\","
            if int(t,2) == 1:
                co_robim+="\"pro\","
            if int(t,2) == 2:
                co_robim+="\"min\","
            if int(t,2) == 3:
                co_robim+="\"max\","
            if int(t,2) == 5:
                co_robim+="\"grt\","
            if int(t,2) == 6:
                co_robim+="\"les\","
            if int(t,2) == 7:
                co_robim+="\"eql\","
            s=s[6:]
            i=s[0]
            s=s[1:]
            if i == "0":          #oznacenie typu operatoroveho paketu 0
                bitov=int(s[:15],2)
                s=s[15:]

                co_robim+="{ "
                parse(s[:bitov])
                co_robim+="} "
                s=s[bitov:]
            else:               #oznacenie typu operatoroveho paketu 1 s poctom subpaketov
                paketov=int(s[:11],2)
                zostava=paketov
                co_robim+="\"<"+str(paketov)+">\","
                s=s[11:]

            parse(s)
        else:
            s=s[6:]
            cislo=s[:5]
            cele=cislo[1:]
            s=s[5:]
            while cislo[0]!="0":
                cislo=s[:5]
                cele+=cislo[1:]
                s=s[5:]
            co_robim+=str(int(cele,2))+","
            parse(s)

parse(s)
print(ans) #prva uloha

c=list(co_robim)
for i in range(len(c)):
    if "".join(c[i:i+2]) == "} ":
        c[i:i+2]=["]",","]
    if "".join(c[i:i+2]) == "{ ":
        c[i:i+2]=["["]

for i in range(len(c)):
    if "".join(c[i:i+2]) == ",]":
        c[i:i+2]=["]"]

a="["+ "".join(c)+"]"
print(a)

#a vystup vyhodnoteny manualne, LOL :D
