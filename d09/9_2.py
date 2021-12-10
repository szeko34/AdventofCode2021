# Tu napíšte svoj kód :-)
subor=open("9.txt","r")

pole=[]

riadky=[x.strip() for x in subor.readlines()]
n=len(riadky[0])
v=len(riadky)

pole.append([10]*(n+2))
for i in riadky:
    pole.append([10]+[int(x) for x in i]+[10])
pole.append([10]*(n+2))

print(pole)

def sused(i,j):
    if pole[i][j]<pole[i-1][j] and pole[i][j]<pole[i+1][j] and pole[i][j]<pole[i][j+1] and pole[i][j]<pole[i][j-1]:
        return(pole[i][j]+1)
    else: return 0

def koniec(i,j):
    if pole[i][j]==9:
        return True
    else: return False

def niz(i,j):
    if not(0<i<v+1 and 0<j<n+1):
        return 0
    elif koniec(i,j):
        return 0
    else:
        pole[i][j]=9
        return 1+niz(i+1,j)+niz(i-1,j)+niz(i,j+1)+niz(i,j-1)

niziny=[]
for i in range(1,v+1):
    for j in range(1,n+1):
        if sused(i,j) > 0:
            niziny.append(niz(i,j))
        print(i,j)

niziny.sort()
print(niziny[-1]*niziny[-2]*niziny[-3])
