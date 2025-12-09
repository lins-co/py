# Source Generated with Decompyle++
# File: firmware_upda.pyc (Python 3.11)

import threading
import flet
from flet import *
from src.firmware_update.boot_loader import BMSUpdater
import serial

class Firmware_upda:

    def __init__(self = None, page = None, p_app = None):
        pass
    # WARNING: Decompyle incomplete


    def check_running_threads(self):
        '''Check and print all currently running threads'''
        print('\n=== Running Threads ===')
        print(f'''Total active threads: {threading.active_count()}''')
        print()
        print('start thread value')
        self.stop_event.set()
        print('self ser', self.ser)
    # WARNING: Decompyle incomplete


    def close_dlg(self, e):
        self.stop_event.clear()
        print('Stop event cleared - threads can run now')
        print('stop event value', self.stop_event.is_set())
        self.p_app.start_threads()


    def thread_check(self, e):
        print('in thread')
        thread_count = self.check_running_threads()
        print('thread count', thread_count)
        return None
    # WARNING: Decompyle incomplete


    def pick_files_result(self = None, e = None):
        if e.files:
            self.file_path = e.files[0].path
            print('file path', self.file_path)
            return None


    def firmware_upda(self):
        return Column([
            Container(height = 100),
            self.b1,
            self.b2,
            self.b3])
