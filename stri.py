name="meena"
city="karimnagar"
message= "hello everyone this is meena from karimnagar"
print(name,city,message)         #  meena karimnagar hello everyone this is meena from karimnagar
print(type(message))             #  <class 'str'>


#accessing characters:

print(message[23])  #    m
print(name[-1])      #   a
print(message[0])     #   h
print(city[3])        #    i

#string slicing:
print(city[0:4])        #kari    
print(city[2:6])     # btwn 2 and 6     rimn
print(city[:5])       #before 5     karim
print(city[5:])   # after 5     nagar
print(city[::4])  #skip 4       kma
print(city[::-1])# reverse      raganmirak


# operations:

#concatination:     meena karimnagar

print(name+" "+city)

#repetition:        meenameenameena

print(name*3)

#length:            44

print(len(message))

#indexing:          m
print(name[0])

#slicing:           naga

print(city[5:-1])



#Methods :

#uppercase nd lowercase:
print(name.upper())   #MEENA
print(city.lower())     #karimnagar
print(name.capitalize())    #Meena
print(city.title())         #Karimnagar
print(name.swapcase())      #MEENA


#removing spaces:
print(message.strip())
print(message.lstrip())
print(message.rsplit())
'''hello everyone this is meena from karimnagar
hello everyone this is meena from karimnagar
['hello', 'everyone', 'this', 'is', 'meena', 'from', 'karimnagar']'''


#searching and replace

print(message.find("meena"))        #23
print(message.index("karimnagar"))      #34
print(message.replace("meena","Mahi"))      #hello everyone this is Mahi from karimnagar
print(message.count("k"))                   #1



print("mahi".isalpha())
print("3114".isdigit())
print("mahi3114".isalnum())
print("MAHI".isupper())
print("meena".islower())
print(" ".isspace())
'''True
True
True
True
True
True'''

#spliting nd joining:
st="meena, mahi,maya"
s= st.split(",")
print(s)
m="-".join(s)
print(m)

'''['meena', ' mahi', 'maya']
meena- mahi-maya'''

