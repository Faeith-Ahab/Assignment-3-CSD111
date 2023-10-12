# Create a function that returns your full name and age as a function
def my_name_and_age(name,age) :
    print(f"My name is {name} and I am {age} years old.")
my_name_and_age("Faith", 28)
    

# Write a python program to sum all numbers in the list [8, 2, 3, -1, 7]
def multiply(thelist):
    product = 1
    for x in thelist:
        product *=x
    return product
print (multiply([8,2,3,-1,7]))

# Write a python program to reverse a string (1, 2, 3, 4, a, b, c, d)
text = "1, 2, 3, 4, a, b, c, d"[::-1]
print(text)

# Write a python function to multiply all the numbers in the list
import numpy
 
list1 = [1,2,3,4,5,6,7,8,9]
ans1 = numpy.prod(list1)

print("Multiplication of elements of list1 is ",ans1)

# Write a python program to print all the even numbers in the list 

numbers = (1,2,3,4,5,6,7,8,9)
count_even = 0
count_odd = 0

for x in numbers:                   
    if x%2 == 0 :                   
       count_even +=1               
    else:
        count_odd +=1               

print(count_even)


