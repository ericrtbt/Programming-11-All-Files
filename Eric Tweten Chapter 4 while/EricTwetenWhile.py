i = 0
while i < 10:
    print(i)
    i = i + 1
    
i = 1
while i <= 2 ** 32:
    print(i)
    i *= 2
    
#quit = "n"
#while quit == "n":
 #   quit = input("Do you want to quit? ")

#done = False
#    quit = input("Do you want to quit? ")
    if quit == "y":
        done = True
     
        attack = input("Does your elf attack the dragon? ")
        if attack == "y":
            print("Bad choice, you died.")
            done = True
            
value = 0
increment = 0.5
while value < 0.999:
    value += increment
    increment *= 0.5
    print(value)
    
import random
my_number = random.randrange(50)
print (my_number)

my_list = ["rock", "paper", "scissors"]
random_index = random.randrange(3)
print(my_list[random_index])