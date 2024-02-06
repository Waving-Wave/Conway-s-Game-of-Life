import tkinter as tk
import math

class Cell:
    def __init__(self, col, row, status):
        # Constructor for the Cell class
        self.col = col  # Column position of the cell
        self.row = row  # Row position of the cell
        self.status = status  # Status of the cell (True for alive, False for dead)

def step(cells):
    # Function to perform one step in the Game of Life simulation
    new_cells = []

    # Iterate over each cell in the grid
    for row in range(len(cells)):
        new_row = []
        for col in range(len(cells[0])):
            cell = cells[row][col]
            
            # Count live neighbors
            live_neighbors = sum(
                cells[i][j].status
                for i in range(row - 1, row + 2)
                for j in range(col - 1, col + 2)
                if 0 <= i < len(cells) and 0 <= j < len(cells[0]) and (i != row or j != col)
            )

            # Apply Game of Life rules to determine the new status of the cell
            if cell.status:
                new_status = live_neighbors in [2, 3]
            else:
                new_status = live_neighbors == 3

            new_row.append(Cell(col, row, new_status))  # Create a new cell with the updated status
        new_cells.append(new_row)

    return new_cells  # Return the new grid of cells

class MouseClickExample:
    def __init__(self, master):
        # Constructor for the MouseClickExample class
        self.master = master
        self.master.title("Life")  # Set the title of the window

        # Initialize a 10x10 grid of cells with all cells initially dead
        self.cells = [[Cell(x, y, False) for x in range(10)] for y in range(10)]

        # Create a canvas for displaying the cells
        self.canvas = tk.Canvas(master, width=300, height=300, bg='white')
        self.canvas.pack()

        # Initialize the canvas with the initial state of the cells
        self.update_canvas()

        # Bind the left mouse button click event to the callback function
        self.canvas.bind('<Button-1>', self.on_mouse_click)

    def on_mouse_click(self, event):
        # Event handler for mouse click
        x = event.x
        y = event.y
        print(f"Mouse clicked at ({x}, {y})")

        # Determine the grid coordinates based on the mouse click position
        flooredX = math.floor(x / 30)
        flooredY = math.floor(y / 30)

        # Toggle the status of the clicked cell
        for row in self.cells:
            for c in row:
                if c.col == flooredX and c.row == flooredY:
                    c.status = not c.status

        # Update the canvas to reflect the new state of the cells
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
