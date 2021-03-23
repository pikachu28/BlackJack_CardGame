#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 09:36:14 2020

@author: anjalisingh
"""

# Blackjack itself is quite a simple card game : the aim is for players to get a high
# score or higher total than dealer without going above the score of 21 now if the total
# value of the cards in a hand comes to more than 21 then the player said to have
# bust or have busted and that is GAME OVER 
# Their is variations on the way the game is played so our version as is gonna be
# simple version and will have the following conditions:
#     The dealer deals one card to each player then to himself 
#     Then player gets another card to decide whether to stick with a total they have 
#     or hit (to get another card) , player can hit as many as times as they like 
#     but soon as their total goes above 21 they are busted and when all the players
#     have stuck or bust either of the 2 things dealer gets a second card and the dealer
#     decides whether to stick or hit ( same as the player ) and then dealer has over
#     21 they bust then all players that haven't bust effectively win 
#     their is another constraint to the dealer though the dealer cannot stick on less
#     than 17. So, if they have 17 or more once the dealer has finished any player
#     whose total is more than dealer wins and any player with a smaller total losses
#     so, if dealer and the player have the same score then they draw ,so to keep it 
#     simple we are gonna play with single player
#     CARDS:
#         13 cards in each of 4 suits and that makes a total of 52 cards in the pack
#         first 10 cards are 1 to 10 and then there are 3 face cards-> jack, king, queen
#         face card also having a value of 10 in this game
#         Hearts, spade, clubs, diamonds
#     To make things interesting the ace card with the value 1 can also have value
#     11 then the player can decide which of the 2 values it should take so they get the
#     best total in their hand now.


# NEW GAME
# function called new_game now the thing to remember here is the most of the initialization code in
# the main program concern setting up the GUI and so consequently we don't need to
# repeat all of that every time a new game started but the deal_card_frame
# and player_card_frame will need to be cleared so
# calling the destroy method will do that and once that is done the list holding
# the hands rather will need to be cleared and the first 3 cards dealt and we can also make


import tkinter
import random
# http://svg-cards.sourceforge.net/
# if u are running 8.6 version then u can use PNG Images otherwise use PPM
print(tkinter.TkVersion)

try:
    import tkinter
    
except:          # python 2
    import Tkinter as tkinter


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']
    
    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'
    
    # for each suit, retrieve the image for the cards
    for suit in suits:
        # first number cards 1 to 10
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))
        
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    # pop the next card off the top of the deck 
    next_card = deck.pop(0)
    #  and add it to back of the pack
    deck.append(next_card)
    # add the image to a Label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the card's face value
    return next_card


def score_hand(hand):
    # Calculate the total score of all cards in the list.
    # Only one ace can have the value 11, and this will be reduce to 1 if the hand would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        # ace was drawn for the first time
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and substract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score




def deal_dealer():
    # deal_card(dealer_card_frame)
    # dealer_hand.append(deal_card(dealer_card_frame))
    # dealer_score = score_hand(dealer_hand)
    # dealer_score_label.set(dealer_score)
    dealer_score = score_hand(dealer_hand)
    while 0<dealer_score<17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    
    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")    
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw!")

    
    
def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!!")
    # by default ace has got a value 1 and what we're saying here is if an ace
    # was drawn from the card from the deck and the player hasn't
    # already got an ace in their hand then we are going to assign 11 to this particular card
    
    # player_score = 0
    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if we would bust, check if there is an ace and substract 10
    # if player_score >21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins!")
    # print(locals())
        
            
        
# Set up the screen and frames for the dealer and player

def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    # embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    # embedded frame to hold the card images
   # player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)
    
    result_text.set("")
    dealer_hand = []
    player_hand = []
    
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()

# def shuffle():
#     random.shuffle(deck)
    

mainWindow = tkinter.Tk()
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background="green")


result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")  
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg='white').grid(row=1, column=0)
# embedded frame hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
# player_score = 0
# player_ace = False

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)
# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

# a funciton associated with the widget using command property
dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2)

# shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
# shuffle_button.grid(row=0, column=3)



# load cards
cards = []
load_images(cards)
print(cards)
# create a new deck of cards and shuffle them
deck = list(cards)
# shuffle()
random.shuffle(deck)

# create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

# deal_player()
# dealer_hand.append(deal_card(dealer_card_frame))
# dealer_score_label.set(score_hand(dealer_hand))
# deal_player()

new_game()

mainWindow.mainloop()








