import tkinter as tk
import math

class Cell:
    def __init__(self, col, row, status):
        self.col = col
        self.row = row
        self.status = status

def step(cells):
    new_cells = []

    for row in range(len(cells)):
        new_row = []
        for col in range(len(cells[0])):
            cell = cells[row][col]
            live_neighbors = sum(
                cells[i][j].status
                for i in range(row - 1, row + 2)
                for j in range(col - 1, col + 2)
                if 0 <= i < len(cells) and 0 <= j < len(cells[0]) and (i != row or j != col)
            )
            if cell.status:
                new_status = live_neighbors in [2, 3]
            else:
                new_status = live_neighbors == 3
            new_row.append(Cell(col, row, new_status))
        new_cells.append(new_row)

    return new_cells

class MouseClickExample:
    def __init__(self, master):
        self.master = master
        self.master.title("Life")

        self.cells = [[Cell(x, y, False) for x in range(10)] for y in range(10)]

        self.canvas = tk.Canvas(master, width=300, height=300, bg='white')
        self.canvas.pack()

        self.update_canvas()

        self.start_button = tk.Button(master, text="Start", command=self.start_game)
        self.start_button.pack()

        self.running = False  # Flag to indicate whether the game is running
        self.timer_interval = 100  # Time interval in milliseconds (adjust as needed)

        # Bind the left mouse button click event to the callback function
        self.canvas.bind('<Button-1>', self.on_mouse_click)

    def start_game(self):
        # Toggle the running flag
        self.running = not self.running

        # If the game is now running, start the timer
        if self.running:
            self.run_step()

    def run_step(self):
        # Perform one step of the Game of Life
        self.cells = step(self.cells)

        # Update the canvas to reflect the new state of the cells
        self.update_canvas()

        # If the game is still running, schedule the next step
        if self.running:
            self.master.after(self.timer_interval, self.run_step)

    def on_mouse_click(self, event):
        # Event handler for mouse click
        if not self.running:  # Check if the game is not running
            x = event.x
            y = event.y
            # print(f"Mouse clicked at ({x}, {y})")

            flooredX = math.floor(x / 30)
            flooredY = math.floor(y / 30)

            for row in self.cells:
                for c in row:
                    if c.col == flooredX and c.row == flooredY:
                        c.status = not c.status

            self.update_canvas()

    def update_canvas(self):
        # Update the canvas based on the current state of the cells
        self.canvas.delete("all")  # Clear the canvas

        # Draw rectangles on the canvas to represent the cells
        for row in self.cells:
            for c in row:
                if c.status:
                    # Draw a black rectangle for a live cell
                    self.canvas.create_rectangle(c.col * 30, c.row * 30, c.col * 30 + 30, c.row * 30 + 30,
                                                outline="black", fill="black", width=2)
                else:
                    # Draw a white rectangle for a dead cell
                    self.canvas.create_rectangle(c.col * 30, c.row * 30, c.col * 30 + 30, c.row * 30 + 30,
                                                outline="black", fill="white", width=2)

# Create the main Tkinter window
root = tk.Tk()

# Create an instance of the MouseClickExample class
mouse_click_example = MouseClickExample(root)

# Start the Tkinter event loop
root.mainloop()
