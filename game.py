from sense_hat import SenseHat
from time import sleep
from electronicDie import RollDice
from datetime import datetime
import random
import csv

class Player():
    name = ''
    score = 0

class TwoPlayerGame():
    sense = SenseHat()
    player1_score = 0
    player2_score = 0
    rollDice = RollDice()
    game_goal = 8
    text_speed = 0.03
    playerTurn = 0
    p1 = Player()
    p2 = Player()

    def __init__(self, player1, player2):
        self.p1.name = player1
        self.p2.name = player2

    def player_turn(self):
        currPlayer = Player()
        if(self.playerTurn%2==0):
            currPlayer = self.p1
        else:
            currPlayer = self.p2

        self.sense.show_message(currPlayer.name + "_Shake", self.text_speed)
        score = self.rollDice.detect_shake()
        currPlayer.score+=score
        self.sense.show_message(str(currPlayer.score) + " pts", self.text_speed)
        print("Rolled:", score)
        print(self.p1.name, "has a score of", self.p1.score)
        print(self.p2.name, "has a score of", self.p2.score)
        print()

        self.playerTurn+=1

    def end_game(self):
        self.sense.show_message("Game_over:(", self.text_speed)
        winner = Player()
        now = datetime.now()
        winning_time = now.strftime("%H:%M:%S")
        if self.p1.score>self.p2.score:
            winner = self.p1
        else:
            winner = self.p2
        self.sense.show_message(winner.name + " won:)", self.text_speed)
        print("Game over - see winner.csv for results")

        with open('winner.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Winner: ", winner.name, "Score: ", winner.score, "Time: ",  winning_time, "Shakes: ", self.playerTurn])

def main():    
    diceGame = TwoPlayerGame("P1", "P2")
    diceGame.rollDice.sense.clear()
    
    diceGame.sense.show_message("2_plyrs_take_turns_to_shake_PI", diceGame.text_speed)
    diceGame.sense.show_message("1st_over_" + str(diceGame.game_goal) + "_pts_wins!", diceGame.text_speed)

    gameInPlay = True
    while gameInPlay:
        diceGame.player_turn()

        if diceGame.p1.score>diceGame.game_goal or diceGame.p2.score>diceGame.game_goal:
            diceGame.end_game()
            gameInPlay = False
        

if __name__ == '__main__':
    main()