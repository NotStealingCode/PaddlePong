from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        y_coordinate = -280
        self.goto(100, 250)
        self.write(f"{self.r_score}", False, align=ALIGNMENT, font=FONT)
        self.goto(-100, 250)
        self.write(f"{self.l_score}", False, align=ALIGNMENT, font=FONT)
        for index in range(0, 10):
            self.goto(0, y_coordinate)
            self.write("|", False, align=ALIGNMENT, font=FONT)
            y_coordinate += 56

    def left_player_points(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def right_player_points(self):
        self.clear()
        self.r_score += 1
        self.update_score()
