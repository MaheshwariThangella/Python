'''# [[1,2,3],[4,5,6],[7,8,9]]
def fun(lists):
    output=[]
    for sub in lists:
        for i in sub:
            output.append(i)
    return output
lists=[[1,2,3],[4,5,6],[7,8,9]]
print(fun(lists))





# cricket:
def Score_board(overs):
    l = []
    start = 1
    total_wickets = 0

    while start <= overs:
        balls = 1
        over_results = []

        while balls <= 6:
            ball_score = input(f"Enter over {start} ball {balls}: ").lower()

            if ball_score == "w":
                l.append("w")
                over_results.append("w")
                total_wickets += 1
            else:
                l.append(ball_score)
                over_results.append(ball_score)

            balls += 1

            if total_wickets == 10:
                print("Stop! 10 wickets completed")
                break

        print("Over", start, "results:", over_results)

        if total_wickets == 10:
            break

        start += 1

    print("Total wickets:", total_wickets)
    print("All balls results:", l)


Score_board(2)

dici={}
def register():
    username=input("enter username:")
    password=input("enter password:")
    if not (2 <= len(username) <=12):
        print("username must be in between 2 to 12 characters")
    elif not username.isalpha():
        print("username must be in letters")
    elif not password.isdigit():
        print("password must be in numbers")
    elif not (6<= len(password) <=10):
        print("password must be in between in 6 to 10 digits")
    elif username in dici:
        print("user Already in Exist")
    else:
        dici[username]= password
        print ("Registration Succed")
def login():
    username=input("enter username:")
   
    if username not in dici :
        print("user does not exits")
        return
    password=input("enter password:")
    if dici[username]== password:
       
            print("login successful")
        
    
    else:
        print("invalid usename or password")        
register()                          
login()'''




import functools
print(help(functools))