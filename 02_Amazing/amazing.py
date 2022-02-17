#!/usr/bin/python3
# -*- coding: utf-8 -*-
import curses, random, time
import numpy as np

def init(stdscr):
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)

def end(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    stdscr.nodelay(False)
    curses.echo()
    curses.endwin()


def generate_maze(width=20,height=20):
    maze = np.ones([2*height+1, 3*width+1])

    x,y = random.randint(0,width-1)*3+1, random.randint(0,height-1)*2+1
    path = [(x,y)]
    offsets = [(-1,0),(0,-1),(1,0),(0,1)]

    while True:
        maze[y,x] = 0
        maze[y,x+1] = 0

        possible = []

        for i in range(4):
            x2, y2 = x+offsets[i][0]*3, y+offsets[i][1]*2
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

            if abs(dy) > 0:
                maze[y+dy, x+dx] = 0
                maze[y+dy, x+dx+1] = 0
                #maze[y+2*dy, x+2*dx] = 0
                #maze[y+2*dy, x+2*dx+1] = 0
                x += dx
                y += 2*dy

            else:
                maze[y+dy, x+dx] = 0
                maze[y+dy, x+2*dx] = 0
                #maze[y+dy, x+2*dx] = 0
                #maze[y+2*dy, x+2*dx+1] = 0
                x += 3*dx
                y += 2*dy
            """maze[y, x] = 0
            x += dx
            y += dy
            maze[y, x] = 0
            x += dx
            y += dy"""

    s, e = random.randint(0,width-1)*3+1, random.randint(0,width-1)*3+1
    maze[0, s:s+2] = 0
    maze[maze.shape[0]-1, e:e+2] = 0

    #maze = np.kron(maze, np.ones((1,2))) # Scale horizontally by 2
    maze2 = np.zeros(maze.shape)

    for y in range(maze.shape[0]):
        for x in range(maze.shape[1]):
            if maze[y,x] == 1:
                for i in range(4):
                    x2, y2 = x+offsets[i][0], y+offsets[i][1]
                    if (0 <= x2 < maze.shape[1]) and (0 <= y2 < maze.shape[0]):
                        if maze[y2, x2] == 1:
                            maze2[y,x] += 1<<i

    return (maze,maze2,s,e)

def draw(maze, pos, styled=False, scr=None, start=0):
    # L U R D
    # 1 2 4 8
    chars = " ╴╵┘╶─└┴╷┐│┤┌┬├┼"
    s = ""

    if not scr is None:
        stdscr.addstr(0, maze.shape[1]//2-3, "Amazing", curses.A_UNDERLINE)

    for y in range(maze.shape[0]):
        for x in range(maze.shape[1]):
            if x == pos[0] and y == pos[1]:
                s += "o"

            else:
                if styled:
                    s += chars[int(maze[y,x])]
                else:
                    s += " #"[int(maze[y,x])]

            if not scr is None:
                scr.addstr(y+1, x, s[-1])
        s += "\n"

    if scr is None:
        print(s)
    else:
        elapsed = int(time.time()-start)
        stdscr.addstr(maze.shape[0]+1, 0, f"Time: {elapsed}", curses.A_BOLD)

def move(maze, pos, offset):
    x, y = pos
    x2, y2 = x+offset[0], y+offset[1]

    if 0 <= x2 < maze.shape[1] and 0 <= y2 < maze.shape[0]:
        if maze[y2, x2] == 0:
            pos[0] = x2
            pos[1] = y2
            return True

    return False

if __name__ == '__main__':
    stdscr = curses.initscr()
    init(stdscr)

    maze, maze2, s, e = generate_maze(10,10)
    pos = [s,0]
    start = time.time()

    while True:
        stdscr.clear()
        draw(maze2, pos, styled=True, scr=stdscr, start=start)
        stdscr.refresh()
        c = stdscr.getch()
        moved = False

        if c == curses.KEY_HOME:
            break

        elif c == curses.KEY_UP:
            moved = move(maze2, pos, (0,-1))

        elif c == curses.KEY_DOWN:
            moved = move(maze2, pos, (0,1))

        elif c == curses.KEY_LEFT:
            moved = move(maze2, pos, (-1,0))

        elif c == curses.KEY_RIGHT:
            moved = move(maze2, pos, (1,0))

        if pos[1] == maze2.shape[0]-1:
            stdscr.addstr("\nWell done !\n")
            stdscr.addstr(f"Maze completed in {int(time.time()-start)} seconds\n")
            stdscr.refresh()

            time.sleep(1)
            stdscr.addstr("Press a key to quit")
            stdscr.refresh()
            stdscr.getch()
            stdscr.nodelay(False)
            stdscr.getch()
            break

        if not moved:
            time.sleep(0.1)

    end(stdscr)
