#!/usr/bin/env python
# coding: utf-8

# # Week 2 - Monday Lesson (variable assignment, loops, lists)

# ## Tasks Today:
# 
# 1) Int & Float assignments <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Assigning int <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Assigning float <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Performing Calculations on ints and floats <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Addition <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Subtraction <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Multiplication <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Floor Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Modulo <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Exponential <br>
# 2) String Input-Output <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) String Assignment <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) print() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) String Concatenation <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Type Conversion <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) input() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) format() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) Old Way (python 2) <br>
# 3) <b>In-Class Exercise #1</b> <br>
# 4) If Statements <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) 'is' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) 'not in' keyword <br>
# 5) <b>In-Class Exercise #2</b> <br>
# 6) Elif Statements <br>
# 7) Else Statements <br>
# 8) <b>In-Class Exercise #3</b> <br>
# 9) For Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Using 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Continue Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Break Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Pass Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Double For Loops <br>
# 10) While Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Looping 'While True' <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) While and For Loops Used Together <br>
# 11) Built-In Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) range() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) len() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) help() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) isinstance() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) abs() <br>
# 12) Try and Except <br>
# 13) Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Indexing a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) .append() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) .insert() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) .pop() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) .remove() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) del() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Concatenating Two Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Lists Within Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Looping Through Lists <br>

# ### Int & Float Assignments

# ##### Assigning int

# In[1]:


number = 6

print(number)


# ##### Assinging float

# In[5]:


numberFloat = 2.3
print(numberFloat)
print(numberfloat)
numberFloat = 7.2
print(numberFloat)


# #### Performing Calculations on ints and floats

# ##### Addition

# In[8]:


num1 = 2
num2 = 4.4

results = num1 + num2

print(results)

results += 3

print(results)


# ##### Subtraction

# In[10]:


results_diff = num2 - num1
print(results_diff)

results_diff -= 2
print(results_diff)


# ##### Multiplication

# In[13]:


results_mul = num1 * num2

print(results_mul)

results_mul *= 3
print(results_mul)


# ##### Division

# In[15]:


results_div = num2/num1 
print(results_div)

results_div /= 2
print(results_div)


# ##### Floor Division

# In[18]:


results_floor = num2 // num1
print(results_floor)
results_floor //=2
print(results_floor)


# ##### Modulo

# In[23]:


results_mod = num2 % num1
print(results_mod)

results_mod = 10 % 3
print(results_mod)

results_mod %= 2
print(results_mod)


# ##### Exponential

# In[25]:


square = 5 ** 2
print(square)

square **= 4
print(square)


# ### String Input-Output

# ##### String Assignment

# In[26]:


name = "Joe"
print(name)


# ##### print() <br>
# <p>Don't forget about end=' '</p>

# In[35]:


print("This is my first name:", name)
print("Full name:", name, end=" Shmoe")


# ##### String Concatenation

# In[46]:


first_name = "Camille"
last_name = "Haile"
full_name = first_name + ' ' + last_name
print(full_name)
full_name += ' Jr'
print(full_name)


# ##### Type Conversion

# In[ ]:


##### format()
number = '32' change_type_num = int(number)
print(number)
print(change_type_num + 3)



# number = '32'
# change_type_num = int(number)
# print(number)
# print(change_type_num + 3)

# ##### input()

# In[ ]:


name = input('What is your name?')
print('Nice to meet you, ' + name)


# In[ ]:


age = input("What is your age?: ")
add_age = age + 5
print(add_age)


# ##### Old Way (python 2)

# In[ ]:


result_string2 = "You are {} {} and you are getting wiser." .format(age, name)
print(result_string2)


# # In-Class Exercise 1 <br>
# <p>Create a format statement that asks for color, year, make, model and prints out the results</p>

# In[ ]:


name = input('What is your name?')
color = input('What color is your car? ')
year = input('What year is your car? ')
model = input('What model is your car? ')
results = f"{name} your{year} {model}'s color is {color}'
print(results)


# ### If Statements

# In[ ]:


# Available operators: Greater(>), Less(<),Equal(==)
# Greater or Equal(>=), Less or Equal (<=)

# Truth Tree:
# T && F = F
# T && T = T
# T || F = T
# F || T = T
# F || F = F

num1 = 5 
num2 = 10
num3 = 1

if num1 == num2:
    print('Equal values')
else:
    print('Not equal')

if num1 < num2 or num3 > 0:
    print('This ran')
else:
    print('You are here!' )


# ##### 'is' keyword

# In[ ]:


num3 = 55

if num3 == 55:
    print('This is the exact number/object')


# ##### 'in' keyword

# In[ ]:


