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

for x in g.keys():
    kade.add(x)


def c(s,e,cesta,kade):
    cesta.append(s)
    if s.lower() == s:
            kade=kade-{s}
    if s == e:
        return [cesta]
    else:

        if len(kade)==0:
            return [cesta]
        else:
            cesty=[]
            for x in g[s]:

                if x in kade:
                    ncesty=c(x,e,cesta,kade)
                    for ncesta in ncesty:
                        cesty.append(ncesta)
            return cesty

print(len(c("start","end",[],kade)))



