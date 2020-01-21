from graph import Graph
from button import Button
from obstacle import Obstacle

sx = 10
sy = 10
dx = 30
dy = 20
g = Graph(sx, sy, dx, dy)
b = Button()
obs = Obstacle()


def setup():
    size(501, 550)
    # g.createGraph()
    # g.helperBFS()
    b.createButton()
    # creating graph nodes at every position of the array


def draw():
    background(255)
    # displaying the grid
    b.display()
    g.displayObs()

    if b.isBuiltPressed():
        g.createGraph()
        g.helperBFS()

    elif b.isPressed():
        path = g.BFSsearch()
        g.show()
        fill(255, 0, 0)
        rect(sx*10, sy*10, 10, 10)
        fill(255, 0, 0)
        rect(dx*10, dy*10, 10, 10)
        if path:
            for k in range(1, len(path)-1):
                path[k].findColour(131, 20, 242)


def mouseDragged():
    g.draw()





