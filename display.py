import Tkinter
import flaggen

class FlagFrame(Tkinter.Frame):
    def __init__(self, master, flag, *args, **kwargs):
        Tkinter.Frame.__init__(self, master, *args, **kwargs)

        self.flag = flag

        self.canvas_height = 250
        self.canvas_width = 500

        self.canvas = Tkinter.Canvas(self, height=self.canvas_height,
                                     width=self.canvas_width)
        self.canvas.grid(row=0, column=0)

        self._draw()

    def _draw(self):
        self.canvas.create_rectangle(0, 0, self.canvas_width,
                                     self.canvas_height, fill=self.flag.bg)

