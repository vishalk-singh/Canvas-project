from graphics import Canvas
"""
File: BoxRow.py
Name: Vishal Singh.
-------------------------
This program creates a row of equally sized boxes along the bottom of the canvas.
Each box is white with a black outline.
"""

# Constants defining the canvas and box properties
CANVAS_WIDTH = 400  # Total width of canvas in pixels
CANVAS_HEIGHT = 200  # Total height of canvas in pixels
N_BOXES = 5  # Number of boxes to draw horizontally
BOX_SIZE = CANVAS_WIDTH / N_BOXES  # Width of each box (auto-calculated)


def main():
    """
    Creates a row of equally sized boxes along the bottom of the canvas.
    Each box is white with a black outline.
    """
    # Initialize the drawing canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    left_x = 0  # Starting from left edge
    top_y = CANVAS_HEIGHT - BOX_SIZE  # Top of boxes (height - box size)
    right_x = BOX_SIZE  # Initial right edge position
    bottom_y = CANVAS_HEIGHT  # Bottom of boxes (canvas bottom)

    # Draw N_BOXES number of boxes in a row
    # Creates a white rectangle
    # with a black outline
    for i in range(N_BOXES):
        canvas.create_rectangle(
            left_x,
            top_y,
            right_x,
            bottom_y,
            "white",  # Fill color
            "black"  # Outline color
        )
        # Update positions for next box
        left_x = left_x + BOX_SIZE  # Move left edge right by one box width
        right_x = right_x + BOX_SIZE  # Move right edge right by one box width

# There is no need to edit code beyond this point
    canvas.mainloop()
# A python function that runs main() function.
if __name__ == '__main__':
    main()
