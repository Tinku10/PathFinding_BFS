import time
class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        # linking a node to its adjecent nodes using array indexes
        self.edges = [None for k in range(4)]
        self.distance = None
        self.wall = False


    # def box(self):
    #     h = 20
    #     w = 20
    #     stroke(0)
    #     rect(self.i*20, self.j*20, w, h)

    def findColour(self, r, g, b):
        h = 10
        w = 10
        fill(r, g, b)
        stroke(0)
        rect((self.i)*10, (self.j)*10, w, h)
