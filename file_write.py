def getdate():
    import datetime
    return datetime.datetime.now()
client_choice = int(input())
client_no = int(input("Enter client number: 1. Harry \n 2. Rohan \n 3. Hammad:"))
if client_choice==1:
    print(client_choice)
    if client_no == 1:
        print(client_no)
        client_routine = int(input("What client wants: 1. exercise \n 2. Diet:"))
        print(client_routine)
        if client_routine == 1:
            f = open("harry.txt","a")
            #content = input("Enter plans:")
            f.write(str(getdate()))
            f.write(input())
            f.close()

