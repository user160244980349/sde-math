import sys
import traceback

from PyQt5.QtCore import QRunnable, pyqtSlot, pyqtSignal, QObject


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    """
    Worker thread. Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
    source: https://www.learnpyqt.com/tutorials/multithreading-pyqt-applications-qthreadpool/

    Example:

    worker = Worker(self.sl)
    worker.signals.finished.connect(self.stop)

    self.stack4.spin()
    QThreadPool.globalInstance().start(worker)

    fn: function
        The function callback to run on this worker thread. Supplied args and
        kwargs will be passed through to the runner.
    args: iterable
        Arguments to pass to the callback function
    kwargs:
        Keywords to pass to the callback function

    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    """

    def __init__(self, fn, *args, **kwargs):
        super(QRunnable, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.custom_signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        """
        Initialise the runner function with passed args, kwargs.
        """

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.custom_signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.custom_signals.result.emit(result)  # Return the result of the processing
        finally:
            self.custom_signals.finished.emit()  # Done
