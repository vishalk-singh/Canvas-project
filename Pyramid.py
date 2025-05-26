"""
File: RandomCircle.py
Name: Vishal Singh
----------------------
This program draws a pyramid consisting of bricks arranged in horizontal rows,
so that the number of bricks in each row decreases by one as you move up the pyramid.
1. Draw a Canvas.
2. Starting at the bottom row that is row 0 and iterating to the top.
    # How many bricks belong in this row? 14 at bottom row, decreasing by one until we reach the top. At the top only one brick.
    # Keep track of the number of bricks minus one.
    # Compute vertical position of the top row by taking the height of the canvas and subtract row index + 1, multiplied by brick height.
    # Compute the horizontal starting position to the center row by taking the canvas and subtracting the number of bricks, multiplied by brick width and dividing by 2.
3. Withing the row loop over each brick index.
    # Computer each brick's left, top, right and bottom coordinates so the bricks go in the right positions.
    # Draw a rectangle with the specified color and outline.

"""
from graphics import Canvas
import random

# Constants for canvas and circle configuration
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 300

BRICK_WIDTH = 30
BRICK_HEIGHT = 12
BRICKS_IN_BASE = 14

# BRICK_COLOR = "yellow"
OUTLINE_COLOR = "black"

def main():
    # Draw a canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    #
    for row in range(BRICKS_IN_BASE):
        bricks_in_row = BRICKS_IN_BASE - row
        y_top_position = CANVAS_HEIGHT - (row + 1) * BRICK_HEIGHT
        x_start_position = (CANVAS_WIDTH - bricks_in_row * BRICK_WIDTH) // 2
        for brick_num in range(bricks_in_row):
            brick_color = random.choice(["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"])
            x_position = x_start_position + brick_num * BRICK_WIDTH
            canvas.create_rectangle(
                x_position, y_top_position,
                x_position + BRICK_WIDTH, y_top_position + BRICK_HEIGHT,
                color=brick_color,
                outline=OUTLINE_COLOR
            )


    canvas.mainloop()

if __name__ == '__main__':
    main()
