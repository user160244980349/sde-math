from ui.charts.visuals.color import Color


class Line:
    count = 0

    def __init__(self, name, t, fn, mx=None, dx=None):
        self.name = name
        self.t = t
        self.fn = fn
        self.mx = mx
        self.dx = dx
        self.line_fn = None
        self.line_mx = None
        self.line_dx = None
        self.visible = True
        self.color = Color()

        self.uid = Line.count
        Line.count += 1
