#if :
#Write a program to check if a number is greater than 10.
'''
n=int(input())
if n > 10:
    print(n,"the given number is greater than 10")'''

#Write a program to check if a person is eligible to vote (age 18 or above).
'''
n= int(input())
if n >= 18:
    print("person is eligible to vote")
  '''

#Write a program to check if a number is positive.
'''
n=int(input())
if n >=0 :
    print("the number is positive")'''

#Write a program to check if a number is negative.
'''
n=int(input())
if n < 0 :
    print("the number is negative")'''

#ifelse :

#Write a program to check if a number is even or odd.
'''
n=int(input())
if n%2==0:
    print("the number is even")
else:
    print("the number is odd")    '''

# Write a program to check if a person is eligible for a driving license (age 18 or above).
'''    
n= int(input())
if n >= 18:
    print("person is eligible for a driving license")
else:
    print("person is not eligible for a driving license")    '''

#Write a program to check if a number is positive or negative.
'''
n=int(input())
if n >=0 :
    print("the number is positive")
else:
    print("the number is negative")'''

#Write a program to check if a student passed or failed based on marks (Pass: 40+, Fail: below 40).

'''n=int(input())
if n >40:
    print("the stu is passed")
else:
    print("the stud is failed")'''
#if-elif-else Statement Questions

#Write a program to classify a number as positive, negative, or zero.
'''
n=int(input())
if n >0 :
    print("the number is positive")
elif n <0:
    print("the number is negative")
else:
    print("the num is zero")    '''

#Write a program to categorize a person’s age as a child (0-12), teenager (13-19), or adult (20+).
'''
n=int(input())
if n >=0 and n <=12:
    print("the person is child")
elif n >=13 and n<=19:
    print("the person is teenager")
elif n >=20:
    print("the person is adult")    '''

#Write a program to determine the grade of a student based on marks (A: 90+, B: 80+, C: 70+, D: 60+, Fail: <40).
'''  
n=int(input())
if n >=90:
    print("A Grade")
elif n >=80 and n <90:
    print("B Grade")
elif n>= 70 and n <80:
    print("C Grade")
elif n >=60 and n<70:
    print("D Grade")
else:
    print("F")    '''     
#Nested_if statements:
#A bank checks if a person is eligible for a loan based on their age and salary.
'''
age=int(input())
salary= int(input())
if age >= 21 :
    print("the loan is eligible ")


    if salary >=20000:
        print("the loan is eligible ")
    else:
        print("NA")      
else:
    print("NA")    

#A student needs at least 35 marks to pass. If they score above 90, they get a scholarship.

marks= int(input())
if marks>=35:
    print("pass")
    if marks>90:
        print("will get a scholarship")
    else:
        print("NA")
else:
    print("student needs at least 35 marks to pass")     '''       
