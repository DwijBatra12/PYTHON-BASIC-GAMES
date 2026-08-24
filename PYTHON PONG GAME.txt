# =====================================================================
# PYTHON PONG GAME - PLAYABLE SPEED (EXPLAINED STEP-BY-STEP)
# =====================================================================

import turtle 
import time  # NEW: We need the time module to control how fast the game runs.

# --- SECTION 1: SETTING UP THE GAME TABLE ---
window = turtle.Screen()
window.title("Classic Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) 

# --- SECTION 2: CREATING THE PLAYERS (PADDLES) ---

# Paddle A (Left Player)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) 
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B (Right Player)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# --- SECTION 3: CREATING THE BALL ---
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# BALL PHYSICS (Velocity): 
# We've increased the movement per frame slightly to balance out the new delay.
ball.dx = 4
ball.dy = 4


# --- SECTION 4: MOVEMENT FUNCTIONS ---
def paddle_a_up():
    y = paddle_a.ycor()
    # Prevent paddle from going off the top screen
    if y < 250:
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()      
    # Prevent paddle from going off the bottom screen
    if y > -240:
        y -= 20
        paddle_a.sety(y)         

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
        paddle_b.sety(y)


# --- SECTION 5: KEYBOARD BINDINGS ---
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


# --- SECTION 6: THE MAIN GAME LOOP ---
while True:
    window.update() 

    # 1. MOVE THE BALL
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # 2. BORDER CHECKING (Top and Bottom Walls)
    if ball.ycor() > 290:       
        ball.sety(290)
        ball.dy *= -1           
        
    elif ball.ycor() < -290:    
        ball.sety(-290)
        ball.dy *= -1

    # 3. SCORING (Left and Right Walls)
    if ball.xcor() > 390:       
        ball.goto(0, 0)
        ball.dx *= -1
        # Give the players a tiny pause before the ball serves again
        time.sleep(0.5)
        
    elif ball.xcor() < -390:    
        ball.goto(0, 0)
        ball.dx *= -1
        time.sleep(0.5)

    # 4. PADDLE COLLISIONS
    # Check Right Paddle (Paddle B)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)          
        ball.dx *= -1           
        
    # Check Left Paddle (Paddle A)
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # 5. FRAME RATE CONTROL (The Speed Limit)
    # We tell the program to pause for 0.01 seconds before restarting the loop.
    # This forces the game to run at roughly 100 frames per second (FPS), 
    # making it playable on any computer.
    time.sleep(0.01)