ilkson = int(input("Write a number: "))
orta = 1

bosluk1 = -1
bosluk2 = ilkson
bosluk3 = ilkson
bosluk4 = -1

for i in range(ilkson):
    bosluk1+=1
    bosluk2-=1
    bosluk3-=1
    bosluk4+=1
    print("-"*bosluk1 + "*" + "-"*bosluk2 + "*" + "-"*bosluk3 + "*" + "-"*bosluk4)
    

for i in range(orta):
    print("*"*((ilkson*2)+orta))


for i in range(ilkson):
    print("-"*bosluk1 + "*" + "-"*bosluk2 + "*" + "-"*bosluk3 + "*" + "-"*bosluk4)
    bosluk1-=1
    bosluk2+=1
    bosluk3+=1
    bosluk4-=1


