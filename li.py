l=[100,30,50,60]
print(l)        #[100, 30, 50, 60]
print(l[0])     #100
print(l[-1])    #60
print(len(l))   #4

data=[10,"python",6.7,True]
print(data)

l.append(68)
print(l)        #[100, 30, 50, 60, 68]
l.insert(1,67)
print(l)        #[100, 67, 30, 50, 60, 68]
l.extend([99,108])
print(l)        #[100, 67, 30, 50, 60, 68, 99, 108]


l.remove(30)
print(l)            #[100, 67, 50, 60, 68, 99, 108]
l.pop()
print(l)            #[100, 67, 50, 60, 68, 99]
del l[0]
print(l)            #[67, 50, 60, 68, 99]

#updating:
l[2]=55
print(l)            #[67, 50, 55, 68, 99]

#slicing:
print(l[1:4])           #[50, 55, 68]
#functions and methods:
print(max(l))           #99
print(min(l))           #50
print(sum(l))           #339
print(sorted(l))        #[50, 55, 67, 68, 99]


#methods:
l.sort() 
print(l)         #[50, 55, 67, 68, 99]


l.reverse()    
print(l)        #[99, 68, 67, 55, 50]


print(l.count(67))      #1
print(l.index(55))      #3

li=[22,22,34,56]
dup=[]
for i in li:
    if i not in dup:
        dup.append(i)
print(dup)              #[22, 34, 56]