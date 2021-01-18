import logging


class LogHandler(logging.Handler):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(message)s'))

    def handle(self, record):
        self.callback(self.format(record))
