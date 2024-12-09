from turtle import Turtle


# keeps track of score and displays it on screen
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.SCORE = 0
        with open("data.txt", mode="r+") as file_handle_data:
            self.high_score = int(file_handle_data.read())

    # creates scoreboard, colors, positions, and displays it
    def create_score(self):
        self.penup()
        self.hideturtle()
        self.color("green")
        self.goto(0.0, 360)
        self.write(f"SCORE : {self.SCORE} HIGH SCORE: {self.high_score}", move=False, align="center", font=("Arial", 25, "bold"))

    # clears current score, adds +1 & recreates scoreboard & displays it
    def refresh_score(self):
        self.clear()
        self.SCORE += 1
        self.create_score()

    # resets highest score if the current score is higher than "highest score"
    def reset(self):
        if self.SCORE > self.high_score:
            self.high_score = self.SCORE
            with open("data.txt", mode="r+") as file_handle_data:
                file_handle_data.write(f"{self.high_score}")
        self.SCORE = 0
        self.refresh_score()
