#Faulty Calculator
op = input("Enter the operation you want to perform(+,-,/,*):")
a=int(input("Enter first number:"))
b= int(input("enter second number:"))

#Addition
if op =="+":
    if a==56 and b==9 or a==9 or b==56:
        print(77)
    else:
        c= a+b
        print(c)
#subtraction
if op=="-":
    print (a-b)

#Multiplication
if op =="*":
    if a==45 and b==3 or a==3 or b==45:
        print(555)
    else:
        c= a*b
        print(c)

#division
if op =="/":
    if a==56 and b==6:
        print(4)
    else:
        c= a/b
        print(c)