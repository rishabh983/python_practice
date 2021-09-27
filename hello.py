# l = ["rishabh","jain",2,4,5,6,7,45,6]
# for item in l:
#     if str(item).isnumeric() and item>4:
#         print(item)

a=int(input("Enter number:"))
while(True):
    if a<=100:
        a=int(input())
        continue
    if a>100:
        print("Congratulation you've entered number greater than 100")
        break
    