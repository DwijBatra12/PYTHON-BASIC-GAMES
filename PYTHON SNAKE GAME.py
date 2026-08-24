# =====================================================================
# PYTHON SNAKE GAME - EXPLAINED STEP-BY-STEP
# =====================================================================

import turtle
import time
import random

# --- SECTION 1: SETTING UP THE GAME VARIABLES ---
# We define how fast the game updates and keep track of the score.
delay = 0.1  # The delay between frames (controls game speed).
score = 0
high_score = 0

# --- SECTION 2: SETTING UP THE SCREEN ---
window = turtle.Screen()
window.title("Classic Snake")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)  # Turns off automatic screen updates for smooth animation

# --- SECTION 3: CREATING THE SNAKE HEAD ---
# This is the part of the snake the player actually controls.
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()            # Don't draw a line when it moves
head.goto(0, 0)         # Start right in the middle
head.direction = "stop" # The snake doesn't move until a key is pressed

# --- SECTION 4: CREATING THE SNAKE FOOD ---
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)       # Start the food slightly above the head

# --- SECTION 5: CREATING THE SCORE DISPLAY ---
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()        # We hide the turtle because we only want to see the text it writes
pen.goto(0, 260)        # Move it to the top of the screen
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# IMPORTANT: We need an empty list to store the pieces of the snake's body as it grows.
segments = []


# --- SECTION 6: MOVEMENT FUNCTIONS ---
# These functions change the direction, but ONLY if the snake isn't trying to reverse into itself.
# (e.g., if you are going UP, you can't instantly go DOWN, or you would crash into your own body).
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# The move function physically updates the coordinates based on the current direction.
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)  # Move 20 pixels UP

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)  # Move 20 pixels DOWN

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)  # Move 20 pixels LEFT

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)  # Move 20 pixels RIGHT


# --- SECTION 7: KEYBOARD BINDINGS ---
window.listen()
window.onkeypress(go_up, "w")       # Press 'w' to go up
window.onkeypress(go_down, "s")     # Press 's' to go down
window.onkeypress(go_left, "a")     # Press 'a' to go left
window.onkeypress(go_right, "d")    # Press 'd' to go right

# We also add the arrow keys for convenience!
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")


# --- SECTION 8: THE MAIN GAME LOOP ---
while True:
    window.update()  # Refresh the screen

    # 1. CHECK FOR COLLISION WITH WALLS
    # The screen is 600x600, meaning edges are at +300 and -300.
    # If the snake hits an edge, the game resets.
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)           # Pause for 1 second before restarting
        head.goto(0, 0)         # Put head back in the middle
        head.direction = "stop" # Stop moving

        # Hide the old body segments by moving them off-screen
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segment list (the snake is short again!)
        segments.clear()

        # Reset the score
        score = 0
        pen.clear() # Clear old text
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # 2. CHECK FOR COLLISION WITH FOOD
    # If the head is less than 20 pixels away from the food (they touched!)
    if head.distance(food) < 20:
        
        # Move the food to a random new spot on the grid (multiples of 20 keep it aligned)
        x = random.randint(-14, 14) * 20 
        y = random.randint(-14, 14) * 20
        food.goto(x, y)

        # Create a new body segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")  # Slightly different color than the head
        new_segment.penup()
        
        # Add the new segment to our list of body parts
        segments.append(new_segment)

        # Update the score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # 3. MOVE THE SNAKE'S BODY
    # We move the body in reverse order. Segment 5 moves to where Segment 4 was,
    # Segment 4 moves to where Segment 3 was, etc.
    totalseg = len(segments)
    for index in range(totalseg - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 (the first piece attached to the head) to where the head just was
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # 4. MOVE THE HEAD ITSELF
    move()

    # 5. CHECK FOR COLLISION WITH ITS OWN BODY
    # If the head touches ANY segment in the list, the player loses.
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # 6. FRAME RATE CONTROL
    # Pause slightly so the game runs at a playable speed.
    time.sleep(delay)