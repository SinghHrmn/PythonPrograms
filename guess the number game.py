import random
while True:
    x = input ("Do you want to play guess a number game.[Y]or[N]")
    if x == "Y" or x == "y":
        print("Guess a number between 1-20.")
        num=random.randint(1, 20)
        count=1
        while count <= 3:
            guess=int(input("Guess a number"))
            if guess == num:
                print("You Won!, You guessed the number right")
                break
            else:
                if guess <= num:
                    print ("You guessed it low")
                else:
                    print("You guessed it High")
            count=count+1
            
        if count == 4:
            print("Sorry, you Lost!")
            print("The right answer was",num)
        
    else:
        print ("Good Bye!")
        break
        

