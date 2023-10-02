############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start_game = False



def start_trigger():
  global start_game
  start_trigger = input('Do you want to play a game of Blackjack? Type "y" or "n": ')
  if start_trigger == 'y':
    start_game = True



def deal_card(deck):
  '''Deal the first 2 cards to dealer & player'''
  card_one = random.randint(0,12)
  deck.append(cards[card_one])
  



def hit(deck):
  '''Stack takes a hit'''
  randomizer = random.randint(0,12)
  deck.append(cards[randomizer])



def player_choice():
  global player_hand
  global player_score 
  global gambling_phase
  choice = input('Type "y" to get another card, type "n" to pass: ')

  if choice == 'y':
    hit(player_hand)
    display_score()


def bust_check_player(score):
  '''Check if bust'''
  global player_busted
  global gambling_phase  

  if score > 21:
    gambling_phase = False
    player_busted = True


    
def ace_check_player(deck):
  ace_in_deck = False
  for cards in deck: 
    if cards == 11:
      ace_in_deck = True

  if ace_in_deck == True:
    return True


def ace_replace_player():
  global player_hand

  ace_position = player_hand.index(11)
  player_hand[ace_position] = 1


def display_score():
  global player_score
  global player_hand
  player_score = sum(player_hand)
  print(f'Your cards: {player_hand}, current score: {player_score}')
  print(f'Computer\'s first card: {dealer_hand[0]}')


    
def game_over():
  '''End Game Triggered'''
  global dealer_score
  global start_game
  dealer_score = sum(dealer_hand)
  print('\n')

  if player_busted == True:
    print(f'Your final hand {player_hand}, final score {player_score}')
    print(f'Computer\'s final hand {dealer_hand}, final score {dealer_score}')
    print('You went over. You lose')
    
  while dealer_score < 17:
    hit(dealer_hand)
    dealer_score = sum(dealer_hand)

  if player_busted == True: 
    print()
    
  elif dealer_score > 21: 
    print('Dealer Busted, You Win!')

  elif dealer_score == player_score:
    print('Draw')

  elif dealer_score > player_score:
    print('You Lose.')

  if player_busted == False:
    print(f'Your hand {player_hand}, final score: {player_score}')
    print(f'Dealer hand {dealer_hand}, final score {dealer_score}')

  start_game = False


def check_score(deck):
  if sum(deck) == 21 and len(deck) == 2:
    return 0 

  if 11 in deck and sum(deck) > 21:
    deck.remove(11)
    deck.append(1)


  return sum(deck)

    
start_trigger()
  
while start_game:
  player_hand = []
  player_score = 0
  player_busted = False
  player_ace_in_deck = False
  
  dealer_hand = []
  dealer_score = 0
  dealer_busted = False
  dealer_ace_in_deck = False

  # DEAL STARTING CARDS
  for _ in range(2):
    deal_card(player_hand)

  for _ in range(2):
    deal_card(dealer_hand)

  display_score()
  
  gambling_phase = True
  while gambling_phase:
    player_choice()
    bust_check_player(player_score)
    player_ace_in_deck = ace_check_player(player_hand)
    if player_ace_in_deck == True:
      gambling_phase = True 
      ace_replace_player()
      print(player_hand)
      bust_check_player(player_score)

  game_over()
  start_trigger()