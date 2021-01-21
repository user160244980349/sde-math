from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class ToolBar(NavigationToolbar):

    def __init__(self, figure_canvas, parent=None):
        self.toolitems = (
            (None, None, None, None),
            ('Home', None, 'home', 'home'),
            ('Back', None, 'back', 'back'),
            ('Forward', None, 'forward', 'forward'),
            (None, None, None, None),
            ('Pan', None, 'move', 'pan'),
            ('Zoom', None, 'zoom_to_rect', 'zoom'),
            (None, None, None, None),
            ('Save', None, 'filesave', 'save_figure'),
        )

        NavigationToolbar.__init__(self, figure_canvas, parent=parent)

        self.setStyleSheet("QToolTip { background: white; }")

    def _init_toolbar(self):
        pass
