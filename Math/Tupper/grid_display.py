import Tkinter as tk

from tupper_helper import *

def grid_display(ROWS, COLS):
    
    # Create a grid of None to store the references to the tiles
    tiles = [[None for _ in range(COLS)] for _ in range(ROWS)]

    def callback(event):
        # Get rectangle diameters
        col_width = c.winfo_width()/COLS
        row_height = c.winfo_height()/ROWS
        # Calculate column and row number
        col = event.x//col_width
        row = event.y//row_height
        # If the tile is not filled, create a rectangle
        if not tiles[row][col]:
            tiles[row][col] = c.create_rectangle(col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height, fill="black")
        # If the tile is filled, delete the rectangle and clear the reference
        else:
            c.delete(tiles[row][col])
            tiles[row][col] = None

    # Create the window, a canvas and the mouse click event binding
    root = tk.Tk()
    c = tk.Canvas(root, width=500, height=500, borderwidth=5, background='white')
    c.pack()
    c.bind("<Button-1>", callback)

    root.mainloop() 

    bmp = []
    for i in range(len(tiles)):
        temp = []
        for j in range(len(tiles[i])):
            if tiles[i][j] == None:
                temp += [0]
            else:
                temp += [1]
        bmp += [temp]

    return bmp

print array_to_tupper(grid_display(23, 22))
