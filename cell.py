from graphics import Line, Point, Window

class Cell:
    def __init__(self, p1: Point, p2: Point, window: Window):
        self._x1=p1.x
        self._y1=p1.y
        self._x2=p2.x
        self._y2=p2.y
        self._win=window
        self.has_left_wall = False
        self.has_right_wall = False
        self.has_top_wall = False
        self.has_bottom_wall = False
        self.color="black"

    def draw(self, top_left: Point, bottom_right: Point):
        self._x1=top_left.x
        self._y1=top_left.y
        self._x2=bottom_right.x
        self._y2=bottom_right.y
        if self.has_left_wall:
            left_wall=Line(Point(top_left.x, top_left.y), Point(top_left.x, bottom_right.y))
            self._win.draw_line(left_wall, self.color)
        if self.has_right_wall:
            right_wall=Line(Point(bottom_right.x, top_left.y), Point(bottom_right.x, bottom_right.y))
            self._win.draw_line(right_wall, self.color)
        if self.has_top_wall:
            top_wall=Line(Point(top_left.x, top_left.y), Point(bottom_right.x, top_left.y))
            self._win.draw_line(top_wall, self.color)
        if self.has_bottom_wall:
            bottom_wall=Line(Point(top_left.x, bottom_right.y), Point(bottom_right.x, bottom_right.y))
            self._win.draw_line(bottom_wall, self.color)

    def draw_move(self, to_cell, undo=False):
        p1=Point(self._x1+((self._x2-self._x1)/2), self._y1+((self._y2-self._y1)/2))

        p2=Point(to_cell._x1+((to_cell._x2-to_cell._x1)//2), to_cell._y1+((to_cell._y2-to_cell._y1)//2))

        if undo:
            self.color="gray"
        else:
            self.color="red"
        nl=Line(p1,p2)
        self._win.draw_line(nl,self.color)

