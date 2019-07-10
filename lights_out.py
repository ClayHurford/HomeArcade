import arcade
import random

ROW_COUNT = 5
COLUMN_COUNT = 5

WIDTH = 100
HEIGHT = 100

MARGIN = 15

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Lights Out"


class LightsOut(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.grid = []
        self.win = False
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(random.randint(0, 1))

        arcade.set_background_color(arcade.color.WHITE_SMOKE)

    def on_draw(self):
        arcade.start_render()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.YELLOW
                else:
                    color = arcade.color.BLACK_LEATHER_JACKET

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        for rcell in range(ROW_COUNT):
            for ccell in range(COLUMN_COUNT):
                if self.grid[rcell][ccell] == 1:
                    self.win = True
                else:
                    self.win = False
                    break

        if self.win is True:
            print('YOU WON')
            return
        elif row < ROW_COUNT and column < COLUMN_COUNT:
            self.update_adjacent_squares(row, column)

    def flip_location(self, row, column):
        # Flip the location between 1 and 0.
        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

    def update_adjacent_squares(self, row, column):
        if row == 0 and column == 0:
            self.flip_location(0, 0)
            self.flip_location(0, 1)
            self.flip_location(1, 0)

        elif row == 4 and column == 4:
            self.flip_location(4, 4)
            self.flip_location(4, 3)
            self.flip_location(3, 4)

        elif row in range(1, 4) and column in range(1, 4):
            for num in range(3):
                self.flip_location((row - 1) + num, column)
            self.flip_location(row, column - 1)
            self.flip_location(row, column + 1)
        elif row in range(1, 4) and column == 0:
            for num in range(3):
                self.flip_location(row - 1 + num, column)
            self.flip_location(row, column + 1)
        elif row in range(1, 4) and column == 4:
            for num in range(3):
                self.flip_location(row - 1 + num, column)
            self.flip_location(row, column - 1)
        elif row == 0 and column in range(1, 4):
            for num in range(3):
                self.flip_location(row, column - 1 + num)
            self.flip_location(row + 1, column)
        elif row == 4 and column in range(1, 4):
            for num in range(3):
                self.flip_location(row, column - 1 + num)
            self.flip_location(row - 1, column)
        elif row == 4 and column == 0:
            self.flip_location(row, column)
            self.flip_location(row - 1, column)
            self.flip_location(row, column + 1)
        elif row == 0 and column == 4:
            self.flip_location(row, column)
            self.flip_location(row + 1, column)
            self.flip_location(row, column - 1)


if __name__ == "__main__":
    LightsOut(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
