uname=[]
pword=[]
num=0
while True:
    opt=int(input("[1]Create \t[2]Login \nEnter:"))
    if opt==1:
        u=input("Enter your username: ")
        if len(uname)==0:
            p=input("Enter password: ")
            uname.append(f'{u}{num}')
            pword.append(p)
            print("Your username digit is : ",num)
        else:
            num+=1
            p=input("Enter password: ")
            uname.append(f'{u}{num}')
            pword.append(p)
            print("You username digit is : ",num)
    elif opt==2:
        u=input("Enter your username: ")
        a=int(input("Enter your username digit : "))
        new=f'{u}{a}'
        if new in uname:
            p=input("Enter your password: ")
            if p == pword[a]:
                print("Login sucessfully..")
            else:
                print("incorrect password.")
        else:
            print("incorrect username.")
    
    else:
        print("invlaid Entery.")
