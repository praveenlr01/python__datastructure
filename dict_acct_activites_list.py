db={}
i=0
act={}

while True:
    opt=int(input("[1]Create [2]Login\nEnter: "))
    if opt==1:
        if len(db)==0:
            un=input("Enter your Username: ")
            pw=input("Enter your Password: ")
            db.update({un:pw})
        elif len(db)!=0:
            un=input("Enter your Username: ")
            for x in db:
                if x in un:
                    print("Usernmae is already taken.")
            else:
                pw=input("Enter your Password: ")
                db.update({un:pw})
    elif opt==2:
        un=input("Enter your Username: ")
        if un in db:
            pw=input("Enter your Password: ")
            if db[un]==pw:
                print("Login Sucessfully.")
                l,c,p,s=0,0,0,0
                while True:
                    optt=int(input("[1]Like [2]Comment [3]Post [4]Share [5]View Activites\nEnter: "))
                    i+=1
                    if optt==1:
                        l+=1
                        print("no of Like is : ",l)
                        act.update({i:f'{i}.no of like {l}'})
                    elif optt==2:
                        c+=1
                        print("no of comment : ",c)
                        act.update({i:f'{i}.no of comment {c}'})
                    elif optt==3:
                        p+=1
                        print("no of Post : ",p)
                        act.update({i:f'{i}.no of Post {p}'})
                    elif optt==4:
                        s+=1
                        print("no of Share : ",s)
                        act.update({i:f'{i}.no of Share {s}'})
                    elif optt==5:
                        for a in range(len(act)):
                            print(act[a+1])
                    else:
                        print("Invalid Entery.")
            else:
                print("Incorrect Password.")
                break
        else:
            print("Invalid Username.")
            break
    else:
        print("Invalid Entery")
