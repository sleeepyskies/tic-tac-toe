import tkinter as tk
from tkinter import ttk

class Renderer():
    """
    A class responsible for rendering the game. Uses tkinter package.
    """
    def __init__(self) -> None:
        self.root = tk.Tk()

        # set window size
        self.root.geometry("600x600")
        # set window title
        self.root.title("Tic-Tac-Toe")
        
        # create widget container
        # self.mainframe = tk.Frame(self.root, background="gray")
        # self.mainframe.pack(fill="both", expand=True)

        # create title
        # self.title = ttk.Label(self.mainframe, text="Tic-Tac-Toe", background="gray", font=("Arial", 30))
        # self.title.grid(row=0, column=0)

        # create canvas widget
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()

        # bind the click event
        self.canvas.bind("<Button-1>", self.handle_click)

        self.draw_grid()

        self.root.mainloop()

    def draw_grid(self):
        """
        Draws a 3x3 grid on the canvas.
        """
        # Dimensions for grid
        grid_size = 3
        cell_width = 600 // grid_size
        cell_height = 600 // grid_size

        # Draw vertical lines
        for i in range(1, grid_size):
            x = i * cell_width
            self.canvas.create_line(x, 0, x, 600, width=2)

        # Draw horizontal lines
        for i in range(1, grid_size):
            y = i * cell_height
            self.canvas.create_line(0, y, 600, y, width=2)

    def handle_click(self, event):
        """
        Handles the click event on the canvas.
        """
        # Get the mouse click coordinates
        x = event.x
        y = event.y

        print(f"Mouse clicked at ({x}, {y})")

        # Determine which cell was clicked
        row = y // 200
        col = x // 200
        print(f"Clicked cell: ({row}, {col})")

        # Implement logic for handling the click on a specific cell
        # For example, you might want to place a move here or update the game state