from graphics import Line, Point, Window
from cell import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._cells=[]
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win=win
        self._create_cells()

    def _create_cells(self):
        for i in range(0, self.num_cols):
            temp_cells=[]
            for j in range(0,self.num_rows):
                tl=Point(self.x1+(j*self.cell_size_x), self.y1+(i*self.cell_size_y))
                br=Point(self.x1+((j+1)*self.cell_size_x), self.y1+((i+1)*self.cell_size_y))
                my_cell=Cell(tl, br, self.win)
                temp_cells.append(my_cell)
            self._cells.append(temp_cells)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x_mod=self.x1+(i*self.cell_size_x)
        y_mod=self.y1+(j*self.cell_size_y)
        x2_mod=self.x1+((i+1)*self.cell_size_x)
        y2_mod=self.y1+((j+1)*self.cell_size_y)

        p1=Point(self.x1+x2_mod,self.y1+y2_mod)
        p2=Point(self.x1+x2_mod,self.y1+y2_mod)

        c1=Cell(p1, p2, self.win)
        c1.draw(p1, p2)

        self._cells[i][j].draw(p1, p2)

        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(.05)

