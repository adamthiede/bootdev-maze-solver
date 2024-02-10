from tkinter import Tk, BOTH, Canvas
from time import sleep

class Point:
    def __init__(self, x: int, y: int):
        self.x=x
        self.y=y

class Line:
    def __init__(self, a: Point, b: Point):
        self.point_a=a
        self.point_b=b
    def draw(self, canvas, fill_color: str):
        canvas.create_line(self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill=fill_color, width=2)

class Window:
    def __init__(self, width,height):
        self.width=width
        self.height=height
        self.__root=Tk()
        self.__root.title="aMAZEing"
        self.__canvas=Canvas(self.__root)
        self.__canvas.pack()
        self.running=False
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    def wait_for_close(self):
        self.running=True
        while self.running:
            self.redraw()
            sleep(.25)
    def close(self):
        self.running=False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)

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

def main():
    win=Window(800,600)
    l1=Line(Point(10,10), Point(300,300))
    l2=Line(Point(10,300), Point(300,10))
    win.draw_line(l1, "red")
    win.draw_line(l2, "blue")

    c1=Cell(Point(100, 100), Point(200, 200), win)
    c1.has_left_wall=True
    c1.has_bottom_wall=True
    c1.has_top_wall=True
    c1.has_right_wall=True
    c1.color="green"
    c1.draw(Point(100, 100), Point(200, 200))
    win.wait_for_close()

main()
