from sense_hat import SenseHat
from time import sleep
from electronicDie import RollDice
from datetime import datetime
import random
import csv

class TwoPlayerGame():
    player1_score = 0
    player2_score = 0
    rollDice = RollDice()
    sense = SenseHat()
    text_speed = 0.0003
    playerTurn = 0

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def end_game(self):
        self.sense.show_message("Game_over:(", self.text_speed)
        winner = ""
        score = 0
        now = datetime.now()
        winning_time = now.strftime("%H:%M:%S")
        if self.player1_score>self.player2_score:
            winner = "P1" 
            score = self.player1_score
        else:
            winner = "P2"
            score = self.player2_score
        self.sense.show_message(winner + "_won:)", self.text_speed)
        print("Game took", self.playerTurn, "shakes")

        with open('winner.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Winner: ", winner, "Score: ", score, "Time: ",  winning_time])



def main():
    diceGame = TwoPlayerGame("P1", "P2")
    diceGame.rollDice.sense.clear()
    gameInPlay = True
    game_goal = 2
    diceGame.sense.show_message("2_plyrs_take_turns_to_shake_PI", diceGame.text_speed)
    diceGame.sense.show_message("1st_to_over" + str(game_goal) + "_wins!", diceGame.text_speed)


    while gameInPlay:
        if(diceGame.playerTurn%2==0):
            diceGame.sense.show_message("P1_Shake", diceGame.text_speed)
            score = diceGame.rollDice.detect_shake()
            diceGame.player1_score+=score
            diceGame.sense.show_message(str(diceGame.player1_score) + "_pts", diceGame.text_speed)
            print("Rolled:", score)
            print(diceGame.player1, "has a score of", diceGame.player1_score)
            print(diceGame.player2, "has a score of", diceGame.player2_score)
            print()
        else:
            diceGame.sense.show_message("P2_Shake", diceGame.text_speed)
            score = diceGame.rollDice.detect_shake()
            diceGame.player2_score+=score
            diceGame.sense.show_message(str(diceGame.player2_score) + "_pts", diceGame.text_speed)
            print("Rolled:", score)
            print(diceGame.player1, "has a score of", diceGame.player1_score)
            print(diceGame.player2, "has a score of", diceGame.player2_score)
            print()

        diceGame.playerTurn+=1

        if diceGame.player1_score>game_goal or diceGame.player2_score>game_goal:
            diceGame.end_game()
            gameInPlay = False
        

if __name__ == '__main__':
    main()