#m=[1,3,2,5,7,9,8]
'''temp=[]
for i in range(len(m)):
#    print(m[i])
    if i%2!=0:
        temp.append(m[i])
        print(temp)    '''
temp=[]
#for i in range(len(m)):
    #even index odd values
#    if i%2==0:
#        if m[i]%2!=0:
#            temp.append(m[i])
#print(temp) 
#squares values 
#    temp.append(m[i]*m[i])
#print(temp)    


#odd values add 10
#    if m[i]%2!=0:
#        temp.append(m[i]+10)
#    else:
#        temp.append(m[i])
#print(temp)            


#reverse
'''for i in range(len(m)-1,-1,-1):
    temp.insert(0,m[i])
    print(temp)'''
'''
m=["meena","mahi","chinna"]
for i in m:
    if i=="meena":
        print("available")
        break
    print("NA")
'''
m=["meena","mahi","chinna"]   
'''temp=[]
for i in m:
    temp.append(len(i) )
    
print(temp)'''

'''i=0
count=[]
while i<len(m):
    count.append(len(m[i]))
    i+=1
print(count)   '''


dici={}
for i in range(len(m)):
    dici[m[i]]=len(m[i])
print(dici)    