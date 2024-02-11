#!/usr/bin/env python3

from graphics import Window, Point
from cell import Cell
from maze import Maze

def test_draw(passed_window):
    win=passed_window
    ## Testing stuff
    l1=Line(Point(10,10), Point(100,300))
    l2=Line(Point(10,300), Point(300,10))
    win.draw_line(l1, "orange")
    win.draw_line(l2, "blue")

    c1=Cell(Point(100, 100), Point(200, 200), win)
    c1.has_left_wall=True
    c1.has_bottom_wall=True
    c1.has_top_wall=True
    c1.has_right_wall=True
    c1.color="green"
    c1.draw(Point(100, 100), Point(200, 200))

    c2=Cell(Point(50, 50), Point(80, 80), win)
    c2.has_left_wall=True
    c2.has_right_wall=True
    c2.color="black"
    c2.draw(Point(50, 50), Point(80, 80))

    c1.draw_move(c2,True)

def main():
    win=Window(800,600)
    #test_draw(win)

    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()

main()
