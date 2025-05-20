from graphics import Canvas
import math
"""
File: SquireLineDraw.py
Name: Vishal Singh.
-------------------------
This program creates a square with a line drawn inside it.
The line is drawn diagonally from the top-left to the bottom-right.
This program uses math library and pythagoras theorem to calculate the diagonal length.
"""

def main():
    # Set the dimensions of the canvas
    CANVAS_HIGHT = 400
    CANVAS_WIDTH = CANVAS_HIGHT

    # Define the side length of the large square (same as canvas height)
    large_square_side = CANVAS_HIGHT

    # Define the side length of the smaller square
    small_square_side = 20

    # Calculate the diagonal length of the large square using Pythagoras theorem
    large_diagonal = math.sqrt(2) * large_square_side

    # Calculate the diagonal length of the small square
    small_diagonal = math.sqrt(2) * small_square_side

    # Calculate how many small squares can fit diagonally inside the large square
    num_squares = int(large_diagonal // small_diagonal)  # Floor division to get whole squares only

    # Create a canvas to draw on using the graphics library
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HIGHT)

    # Draw the calculated number of small blue squares diagonally
    for i in range(num_squares):
        value = i * small_square_side  # Position offset for each square

        # Calculate the coordinates for the top-left and bottom-right of the square
        left_x = value
        top_y = value
        right_x = value + small_square_side
        bottom_y = value + small_square_side

        # Draw a blue square (rectangle with equal sides) at the calculated position
        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'red')

        # Print the current index to track how many squares are drawn
        print(i)
# There is no need to edit code beyond this point
    canvas.mainloop()
    # A python function that runs main() function.
if __name__ == '__main__':
    main()