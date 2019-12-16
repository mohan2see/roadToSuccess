
# {CHAPTER 5 : DICTIONARIES}#
# -------------------------
# dictionary is a collection of key-value pairs. defined in curly brackets.
print("WORKING WITH DICTIONARIES:")
print("--------------------------")
fighter = {'name': 'Nate Diaz', 'company': 'UFC', 'division': 'Welterweight'}
# access the value by key name. If key doesn't exist, it will throw an error.
print(fighter['division'])

# adding key-value pair to existing dictionary.
print('# # adding the key-value pair to# # ')
fighter['recent event'] = 'UFC 244'
fighter['status'] = 'Lost'
print(fighter['status'])

# dictionary retains the order it was added
for i in fighter:
    print(f'{i}={fighter[i]}')
print(f'\n')
# update the dictionary
print('# # updating the dictionary value# # ')
fighter['status'] = 'Lost via Doctor Stoppage'
for i in fighter:
    print(f'{i}={fighter[i]}')
print(f'\n')

# removing the dictionary key-value
print('# # removing the dictionary key-value# # ')
del fighter['recent event']
for i in fighter:
    print(f'{i}={fighter[i]}')

# Multi line definition
fighters = {'1': 'Nate diaz',
            '2': 'Nick Diaz',
            '3': 'Justin Gaethje'}

for i in fighters:
    print(i)
print(f'\n')

# get() to access values. to avoid throwing KeyError when key doesn't exist
# print(fighters['hello']) -- throws KeyError
print('# # # get() method to print default values if no key present# # # ')
print(fighters.get('hello', 'No key exists with value hello'))
print(f'\n')

# looping through dictionary
print('# # # Looping Through Dictionary# # # ')
user_profile = {'user_name': 'mohan2see', 'first_name': 'Mohanram', 'last_name': 'Krishnan'}
for key in user_profile:
    print(f'{key} - {user_profile[key]}')

# another way to loop through. probably the obvious way
for key, value in user_profile.items():
    print(f'\nKey : {key}\nValue : {value}')
print(f'\n')

# Looping the keys
for key in user_profile.keys():
    print(f'key : {key}')

# Looping through values
for value in user_profile.values():
    print(f"value : {value}")
