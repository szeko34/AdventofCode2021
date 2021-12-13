subor = open("13.txt", "r")

kde=set({})
d=subor.readline()
while d!="\n":
    x,y=d.split(",")
    kde.add((int(x),int(y)))
    d=subor.readline()

ohyby=[]
for f in subor.readlines():
    ako=f.split("=")[0][-1]
    akoc = int(f.split("=")[1])
    ohyby.append((ako,akoc))


def ohni(o):
    global kde
    ako,akoc=o[0],o[1]
    nkde=set({})
    if ako=="y":
        for x in kde:
            if x[1]>akoc:
                nkde.add((x[0],akoc-(x[1]-akoc)))
            else:
                nkde.add(x)
    if ako=="x":
        for x in kde:
            if x[0]>akoc:
                nkde.add((akoc-(x[0]-akoc),x[1]))
            else:
                nkde.add(x)

    kde=nkde

for x in ohyby:
    ohni(x)

print(len(kde))
