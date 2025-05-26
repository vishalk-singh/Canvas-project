from graphics import Canvas  # Make sure this imports the Canvas class correctly

# Constants
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 300
BRICK_WIDTH = 30
BRICK_HEIGHT = 12
BRICKS_IN_BASE = 14
BRICK_COLOR = "yellow"
OUTLINE_COLOR = "black"


def main():
    # Create canvas instance - ensure we're not shadowing the Canvas class name
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Calculate pyramid dimensions
    pyramid_height = BRICKS_IN_BASE * BRICK_HEIGHT

    # Draw each row from bottom to top
    for row in range(BRICKS_IN_BASE):
        bricks_in_row = BRICKS_IN_BASE - row
        y_position = CANVAS_HEIGHT - (row + 1) * BRICK_HEIGHT

        # Calculate row width and center it
        row_width = bricks_in_row * BRICK_WIDTH
        start_x = (CANVAS_WIDTH - row_width) // 2

        # Draw each brick in the row
        for brick_num in range(bricks_in_row):
            x_position = start_x + brick_num * BRICK_WIDTH
            canvas.create_rectangle(
                x_position, y_position,
                x_position + BRICK_WIDTH, y_position + BRICK_HEIGHT,
                color=BRICK_COLOR,
                outline=OUTLINE_COLOR
            )
        canvas.mainloop()

if __name__ == '__main__':
    main()