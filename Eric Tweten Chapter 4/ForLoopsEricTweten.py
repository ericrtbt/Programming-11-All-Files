for i in range(5):
    print("I will not chew gum in class.")
    
for i in range(5):
        print("Please,")
print("Can I go to the mall?")

for i in range(10):
    print(i)    
    
for i in range(1, 11):
        print(i)
        
# Print the numbers 1 to 10.
for i in range(10):
    print(i + 1)

# Two ways to print the even numbers 2 to 10
for i in range(2,12,2):
    print(i)
     
for i in range(5):
    print((i + 1) * 2)
    
for i in range(10, 0, -1):
    print(i)
  
for i in [2,6,4,2,4,6,7,4]:
    print(i)
    
for i in range(3):
    print("a")
for j in range(3):
    print("b")
    
for i in range(3):
    print("a")
    for j in range(3):
        print("b")
print("Done")

total = 0
for i in range(5):
    new_number = int(input("Enter a number: " ))
    total = total + new_number
#    total += new_number
print("The total is: ", total)

# What is the value of sum?
sum = 0
for i in range(1, 101):
    sum = sum + i
print(sum)

total = 0
for i in range(5):
    new_number = int(input( "Enter a number: "))
    if new_number == 0:
        total += 1
print("You entered a total of", total, "zeros")

# What is the value of a?
a = 0
for i in range(10):
    a = a + 1
print(a)
 
# What is the value of a?
a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1
print(a)
 
# What is the value of a?
a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)