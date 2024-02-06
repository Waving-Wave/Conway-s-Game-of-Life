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

        # Set the initial grid size to 20x20
        self.cells = [[Cell(x, y, False) for x in range(20)] for y in range(20)]
        self.cell_size = 20  # Adjust the cell size accordingly

        self.canvas = tk.Canvas(master, width=400, height=400, bg='white')
        self.canvas.pack()

        self.update_canvas()

        self.start_button = tk.Button(master, text="Start/Stop", command=self.start_game)
        self.start_button.pack()

        self.running = False
        self.timer_interval = 100  # Adjust the timer interval accordingly

        self.canvas.bind('<Button-1>', self.on_mouse_click)

    def start_game(self):
        self.running = not self.running
        if self.running:
            self.run_step()

    def run_step(self):
        self.cells = step(self.cells)
        self.update_canvas()
        if self.running:
            self.master.after(self.timer_interval, self.run_step)

    def on_mouse_click(self, event):
        if not self.running:
            x = event.x
            y = event.y

            flooredX = math.floor(x / self.cell_size)
            flooredY = math.floor(y / self.cell_size)

            for row in self.cells:
                for c in row:
                    if c.col == flooredX and c.row == flooredY:
                        c.status = not c.status

            self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")

        for row in self.cells:
            for c in row:
                if c.status:
                    self.canvas.create_rectangle(c.col * self.cell_size, c.row * self.cell_size,
                                                 (c.col + 1) * self.cell_size, (c.row + 1) * self.cell_size,
                                                 outline="black", fill="black", width=2)
                else:
                    self.canvas.create_rectangle(c.col * self.cell_size, c.row * self.cell_size,
                                                 (c.col + 1) * self.cell_size, (c.row + 1) * self.cell_size,
                                                 outline="black", fill="white", width=2)

        # Adjust the canvas size based on the current grid size
        canvas_width = len(self.cells[0]) * self.cell_size
        canvas_height = len(self.cells) * self.cell_size
        self.canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))

# Create the main Tkinter window
root = tk.Tk()

# Create an instance of the MouseClickExample class
mouse_click_example = MouseClickExample(root)

# Start the Tkinter event loop
root.mainloop()
