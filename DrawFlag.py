from graphics import Canvas

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # the flag of Indonesia: red should start at 0,0 pixels and end at half the height and all the width
    canvas.create_rectangle(
        0,
        0,
        CANVAS_WIDTH,
        CANVAS_HEIGHT / 2,
        'red'
        )

    canvas.mainloop()


if __name__ == '__main__':
    main()