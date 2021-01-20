class Line:
    count = 0

    def __init__(self, name, t, y):
        self.name = name
        self.t = t
        self.y = y
        self.line2d = None

        self.uid = Line.count
        Line.count += 1
