dici = {
    "id": "M16i0032004",
    "pin": "20041103",
    "money":50000
}
 
def deposite():
    newmoney=int(input("enter diposite money:"))
    if newmoney >0:
        dici['money'] += newmoney     
        print("deposite sucessfull","Balance:",dici['money'])
    else:
        print("enter valid amount")
def withdraw():
    amount = int(input("enter the amount for withdrawl"))
    if amount >0 and amount <= dici["money"]:
        dici["money"]-=amount
        print("Withdrawal successful","Balance:",dici['money'])    
    else:
        print("insufficient balance" )    
def pinchange():
    oldpin=input("enter old pin")
    if oldpin==dici["pin"] :
        newpin=input("enter new pin")
        dici["pin"]=newpin
        print("Pin changed successfully")
    else:
        print("invalid old pin")           
def login():
    id=input("enter id:")  
    
    if id == dici["id"]:
        pin=input("enter pin:")
        if pin == dici["pin"]:
            print("login successes")
            print("1.Deposite")
            print("2.Withdrawl")
            print("3.Pin Change")
            print("4. Exit")
            choice=int(input("Please enter your choice:"))
            if choice==1:
                deposite()
            elif choice==2:
                withdraw() 
            elif choice==3:
                pinchange()    
            elif choice==4:
                print("Thank you ")
                print("visit again")     
            else:
                print("invalid choice")
                  

        else:
            print("incorrect pin")    
    else:
        print("incorrect id")  

login()
    