# {CHAPTER 5 : User Inputs and while loops}#
# -------------------------
# input method accepts all inputs as strings
import sys

message = input("What's your name?\n")
print(f"Hello {message}!!")

# for numeric inputs use int()
age  = input("how old are you? \n")
age = int(age)
print(f"your age is {age}")

if (age > 18):
    print("eligible to vote.")
else:
    print("not eligible to vote")



# WHILE Loops
year = 2019

while year < 2021:
    print(f"year is {year}")
    year += 1

# user input on while
attempts = 0
while attempts < 3 :
    password = input("enter the password \n")
    if password == "12345":
        print("correct password")
        break  # to exit a while loop immediately
    else:
        print("invalid password")
        attempts += 1

# 'continue' to return to the beginning loop
isActive = False
age = int(input('your age ? \n'))
while age < 20:
    continue
print(f"age is {age}")


# while loop with lists and dictionaries
print("\n\n\n#WHILE LOOP WITH LISTS#")
unconfirmed_users = ['brandon', 'macy', 'george']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"verifying user : {current_user.title()}")
    confirmed_users.append(current_user)
    confirmed_users.reverse() # bringing back the original order
print("confirmed users are:")
for user in confirmed_users:
    print(user)
print("\n")


# remove() in while to remove all instances
pets = ['dogs', 'cats', 'monkeys', 'cows', 'dogs']
# remove() only removes one instance. Use while loop to remove all instances.

while 'dogs' in pets:
    pets.remove('dogs')
print(f"all instance of dogs are removed\nremaining pets are {pets}")




