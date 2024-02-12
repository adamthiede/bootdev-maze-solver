from tkinter import Tk, BOTH, Canvas, Button
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
        #self.__root.title="aMAZEing"
        self.__canvas=Canvas(self.__root, bg="darkgray", height=height, width=width)
        self.__canvas.pack()
        Button(self.__root, text="Quit", command=self.close).pack()
        self.running=False
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    def wait_for_close(self):
        self.running=True
        while self.running:
            self.redraw()
            #sleep(.25)
    def close(self):
        self.running=False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)

