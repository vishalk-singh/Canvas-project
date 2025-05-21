
"""
File: Pillow.py
Name: Vishal Singh
-------------------------
This file shows how to use quilt pattern to draw on canvas.
1. A quilt, as you may know, is a blanket often composed of repeating "patches".
2. Each patch is a square or circle.
3. The patches alternate between square and circle.
4. Each patch has height and width of 100 pixels, given by the constant PATCH_SIZE.
"""

# Importing the graphics library
from graphics import Canvas

# each patch is a square with this width and height:
PATCH_SIZE = 100
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 2


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Loop over rows and columns
    for row in range(2):  # 0 and 1
        for col in range(4):  # 0 to 3
            x = col * PATCH_SIZE
            y = row * PATCH_SIZE

            # Alternate between square and circle patches based on position
            if (row + col) % 2 == 0:
                draw_square_patch(canvas, x, y)
            else:
                draw_circle_patch(canvas, x, y)

    canvas.mainloop()
# Functions for drawing patches
# ---------------------------------
def draw_circle_patch(canvas, start_x, start_y):
    # draws a salmon circle frame at (start_x, start_y)
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    canvas.create_oval(start_x, start_y, end_x, end_y, 'salmon')


def draw_square_patch(canvas, start_x, start_y):
    # draws a purple frame at (start_x, start_y)
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 20
    # first draw a purple square over the entire patch
    canvas.create_rectangle(start_x, start_y, end_x, end_y, 'purple')
    # then draw a smaller white square on top
    canvas.create_rectangle(start_x + inset, start_y + inset,
                            end_x - inset, end_y - inset, 'white')

# There is no need to edit code beyond this point
# A python function that runs main() function.
if __name__ == '__main__':
    main()