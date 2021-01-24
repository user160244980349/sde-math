import logging


class LogHandler(logging.Handler):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.setFormatter(logging.Formatter("%(asctime)s - %(message)s", "%H:%M:%S"))
        # self.setFormatter(logging.Formatter('%(name)s: %(message)s'))

    def handle(self, record):
        self.callback(self.format(record))
