#Write a function that takes an unknown
#number of arguments and returns their sum.
def args(*args):
    sum=0
    for arg in args:
        sum +=arg
    return sum
print(args(400,600,200,150,400)) 

#Write a function that takes two arguments, the
#first being a string and the second being an unknown number 
#of integers. The function should return a new string where the 
#integers have been added to the original string

def add_integers_to_string(string, *integers):
    string_new = string
    for integer in integers:
        string_new += str(integer)
    return string_new
original_string = "sum of my integers is:"
string_new = add_integers_to_string(original_string, 30,50,10)
print(string_new)

#Write a function that takes an unknown number 
#of keyword arguments and returns a dictionary
#where the keys are the argument names 
#and the values are the argument values.
def key_args(**kwargs):
    return kwargs
answer = key_args(name='Fawzia', age=23, city='Nairobi Kenya')
print(answer)

#Write a function that takes a function and an 
#unknown number of arguments, and returns the result 
#of calling the function with the arguments.

def add_numbers(*args):
    return sum(args)

result = add_numbers( 1, 2, 3, 4, 5)
print(result) 

#Write a function that takes a list of integers 
#and an unknown number of keyword arguments. The function
#should return a new list where each integer in the original 
#list has been multiplied by
#the value of the corresponding keyword argument.
def multiply_list_with_kwargs(int_list, **kwargs):
    new_list = []
    for num in int_list:
        multiplied_num = num
        for key, value in kwargs.items():
            if key == str(num):
                multiplied_num *= value
        new_list.append(multiplied_num)
    return new_list
int_list = [1, 2, 3, 4, 5]
multiplied_list =(1*2, 2*3, 3*4, 4*5, 5*6)
print(multiplied_list)

#Write a function that takes a list of integers 
#and an unknown number of additional integers as arguments.
#The function should return the index of the first occurrence 
#of the sum of the list and the additional integers

#Write a function that takes an unknown number of 
#keyword arguments, each with a string value. The function should 
#concatenate all the strings
 #and return the resulting string.