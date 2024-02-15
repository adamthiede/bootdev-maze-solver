from graphics import Line, Point, Window
from cell import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells=[]
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win=win
        self.seed=random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()


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

        print(f"Drawing cell {i} {j}")
        self._cells[i][j].draw(p1, p2)

        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(.005)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
        self._draw_cell(0, 0)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited=True
        while True:
            to_visit=[]
            current_visitable=len(to_visit)
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i-1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i+1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j-1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j+1))

            if len(to_visit)==0:
                self._draw_cell(i,j)
                return

            random_pick=random.randrange(len(to_visit))
            pick=to_visit[random_pick]

            if pick[0]==i+1:
                self._cells[i][j].has_right_wall=False
                self._cells[i+1][j].has_left_wall=False
            elif pick[0]==i-1:
                self._cells[i-1][j].has_right_wall=False
                self._cells[i][j].has_left_wall=False
            elif pick[1]==j+1:
                self._cells[i][j].has_bottom_wall=False
                self._cells[i][j+1].has_top_wall=False
            elif pick[1]==j-1:
                self._cells[i][j].has_top_wall=False
                self._cells[i][j-1].has_bottom_wall=False

            self._break_walls_r(pick[0], pick[1])
 
    def _reset_cells_visited(self):
        for i in cell_size_x:
            for j in cell_size_y:
                self._cells[i][j].visited=False

