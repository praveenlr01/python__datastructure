db={}
while True:
    opt=int(input("[1]create \t[2]Login \nEnter: "))
    if opt==1:
        un=input("Enter your username: ")
        if un in db:
            print("username is taken..")
        else:
            pw=input("Enter your password: ")
            db.update({un:pw})
    elif opt==2:
        un=input("Enter your username: ")
        for i in db:
            if i == un:
                pw=input("Enter your password: ")
                if pw==db[un]:
                    print("login sucessfully..")
                    print(db)
                    while True:
                        optt=int(input("[1]username change \t[2]password change \nEnter : "))
                        if optt==1:
                            una=input("Enter your current username: ")
                            if una==un:
                                if una in db:
                                    uname=input("Enter your new username: ")
                                    db[uname]=db.pop(una)
                                    un=uname
                                    print(db)
                                    print("Username is changed successfully..")
                                else:
                                    print("invalid username.")
                            else:
                                print("invalid username...")
                        elif optt==2:
                            una=input("Enter your username: ")
                            if una==un:
                                for i in db:
                                    if una==i:
                                        pasw=input("Enter new password: ")
                                        db[una]=pasw
                                        print("The password changed sucessfully..")
                                        print(db)
                                        un=una
                                        break
                                else:
                                    print("invalid username..")
                                    print(db)
                            else:
                                print("invalid username..")
                        else:
                            print("invalid entery.")
                            break
                else:
                   print("incorrect password.")
                   break
            else:
                print("incorrect username")
                break
        else:
            print("incorrect username.")
            break
