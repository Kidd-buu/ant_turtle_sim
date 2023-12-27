import turtle
import random

# initialize the screen
screen = turtle.Screen()
screen.bgcolor("black")

#create enemy ant turtle
ant0 = turtle.Turtle()
ant0.shape("turtle")
ant0.color("purple")
ant0.penup()
ant0.speed(1)
ant0.shapesize(2)

# create the first ant turtle
ant1 = turtle.Turtle()
ant1.shape("turtle")
ant1.color("green")
ant1.penup()
ant1.speed(1)
ant1.shapesize(1)

# create the second ant turtle
ant2 = turtle.Turtle()
ant2.shape("turtle")
ant2.color("blue")  # Set color for the second ant
ant2.penup()
ant2.speed(1)
ant2.shapesize(1)

# create the food for the ants
food = turtle.Turtle()
food.shape("square")
food.color("red")
food.penup()
food.speed(0)
food.setposition(random.randint(-200, 200), random.randint(-200, 200))

# track the number of food eaten by each ant
food_eaten1 = 0
food_eaten2 = 0
food_eaten3 = 0
max_food = 5  # define the maximum food the ants can eat before "dying"

def enemy_movement(enant): # created so ant0 follow player
    enemy_movement = ant2.position() # follow ant2/player 
    enant.setheading(enant.towards(ant2))
    enant.forward(1)
    

def move_towards_food(ant):
    food_position = food.position()
    ant.setheading(ant.towards(food_position))
    ant.forward(1)


def is_collision(t1, t2):
    distance = t1.distance(t2)
    if distance < 5:
        return True
    else:
        return False


def regenerate_food():
    food.hideturtle()
    food.setposition(random.randint(-200, 200), random.randint(-200, 200))
    food.showturtle()


# Define functions to control the second ant using arrow keys
def move_up():
    y = ant2.ycor()
    ant2.sety(y + 10)

def move_down():
    y = ant2.ycor()
    ant2.sety(y - 10)

def move_left():
    x = ant2.xcor()
    ant2.setx(x - 10)

def move_right():
    x = ant2.xcor()
    ant2.setx(x + 10)

def launch_reaper():
    #create missile that shoots from ant2
    reaper = turtle.Turtle()
    reaper.shape("triangle")
    reaper.color("yellow")
    reaper.penup()
    reaper.speed(3)
    reaper.shapesize(.3)
    reaper.showturtle

#set up keyboard bindings for launching reaper triangle from ant2
screen.onkeypress(launch_reaper, "F1")


# Set up keyboard bindings for controlling the second ant
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Listen for keyboard input
screen.listen()

while food_eaten1 < max_food or food_eaten2 < max_food:
    move_towards_food(ant1)
    
    if is_collision(ant0, ant2):
        ant0.shapesize(ant0.shapesize()[0] + 1) # increase size
        food_eaten3 += .1

    if is_collision(ant1, food):
        food.hideturtle()
        ant1.shapesize(ant1.shapesize()[0] + 1)  # increase size
        regenerate_food()
        food.showturtle()
        food_eaten1 += 1  # increment the food eaten

    if is_collision(ant2, food):
        food.hideturtle()
        ant2.shapesize(ant2.shapesize()[0] + 1)  # increase size
        regenerate_food()
        food.showturtle()
        food_eaten2 += 1  # increment the food eaten
        
    if ant2.shapesize() < ant0.shapesize():
        enemy_movement(ant0)
    
    if food_eaten2 or food_eaten1 == max_food:
        print("Both ants have eaten enough food and have died.")
        break
