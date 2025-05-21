"""
File: CheckerboardCanvas.py
Name: Vishal Singh
-------------------------
This file shows how to use the graphics library to
draw a checkerboard pattern on a canvas.
"""
from graphics import Canvas
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

N_ROWS = 8
N_COLS = 8

def main():
    """
    Creates a checkerboard pattern on a canvas.
    The pattern is a 50 pix square with black and white squares alternating.
    """
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    square_size = CANVAS_WIDTH / N_COLS  # Size of each square auto-calculated by dividing canvas width by number of columns
    for row in range(N_ROWS):
        for col in range(N_COLS):
            # Calculate the top-left corner of the square
            left_x = col * square_size
            top_y = row * square_size
            # Calculate the bottom-right corner of the square
            right_x = left_x + square_size
            bottom_y = top_y + square_size
            # Determine the color of the square based on row and column
            color = draw_checkerboard_color(row, col)
            # Draw the square on the canvas
            canvas.create_rectangle(
                left_x,
                top_y,
                right_x,
                bottom_y,
                color,
                "black"
            )
    canvas.mainloop()

def draw_checkerboard_color(row, col):
    """
    Determines the color of the square based on row and column.
    """
    if (row + col) % 2 == 0:
        return "black"
    else:
        return "white"

# ----- DO NOT MODIFY CODE BELOW THIS LINE -----
if __name__ == "__main__":
    main()
