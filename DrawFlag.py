"""
File: DrawFlag.py
Name: Vishal Singh
-------------------------
This file shows how to use the graphics library to
draw a flag. It's a red rectangle that covers the top half
of the canvas.
"""
from graphics import Canvas

# The width of the canvas
CANVAS_WIDTH = 450
# The height of the canvas
CANVAS_HEIGHT = 300


def main():
    """
    Creates a red rectangle that covers the top half of the canvas.
    The rectangle spans from the middle of the canvas to the top-right corner.
    """
    # Initialize the drawing canvas with specified dimensions
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Define coordinates for the red rectangle:

    # Starts at left edge (x=0)
    red_left_x = 0
    # Starts at vertical middle (y=150)
    red_top_y = CANVAS_HEIGHT // 2
    # Extends to right edge (x=450)
    red_right_x = CANVAS_WIDTH
    # Extends to top edge (y=0)
    red_bottom_y = 0

    # Create the rectangle with the defined coordinates and red color
    canvas.create_rectangle(
        red_left_x,
        red_top_y,
        red_right_x,
        red_bottom_y,
        "red")

    canvas.mainloop()


if __name__ == '__main__':
    main()