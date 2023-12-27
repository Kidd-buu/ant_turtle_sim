import turtle
import random
import time

#intialize the screen
screen = turtle.Screen()
screen.bgcolor("black")

#create the ant turtle
ant = turtle.Turtle()
ant.shape("turtle") # turtle shape
ant.color("green") # ant color
ant.penup() # no idea full concept will have to research more but need in here
ant.speed(1) # speed of ant
ant.shapesize(1) #inital size

#create the food for the ant turtle
food = turtle.Turtle()
food.shape("square")
food.color("red")
food.penup()
food.speed(0)
food.setposition(random.randint(-200, 200),
                 random.randint(-200, 200))

def move_towards_food():
    food_position = food.position()
    ant.setheading(ant.towards(food_position))
    ant.forward(10) # adjust as needed for speed of movement
    
def is_collision(t1, t2):
    distance = t1.distance(t2)
    if distance < 5: # adjust the collision distance as needed
        return True
    else:
        return False

def regenerate_food():
    food.hideturtle()
    food.setposition(random.randint(-200, 200),
                     random.randint(-200, 200))

while True:
    move_towards_food()
    if is_collision(ant, food):
        food.hideturtle()
        ant.shapesize(ant.shapesize()[0] + 1) # increase size
        regenerate_food()
        food.showturtle()

def ant_shape():
    ant.shapesize()
    if ant.shapesize() == ant.shapesize(3):
        ant.hideturtle()
    
        
        

# ***Copyright 2023****
# ***Dangerous Industries 808***
# ***Simple Minds****
# ***G3iK0***


















