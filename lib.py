import csv
import random
class User():
    lib={}
    def create_acc(self,name,email,phone_no):
        self.year=2026
        self.section="A"
        self.id=random.randint(1,100)
        self.id=str(self.year)+self.section+ str(self.id)
        self.name=name
        self.email=email
        self.phone_no=phone_no

        User.lib[self.id]={ 
                    "name":self.name,
                    "phone_no":self.phone_no,
                    "email":self.email
                    }
               
        print("Successfully Created Your Account!!!","id :",self.id)
    
    def display(self):
        print("id:",self.id)
        print("name:",self.name)
        print("phone_no:",self.phone_no)
        print("email:",self.email)    

    def login(self):
        login_id=input("enter your id:")
        if login_id in User.lib:
            print("login successfully...")
            return login_id
        else:
            print("Invalid Id!!!!")  
            print("Try Again..")  
            return None
class Library:
    books={101:["Python",5],
           102:["Java",5],
            103:["SQL",5],
             104:["HTML",5],
              105:["CSS",5],
               106:["Javascript",5],
                107:["Flask",5],
                 108:["C",5],
                  109:["C++",5],
                   110:["C#",5] }
    isued_book={}
    def store_book(self):
        with open("books.csv","r")as file:
            reader=csv.DictReader(file)

            Library.books={}
            for row in reader:
                book_id=int(row["book_id"])
                Library.books[book_id]=[
                    row["book_name"],
                    int(row["copies"])
                ]
    def save_book(self):
        with open("books.csv","w") as file:
            writer=csv.writer(file)
            writer.writerow(["book_id","book_name","copies"])            

            for book_id,data in Library.books.items():
                writer.writerow([book_id,data[0],data[1]])


    def storeisued_book(self):
        with open("isued_book.csv", "r") as file:
            reader = csv.DictReader(file)
            Library.isued_book = {}
            for row in reader:
                user_id = row["user_id"]
                book_id = int(row["book_id"])
                if user_id not in Library.isued_book:
                    Library.isued_book[user_id] = []
                Library.isued_book[user_id].append(book_id)

    def save_issued_books(self):
        with open("isued_book.csv", "w") as file:
            writer = csv.writer(file)

            writer.writerow(["user_id", "book_id"])

            for user_id, book_ids in Library.isued_book.items():
                for book_id in book_ids:
                    writer.writerow([user_id, book_id])            
    def search_book(self):
        book_id=int(input("enter book id:"))
        if book_id in Library.books:
            print("Book found!!",Library.books[book_id][0])
            print("Available copies are:",Library.books[book_id][1])


        else:
            print("Book not Found!")    
    def allocate(self,user_id):
        book_id=int(input("enter book id To Allocate:"))
        if book_id in Library.books:
            if Library.books[book_id][1]>0:
                
                if user_id not in Library.isued_book:
                    Library.isued_book[user_id]=[]
                    Library.isued_book[user_id].append(book_id)
                    self.save_book()
                    self.save_issued_books()
                    print("book allocated successfully","book name:",Library.books[book_id][0])
                    
            else:
                print("Book not Available")   
        else:
            print("Book not found")      

    def return_book(self,user_id):
        book_id=int(input("Enter book id to return :"))
        if user_id in Library.isued_book:
            if book_id in Library.isued_book[user_id]:
                Library.isued_book[user_id].remove(book_id)
                Library.books[book_id][1]+=1
                self.save_book()
                self.save_issued_books()
                print("Book returned successfully")
                
            else:
                print("you have not took this book")
        else:
            print("no books issued")                   

 

u = User()
l = Library()
l.store_book()
l.storeisued_book()

while True:
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter your name: ")
        phone_no = input("Enter your phone number: ")
        email = input("Enter your email: ")

        u.create_acc(name, phone_no, email)

    elif choice == "2":

        user_id = u.login()

        if user_id is  not None:

            while True:  
                print("1. Search Book")
                print("2. Allocate Book")
                print("3. Return Book")
                
                print("4. Logout")

                option = input("Enter your choice: ")

                if option == "1":
                    l.search_book()

                elif option == "2":
                    l.allocate(user_id)

                elif option == "3":
                    l.return_book(user_id)

                elif option == "4":
                    print("Logged Out Successfully!")
                    break

                else:
                    print("Invalid Choice!")
    elif choice=="3":
        print("Thank you")  
        break
    else:
        print("invalid choice")                  

    





