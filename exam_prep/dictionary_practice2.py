################ SET 1: Country and Capital ################

################ Define a dictionary ###############
# Define a dictionary named countries which will store a country and its capital city.

# 'Singapore' has capital 'Singapore'
# 'Malaysia' has capital 'Kuala Lumpur'
# 'Thailand' has capital 'Bangkok'
# 'Japan' has capital 'Tokyo'
countries = {'Singapore' : 'Singapore',
             'Malaysia' : 'KL',
             'Thailand' : 'Bangkok',
             'Japan' : 'Tokyo' 

}







################ Retrieve values from a dictionary ###############
# Print out the capital city of Malaysia only.
# Print out the capital city of Japan only.
print(f"{countries['Malaysia']}")
print(f"{countries['Japan']}")

########### Change the value of a dictionary key ###############
# Change the capital city of Thailand to 'Phuket'.
# Change the capital city of Singapore to 'Toa Payoh'.
countries['Thailand'] = 'Phuket'
countries['Singapore'] = 'Toa payoh'
print(countries)



############ Add a new key / value to the dictionary #####################
# Add a new country => Indonesia with capital Jakarta.
# Add a new country => South Korea with capital Seoul.
countries['Indonesia'] = 'Jakarta'
countries['South Korea'] = 'Seoul'
print(countries)



############ Delete a key / value from the dictionary #####################
# Delete the country Singapore from the dictionary.
del countries['Singapore']
print(countries)



########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of each country.
# Only display the keys.

for country in countries:
    print(country)


########### Loop through to Retrieve Values ##################
# Write a for loop, and only print out the capital cities.

print(countries['Malaysia']) # KL

for country in countries:
    print(country)
    print(countries[country])


########### Loop through to Retrieve Key and Values ##################
# Write a for loop, and print out the country and its capital city.

# Example:
# Malaysia has capital city Kuala Lumpur
# Japan has capital city Tokyo

for country in countries:
    print(f"{country} has a capital city {countries[country]}")


################ SET 2: Student and Marks ################

################ Define a dictionary ###############
# Define a dictionary named marks which will store a student name and the marks they scored.

# 'Alice' scored 78
# 'Ben' scored 64
# 'Chloe' scored 89
# 'Daniel' scored 55


# write and test your code here
names = {'Alice' : 78,
 'Ben' : 64,
 'Chloe' : 89,
 'Daniel' : 55

}

################ Retrieve values from a dictionary ###############
# Print out the marks scored by Alice only.
# Print out the marks scored by Daniel only.
print(f"{names['Alice']}")
print(f"{names['Daniel']}")
########### Change the value of a dictionary key ###############
# Change Ben's marks to 70.
# Change Daniel's marks to 60.

names['Ben'] = 70
names['Daniel'] = 60
print(names)


############ Increase the value of a dictionary key ############
# Increase Chloe's marks by 5.
# Decrease Alice's marks by 3.

names['Chloe'] = names['Chloe'] + 5
names['Alice'] = names['Alice'] - 3
print(names)


############ Add a new key / value to the dictionary #####################
# Add a new student => Ethan who scored 82.
# Add a new student => Fiona who scored 91.

names['Ethan'] = 82
names['Fiona'] = 91
print(names)

############ Delete a key / value from the dictionary #####################
# Delete Daniel from the dictionary.

del names['Daniel']
print(names)


########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of each student.
# Only display the keys.

for name in names:
    print(name)



########### Loop through to Retrieve Values ##################
# Write a for loop, and only print out the marks.

for name in names:
    print(names[name])


########### Loop through to Retrieve Key and Values ##################
# Write a for loop, and print out the student name and marks.

# Example:
# Alice scored 78 marks
# Ben scored 64 marks

# write and test your code here

################ SET 3: Game Item and Quantity ################

################ Define a dictionary ###############
# Define a dictionary named inventory which will store a game item 
# and the quantity owned by the player.

# 'potion' quantity is 5
# 'sword' quantity is 1
# 'shield' quantity is 1
# 'arrow' quantity is 20
inventory = {
    'potion' : 5,
 'sword' : 1,
 'shield' : 1,
 'arrow' : 20
}


################ Retrieve values from a dictionary ###############
# Print out the quantity of potion only.
# Print out the quantity of arrow only.
print(inventory['arrow'])
print(inventory['potion'])

########### Change the value of a dictionary key ###############
# Change the quantity of sword to 2.
# Change the quantity of shield to 3.
inventory['sword'] = 2
inventory['shield'] = 3
print(inventory)


############ Increase the value of a dictionary key ############
# Increase the quantity of potion by 10.
# Decrease the quantity of arrow by 5.

inventory['potion'] = inventory['potion'] + 10
inventory['arrow'] = inventory['arrow'] + 5
print(inventory)

############ Add a new key / value to the dictionary #####################
# Add a new item => bow with quantity 1.
# Add a new item => apple with quantity 8.

inventory['bow'] = 1
inventory['apple'] = 8
print(inventory)

############ Delete a key / value from the dictionary #####################
# Delete apple from the dictionary.

del inventory['apple']
print(inventory)


########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of each item.

# Only display the keys.

for items in inventory:
    print(items)

########### Loop through to Retrieve Values ##################
# Write a for loop, and only print out the quantities.
# '''

# # write and test your code here
for items in inventory:
    print(inventory[items])

########### Loop through to Retrieve Key and Values ##################
# Write a for loop, and print out the item and quantity.

# Example:
# potion quantity: 5
# arrow quantity: 20
for items in inventory:
    # print([items] ,":", inventory[items])
    print(f"{items} : {inventory[items]}")

# write and test your code here