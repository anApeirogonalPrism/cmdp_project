import traceback
import sys


class MathError(Exception):
    def myexcepthook(type, value, tb):
        msg = "".join(traceback.format_exception_only(type, value))
        print(msg)

    sys.excepthook = myexcepthook
