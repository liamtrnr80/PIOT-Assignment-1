from sense_hat import SenseHat
from time import sleep
from electronicDie import RollDice
from datetime import datetime
import random
import csv

class TwoPlayerGame():
    player1_score = 0
    player2_score = 0

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2



def main():
    sense = SenseHat()
    rollDice = RollDice()
    diceGame = TwoPlayerGame("P1", "P2")
    rollDice.sense.clear()
    playerTurn = 0
    gameInPlay = True
    game_goal = 30
    text_speed = 0.03
    sense.show_message("2_plyrs_take_turns_to_shake_PI", text_speed)
    sense.show_message("1st_over_" + str(game_goal) + "_pts_wins!", text_speed)


    while gameInPlay:

        if(playerTurn%2==0):
            sense.show_message("P1_Shake", text_speed)
            score = rollDice.detect_shake()
            diceGame.player1_score+=score
            sense.show_message(str(diceGame.player1_score) + " pts", text_speed)
            print("Rolled:", score)
            print(diceGame.player1, "has a score of", diceGame.player1_score)
            print(diceGame.player2, "has a score of", diceGame.player2_score)
            print()
        else:
            sense.show_message("P2_Shake", text_speed)
            score = rollDice.detect_shake()
            diceGame.player2_score+=score
            sense.show_message(str(diceGame.player2_score) + " pts", text_speed)
            print("Rolled:", score)
            print(diceGame.player1, "has a score of", diceGame.player1_score)
            print(diceGame.player2, "has a score of", diceGame.player2_score)
            print()

        playerTurn+=1

        if diceGame.player1_score>game_goal or diceGame.player2_score>game_goal:
            sense.show_message("Game_over:(", text_speed)
            winner = ""
            score = 0
            now = datetime.now()
            winning_time = now.strftime("%H:%M:%S")
            if diceGame.player1_score>diceGame.player2_score:
                winner = "P1" 
                score = diceGame.player1_score
            else:
                winner = "P2"
                score = diceGame.player2_score
            sense.show_message(winner + " won:)", text_speed)
            print("Game took", playerTurn, "shakes")

            with open('winner.csv', 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Winner: ", winner, "Score: ", score, "Time: ",  winning_time, "Shakes: ", playerTurn])
            gameInPlay = False
        

if __name__ == '__main__':
    main()