import sys
import atexit

_log = None

class _Logger:
    def __init__(self, file_path):
        print("Logger disabled")
    
    def __del__(self):
        print("Logger disabled")

    class _LoggerStdout:
        def __init__(self, file_in):
            print("Logger disabled")
        
        def __del__(self):
            print("Logger disabled")
        
        def write(self, data):
            print("Logger disabled")
        
        def flush(self):
            print("Logger disabled")

    class _LoggerStderr:
        def __init__(self, file_in):
            print("Logger disabled")
        
        def __del__(self):
            print("Logger disabled")
        
        def write(self, data):
            print("Logger disabled")
        
        def flush(self):
            print("Logger disabled")

def start(file_path):
    print("Logger disabled")

def stop():
    print("Logger disabled")
