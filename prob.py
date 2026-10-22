'''n=int(input())
for i in range(n):
    command=input().split()
print(command)    '''
'''
a=10
 b=20
c=5
p=0
if a>b and a>c:
    p=a
elif b>a and b>c:
    p=b
else:
    p=c
print(p)         '''

'''
a=1
b=8
c=9
g=s=0

if a>g:
    g=a
if b>g:
    s,g=g,b
elif b>s:
    s=b

if c>g:
    s,g=g,c
elif c>s:
    s=c
print(g,s)                    
   '''

'''
x=[10,1,2,9,7,8,6]
g=s=0
for i in x:
    if i > g:
        s,g=g,i
    elif i>s and i!=g: 
        s=i
print (g,s)    '''  



x=[7,6,5,4]
g=s=0
for i in x:
    print()