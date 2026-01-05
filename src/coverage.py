import sys
import fuzzer

class Coverage:
    def __init__(self):
        self._trace = set()

    def trace(self, frame, event, arg):
        if event == 'line':
            self._trace.add((frame.f_code.co_filename, frame.f_lineno))
        return self.trace

    def __enter__(self):
        sys.settrace(self.trace)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        sys.settrace(None)

with Coverage() as cov:
    try:
     fuzzer.program("bug")
    except ValueError:
        print("Crash Caught!")

print(cov._trace)