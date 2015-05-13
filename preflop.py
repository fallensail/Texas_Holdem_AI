#-------------------------------------------------------------------------------
# Name:        preflop.py
# Purpose:     Controls the game of the preflop stage. (only two hole cards are known)
#-------------------------------------------------------------------------------

import numpy as np
import pickle
import roundcontrol
import preflop_table
from preflop_table import card_prob
import math
import winningprob

# Player makes the bet action.
def preflopMakeAction(game, playerIndex, tableIndex = 1):
    '''
    game: an object of all imformation of the game
    playerIndex: indicate which player is making action
    tableIndex: indicate which table to use in preflop_table.py
    return: modified tableIndex.
    '''
    pi = card_prob(game.player(playerIndex).holdcards()[0], game.player(playerIndex).holdcards()[1], tableIndex)
    # if this player is computer, use our AI.
    if game.player(playerIndex).isComputer:
        if pi >= 0.5 and tableIndex != 4:
            betValue = math.ceil((pi + 0.5)*max(1, game.player(1-playerIndex).lastBet) * 2)
            betValue = min(betValue, game.player(playerIndex).moneyInHand)
            print "Computer", playerIndex, "Raise ", int(betValue)
            game.player(playerIndex).bet(betValue, "R", pi, game.currentmoneyinpot())
        else:
            callValue = abs(game.player(0).potMoney - game.player(1).potMoney)
            print "Computer", playerIndex, "Call ", callValue
            game.player(playerIndex).bet(callValue, "C", pi, game.currentmoneyinpot())
    # if this player is human, ask for input
    else:
        while True:
            action = raw_input("Enter your decision: input 'C' for Call or 'R' for Raise:\n")
            if tableIndex == 4:
                print "You can only Call now!"
            if action == "C" or tableIndex == 4:
                callValue = abs(game.player(0).potMoney - game.player(1).potMoney)
                game.player(playerIndex).bet(callValue, "C", pi, game.currentmoneyinpot())
                print
                break
            elif action == "R":
                print "Your total money: ", game.player(playerIndex).moneyInHand
                betValue = math.ceil(game.player(1-playerIndex).lastBet * 2)
                if betValue >= game.player(playerIndex).moneyInHand:
                    betAmount = game.player(playerIndex).moneyInHand
                else:
                    #print "Debug..........", game.player(1-playerIndex).lastBet, betValue
                    betAmount = raw_input("Enter the amount you want to raise:\n")
                    while int(betAmount) < betValue or int(betAmount) > game.player(playerIndex).moneyInHand:
                        print "Your min and max raise values are", int(betValue), int(game.player(playerIndex).moneyInHand)
                        betAmount = raw_input("Enter the amount you want to raise:\n")
                game.player(playerIndex).bet(int(betAmount), "R", pi, game.currentmoneyinpot())
                print
                if betAmount > 0.2 * min(game.player(0).moneyInHand, game.player(1).moneyInHand):
                    tableIndex = 3
                else:
                    tableIndex = max(2, tableIndex)
                break
            else:
                print "Wrong input entered"
    return tableIndex


# Handle the preflop flow
def preflop(game, alterDealer):
    '''
    game: an object of all imformation of the game
    alterDealer: the dealer of this stage
    '''
    # computer == player1
    # user == player0

    # print out human player's hole cards
    for i in xrange(game.numPlayer):
        if not game.player(i).isComputer:
            print "Your Cards: ", game.player(i).holdcards()
            print

    #print "Computer Cards: ", game.player(1).holdcards()

    # start with computer small and move first
    game.player(alterDealer).bet(2, "")
    game.player(1 - alterDealer).bet(1, "")

    game.increStageIndex()
    for i in xrange(game.numPlayer):
        if game.player(i).isComputer:
            print "Computer's money:", game.player(i).moneyInHand
        else:
            print "Your money:", game.player(i).moneyInHand
            print "Your Cards: ", game.player(i).holdcards()

    print "Total money on pot:", game.currentmoneyinpot()

    tableIndex = 1
    tableIndex = preflopMakeAction(game, 1 - alterDealer, tableIndex)
    tableIndex = preflopMakeAction(game, alterDealer, tableIndex)

    # All players make actions alternatively
    while game.player(0).potMoney != game.player(1).potMoney and game.player(0).moneyInHand != 0 and game.player(1).moneyInHand != 0:
        tableIndex = preflopMakeAction(game, 1 - alterDealer, tableIndex)
        if game.player(0).potMoney == game.player(1).potMoney or game.player(0).moneyInHand == 0 or game.player(1).moneyInHand == 0:
            break
        tableIndex = preflopMakeAction(game, alterDealer, tableIndex)

    # If one of the players has no money in hand, only the other player can take one more action.
    if game.player(0).moneyInHand == 0 and game.player(1).moneyInHand != 0:
        tableIndex = preflopMakeAction(game, 1, tableIndex + 1)
    elif game.player(1).moneyInHand == 0 and game.player(0).moneyInHand != 0:
        tableIndex = preflopMakeAction(game, 0, tableIndex + 1)

    for i in xrange(game.numPlayer):
        if game.player(i).isComputer:
            print "Computer's money:", game.player(i).moneyInHand
            print
        else:
            print "Your money:", game.player(i).moneyInHand
            print "Your Cards: ", game.player(i).holdcards()
            print

    print "Total money on pot:", game.currentmoneyinpot()

    winIndex = -1
    # Advance to the end of game when one of the players has no money in hand
    if game.player(0).moneyInHand == 0 or game.player(1).moneyInHand == 0:

        hand0 = game.player(0).holdcards() + game.publicCards
        hand1 = game.player(1).holdcards() + game.publicCards
        best0, strength0 = winningprob.bestfive(hand0)
        best1, strength1 = winningprob.bestfive(hand1)

        print "Your Best Five:", best0, "Original Cards in hand:", game.player(0).holdcards()
        print "Computer's Best Five:", best1, "Original Cards in hand:", game.player(1).holdcards()

        if hand0 == hand1:
            winIndex = -1
            print "Tie!!\n"
        elif hand0 > hand1:
            winIndex = 0
            print "You win!\n"
        else:
            winIndex = 1
            print "Computer wins!\n"
        return False, 1-winIndex
    return True, -1



