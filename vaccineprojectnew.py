#VACCINATION REGISTERATION SOFTWARE USING PRIORITY QUEUE DATA STRUCTURE IN PYTHON


record=[]   #empty queue created to  store data  
numvac=0    #number of vaccines available initialized to 0    
total=0     #total citizen registered initialized to 0

#register function definition
def register():
    global numvac,total
    if numvac<=total:
        print("Vaccines are out of stock.")
        print()
        print("But you can proceed to register.")
    name=input("Enter your name:")
    id=int(input("Enter your id:"))
    age=int(input("Enter your age:"))
    record.append((age,id,name))
    record.sort(reverse=True)
    total+=1

#display funtion definition
def display():
    k=1
    print()
    print("The list of Citizens are:\n")
    for i in record:
            print("Citizen:",k)
            print("AGE:",i[0])
            print("ID:",i[1])
            print("NAME:",i[2])
            print()
            k+=1

#next citizen to vaccinate display function definition      
def nextv():
    global total
    if total>0:
        print()
        print("AGE:",record[0][0])
        print("ID:",record[0][1])
        print("NAME:",record[0][2])
    else:
        print("No citizen registered")

#vaccination done funtion definition
def done():
    global total,numvac
    if total>0 and numvac>0:
        print()
        print("NAME:",record[0][2],"Done with Vaccination.")
        record.pop(0)
        total-=1
        numvac-=1
    else:
        if total==0:
            print("No citizen registered")
        if numvac==0:
            print("No vaccines available")
    
#funtion to take input of number of vaccines available
def numvaccine():
    global numvac
    numvac=int(input("Enter the number of vaccines available:"))
    print("Thank you for Updating")

#menu driven program starts
while True:
    print()
    print("Vaccine registration Software")
    print()
    print("1.Register for vaccination\n2.Display details of citizens registered\n3.Next for vaccination\n4.Vaccination done\n5.Enter number of Vaccines available\n6.exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        register()
    elif choice==2:
        display()
    elif choice==3:
        nextv()
    elif choice==4:
        done()
    elif choice==6:
        exit(0)
    elif choice==5:
        numvaccine()
    else:
        print("Invalid Choice")
