# -*- coding: utf-8 -*-
"""
Multiline comment
"""

#one line commment

print("Pier's code")

eggs = 5
if eggs > 9:
    print('egss')
elif eggs > 4:
    print('elif')
else:
    print('no eggs')


spam_amount = 3
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

viking_song = "Spam-" * spam_amount
print(viking_song)

print("a","b","c", sep="-")
print('You', 'passed', 'the quiz with a grade of', 99)
print(type('hola'))

negative = '-100'

print(abs(int(negative))+100)

print(round(6.1258789,2))


"""
==============================================
3. Functions and Getting Help
==============================================
"""

#help(abs)
#help(round(-2.01))

def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)




print(
    least_difference(1.6, 2.5, 3)
)


def my_add(one, two):
    """ Adds to values
    >>> my_add(1,2)
    3
    """
    return one + two; 

print(
      my_add(10,5), 
      my_add(10.2,5.3))
help(my_add)

#Function without return, by default return None
def say_something(name):
    print("Hello " + name)

say_something("Ana")
print(say_something("Ana"))

##### Default arguments
def fff(par_one="one", par_two="two"):
    print (par_one + "-" + par_two)
    
fff();
fff("ana","pierina");
fff(par_two="pierina");

### Functions that operate on other funcitons are called 'Higher order functions'

# Example 1
def hi(name):
    return "Hi " + name

def rehi(hifunt, hiargs):
    return hifunt(hiargs)

def recontrahi(hifunt, hiargs):
    return hifunt(hifunt(hiargs)) 

print(hi("dany"))
print(rehi(hi, "maria"))
print(recontrahi(hi, "ana"))



# Example 2
def module_ten(num):
    return num % 10;

thislist = [27, 19, 58]
print(max(thislist, key=module_ten))


"""
==============================================
5. Booleans and Conditionals
==============================================
"""

print(
      "are you adult ",
      29>18)
print(
      "are these equal ",
      3==3.0)
print(
      "are these equal ",
      3=='3')
print(
      "id the number odd ",
      8%2==0)
print(
      "are these numbers equal? ",
      0.0==0 and 1.0==1 )
print(
      "is any one true? ",
      0==2 or 1==1 )
# high precedence of AND
print(
      "evaluate the expression: ",
      True or True and False )

#Boolean conversion
print( bool(0) )
print( bool("") )
print( bool(1) )
print( bool(20) )
print( bool("asd") )

if 0:
    print(0)
elif "spam":
    print("spam")

# Ternary
def quiz_message(grade):
    outcome = 'failed' if grade < 50 else 'passed'
    print('You', outcome, 'the quiz with a grade of', grade)
    
quiz_message(45)


"""
==============================================
7. Lists
==============================================
"""


a = [
     'Mercury', 
     'Venus', 
     'Earth', 
     'Mars', 
     'Jupiter', 
     'Saturn', 
     'Uranus',
     'Neptune']

#indexing
a[0]
a[-1]

#slicing
a[:2]
a[2:]
a[:-3]
a[-3:]


#A list can contain a mix of different types of variables and comma at the end
import random
def random_function():
    return random.randint(1,10)

b = [
     1,
     random_function,
     ['Mercury', 98988.98], 
     ['Earth', 4564.98], 
     ['Uranus', 31434.98], 
     ['Neptune', 48914.98],
]

#Changing lists
a[3] = 'SpaceX'
a[:2] = ['Mer','Ven']


#List functions
len(a)
sorted(a)

nums = [5,6,7]
sum(nums)
min(nums)

#>>>>>>>> Interlude: objects
#objects have method and attributes

int_obj = 12
# its imaginary part is 0.
int_obj.imag
int_obj.bit_length()
int_obj.bit_length


#help from a object method (help recibes methods as paramaters)
help(max)
help(int_obj.bit_length)

#<<<<<<<< Interlude: objects

#add or remove item
a.append('Pluto')
a.pop()

#find an item
a.index('Uranus')

#find a missing item
a.index('Xray') #unpleasant surprise
'Xray' in a #return boolean

# TUPLES

# two declaration forms
t = (1,2,3)
t = 1,2,4
t

# tuples's items are inmutables
t[0] = 0

# Tuples are often used for functions that have multiple return values
d = 1.5
numerator, denominator = d.as_integer_ratio()
print(numerator)
print(denominator)

"""
==============================================
9. Loops
==============================================
"""

planets = [
     'Mercury', 
     'Venus', 
     'Earth', 
     'Mars', 
     'Jupiter', 
     'Saturn', 
     'Uranus',
     'Neptune']


# iterate over a list
for planet in planets:
    print(planet, end=' ')

# iterate over a tuple
ttt = (1,2,3,4)
multiply_value = 1
for t in ttt:
    multiply_value = t * multiply_value
print('multiply_value is ', multiply_value)

# iterate over s string
poetry = "steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video."

for c in poetry:
    if c.isupper():
        print(c, end = '')
        
# loop in a range
for r in range(5):
    print('number ... ', r)
    
# while
i = 0
while i<5 :
    print("numbers less than 5 ", i)
    i += 1
    
# List comprehensions

