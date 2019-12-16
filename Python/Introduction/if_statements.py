
# {CHAPTER 4 : IF STATEMENTS}#
# ------------------
# to test a a condition.
print("WORKING WITH IF STATEMENTS:")
print("--------------------------")
cars = ['bmw', 'audi', 'volkswagen', 'benz', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
car = 'bmw'

# CONDITIONAL TESTS.
print(car == 'bmw')
# values are case sensitive
print(car == 'Bmw')

# checking for inequality
fruit = 'apple'
print(fruit != 'orange')  # returns True

# numerical comparisons
age = 21
print(age > 20)  # returns True
print(age == 21)  # returns True

# multiple conditions
print(20 < age < 25)  # returns True
print(21 < age < 22)  # returns False
# OR condition
print(age > 21 or age < 24)  # returns True

# Checking Whether a Value Is in a List
veg = ['carrot', 'tomato', 'potato', 'beetroot', 'eggplant']
if 'carrot' in veg:
    print('found the veggy!!')

# Checking Whether a Value Is NOT in a List
if 'onion' not in veg:
    print(f'unable to found onion')

# Boolean expression
citizen = True
Immigrant = False

if citizen:
    print('you\'re a citizen')  # notice that you can escape the single quote using backslash

# if-elif-else.
age = 40

if age < 18:
    print('you\'re a teenager')
elif 18 < age < 60:
    print('you\'re an adult')
else:  # else block is optional
    print('you\'re a senior')

# optional else block. Notice no else block here. Else is only for default execution if other conditon fails.
if age < 18:
    print('you\'re age is less than 18')
elif 18 < age < 30:
    print('you\'re between 18 and 30')
elif age > 30:
    print('you\'re over 30')

# checking for empty list
empty_list = []
if empty_list:
    print('list is not empty.')
else:
    print('add some items to the list.')

print(f'\n\n\n')
