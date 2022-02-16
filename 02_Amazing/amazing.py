#!/usr/bin/python3
# -*- coding: utf-8 -*-
import curses
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


def generate_maze(width=20,height=20):
    maze = np.ones([2*height+1, 2*width+1])



    return maze

def draw(maze):

if __name__ == '__main__':
    stdscr = curses.initscr()
    init(stdscr)

    maze = generate_maze()

    while True:
        draw(maze)

    end(stdscr)
