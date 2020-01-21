from node import Node
from collections import deque
import math


class Graph:
    def __init__(self, sx, sy, dx, dy):
        self.nodes = [[None for i in range(50)] for j in range(50)]
        self.q = deque([])
        self.close = []
        self.path = [[None for i in range(50)] for j in range(50)]
        self.sx = sx
        self.sy = sy
        self.dx = dx
        self.dy = dy
        self.obstacles = [[False for i in range(50)] for j in range(50)]

    def insertEdges(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                node = arr[i][j]
                if i-1 >= 0:
                    if arr[i-1][j].wall == False:
                        node.edges[0] = arr[i-1][j]
                if i+1 <= len(arr)-1:
                    if arr[i+1][j].wall == False:
                        node.edges[1] = arr[i+1][j]
                if j-1 >= 0:
                    if arr[i][j-1].wall == False:
                        node.edges[2] = arr[i][j-1]
                if j+1 <= len(arr)-1:
                    if arr[i][j+1].wall == False:
                        node.edges[3] = arr[i][j+1]
                # for diagonal movement
                # if j-1 >= 0 and i-1 >= 0:
                #     if arr[i-1][j-1].wall == False:
                #         node.edges[4] = arr[i-1][j-1]
                # if j-1 >= 0 and i+1 <= len(arr)-1:
                #     if arr[i+1][j-1].wall == False:
                #         node.edges[5] = arr[i+1][j-1]
                # if j+1 <= len(arr)-1 and i-1 >= 0:
                #     if arr[i-1][j+1].wall == False:
                #         node.edges[6] = arr[i-1][j+1]
                # if j+1 <= len(arr)-1 and i+1 <= len(arr)-1:
                #     if arr[i+1][j+1].wall == False:
                #         node.edges[7] = arr[i+1][j+1]
   
    def draw(self):
        for i in range(len(self.obstacles)):
            for j in range(len(self.obstacles)):
                if mouseX//10 > i and mouseX//10 < i+10:
                    if mouseY//10 > j and mouseY//10 < j+10:
                        self.obstacles[mouseX//10][mouseY//10] = True


    def displayObs(self):
        for i in range(len(self.obstacles)):
            for j in range(len(self.obstacles)):
                if i == self.sx and j == self.sy or i == self.dx and j == self.dy:
                    stroke(0)
                    fill(255, 0, 0)
                    rect(10*i, 10*j, 10, 10)
                else:
                    stroke(0)
                    if self.obstacles[i][j]:
                        fill(0)
                        rect(10*i, 10*j, 10, 10)
                    else:
                        fill(255)
                        rect(10*i, 10*j, 10, 10)
                        

    def createGraph(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                self.nodes[i][j] = Node(i, j)

                if self.obstacles[i][j] == True:
                    self.nodes[i][j].wall = True
        self.insertEdges(self.nodes)

    # def displayGraph(self):
    #     for i in range(len(self.nodes)):
    #         for j in range(len(self.nodes)):
    #             # if self.nodes[i][j].wall:
    #             #     self.nodes[i][j].findColour(48, 45, 46)
    #             # else:
    #             self.nodes[i][j].findColour(255, 255, 255)

    def helperBFS(self):
        if len(self.q) == 0:
            self.nodes[self.sx][self.sy].distance = 0
            self.q.append(self.nodes[self.sx][self.sy])
            self.path[self.sx][self.sy] = [self.nodes[self.sx][self.sy]]

    def BFSsearch(self):
        dest = self.nodes[self.dx][self.dy]
        if len(self.q) > 0:
            rm = self.q.popleft()
            self.close.append(rm)
            for node in rm.edges:
                if node:
                    
                    if node.distance == None:
                        node.distance = rm.distance + 1
                        if self.path[rm.i][rm.j]:
                            self.path[node.i][node.j] = [node]
                            self.path[node.i][node.j].extend(
                                self.path[rm.i][rm.j])

                        self.q.append(node)
                        if node is dest:
                            noLoop()
                            # node.findColour(105, 105, 105)
                            return self.path[self.dx][self.dy]

    def show(self):
        for i in range(len(self.q)):
            self.q[i].findColour(113, 216, 80)
        for j in range(len(self.close)):
            self.close[j].findColour(159, 234, 239)
            # if j == 0:
            #     self.close[j].findColour(105, 105, 105)
