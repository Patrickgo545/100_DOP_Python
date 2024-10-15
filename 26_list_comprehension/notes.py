import random

# FOR LOOP
numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
    
    
# LIST COMPREHENSION
"""
list = [new_item for item in list]
list_conditional = [new_item for item in list if test]
"""

new_list_comprehension = [n + 1 for n in numbers]

name_list = "Angela"
name_capitol_list = [letter.upper() for letter in name_list]

range_list = range(1,5)
range_list_doubled = [number * 2 for number in range_list]
range_list_shortened = [n * 2 for n in range(1,5)]


# CONDITIONAL LIST COMPREHENSION
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
names_short = [name for name in names if len(name) < 5]

names_long_caps = [name.upper() for name in names if len(name) > 4]


# DICTIONARY COMPREHENSION

"""
new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for (key,value) in dict.items}
"""

student_score = {student:random.randint(0,100) for student in names}
passed_students = {student:score for (student, score) in student_score.items() if score >= 60}
print()