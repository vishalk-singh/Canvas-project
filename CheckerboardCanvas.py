"""
File: CheckerboardCanvas.py
Name: Vishal Singh
---------------------------
This Program draws a checkerboard on the Canvas window.
 * The size of the checkerboard is specified by the
 * constants N_ROWS and N_COLUMNS, and the checkerboard fills
 * the vertical space available.

"""
from graphics import Canvas
# Note: This is custom class graphics created by Stanford University. It's needs external file to works with pycharm or other IDE.

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

# No of rows and columns to be drawn.
N_ROWS = 8 # Number of rows in the checkerboard (standard chessboard size)
N_COLUMNS = 8 # Number of columns in the checkerboard

def main():
    """
    Main rendering function:
    1. Creates the canvas
    2. Calculates square dimensions
    3. Draws the checkerboard pattern
    """
    # Initialize canvas with specified dimensions
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Calculate the size of each square to perfectly fit the canvas height
    # (Using height ensures squares remain equal if canvas isn't square)
    sq_size = CANVAS_HEIGHT / N_ROWS # Results in 50px squares for 400px/8 rows

    # Nested loop to draw each square in the grid
    for row in range(N_ROWS): # Main Loop through each row (0 to 7)
        for column in range(N_COLUMNS): # Nested Loop through each column (0 to 7).
            # Note: At the end of the loop column variable in this loop resets to 0 after main loop runs.

            # Calculate square coordinates:
            # Left edge position
            left_x = column * sq_size
            # Top edge position
            top_y = row * sq_size
            # Right edge position
            right_x = left_x + sq_size
            # Bottom edge position
            bottom_y = top_y + sq_size

            # Determine square color using the draw checkerboard pattern function
            color = draw_checkerboard_pattern(row, column)

            # Draw the square with:
            # - Calculated coordinates
            # - Pattern-determined fill color
            # - Black outline
            canvas.create_rectangle(
                left_x,
                top_y,
                right_x,
                bottom_y,
                color,
                "black" # Outline color
            )
    canvas.mainloop() # Its needed to show canvas in pycharm. Not required here.
def draw_checkerboard_pattern(rows, columns):
    """
    Determines the color of a square based on its position.

    Args:
        row: The row index
        column: The column index

    Returns:
        "black" or "white" based on the checkerboard pattern

    Pattern Logic:
    - If (row + column) is odd → black square
    - If (row + column) is even → white square
    This creates the alternating checkerboard effect.
    """
    if (rows + columns) % 2 != 0:
        return "black"
    else:
        return "white"


if __name__ == '__main__':
    main()