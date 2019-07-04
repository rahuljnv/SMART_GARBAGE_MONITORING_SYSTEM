try:
    import tkinter as tk  # assume Python 3
except ImportError:
    import Tkinter as tk  # nope, Python 2

class Level:
    def __init__(self, name, height, width):
        self.name = name
        self.height = height
        self.width = width
        self.tiles = makeTiles(height, width)

    class Tile:
        def __init__(self, x, y, type, color, isOccupied, enemy):
            self.x = x
            self.y = y
            self.type = type
            self.color = color
            self.isOccupied = isOccupied
            self.enemy = enemy

def makeLevel(name, height, width):
    level = Level(name, height, width)
    return level

def makeTiles(height, width):
    tiles = [[Level.Tile(x, y, "Surface", "red", False, "None") for x in range(width)] for y in range(height)]
    return tiles

test1 = makeLevel("test", 10, 10)
for x in range(10):
    for y in range(10):
        if x % 2 == 0 and y % 2 == 0:
            test1.tiles[x][y].color = "black"
        elif x % 2 == 0:
            test1.tiles[x][y].color = "blue"
        elif y % 2 == 0:
            test1.tiles[x][y].color = "yellow"

colorMatrix = [[0 for x in range(10)] for y in range(10)]
for x in range(10):
    for y in range(10):
        colorMatrix[x][y] = test1.tiles[x][y].color

# print(colorMatrix)

width, height = 400, 400

root = tk.Tk()
root.title("colorMatrix")

frame = tk.Frame()
frame.pack()

canvas = tk.Canvas(frame, width=width, height=height)
rows, cols = len(colorMatrix), len(colorMatrix[0])

rect_width, rect_height = width // rows, height // cols
for y, row in enumerate(colorMatrix):
    for x, color in enumerate(row):
        x0, y0 = x * rect_width, y * rect_height
        x1, y1 = x0 + rect_width-1, y0 + rect_height-1
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
canvas.pack()

root.mainloop()