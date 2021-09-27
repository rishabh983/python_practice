n=25
no_of_guess = 0
total_guess = 5
print("You have 5 chance to guess the number")

while(no_of_guess<5):
    a = int(input("Enter the number:"))
    if a>n:
        print("enter less value")
        no_of_guess = no_of_guess+1
        total_guess = total_guess-1
        print("you have",total_guess," chances left")
    elif a<n:
        print("enter greater value")
        no_of_guess = no_of_guess+1
        total_guess = total_guess-1
        print("you have",total_guess," chances left")
    else:
        print("Congratulations you've entered correct value")
        break
c = int(no_of_guess)+1
print("No of guesses took", c)
if no_of_guess == 5:
    print("Game Over")