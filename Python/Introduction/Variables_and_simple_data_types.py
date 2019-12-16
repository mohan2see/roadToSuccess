#  {CHAPTER 2 : VARIABLES AND SIMPLE DATA TYPES}
#  ---------------------------------------------
print("WORKING WITH VARIABLES AND SIMPLE DATA TYPES:")
print("---------------------------------------------")
#  Working with Strings
name = "MOHAN Ram"
#  Camel case
print(name.title())
# Upper and Lower Case
print(name.upper())
print(name.lower())

# fstring introduced in v3.6
message = f"Welcome, {name.title()}!"
print(message)
# for older python versions
message = "Welcome, {0}!".format(name.title())
print(message)

# new line and tab
print("Hello\nWorld!")
print("Fruits:\n\t1.Apple\n\t2.Orange\n\t3.Grapes")

# whitespace strip
message = " Hitman "
print(message.rstrip())
print(message)  # message variable still has the space.
print(message.lstrip())
print(message.strip())

# Working With Numbers
print(0.2 + 0.1)
print(3.0 * 2)
print(3.0 ** 2)
print(4 % 3)  # returns the remainder

# long Numbers
# Note: Underscore is omitted when printing the numbers
long_num = 6_000_000_000
print(long_num)

# Multiple Assignments
# Note: Number of variables and values should match
a, b, c = 10, 20, 30
print(a, b, c)

# Constants
# Note: Define in Capital letters. There is no inbuilt Constant type in Python
MAX_CONNECTION = 10
print(f'\n\n\n')