#Real time
'''
E-commerce Platforms (Amazon, Flipkart, eBay)
Order Discounts & Shipping Charges
if order_amount > 500: free_shipping() else: add_shipping_charge()'''
'''
amount=int(input())
if amount >=500:
    print("free_shipping")
else:
    print("add_shipping_charge")    


'''
'''
Banking & Finance (HDFC, ICICI, PayPal, Razorpay)
Loan Eligibility Checking
if salary > 50000 and cibil_score > 750: approve_loan() else: reject_loan()

salary=int(input())
cibil_score =int(input())
if salary >= 50000 and cibil_score >= 750:
    print("approve_loan")
else:
    print("reject_loan")    



Ride-Sharing Services (Uber, Ola,rapido)
Surge Pricing Logic
if peak_hours and high_demand: apply_surge_pricing() else: normal_fare()
peak_hours = input()
high_demand = input()
if peak_hours == "Yes" and high_demand == "Yes":
    print("Apply surge pricing")
else:
    print("Normal fare")


Food Delivery Services (Zomato, Swiggy, Uber Eats)
Restaurant Order Availability
if restaurant_open and item_available: accept_order() else: show_unavailable_message()

restaurant=int(input())
if restaurant ==open  :
    print("accept_order")
else:
    print("unavailable")    


Streaming Services (Netflix, YouTube, Hotstar)
Video Quality Adjustment
if internet_speed > 10Mbps: set_quality('1080p') elif internet_speed > 5Mbps: set_quality('720p') else: set_quality('480p')

internet_speed=int(input)
if internet_speed >= 10:

    print("set_quality('1080p')")
elif internet_speed > 5:
    print("set_quality('720p')")
else:
    print("set_quality('480p')")    





Practice programs: # medium_level

Scenario: A system checks if a user is eligible for a senior citizen discount (age ≥ 60).
Write a program that takes a person's age as input and prints "Eligible for discount" if they are 60 or older.

age= int(input())
if age >= 60:
    print("Eligible for discount")

Scenario: A shopping site offers free shipping for orders above ₹500.
Write a program that takes the total bill amount as input. If it's above ₹500, print "Free Shipping", otherwise print "Shipping Charges Applied".

bill=int(input())
if bill >= 500:
    print("Free Shipping")
else:
    print("Shipping Charges Applied")    







Using if-elif-else (Multiple Conditions)
📌 Scenario: A system classifies water usage based on liters used.
Write a program that takes the number of liters used as input.
If usage is less than 100 liters, print "Low usage".
If usage is between 100 and 500 liters, print "Moderate usage".


If usage is above 500 liters, print "High usage".

water_usage=int(input())
if water_usage<100:
    print("Low usage")
elif water_usage >=100 and water_usage<=500:
    print("Moderate usage")
elif  water_usage  >500:
    print("High usage")







Using Nested if (Multiple Conditions Inside)
📌 Scenario: A movie booking system checks age and ticket availability.
Write a program that asks for a person's age and checks if tickets are available.
If the person is 18 or older, check if seats are available:


If seats are available, print "Booking Confirmed".


Otherwise, print "Tickets Sold Out".


If the person is under 18, print "Not eligible for this movie".



age= int(input())
seat=input()
if age >=18:
    if seat=="available":
        print("Booking Confirmed")
    else:
        print("Tickets Sold Out")    

else:
    print("Not eligible for this movie")

'''

#Programs on strings:

#Replace all occurrences of "a" with "@" in a given string.
'''
string=input()
print(string.replace('a','@'))'''

#Write a program to print the first and last character of a given string.

'''name=input()
print(name[0])
print(name[-1])'''

#Write a program to convert a string to uppercase and lowercase.
'''
name=input()
print(name.upper())
print(name.lower())'''

#Write a program to remove all spaces from a given string.
'''name=input()
print(name.rstrip())'''
#Check if the word "Python" exists in the given sentence.
'''
sentence= input()
if "python " in sentence:
    print("exist")
else:
    print("Not exist")   ''' 
#Print the first three characters of a given string.
'''
word= input()
print(word[0:3])'''
#Take two strings as input and merge them.
'''
s1=input()
s2=input()
print(s1+s2)'''
#Write a program to check if a string contains only numbers.
'''
s=input()
print(s.isdigit())'''

#Remove all occurrences of "e" from a string.
'''s=input()
print(s.replace('e'," "))
'''

#Count how many times the letter 'o' appears in a given string.
'''
s=input()
print(s.count("o"))'''

#Medium_level:

