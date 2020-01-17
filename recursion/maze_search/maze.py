from turtle import Turtle, Screen
import turtle
from os import path
import os

"""
A visualization of the recursive algorithm to find the way out of a maze
"""

OBSTACLE = "+"
PART_OF_PATH = 'O'
TRIED = '.'
DEAD_END = '-'

class Maze:
    def __init__(self, fname: str):
        super().__init__()
        self.maze_li = []

        file = open(fname, "r")

        cols = 0
        rows = 0

        row = 0
        for line in file:
            row_li = []
            col = 0
            for ch in line[:-1]:
                row_li.append(ch)
                if ch == "S":
                    self.start_row = row
                    self.start_col = col
                col += 1
            rows +=1
            cols = len(row_li)
            row += 1
            self.maze_li.append(row_li)

        self.rows = rows
        self.cols = cols
        self.x_translate = - cols / 2
        self.y_translate = rows / 2

        self.t = Turtle(shape="turtle")
        self.wn = Screen()
        self.wn.setworldcoordinates(-(cols - 1) / 2 - .5, -(rows - 1) / 2 - .5, (cols - 1) / 2 + .5, (rows - 1) / 2 + .5)


    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rows):
            for x in range(self.cols):
                    if self.maze_li[y][x] == OBSTACLE:
                        self.draw_centered_box(x + self.x_translate, -y + self.y_translate, "orange")
        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
        self.wn.tracer(1)

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x-.5, y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def update_pos(self, row, col, val=None):
        if val: # Change the value of the position to TRIED
            self.maze_li[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None

        if color:
            self.drop_bread_crumb(color)

    def drop_bread_crumb(self, color):
        self.t.dot(10, color)
        
    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, - y + self.y_translate)

    def is_exit(self, row, col):
        """
        The grid is an empty grid on the edge / exit of the maze
        """
        return row == 0 or row == self.rows - 1 or col == 0 or col == self.cols - 1

    def __getitem__(self, idx):
        return self.maze_li[idx]


def search_from(maze: Maze, start_row: int, start_col: int):
    maze.update_pos(start_row, start_col)
    # Run into an obstacle, return false
    if maze[start_row][start_col] == OBSTACLE:
        return False
    
    # A square that has been explored
    if maze[start_row][start_col] == OBSTACLE or maze[start_row][start_col] == TRIED:
        return False

    # An outside edge not occupied by an obstacle
    if maze.is_exit(start_row, start_col):
        return True
    maze.update_pos(start_row, start_col, TRIED)

    # Try each direction in turn
    found = search_from(maze, start_row - 1, start_col) or \
            search_from(maze, start_row + 1, start_col) or \
            search_from(maze, start_row, start_col + 1) or \
            search_from(maze, start_row, start_col - 1)
    
    if found:
        maze.update_pos(start_row, start_col, PART_OF_PATH)
    else:
        maze.update_pos(start_row, start_col, DEAD_END)
    return found


dir_path = os.path.dirname(os.path.realpath(__file__))
fpath = path.join(dir_path, "maze2.txt")
maze = Maze(fpath)
maze.draw_maze()
maze.update_pos(maze.start_row, maze.start_col)
search_from(maze, maze.start_row, maze.start_col)

turtle.done() # keep the window open