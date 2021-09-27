x=int(input())
print(bool(x))
n = int(input("Enter the number:"))
if (bool(x)==True):
    for i in range(0, n):
        for j in range (0,i+1):
            print("*", end=" ") 
        print("\n")

elif (bool(x)==False):
    for i in range (5,0,-1):
        #print(i)
        for j in range(0,i):
            print(j)
            print("*", end= " ")
        print("\n")