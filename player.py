from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.setheading(90)
        self.turtlesize(0.8, 0.8)
        print(self.turtlesize)
        self.penup()
        self.sety(-280)
        self.speed = 10


    def up(self):
        if self.ycor() < 270:
            self.sety(self.ycor() + self.speed)


    def collision_with_car(self, cars):
        for car in cars:
            # something = car.ycor()-self.ycor()
            # if self.ycor() == car.ycor() - something and self.ycor() == car.ycor() + something:
            #     if self.distance(car) < 40 and car.ycor() <= something and car.xcor() <= 0:
            # print("x:", self.xcor(), car.xcor())
            # print("y: ", self.ycor(), car.ycor())
            if self.distance(car) <= 15:
                return True

        return False