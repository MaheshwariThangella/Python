'''
a=input()
b=input()
if sorted(a) ==sorted(b):
    print("Anagram")
else:
    print("NA")    '''

dici={}
count=0
a=input()
b=input()
for i in a:
    if i in dici:
        dici[i]+=1
    else:
        dici[i]=1
        
for i in b:
    if i in dici:
        dici[i]-=1
    else:
        dici[i]=1
for i in dici:
    if dici[i]==1:
        count+=1        
print(dici)
print(count)
flames="FLAMES"
s=0
while len(flames) >1:
    s=( count-1)%len(flames)
    flames=flames[s+1:]+flames[:s]

print(flames[0])    