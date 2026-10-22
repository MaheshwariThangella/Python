'''n=int(input())
for i in range(n-1):
    for j in range(n-1):
        print(i,end=" ")
    print()    '''
'''
m=3
for i in range(2,0,-1):
    for j in range(3):
        print(j,end=" ")
    print()    '''

#m=int(input())
'''
for i in range(0,m):
    for j in range(i+1):
        print("*",end="")
    print()    '''   

#m=4
'''for i in range(m):
    for j in range(m-i-1):
        
        print(" ",end="")
    for star in range(i+1):
        print("*",end="")    
    print()   ''' 


'''
for i in range(5):
    for space in range(5-i-1):
        print(" ",end="")
    for num in range(5,5-i,-1):
        print(num,end="")
    print()        
'''


'''
for i in range(68,64,-1):
    for j in range(68,i-1,-1):
        print(chr(j),end=" ")
    print()   '''

'''
for i in range(4):
    for j in range(68,68-i-1,-1):
        print(chr(j),end=" ")
    print()'''

'''
for i in range(5):
    for j in range(5):
        if i==0 or j==0 or i==4 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()     '''   

'''
year= [2000,2003,2004,1990]
for i in year:
    if i %400==0 or (i % 4==0 and i %100!=0):
        print(i)'''
'''
n = "sampu"
vowels = "aeiou"
count=0
c1=0
v=" "
c=" "
for i in n:
    if i in vowels:
        v+=i
        count+=1
        
    else:
        c+=i
        c1+=1
print(v,count)
print(c,c1)        


n= int(input())
m=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2 or i==n-1 and j < n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()                    #j


n= int(input())
m=int(input())
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            #x

n= int(input())
m=int(input())
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1 and :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    #y



n= int(input())
m=int(input())
for i in range(n):
    for j in range(n):
        if j==0  or i==j or j==n-1 :
        
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()   

n= int(input())
m=int(input())
for i in range(n):
    for j in range(m):
        if i==j or i+j==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()      # V   



n= int(input())

for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
    else:
        print("prime")    #10  prime       



n= int(input())

for num in range(1,n):
    for i in range(2,num):
        if num%i==0:
           
            break
    else:
        print(num)   #10     12357  


n= int(input())
c=0
for num in range(1,n):
    for i in range(2,num):
        if num%i==0:
           
            break
    else:
        c+=1
print(c)   #10    5


n= int(input())
c=0
for num in range(1,n):
    for i in range(2,num):
        if num%i==0:
           
            break
    else:
        c+=num
print(c)         #12  29


n=7
for i in range(1,7,2):
    print((i*".|.").center(21,"-"))
print("WELCOME".center(21,"-"))

p=4
k="z"
x="abracadabra"
l=list(x)
print(l)
l[p]=k
print("".join(l)   


s=str(input())
i=0
j=len(s)-1
while i < j:
    if s[i]==s[j]:
        i+=1
        j-=1
    else:
        print("not pali")
        break
else:
    print("pali")       


n=int(input())
m= int(input())
for i in range(n):
    for j in range(m):
        if i== 1 or i==n-2 or j ==1 or j==n-2:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()  '''      

'''
5
5
1 0 1 0 1 
0 0 0 0 0 
1 0 1 0 1 
0 0 0 0 0 
1 0 1 0 1 '''


'''

n= "python"
i=0
while i < len(n):
    j=i
    while j <len(n):
        print(n[j], end=" ")
        j+=1
    print()
    i+=1   


for i in range(0,5):
    for j in range(i,5):
        print(j , end=" ")
    print()    '''
'''0 1 2 3 4 
1 2 3 4  
4 '''
'''
m=5
fact=1
while m>0:
    fact*=m
    m-=1
print(fact)    '''




'''
n= int(input())
rev=" "
i=0
while i<len(n):
    rev=n[i]+rev
    print(id(rev))
    i+=1
if rev==n:
    print("P")

print("NA")       


n=2004
rev=0
while n>0:
    '''



'''
dici={"meena":600,"maya":400,"mahi":600,"chitti":500}
h=0
for key, value in dici.items():
    if value>=h:
        h=value
        print(key)
print(h)        



dici={"meena":600,"maya":400,"mahi":600,"chitti":500,"mike":900}
h=0
for key, value in dici.items():
    if value>=h:
        h=value
for k,v in dici.items():
    if v==h:
        print(k)         '''


def a(name,pw):
    print(name)
    print(pw)

name=input()   