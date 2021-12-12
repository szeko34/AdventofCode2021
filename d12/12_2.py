subor = open("12.txt", "r")

g = {}

for x in subor:
    a,b = x.strip().split("-")
    if a in g:
        g[a].add(b)
    else:
        g[a] = {b}
    if b in g:
        g[b].add(a)
    else:
        g[b] = {a}

kade=set({})
p={}
for x in g.keys():
    kade.add(x)
    p[x]=0

def c(s,e,cesta,kade,kolko,p):
    tp={}
    for x in p.keys():
        tp[x]=p[x]
    cesta= cesta + [s]
    if s.lower() == s:
            tp[s]+=1
            if tp[s]==2: kolko=1
            if kolko==1 or s=="start":
                kade=kade-{s}
                for x in kade:
                    if x == x.lower() and tp[x]>0:
                        kade=kade-{x}

    if s == e:
        return [cesta]
    else:
        if len(kade)==0:
            return [cesta]
        else:
            cesty=[]
            for x in g[s]:
                if x in kade:
                    ncesty=c(x,e,cesta,kade,kolko,tp)
                    for ncesta in ncesty:
                        cesty.append(ncesta)
            return cesty

print(len( c("start","end",[],kade,2,p)))




