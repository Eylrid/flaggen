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
        self.draw_flag(self.flag, (0, 0, self.canvas_width, self.canvas_height))

    def draw_flag(self, flag, coords):
        x0, y0, x1, y1 = coords
        xmid = (x0+x1)/2
        ymid = (y0+y1)/2

        if x0 >= x1 or y0 >= y1:
            #flag either too small or inverted, don't draw
            return

        #draw background
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=flag.bg)        

        if flag.mode == 'cross':
            #draw cross
            ##vertical
            vx0 = xmid - (x1-x0)/16
            vy0 = y0
            vx1 = xmid + (x1-x0)/16
            vy1 = y1
            self.canvas.create_rectangle(vx0, vy0, vx1, vy1, fill=flag.cross,
                                         outline=flag.cross)

            ##horizontal
            hx0 = x0
            hy0 = ymid - (y1-y0)/8
            hx1 = x1
            hy1 = ymid + (y1-y0)/8
            self.canvas.create_rectangle(hx0, hy0, hx1, hy1, fill=flag.cross,
                                         outline=flag.cross)
        elif flag.mode == 'quaters':
            #draw quaterpanels
            panel_coords = [(x0, y0, xmid, ymid), (xmid, ymid, x1, y1),
                            (x0, ymid, xmid, y1), (xmid, y0, x1, ymid)]

            for panel, pcoords in zip(flag.quaterpanels, panel_coords):
                self.draw_flag(panel, pcoords)
        elif flag.mode == 'canton':
            self.draw_flag(flag.canton, (x0, y0, xmid, ymid))

