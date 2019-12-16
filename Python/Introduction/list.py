
# {CHAPTER 3 : LIST}#
# ------------------
# Introduction to list
# Note: Lists are ordered collections. List name is preffered to be in plural. A list can contain alphabets, Numbers,
# etc.,
print("WORKING WITH LISTS:")
print("-------------------")
fruits = ['Apple', 'Orange', 'Grapes']
print(fruits)

# access element through index. Starts at 0
print(fruits[0])

# using String methods
print(fruits[0].upper())

# accessing last elements
print(fruits[-1], fruits[-2])

# list in f Strings
message = f"I have 12 {fruits[0]}"
print(message)

# changing, adding, removing elements from List
# changing
fruits[0] = 'BlueBerry'
print(fruits)

# adding. append will add the element in last position
fruits.append("Watermelon")
print(fruits)

# insert element at desired position
fruits.insert(0, 'Raspberry')
print(fruits)

# removing elements
# Note: use del to remove the element from a particular position
del fruits[0]
print(fruits)

# Note : To work with removed elements use pop. pop removes the element from list permanently
popped_fruits = fruits.pop()
print(fruits)
print(f"the last removed fruit was {popped_fruits}")

# pop to remove an element from a position
pop_second_fruit = fruits.pop(1)
print(f"the second fruit : {pop_second_fruit} is removed.")

# Removing an Item by Value. deletes only the first occurance.
fruits.remove('Grapes')
print(fruits)

# SORTING
# Note: Sort method permanently changes the order. can't reverse to original order
mobiles = ['Nokia', 'Huawei', 'Apple', 'OnePlus']
mobiles.sort()
print(mobiles)

# sorting in reverse alphabetical order
mobiles.sort(reverse=True)
print(mobiles)

# use sorted to sort the list temporarily.
watches = ['Timex', 'Casio', 'Rolex']
print(sorted(watches))
print(sorted(watches, reverse=True))
# original order of the watches list is still intact
print(watches)

# reverse the order without sort. Reverse is permanent. Apply reverse again to restore to original order. Voila!!
languages = ['Tamil', 'English', 'Hindi', 'Spanish']
languages.reverse()
print(languages)

# length of the list
games = ['Hitman', 'Farcry', 'Wolfenstein']
print(len(games))

#  To Avoid index error access the last element by list[-1]
print(games[-1])

# Looping Through Loops
# For loops. Indentation is critical
magicians = ['Alex', 'Jordan', 'Matthew']
for magician in magicians:
    print(f"Your magician name is {magician.upper()}\n")

# Generate Numeric values
for value in range(1, 5):
    print(value)

# list of numbers
numbers = list(range(1, 5))
print(numbers)

# skip Numbers. skips the numbers based on third argument. here skips 2 numbers each time till it reaches the end value.
numbers = list(range(1, 100, 2))
print(numbers)

# mixing up for loop with range
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(f"the squares of given range is {squares}")

# working with number Lists
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# LIST COMPREHENSION def:  A list comprehension combines the for loop and the creation of new elements into one line,
# and automatically appends each new element.
squares = [value ** 3 for value in range(1, 11)]
print(squares)

# Working with part of the list.
# Slicing
grounds = ["Lord's", "Chepauk", "Melbourne", "Oval"]
# prints index 0 till 2
for i in grounds[0:3]:
    print(f'Your ground is {i}')
print(f'\n')
# if first index is not specified, it will process from 0
for i in grounds[:4]:
    print(i)
print(f'\n')
# Slicing till last element
for i in grounds[1:]:
    print(i)
print(f'\n')
# slicing from last element
for i in grounds[-1:]:
    print(i)

# copying a list
my_foods = ['rasam', 'sambar', 'payasam', 'panner masala']
# copying through slice creates a different list. any change on the list wont affect the other list
friends_foods = my_foods[:]
print(my_foods)
print(friends_foods)
# adding a food to my friends_foods to see if it affects my_foods
friends_foods.append('vadai')
# my list is not affected.
print(my_foods)
print(friends_foods)

# copying without slice. both lists refers to the same values.
friends_foods = my_foods
my_foods.append("appalam")
print(my_foods)
print(friends_foods)

# TUPLES
# An immutable list is called tuple. uses paranthesis instead of square bracket as in list.
names = ('mohan', 'ram')
print(names)

# below will throw an error, since tuples are immutable.
# names[0] = 'murali'

# tuple supports re-assigning a variable with new values altogther
names = ('mohan', 'raj')
print(f'modified names : {names}')
print(f'\n\n\n')
