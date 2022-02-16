#!/usr/bin/python3
# -*- coding: utf-8 -*-
import curses

def init(stdscr):
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

def end(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def draw(maze):

if __name__ == '__main__':
    stdscr = curses.initscr()
    init(stdscr)

    maze = generate_maze()

    while True:
        draw(maze)

    end(stdscr)
