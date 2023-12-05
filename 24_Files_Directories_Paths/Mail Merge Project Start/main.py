#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# STARTING LETTER 
with open("./Input/Letters/starting_letter.txt") as letter:
    starting_letter = letter.read()

print(starting_letter)

# LIST OF NAMES
with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

print(names_list)

# REMOVE \N
names_list_filtered = []
for name in names_list:
    names_list_filtered.append(name.strip("\n"))

print(names_list_filtered)

for names in names_list_filtered:
    # REPLACE NAME PLACEHOLDER
    new_letter = starting_letter.replace("[name]", names)
    
    # CREATE NEW LETTER
    with open(f"./Output/ReadyToSend/{names}.txt", "w") as file:
        file.write(new_letter)


