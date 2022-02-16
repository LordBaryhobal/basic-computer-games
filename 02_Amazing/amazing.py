#!/usr/bin/python3
# -*- coding: utf-8 -*-
import curses, random
import numpy as np

def init(stdscr):
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

def end(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()


def generate_maze(width=20,height=10):
    maze = np.ones([2*height+1, 2*width+1])

    x,y = random.randint(0,width-1)*2+1, random.randint(0,height-1)*2+1
    path = [(x,y)]
    offsets = [(-1,0),(0,-1),(1,0),(0,1)]

    while True:
        maze[y,x] = 0

        possible = []

        for i in range(4):
            x2, y2 = x+offsets[i][0]*2, y+offsets[i][1]*2
            if (0 <= x2 < maze.shape[1]) and (0 <= y2 < maze.shape[0]):
                if maze[y2, x2] == 1:
                    possible.append(i)

        if len(possible) == 0:
            if len(path) == 0:
                break

            x, y = path.pop()

        else:
            path.append((x,y))
            dx, dy = offsets[random.choice(possible)]
            x += dx
            y += dy
            maze[y, x] = 0
            x += dx
            y += dy

    maze[0, random.randint(0,width-1)*2+1] = 0
    maze[maze.shape[0]-1, random.randint(0,width-1)*2+1] = 0

    maze2 = np.zeros(maze.shape)

    for y in range(maze.shape[0]):
        for x in range(maze.shape[1]):
            if maze[y,x] == 1:
                for i in range(4):
                    x2, y2 = x+offsets[i][0], y+offsets[i][1]
                    if (0 <= x2 < maze.shape[1]) and (0 <= y2 < maze.shape[0]):
                        if maze[y2, x2] == 1:
                            maze2[y,x] += 1<<i

    return maze2

def draw(maze):
    # L U R D
    # 1 2 4 8
    chars = " ╴╵┘╶─└┴╷┐│┤┌┬├┼"
    s = ""

    for y in range(maze.shape[0]):
        for x in range(maze.shape[1]):
            #s += " #"[int(maze[y,x])]
            s += chars[int(maze[y,x])]
        s += "\n"

    print(s)

if __name__ == '__main__':
    #stdscr = curses.initscr()
    #init(stdscr)

    maze = generate_maze()

    while True:
        draw(maze)
        break

    #end(stdscr)
