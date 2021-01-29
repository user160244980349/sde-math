from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class ToolBar(NavigationToolbar):

    def __init__(self, figure_canvas, parent=None):
        self.toolitems = (
            # (None, None, None, None),
            # ('Home', None, 'home', 'home'),
            # ('Back', None, 'back', 'back'),
            # ('Forward', None, 'forward', 'forward'),
            # (None, None, None, None),
            # ('Pan', None, 'move', 'pan'),
            # ('Zoom', None, 'zoom_to_rect', 'zoom'),
            # (None, None, None, None),
            # ('Save', None, 'filesave', 'save_figure'),
            ('Home', 'Reset original view', 'home', 'home'),
            ('Back', 'Back to previous view', 'back', 'back'),
            ('Forward', 'Forward to next view', 'forward', 'forward'),
            (None, None, None, None),
            ('Pan',
             'Left button pans, Right button zooms\n'
             'x/y fixes axis, CTRL fixes aspect',
             'move', 'pan'),
            ('Zoom', 'Zoom to rectangle\nx/y fixes axis, CTRL fixes aspect',
             'zoom_to_rect', 'zoom'),
            ('Subplots', 'Configure subplots', 'subplots', 'configure_subplots'),
            (None, None, None, None),
            ('Save', 'Save the figure', 'filesave', 'save_figure'),
        )

        NavigationToolbar.__init__(self, figure_canvas, parent=parent)

        self.setStyleSheet("QToolTip { background: white; }")

    def _init_toolbar(self):
        pass
