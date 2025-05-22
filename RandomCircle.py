"""
File: RandomCircle.py
Name: Vishal Singh
----------------------
This program draws random numbers of circles at random positions
with random sizes and colors on the canvas.
"""
from graphics import Canvas
import random

# Constants for canvas and circle configuration
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300


def main():
    # Title printed in console
    print('Random Circles')

    # Loop to draw N_CIRCLES number of circles
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # Draw random circles
    random_circle(canvas)
    # Draw the canvas and keep it open until user quits.
    canvas.mainloop()


def random_circle(canvas):
    """
    This function draws random circles on the canvas.
     1. Draw a random number of circles between 1 and 20.
     2. Draw circles of a random size
     3. Draw the circles such that all parts of the circle are within the canva
    """
    # Random number of circles to draw
    random_n_circle = random.randint(1, 20)
    for i in range(random_n_circle):
        # Random circle size
        random_circle_size = random.randint(10, 50)
        # Random (x, y) coordinates for the top-left corner of the circle
        x = random.randint(1,
                           CANVAS_WIDTH - random_circle_size)  # Generation random numbers between 1 to 280. It's insures that circle will be within canvas.
        y = random.randint(1, CANVAS_HEIGHT - random_circle_size)

        right_x = x + random_circle_size  # Calculate bottom-right x-coordinate
        bottom_y = y + random_circle_size  # Calculate bottom-right y-coordinate

        # Create and draw an oval (circle) on the canvas
        canvas.create_oval(x, y, right_x, bottom_y, random_color())

def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested.
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)


if __name__ == '__main__':
    main()