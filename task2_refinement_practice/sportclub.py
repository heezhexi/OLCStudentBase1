# num_members = 15
# for x in range(num_members):
#     sport = input("What is the member's preferred sport?")
#     if sport == ("done"):
#         break
        
# while loop validation
# num_members = 15
# for x in range(num_members):
# Task 5.1
while True:
    sport = input("What is the member's preferred sport?")
    if sport.lower() == ("done"):
        break

# Task 5.2
# [2 marks]
# Edit your program to convert each sport to lowercase and then store it into a list.
# Task 5.2



while True:
    sport = input("What is the member's preferred sport?").lower()
    
    if sport == "done":
        break  