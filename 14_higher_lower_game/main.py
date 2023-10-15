'''
Flowchart
1. Import random module 
2. Function - Pull dictionary from json file
    -Pull a specific dictionary
3. Function - Pull 2 Dictionaries to go up against each other
    -Check if user got the question right & return Boolean
4. Add to score & loop vs function
5. IF Incorrect, end program
'''

# Import Modules
import random 
import art
from replit import clear
from game_data import data

player_lost = False
player_score = 0

# Pull JSON from game_data
def pull_data():
  '''[subject , follow count , description , country]'''
  dictionary = {}
  list = []
  dictionary.update(data[random.randint(0,49)])
  for values in dictionary:
    list.append(dictionary[values])
  return list

# GAME CODE
def higher_lower(last_answer):
  '''Account a VS Account b - Return b'''
  global player_lost
  global player_score

  list_a = last_answer
  list_b = pull_data()

  if list_a == "":
    list_a = pull_data()

  follow_count_a = list_a[1]
  follow_count_b = list_b[1]
  correct_answer = ""

  if follow_count_a > follow_count_b:
    correct_answer = "a"
  else: correct_answer = "b"

  print(art.logo)

  if player_score > 0: 
    print(f'Correct! Current Score {player_score}.')
    
  print(f"Compare A: {list_a[0]}, a {list_a[2]}, from {list_a[3]}. {list_a[1]}")
  print(art.vs)
  print(f"Against B: {list_b[0]}, a {list_b[2]}, from {list_b[3]}. {list_b[1]}")

  player_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  if player_answer == correct_answer:
    clear()
    player_score += 1
    higher_lower(list_b)
    
  else: 
    clear()
    print(art.logo)
    print(f'Incorrect, you lose. Final Score {player_score}.')
    player_lost = True
  
higher_lower("")