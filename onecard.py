# -*- coding: utf-8 -*-
import random

class Card():
    def __init__(self, shape, num):
        self.shape = shape
        self.num = num

    def __str__(self):
        return '%-8s %2s' %(self.shape, self.num)

def check_can_drop(hand_):
    global pile
    for i in hand_:
        if i.shape == pile[len(pile)-1].shape or i.num == pile[len(pile)-1].num:
            return True
    return False

def refresh_deck():
    global deck
    global pile
    temp = pile[len(pile)-1]
    pile.pop()
    for i in range(len(pile)-1):
        deck.append(pile[i])
    random.shuffle(deck)
    pile.clear()
    pile.append(temp)
    print('Current top of Pile:')
    print(pile[len(pile)-1], '\n')

# Generating Deck
deck = []
shape_set = ['Spade', 'Heart', 'Diamond', 'Clover']
number_set = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

for i in shape_set:
    for j in number_set:
        card = Card(i, j)
        deck.append(card)

random.shuffle(deck)
random.shuffle(deck)

# Game Setting
player_hand = []
computer_hand = []
pile = []

top = 51        #top of deck
while len(player_hand) < 6 and len(computer_hand) < 6:
    player_hand.append(deck[top])
    del deck[top]
    top -= 1
    computer_hand.append(deck[top])
    del deck[top]
    top -= 1

pile.append(deck[top])
top -= 1

print('Current top of Pile:')
print(pile[len(pile)-1], '\n')

print('Now you have:')
print('Key  Card')
for i in range(len(player_hand)):
    print(i, '  ', player_hand[i])

print('\nInput a [Key] number corresponding the [Card] you want to drop.')
print('If you cannot drop any card, input any other character to get a card.')

while 1:
    # Player's phase
    # If player can drop a card
    print('\n...Your Turn...\n')
    if check_can_drop(player_hand) == True:
        drop_key = input()

        while drop_key.isdigit()  == False or int(drop_key) >= len(player_hand):
            print('You should input an INTEGER in range your index.')
            drop_key = input()

        drop_key = int(drop_key)
        drop_card = player_hand[drop_key]
        while drop_card.shape != pile[len(pile)-1].shape and drop_card.num != pile[len(pile)-1].num:
            print('Wrong input')
            drop_key = input()
            if drop_key.isdigit() == False:
                continue
            drop_key = int(drop_key)
            drop_card = player_hand[drop_key]

    # Add player's drop to the pile
        pile.append(drop_card)

    # Delete player's drop from player's hand
        del player_hand[drop_key]

    # If player can't drop a card
    else:
        print('You don\'t have a card to drop.')
        print('Print [Enter] key to get a card.')
        wait = input()
        if len(deck) == 0:
            refresh_deck()
            print('deck refreshed')
        else:
            player_hand.append(deck[top])
            top -= 1

    if len(player_hand) == 0:
        print('Player wins!')
        break
    else:
        print('\n...Your Turn End...\n')

    print('Current top of Pile:')
    print(pile[len(pile)-1], '\n')

    # Computer's phase: find cards computer can drop
    print('\n...Computer\'s Turn...\n')
    if check_can_drop(computer_hand) == True:
        k = len(computer_hand)
        cc = []
        for i in range(k):
            if computer_hand[i].shape == pile[len(pile)-1].shape or computer_hand[i].num == pile[len(pile)-1].num:
                cc.append(computer_hand[i])

    # Computer's phase: computer's dropping
        drop_card = random.choice(cc)

    # Add Computer's drop to the pile
        pile.append(drop_card)


    # Delete computer's drop from computer's hand
        computer_hand.remove(drop_card)

    # If computer can't drop a card
    else:
        print('Computer doesn\'t have a card to drop.')
        if len(deck) == 0:
            refresh_deck()
            print('deck refreshed')
        else:
            computer_hand.append(deck[top])
            top -= 1

    if len(computer_hand) == 0:
        print('Computer wins!')
        break
    else:
        print('\n...Computer\'s Turn End...\n')

    print('Current top of Pile:')
    print(pile[len(pile)-1], '\n')

    print('\nNow you have:')
    print('Key  Card')
    for i in range(len(player_hand)):
        print(i, '  ', player_hand[i])
