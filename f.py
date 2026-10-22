#n=int(input())
#for i in range(1,11):
#    if i!=5:
#        print(n,"*",i,"=",n*i)
#    else:
#        print("break")
#        break

'''n=int(input())
for i in range(1,11):
    if i%2==0:
        #break
        continue
    elif i>=6:
        break
    else:
        print(n,"*",i,"=",n*i)

'''
#while syntax: i<=10          while cond            + or -
'''
i=5
while i>=0:
    if i==1:
       i-=1
       continue
    else:
        print(i)
        i-=1
else:
    print("completed")


i=5
while i<=10:
    if i ==8:
        pass
    else:
        print(i)
        i+=1
else:
    print("completed")       





n=["meena","mahi","chinna"]
for i in n:
    if i.startswith("m"):
        print(i) '''





