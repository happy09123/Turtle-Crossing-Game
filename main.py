from turtle import Screen, Turtle
from player import Player
from car import Car
from levels import Level
import time

line = Turtle(visible=False)
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Turtle Crossing")

line.pensize(3)
line.color("gray")
line.penup()
line.goto(-300, 275)

for _ in range(30):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)

finished = False
t = Player()
car = Car()
level = Level()

screen.listen()
screen.onkey(t.up, "Up")

while not finished:
    screen.update()
    time.sleep(0.1)

    for i in car.cars:
        car.move_car(i)

    if t.collision_with_car(car.cars):
        finished = True
        level.game_over()

    # car.move_multiple_cars(car.cars)
    if t.ycor() >= 270:
        t.goto(0, -280)
        level.level_up()
        car.clear_all_cars()
        car.increase_speed()

    if len(car.cars) <= 3:
        car.create_multiple_cars()


screen.exitonclick()