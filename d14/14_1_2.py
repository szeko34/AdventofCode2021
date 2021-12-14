subor = open("14.txt", "r")

z=subor.readline().strip()

d={}

for i in range(len(z)-1):
    if z[i:i+2] in d:
        d[z[i:i+2]]+=1
    else:
        d[z[i:i+2]]=1

subor.readline()

start=z[0]
end=z[-1]


p=[x.strip().split(" -> ") for x in subor]
pd={}
for x in p:
    pd[x[0]]=x[1]

#for i in range(10) - uloha 1
for i in range(40):
    nd={}
    for x in d:
        if x[0]+pd[x] in nd:
            nd[x[0]+pd[x]]+=d[x]
        else:
            nd[x[0]+pd[x]]=d[x]
        if pd[x]+x[1] in nd:
            nd[pd[x]+x[1]]+=d[x]
        else:
            nd[pd[x]+x[1]]=d[x]
    d=nd

pocty={}
for a in d.keys():
    for x in a:
        if x in pocty.keys():
            pocty[x]+=d[a]
        else:
            pocty[x]=d[a]


for x in pocty:
    pocty[x]=pocty[x]//2
    if x==start or x==end:
        pocty[x]+=1



print(max(pocty.values())-min(pocty.values()))
