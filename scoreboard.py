from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.color("blue")
        self.penup()
        self.goto(0, 279)
        self.write(f"Score :0" ,align="center", font=("Arial", 15, 'normal'))

    def refresh_scoreboard(self):
        """Increases score"""
        self.score +=1
        self.clear()
        self.write(f"Score :{self.score}" ,align="center", font=("Arial", 15, 'italic'))

    def print_game_over(self):
        """Displays  Game Over and score """
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over! Your score is:{self.score}",align="center", font=("Arial", 15, 'italic'))

    