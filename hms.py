# f = open("client1.txt","w")
# # print(f.readline())
# content = f.read(5)
# print(content)
# f.close()

def getdate():
    import datetime
    return datetime.datetime.now()

def retrieve_data(a):
    if a==1:
        f = open("harry.txt","r")
        print(f.read())
        f.close()
    elif a==2:
        f = open("rohan.txt","r")
        print(f.read())
        f.close()
    elif a==3:
        f = open("hammad.txt","r")
        print(f.read())
        f.close()

print("Fitness plans for clients: Do you want to 1.lock the data or 2.retrieve the data?")
client_choice = int(input())
client_no = int(input("Enter client number: 1. Harry \n 2. Rohan \n 3. Hammad:"))
if client_choice==1:
    if client_no == 1:
        client_routine = int(input("What client wants: 1. exercise \n 2. Diet:"))
        if client_routine == 1:
            f = open("harry_exercise.txt","a")
            content = input("Enter plans:")
            f.write(str(getdate()) + ":")
            f.write(input() + "\n")
            f.close()
            
        elif client_routine == 2:
            f = open("harry_diet.txt","a")
            content = input("Enter plans:")
            f.write(str(getdate()) + ": " + content+ "\n" )
    
    elif client_no == 2:
        client_routine = int(input("What client wants: 1. exercise \n 2. Diet:"))
        if client_routine == 1:
            f = open("rohan_exercise.txt","a")
            content = input("Enter plans:")
            f.write(str(getdate()) + " :" + content + "\n")
        elif client_routine == 2:
            f = open("harry_diet.txt","a")
            content = input("Enter plans:")
            f.write(str(getdate()) + " :" + content + "\n")
    
    elif client_no == 3:
        client_routine = int(input("What client wants: 1. exercise \n 2. Diet:"))
        if client_routine == 1:
            f = open("hammad_exercise.txt","a")
            content = input("Enter plans:")
            f.write(str(getdate()) + " :" + content + "\n")
        elif client_routine == 2:
            f = open("harry_diet.txt","a")
            content = input("Enter plans:")
            f.write(str(getdate()) + ":" + content + "\n")

elif client_choice == 2:
    if client_no == 1:
        retrieve_data(1)
    elif client_no == 2:
        retrieve_data(2)
    elif client_no == 3:
        retrieve_data(3)