#Check if a username contains only letters and numbers
'''
username=input()

print(username.isalnum())
'''
#An email has "@" and ends with ".com".
'''
email=input()
print('@' in email and email.endswith (".com") )

#Ensure a password contains at least 8 characters, a number, and a special character.
password=input()
print(len(password)>=8 and any(c.isdigit() for c in password) and any(not c.isalnum() for c in password))
#Write a program to find the length of a given string without using len().
string="meena"
count=0
for i in string:
    count+=1
print(count)    
#Write a Python program to reverse a given string.
name="meenaa"
print(name[::-1])
#Count Vowels in a String
name=input()
vowels='aeiou'
count=0
for i in name:
    if i in vowels:
    
        count+=1
print(count)    
#Count consonants in a string

name=input()
vowels='aeiou'
count=0
for i in name:
    if i not in vowels:
    
        count+=1
print(count)

#Python_programs:

#Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)
#Print numbers from 10 to 1 using a while loop.
i=10
while i >0:
    print(i)
    i-=1

#Print all even numbers from 1 to 20.
for i in range(1,21):
    if i %2==0:
        print(i)
#Print the sum of the first 10 natural numbers.
su=0
for i in range(1,11):
    su+=i
print(su)    
#Print the multiplication table of a given number.
n=int(input())

for i in range(1,11):
    
    print(f"{n}*{i} ={n*i}") 

#Find the factorial of a given number using a while loop.
n=int(input())
fact=1
while n>0:
    fact*=n
    n-=1
print(fact)    

#Check if a number is prime or not.
n=int(input())
count=0
if n>1:
    for i in range(1,n+1):
        if n%1==0:
            count+=1
if count ==2:
    print("not prime")
else:
    print("prime")            



#Find the sum of digits of a given number.
n=int(input())
total=0
while n >0:
    digit=n%10
    total+=digit
    n//=10
print(total)    
#Print all odd numbers from 1 to 50.
for i in range(1,51):
    if i %2!=0:
        print(i) 
#Find the largest number in a list using a loop.
list=[1,2,3,4,5,6,3]
large=list[0]
for i in list:
    if i >large:
        large=i
print(large)        

#Print all numbers from 1 to 100 that are divisible by 5.
for i in range(1,101):
    if i %5==0:
        print(i)


#Programs on tuples:
#Write a program to create a tuple containing integers, strings, and floats. Print the tuple.
tup=(123,"hi meena",4.5)
print(tup)
#Given the tuple t = (10, 20, 30, 40, 50), write a program to print the first and last elements using indexing.
t = (10, 20, 30, 40, 50)
print(t[0])
print(t[-1])
#Write a program to slice a tuple t = (1, 2, 3, 4, 5) and print elements from index 1 to 3.
t = (1, 2, 3, 4, 5)
print(t[1:4])

#Given a tuple t = (1, 2, (3, 4), 5), write a program to access the second element of the nested tuple
t = (1, 2, (3, 4), 5)
print(t[2][1])

#Given a tuple t = (1, 2, (3, 4), 5), write a program to access the second element of the nested tuple.
t = (1, 2, (3, 4), 5)
print(t[2][1])
#Write a program to find how many times a specific element appears in a tuple t = (1, 2, 3, 1, 4, 1).
t = (1, 2, 3, 1, 4, 1)
n= int(input())
print(t.count(n))


#Write a program to find the index of a specific element in the tuple 
t = ("apple", "banana", "cherry")
n=input()
print(t.index(n))


#Write a program to concatenate two tuples and print the result. For example, 
t1 = (1, 2, 3) 
t2 = (4, 5, 6)
result=t1+t2
print(result)

#Write a program to multiply a tuple by an integer. For example, multiply the tuple t = (1, 2) by 3.
t=(1,2)
n=int(input())
result=t*n
print(result)

#Write a program to find the length of a given tuple.
n=("apple","melon","mango")
print(len(n))

#Write a program to check if an element exists in a given tuple.
tup=(3,4,2,6,1)
n=int(input())
if n in tup:
    print("exists")     
#Write a program to delete a tuple after it has been created and print a message.
tup=(1,2,3,5,4,2)
del tup
print("tuppu deleted *-*")                 


#programs:

#Create and Print a Dictionary
dici={"shorttops":5,"jeans":3,"sarees":8}
print(dici)                 

#Access a Value Using Key
dici={"shorttops":5,"jeans":3,"sarees":8}
key=input()
print(dici[key])


#Add a New Key-Value Pair
dici={"shorttops":5,"jeans":3,"sarees":8}
key=input()
value=input()
dici[key]=value
print(dici)
 
#Update an Existing Value
dici={"shorttops":5,"jeans":3,"sarees":8}
key=input()
value=input()
dici[key]=value
print(dici)
#Delete a Key-Value Pair
dici={"shorttops":5,"jeans":3,"sarees":8}
key=input()
del dici[key]
print(dici)
#Check if a Key Exists

dici={"shorttops":5,"jeans":3,"sarees":8}
key=input()
if key in dici:
    print("exisit")

'''
