from turtle import Turtle
import random

class Car(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.cars = []
        self.colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
        self.max_car_speed = 35
        self.stop_car = False
        self.create_multiple_cars()

    def create_multiple_cars(self):
        n = random.randint(1, 1)

        for _ in range(n):
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(self.colors[random.randint(0, len(self.colors)-1)])
            new_car.turtlesize(1, 2.5)
            new_car.goto(320, random.randint(-250, 240))
            self.cars.append(new_car)


    def move_car(self, car):
        # -305 is when the car is gonna get deleted!
        car.setx(car.xcor() - random.randrange(0, self.max_car_speed, 5))

        if car.xcor() <= -305:
            car.hideturtle()
            car.clear()
            self.cars.remove(car)

        # for car in list_of_cars:
        #     car.setx(car.xcor() - random.randint(0, self.max_car_speed))
        #
        #     if car.xcor() <= -305:
        #         car.hideturtle()
        #         car.clear()
        #         list_of_cars.remove(car)

    def clear_all_cars(self):
        for car in self.cars:
            car.hideturtle()
            car.clear()

        self.cars.clear()

    def increase_speed(self):
        self.max_car_speed += 5