from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Level(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.level = 1
        self.penup()
        self.color("black")
        self.write_current_level()

    def write_current_level(self):
        self.goto(-250, 275)
        self.write(f"Level {self.level}", False, ALIGNMENT, FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write_current_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)
