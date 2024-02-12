from graphics import Line, Point, Window
from cell import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
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
        x2_mod=x_mod+self.cell_size_x
        y2_mod=y_mod+self.cell_size_y
        p1=Point(x_mod,y_mod)
        p2=Point(x2_mod,y2_mod)
        self._cells[i][j].has_right_wall=True
        self._cells[i][j].has_bottom_wall=True

        print(f"Drawing cell {i} {j}")
        self._cells[i][j].draw(p1, p2)

        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(.005)

