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
        if x0 >= x1 or y0 >= y1:
            #flag either too small or inverted, don't draw
            return

        def translate_point(x, y):
            # Translate a point from 0 to 1 coords on the flag to canvas coords
            width = x1-x0
            height = y1-y0

            xout = x*width + x0
            yout = y*height + y0
            return xout, yout

        def translate_coords(x0, y0, x1, y1):
            # Translate coords from 0 to 1 coords on the flag to canvas coords
            x0out, y0out = translate_point(x0, y0)
            x1out, y1out = translate_point(x1, y1)
            return x0out, y0out, x1out, y1out

        #draw background
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=flag.bg)        

        def draw_disc(hole=None):
            xradius = 1./6.
            yradius = 1./3.
            rawdx0, rawdy0 = 0.5-xradius, 0.5-yradius
            rawdx1, rawdy1 = 0.5+xradius, 0.5+yradius
            dx0, dy0 = translate_point(rawdx0, rawdy0)
            dx1, dy1 = translate_point(rawdx1, rawdy1)
            if flag.symbol_color == flag.bg:
                if flag.bg == 'black' or flag.bg == '#000000':
                    outline = 'white'
                else:
                    outline = 'black'
            else:
                outline = flag.bg

            self.canvas.create_oval(dx0, dy0, dx1, dy1,
                                    fill=flag.symbol_color,
                                    outline=outline)

            if hole:
                hx0, hy0 = translate_point(rawdx0 + xradius*hole[0],
                                           rawdy0 + yradius*hole[1])
                hx1, hy1 = translate_point(rawdx1 - xradius*hole[2],
                                           rawdy1 - yradius*hole[3])
                self.canvas.create_oval(hx0, hy0, hx1, hy1,
                                        fill=flag.bg,
                                        outline=outline)

        if flag.mode == 'cross':
            #draw cross
            ##vertical
            vx0, vy0 = translate_point(7./16., 0)
            vx1, vy1 = translate_point(9./16., 1)
            self.canvas.create_rectangle(vx0, vy0, vx1, vy1, fill=flag.cross,
                                         outline=flag.cross)

            ##horizontal
            hx0, hy0 = translate_point(0, 3./8.)
            hx1, hy1 = translate_point(1, 5./8.)
            self.canvas.create_rectangle(hx0, hy0, hx1, hy1, fill=flag.cross,
                                         outline=flag.cross)
        elif flag.mode == 'quarters':
            #draw quarterpanels
            panel_coords = [translate_coords(0, 0, 0.5, 0.5),
                            translate_coords(0.5, 0.5, 1, 1),
                            translate_coords(0, 0.5, 0.5, 1),
                            translate_coords(0.5, 0, 1, 0.5)]

            for panel, pcoords in zip(flag.quarterpanels, panel_coords):
                self.draw_flag(panel, pcoords)
        elif flag.mode == 'canton':
            self.draw_flag(flag.canton, translate_coords(0, 0, 0.5, 0.5))
        elif flag.mode == 'symbol':
            if flag.symbol == 'disc':
                draw_disc()
            elif flag.symbol == 'crescent':
                draw_disc(hole=(0.5,0.25,0,0.25))
            elif flag.symbol == 'ring':
                draw_disc(hole=(0.25,0.25,0.25,0.25))


class Demo(Tkinter.Frame):
    def __init__(self, *args, **kwargs):
        Tkinter.Frame.__init__(self, *args, **kwargs)
        self.newbutton = Tkinter.Button(self, text='New', command=self.new)
        self.newbutton.grid(row=1, column=0)

        self.flagframe = None

    def new(self):
        if self.flagframe: self.flagframe.destroy()
        self.flag = flaggen.Flag()
        self.flagframe = FlagFrame(self, self.flag)
        self.flagframe.grid(row=0, column=0)


def demo():
    rt = Tkinter.Tk()
    demo = Demo(rt)
    demo.pack()
    rt.mainloop()

if __name__ == '__main__':
    demo()
