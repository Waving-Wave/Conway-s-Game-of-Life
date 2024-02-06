import tkinter as tk
import math

class Cell:
    def __init__(self, col, row, status):
        self.col = col
        self.row = row
        self.status = status

    def get_neighbors_status(self, grid):
        neighbors = []

        # Define relative positions of immediate neighbors
        neighbor_positions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for dx, dy in neighbor_positions:
            neighbor_col, neighbor_row = self.col + dx, self.row + dy

            # Check if the neighbor is within the grid boundaries
            if 0 <= neighbor_col < len(grid[0]) and 0 <= neighbor_row < len(grid):
                neighbor = grid[neighbor_row][neighbor_col]
                neighbors.append(neighbor.status)

        return neighbors

# Create a 10x10 grid of cells
cells = [[Cell(x, y, False) for x in range(10)] for y in range(10)]

# Example usage to get neighbors' statuses for cell at position (3, 4)
target_cell = cells[4][3]
neighbors_statuses = target_cell.get_neighbors_status(cells)

print(neighbors_statuses)


class MouseClickExample:
    def __init__(self, master):
        self.master = master
        self.master.title("Mouse Click Example")

        self.canvas = tk.Canvas(master, width=400, height=300, bg='white')
        self.canvas.pack()

        # Bind the left mouse button click event to the callback function
        self.canvas.bind('<Button-1>', self.on_mouse_click)

        for z in cells:
            self.canvas.create_rectangle(z.col * 30, z.row * 30 ,z.col * 30 + 30,z.row * 30 + 30,outline ="black",fill ="white",width = 2)

    def on_mouse_click(self, event):
        # Event handler for mouse click
        x = event.x
        y = event.y
        print(f"Mouse clicked at ({x}, {y})")
        self.canvas.delete("all")

        # You can perform additional actions here based on the mouse click
        flooredX = math.floor(x/30)
        flooredY = math.floor(y/30)
        for c in cells: 
            if (c.col == flooredX) and (c.row == flooredY):
                c.status = not c.status
            if c.status:
                self.canvas.create_rectangle(c.col * 30, c.row * 30 ,c.col * 30 + 30,c.row * 30 + 30,outline ="black",fill ="black",width = 2)
            else:
                self.canvas.create_rectangle(c.col * 30, c.row * 30 ,c.col * 30 + 30,c.row * 30 + 30,outline ="black",fill ="white",width = 2)
        


root = tk.Tk()
mouse_click_example = MouseClickExample(root)
root.mainloop()







