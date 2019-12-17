# reading a file. 'with' statement will automatically close the file when the file is no longer needed.
with open('sample_data.txt') as file:
    content = file.read()
    print(content)  # notice the output has empty line
    print(content.rstrip())

# file path
with open('file_folder/another_sample_file.txt') as another_file:
    content = another_file.read()
    print(content)

# reading a file line by line
with open('sample_data.txt') as file:
    for i in file:
        print(i.rstrip()) # strips the empty line between each line printed by python

# store the file in a list. readlines() reads the file and store each line as a list
with open('sample_data.txt') as list_file:
    lines = list_file.readlines() # lines is a list now

print(lines) # lines is a list
for i in lines:
    print(i.rstrip())


""" writing to a file. By default open() method opens the file in read mode. You can also use write(w), append(a),
read and write(r+) mode """

with open('sample_data.txt', mode='w') as file:
    file.write("writing a line from python code\n")  # this overwrites the file


# to append instead of overwriting
with open('sample_data.txt',mode='a') as append_file:
    append_file.write("appending a line from python code\n")





