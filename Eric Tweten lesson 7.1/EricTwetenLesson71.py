x = [1,2]
print(x)

print(x[0])

x[0] = 22
print(x)


my_list = [101, 20, 10, 50, 60]
for item in my_list:
    print(item)
    
my_list = ["Spoon", "Fork", "Knife"]
for item in my_list:
    print(item)
    
my_list.append("Ladle")
for item in my_list:
    print(item)
    
my_list = [] # Empty list

#for i in range(5):
#    user_input = input( "Enter an integer: ")
 #   user_input = int(user_input)
 #   my_list.append(user_input)
 #   print(my_list)
    
    # Copy of the array to sum
my_list = [5,76,8,5,3,3,56,5,23]
     
    # Initial sum should be zero
list_total = 0
     
    # Loop from 0 up to the number of elements
    # in the array:
for i in range(len(my_list)):
        # Add element 0, next 1, then 2, etc.
    list_total += my_list[i]
     
    # Print the result
print(list_total)

# Copy of the array to modify
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
 
# Loop from 0 up to the number of elements
# in the array:
for i in range(len(my_list)):
    # Modify the element by doubling it
    my_list[i] = my_list[i] * 2
 
# Print the result
print(my_list)
