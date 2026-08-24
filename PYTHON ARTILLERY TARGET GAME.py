import turtle
import math
import random

# 1. Setup the visual screen
screen = turtle.Screen()
# We are setting the size of the screen in which the game will be made
screen.setup(width=800, height=400)
# We are defining the name of the window 
screen.title("Artillery Target Game")
# Setting the background of the window
screen.bgcolor("skyblue")

# 2. Draw the ground
ground = turtle.Turtle()
# Penup lifts the pen of the turtle and stops it actually writing something on the screen
ground.penup()
# Moving the pen of the turtle to a particular position (-400, -150) without drawing
ground.goto(-400, -150)
# Pendown for actually drawing someting
ground.pendown()
# filling with the color forest green 
ground.fillcolor("forestgreen")
# fill the bottom with the green color
ground.begin_fill()
# Make a for loop
for _ in range(2):
    # move the turtle forward by 800 
    ground.forward(800)
    # move the turtle right by 90 degrees
    ground.right(90)
    # move the turtle down by 50 
    ground.forward(50)
    # move the turtle right by 90 degrees
    ground.right(90)
# Fill the entire ground by green color at the bottom
ground.end_fill()
#  hide the turtle
ground.hideturtle()

# 3. Place the target at a random distance
# create a random integer value between 0 and 300 for our target x coordinate
target_x = random.randint(0, 300)
target = turtle.Turtle()
# Shape of target will be a Square
target.shape("square")
# Target color will be red
target.color("red")
# pen up the turtle so that do not draw a line
target.penup()
# Go to the coordinate whose x coordinate is a random value but y coordinate is fixed ie -140
target.goto(target_x, -140)

# 4. Create the cannonball
ball = turtle.Turtle()
# shape of the canon ball is circle
ball.shape("circle")
# color of the canon ball is black
ball.color("black")
# pen up the turtle 
ball.penup()
# go to the coordinate -350, -140
ball.goto(-350, -140)

# 5. Get input from the user via pop-up dialogs
# input the angle which the projectile have to be fired
# get a numeric input from the user whose default value is 45 and the angle is allowed between 0  to 90 degrees
angle = screen.numinput("Aim", "Enter launch angle (0 to 90 degrees):", 45, 0, 90)
# get a numeric input from the user whose default value is 70 and the speed is allowed between 30  to 120 degrees

speed = screen.numinput("Power", "Enter launch speed (30 to 120):", 70, 30, 120)

if angle is not None and speed is not None:
    # Convert angle to radians for the math module
    rad_angle = math.radians(angle)
    
    # Calculate initial x and y velocity components
    # Horizontal component of velocity is v cos theta, where theta is in radian
    vx = speed * math.cos(rad_angle)
    # Vertical component of velocity is v sin theta, where theta is in radian
    vy = speed * math.sin(rad_angle)
    # acceleration due to gravity
    gravity = -9.8
    
    dt = 0.2  # Time step for the simulation

    # 6. The Physics/Game Loop
    # We want that the trajectory or path of the ball is visible
    ball.pendown() # Leaves a trail behind the ball
    
    while ball.ycor() >= -140:
        # Update positions
        # Since there is no acceleration in the x direction, equation of motion will be delta s = ut 
        new_x = ball.xcor() + (vx * dt)
        # In y direction s = ut + 0.5 at^2
        new_y = ball.ycor() + (vy * dt)
        # move the tutle to the newx and new y coordinates. mark the trail
        ball.goto(new_x, new_y)
        
        # Apply downward acceleration to vertical velocity
        # we are updating the veloctity very fast
        # Vy = Usin theta - gt
        vy += gravity * dt

    # 7. Check for a hit
    # if the x coordinate difference of the cannon ball and the target is same then its a success
    distance = abs(ball.xcor() - target_x)
    
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(0, 50)

    # if the distance is less than 20 then its a hit else not hit
    if distance < 20:
        writer.write("DIRECT HIT!", align="center", font=("Arial", 24, "bold"))
    else:
        writer.write(f"Missed! You were off by {int(distance)} units.", align="center", font=("Arial", 20, "normal"))

# Keep the window open until clicked
screen.exitonclick()