import os

from PyQt5.QtCore import QSize
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QSizePolicy

from config import resources


class SVG(QSvgWidget):
    def __init__(self, name: str, scale_factor=1.):
        super(QSvgWidget, self).__init__()

        self.load(os.path.join(resources, name))

        self.scale_factor = scale_factor
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def sizeHint(self):
        size = self.renderer().defaultSize()
        return QSize(size.width() * self.scale_factor,
                     size.height() * self.scale_factor)
