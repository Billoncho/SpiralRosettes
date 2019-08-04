# SpiralRosettes.py
# Billy Ridgeway
# Demostrates nested loops by creating a spiral of spirals.

import turtle               # Imports turtle graphics library.
t = turtle.Pen()            # Creates a new turtle called t.
t.speed(0)                  # Sets the pen speed to fast.
t.width(2)                  # Sets the width of the pen to 2.
t.penup()                   # Stop drawing.
turtle.bgcolor("black")     # Sets background color to black.


# Ask the useer for the number of sides, default to 4, min 2 and max 6.
sides = int(turtle.numinput("Number of sides",
                         "How many sides in your spiral of rosettes? (2-6)", 4, 2, 6))

# Create a list of colors.
colors = ["red", "yellow", "blue", "green", "purple", "orange"]

cycleColors = int(0)            # Set the variable to 0.

# Our outter spiral loop.
for m in range(100):            # Set the variable 'm' to count to 100.
    t.forward(m*4)              # Move the pen forward by the value of m times 4.
    position = t.position()     # Remember this corner of the spiral.
    heading = t.heading()       # Remember the direction we were heading.
    print(position, heading)    # Print the pen's position and heading.
    t.width(m/20)               # Set the width of the pen to the value of m divided by 20.

    # Our inner spiral loop.
    # Draws a little spiral at each corner of the big spiral.
    for n in range(sides):              # Set the variable n to count to the value of the range of sides.
          t.pendown()                   # Begin drawing.
          t.pencolor(colors[n%sides])   # Cycle through the pen's colors.
          t.circle(m/5)                 # Draw a circle the size of m divided by 5.
          t.right(360/sides)            # Move the pen right by 360 degrees divided by the number of sides.
          t.penup()                     # Stop drawing.
         
          
    t.setpos(position)          # Go back to the big spiral's x location.
    t.setheading(heading)       # Point in the big spiral's heading.
    t.left(360/sides + 2)       # Aim at the next point on the big spiral.
    
    
    
    
