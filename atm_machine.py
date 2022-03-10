users={"praveen":"123","kumar":"1234","vijay":"12345","arun":"321","python":"4321"}
while True:
    opt=int(input("[1] Login \nEnter: "))
    if opt==1:
        un=input("Enter your username: ")
        for i in users:
            if un==i:
                pw=input("Enter your password: ")
                if pw==users[un]:
                    print("Login successfully..")
                    db={"praveen":0,"kumar":0,"vijay":0,"arun":0,"python":0}
                    while True:
                        opt2=int(input("[1]view balance\t[2]Deposit\t[3]Withdrawl\t[4]Transfer \nEnter:"))
                        if opt2==1:
                            print(db[un])
                        elif opt2==2:
                            dp=int(input("Enter the amount to be deposit: "))
                            db[un]=db[un]+dp
                            print(db)
                        elif opt2==3:
                            wd=int(input("Enter amount to be withdrawl: "))
                            db[un]=db[un]-wd
                            print("Your bank balance is : ",db[un])
                        elif opt2==4:
                            unam=input("Enter the reciver username:  ")
                            for i in db:
                                if i==unam:
                                    dpun=int(input("Enter the amount to be transfer: "))
                                    db[un]=db[un]-dpun
                                    db[unam]=db[unam]+dpun
                                    print(db)
                                    break
                            else:
                                print("Ivalid reciver name..")
                        else:
                           print("Invalid input..")
                else:
                    print("Incorrect password.")
                    break
        else:
            print("Incorrect username.")
    else:
        print("Invalid input.")
