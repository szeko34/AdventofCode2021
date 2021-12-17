from collections import defaultdict
subor=open("17.txt","r")

cele=subor.read().strip()
mx,vx=[int(x) for x in cele[cele.find("x"):].split()[0][2:-1].split("..")]
my,vy=[int(x) for x in cele[cele.find("y"):][2:].split("..")]
print(mx,vx)
print(my,vy)

vysky=[]
ans=0
for speed in range(vx+1):
    for height in range(-500,500):

        r = speed
        v=height
        x,y = 0,0
        mxa=y
        konci=False
        #print(speed,height)
        while y>my and x<vx and not konci:
            #print((x,y),end=" ")
            x+=r
            y+=v
            if y > mxa:
                mxa = y
            if r>0:
                r-=1
            v -=1
            if x in range(mx,vx+1) and y in range(my,vy+1):
                print(speed, height,"som tam na",x,y)
                vysky.append(mxa)
                ans+=1
                konci=True

print(max(vysky),ans)
