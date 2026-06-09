# A school has a new computer network. 
# The following program allows students to create 
# a username and password to log onto the network.

list_username = ["StudentNo1", "JaneJones", "ABC123"]
username = input("Please enter a username: ")
password = input("Please enter a password: ")

# Task 1.1
# Edit the program so that it checks to see 
# if the username entered exists in the list.
# If it does not exist in the list, it must store the username in the list.
# If it does exist in the list, the program must loop 
# until a username is entered that does not already exist in the list.
# [4]
# 3 marks
while True:
    list_username = ["StudentNo1", "JaneJones", "ABC123"] # should not be in while loop
    username = input("Please enter a username: ")
    if username in list_username:
        input("Please enter a username: ")
    else:
        list_username.append(username)
        # print(list_username)
        break

# Edit your program so that it checks if the password:
# ·        contains at least one numerical character
# ·        contains at least one special character from: @ ! / ?
# ·        is at least 8 characters in length

# The program should loop until the password 
# fulfils all the three requirements.

# Use suitable input and output messages.
# [6]

# 0.5
if len(password) < 8:
    print("Password must be at least 8 characters: ")
elif password != 1,2,3,4,5,6,7,8,9