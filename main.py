import dbCRUD
mydb=dbCRUD.dbutil()
mydb.init()
while(True):
    print("select an option you want to perform on database")
    print("1.insert\n2.delete\n3.read\n4.update")
    ch=int(input())
    if(ch==1):
        lst = []
        lst.append(int(input("Enter ID:\n")))
        lst.append(input("Enter Name:\n"))
        lst.append(input("Enter Email:\n"))
        mydb.insert(tuple(lst))
    elif(ch==2):
        print("Enter id you want to delete:")
        key=int(input())
        mydb.delete(key)
    elif(ch==3):
        mydb.read()
    elif(ch==4):
        print("Enter id you want to update:")
        id=int(input())
        print("Enter Column you want to update:\n1.id\n2.name\n3.column")
        col=int(input())
        if(col==1):
            colmn='id'
        elif(col==2):
            colmn='name'
        else:
            colmn='email'
        print("Enter the new value in "+colmn+" column:")
        new=input()
        mydb.update(id,colmn,new)
    else:
        break