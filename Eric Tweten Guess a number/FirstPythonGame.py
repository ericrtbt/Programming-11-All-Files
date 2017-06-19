import random 
my_number = random.randrange(101)
mistakesmade = 0
guess = 0
print("a: Guess The Number!\nb: Or Quit!")
my_input = input("\n")
if my_input.lower() == "a":

    while mistakesmade < 1000:
        print('Take a guess!')
        guess = input()
        guess = int(guess)
    
        mistakesmade = mistakesmade + 1
    
        if guess < my_number:
            print("Your guess is too low.") 
    
        if guess > my_number:
                print("Your guess is too high.")    
            
        if guess == my_number:
                    print("Congratulations, you guessed correctly!")
                    break
                
else: 
    my_input.lower() == "b"
    done = False
    if quit == "b":
        done = True   

if guess == my_number:
    mistakesmade = str(mistakesmade)
    print("Good job,! You guessed my number in "  + mistakesmade +  " guesses!")
    
   