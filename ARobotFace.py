from graphics import Canvas
"""
File: ARobotFace.py
Name: Vishal Singh.
-------------------------
This program creates bunch of shapes along the bottom of the canvas.
1. Makes a Big Square
2. Makes two eyes
3. Makes a mouth
Note: Learning concepts of graphics, canvas, x and y coordinates and positioning.
Learning about functions and parameters.
"""

from graphics import Canvas

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
X_CENTRE = CANVAS_WIDTH / 2
Y_CENTRE = CANVAS_HEIGHT / 2

# Robot face dimensions
BIG_SQUARE_SIZE = 120
BIG_SQUARE_LEFT = X_CENTRE - BIG_SQUARE_SIZE
BIG_SQUARE_TOP = Y_CENTRE - BIG_SQUARE_SIZE
BIG_SQUARE_RIGHT = X_CENTRE + BIG_SQUARE_SIZE
BIG_SQUARE_BOTTOM = Y_CENTRE + BIG_SQUARE_SIZE

# Eye dimensions
EYE_WIDTH = 50
EYE_HEIGHT = 60
EYE_Y_POSITION = BIG_SQUARE_TOP + 30  # 30px down from top of head

LEFT_EYE_LEFT = X_CENTRE - BIG_SQUARE_SIZE / 2
LEFT_EYE_RIGHT = LEFT_EYE_LEFT + EYE_WIDTH

RIGHT_EYE_LEFT = X_CENTRE + BIG_SQUARE_SIZE / 2 - EYE_WIDTH
RIGHT_EYE_RIGHT = RIGHT_EYE_LEFT + EYE_WIDTH

# Mouth dimensions
MOUTH_LEFT = X_CENTRE - 55
MOUTH_RIGHT = X_CENTRE + 55
MOUTH_TOP = Y_CENTRE + BIG_SQUARE_SIZE / 3
MOUTH_BOTTOM = MOUTH_TOP + 20


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Draw robot head
    create_rectangle(canvas,
                     BIG_SQUARE_LEFT, BIG_SQUARE_TOP,
                     BIG_SQUARE_RIGHT, BIG_SQUARE_BOTTOM,
                     "#564C4C", "black")

    # Draw eyes
    create_oval(canvas,
                LEFT_EYE_LEFT, EYE_Y_POSITION,
                LEFT_EYE_RIGHT, EYE_Y_POSITION + EYE_HEIGHT,
                "yellow")

    create_oval(canvas,
                RIGHT_EYE_LEFT, EYE_Y_POSITION,
                RIGHT_EYE_RIGHT, EYE_Y_POSITION + EYE_HEIGHT,
                "yellow")

    # Draw mouth
    create_rectangle(canvas,
                     MOUTH_LEFT, MOUTH_TOP,
                     MOUTH_RIGHT, MOUTH_BOTTOM,
                     "white", "white")


def create_rectangle(canvas, left_x, top_y, right_x, bottom_y, fill_color, outline_color):
    """Helper function to create a rectangle with consistent parameters."""
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill_color, outline_color)


def create_oval(canvas, left_x, top_y, right_x, bottom_y, color):
    """Helper function to create an oval with consistent parameters."""
    canvas.create_oval(left_x, top_y, right_x, bottom_y, color)

# There is no need to edit code beyond this point
    canvas.mainloop()
# A python function that runs main() function.
if __name__ == '__main__':
    main()
