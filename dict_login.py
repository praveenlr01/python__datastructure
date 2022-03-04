users={"praveen":"123","kumar":"1234","lr":"12345","vijay":"321","vj":"4321"}
while True:
    opt=int(input("[1] Login \nEnter: "))
    if opt==1:
        un=input("Enter your username: ")
        if un in users:
            pw=input("Enter your password: ")
            if users[un]==pw:
                print("Login successfully..")
            else:
                print("incorrect password.")
        else:
            print("incorrect username.")
    else:
        print("invalid Entery.")