char_name = "Frodo Baggins"
if "Frodo" in char_name:
    print("The ring bearer")


# ##### 'not in' keyword'

# In[ ]:


if 'a' not in sega_char:
    print('a is not here...')


# # In-Class Exercise 2 <br>
# <p>Ask user for input, check to see if the letter 'p' is in the input</p>

# In[ ]:


my_variable = input('What is your input?')
if 'p' in my_variable:
    print('The letter p is in here')
else:
    print('The letter p is not here')


# ## Using 'and'/'or' with If Statements

# In[ ]:


num_11 = 15
num_12 = 3
num_13 = 10
num_14 = 3

if num_11 / 5 == num_12 and num_13 - 7 == num_14:
    print('ture and true')
    
if num_13 == num_14 or num_11 > num_12:
    print('False and true')


# ### Elif Statements

# In[ ]:


first_name = input('What is your name? ')

if first_name == Smith:
    print('The name is Smith')
elif first_name == "Brandon":
    print('The name is Brandon')
elif first_name != 'Max':
    print('The name is NOT Max')
else:
    print('The name is Max')
    


# 

# ### Else Statements

# In[ ]:


# see above


# ### For Loops

# In[ ]:


name = 'Brandon Apol'

for ANYTHING_YOU_WANT in name:
    print(ANYTHING_YOU_WANT)
    
for i in a list:
    print(i)


# ##### Using 'in' keyword

# In[ ]:


# see above


# ##### Continue Statement

# In[ ]:


# will continue to next iteration


# In[ ]:


if i == 5:
        continue
        print(i)


# ##### Break Statement

# In[ ]:


# will break out of current loop


# In[ ]:


for i in range (20):
    if i == 5:
        break
        print(i)


# ##### Pass Statement

# In[ ]:


# mostly used as a placeholder, and will continue on same iteration


# In[ ]:


name = 'Brandon Apol'

for i in name:
    pass
    print(i)


# ##### Double For Loops

# In[ ]:


for i in range(500000000):
    for j in range(500000000):
        print('i = ', 'i', 'j = ', 'j')


# ### While Loops

# In[ ]:


num = 0

while num < 10:
    print(num)
    num += 1


# ##### Looping 'While True'

# In[ ]:


game_over  = False
game_over = True
print(game_over)


# ##### While & For Loops Used Together

# In[ ]:


num = 0

while num < 5:
    print('/nwhile loop iteration:' + str(num))
for i in range(2):
    print('for loop iteration:' str(i + 1))


# ### Built-In Functions

# ##### range()

# In[53]:


for i in range(2, 20, 2):
    print(i)


# ##### len()

# In[52]:


name = input('give me the name of your favorite book:' )

length = len(name)
print(length)


# ##### help()

# In[54]:


help(len)


# ##### isinstance()

# In[ ]:


num = 4

if isinstance(name, int):
    print('f {num} is an int')
else:
    print('f {num} is a float')


# ##### abs()

# In[55]:


print(abs(-5))


# ### Try and Except

# In[ ]:


try

number_test = 0
input_num = int(input('Guess a number'))
if input_num != input_num + number_test:
    input_num = input_num + number_test
    print('your number is, ' + str')


# ### Lists

# ##### Declaring Lists

# In[56]:


list_1 = []
name = ['max, keith, cindy, lou, patrick']
print(name)


# ##### Indexing a List

# In[60]:


#list_names = 'start, stop, step'
#print(list_names(0))


# ##### .append()

# In[64]:


print(name[1])

print(name[1 :])

print(name[: 2])


# ##### .insert()

# In[ ]:





# ##### .pop()

# In[ ]:





# 
# ##### .remove()

# In[ ]:





# ##### del()

# In[ ]:





# ##### Concatenating Two Lists

# In[ ]:





# ##### Lists Within Lists

# In[ ]:





# ##### Looping Through Lists

# In[ ]:





# ## Exercise #1 <br>
# <p>Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.</p>

# In[71]:


def cube_number_test():
    num = 1
    while True:
        cube = num ** 3
        if cube > 1000:
            break
        print(cube)
        num += 1


# ## Exercise #2 <br>
# <p>Get first prime numbers up to 100</p>

# In[72]:


# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break

def get_first_primes_up_to_100():
    for num in range(2, 101):
        if is_prime(num):
            print(num)
        else:
            break


# # Exercise 3 <br>
# <p>Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors</p>

# In[73]:


def categorize_age():
    age = int(input("Please enter your age: "))
    
    if age < 18:
        print("Kids")
    elif age >= 18 and age <= 65:
        print("Adults")
    else:
        print("Seniors")


# In[74]:


31


# In[75]:


15

