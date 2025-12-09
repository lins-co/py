# Source Generated with Decompyle++
# File: boot_loader.pyc (Python 3.11)

import threading
import serial
import logging
import time
import os
logger1 = logging.getLogger(__name__)
documents_folder = os.path.expanduser('~/Documents')
new_folder = os.path.join(documents_folder, 'MyLogs1')
os.makedirs(new_folder, exist_ok = True)
logger1 = logging.getLogger('logger1')
logger1.setLevel(logging.INFO)
log_file1 = os.path.join(new_folder, 'bootloader_log1.txt')
file_handler1 = logging.FileHandler(log_file1, mode = 'a')
file_handler1.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger1.addHandler(file_handler1)

class BMSUpdater:

    def __init__(self, ser, file_path, page, b1):
        self.page = page
        self.b1 = b1
        self.c = False
        self.ser = ser
        self.file_path = file_path
        self.read_thread = None
        self.ser = None
        self.data = ''
        self.cmd = False
        self.state = 0
        self.file_da = self.file_red()
        self.stop_requested = False
        self.l = int(len(self.file_da) / 64)
        self.p = 100 / self.l
        self.retry = 0
        self.retry_limit = 5
        self.data_event = threading.Event()
        self.state_handlers = {
            0: self.handle_state_0,
            1: self.handle_state_1,
            2: self.handle_state_2,
            3: self.handle_state_3,
            4: self.handle_state_4,
            5: self.handle_state_5 }


    def setup_serial(self):
        self.ser
    # WARNING: Decompyle incomplete


    def close_serial(self):
        if self.ser:
            self.ser.close()
            logger1.info('Serial connection closed')
            return None


    def read_data(self):
        pass
    # WARNING: Decompyle incomplete


    def send_command(self, command):
        self.ser.write(command)
        self.cmd = False
        logger1.info('Sent command: %s', command.decode().strip())
        return None
    # WARNING: Decompyle incomplete


    def reset(self):
        self.data = ''
        self.cmd = False
        self.state = 0
        self.stop_requested = False
        self.retry = 0
        self.file_da = self.file_red()
        self.l = int(len(self.file_da) / 64)
        self.p = 100 / self.l if self.l > 0 else 100
        self.ser = None
        self.read_thread = None
        self.data_event.clear()
        self.page.controls[4].value = ''
        self.page.update()


    def bms_update(self):
        self.reset()
        self.c = True
        self.b1.disabled = True
        self.page.update()
        if not self.ser:
            self.setup_serial()
    # WARNING: Decompyle incomplete


    def handle_state_0(self):
        if 'AT+DONE' in self.data:
            logger1.info('AT+DONE received for AT+BOOT=1')
            self.data = ''
            self.cmd = True
            self.state = 1
            logger1.info('Completed state 0, moving to state 1')
            self.handle_state_1()
            return None


    def handle_state_1(self):
        print('self.data in 1', self.data)
        if self.cmd:
            self.send_command(b'AT+BOOT=2\r\n')
            print('send at+boot=2')
            self.cmd = False
            logger1.info('Sent AT+BOOT=2')
            print('data', self.data)
            return None
        if None in self.data:
            print('got at+bmsinfo after sending at+boot=2', self.data)
            logger1.info('AT+BMSINFO received for AT+BOOT=2')
            self.data = ''
            self.cmd = True
            self.state = 2
            logger1.info('Completed state 1, moving to state 2')
            self.handle_state_2()
            return None


    def handle_state_2(self):
        print('self.data in 2', self.data)
        if self.cmd:
            s = str(len(self.file_da)) + ',' + str(self.crc_cal()) + ',' + str(32768) + '\r\n'
            full_cmd = b'AT+FileInfo=310,' + s.encode()
            self.send_command(full_cmd)
            self.cmd = False
            logger1.info('Sent AT+FileInfo')
            return None
        if None in self.data:
            logger1.info('AT+DONE received for AT+FileInfo')
            self.state = 3
            self.cmd = True
            logger1.info('Completed state 2, moving to state 3')
            self.data = 'AT+DONE'
            self.handle_state_3()
            return None


    def handle_state_3(self):
        st = 0
        i = 0
        self.send_command(b'AT+BOOT=3,64,')
        chunk = self.file_da[st:st + 64]
        self.ser.write(chunk)
        self.ser.write(bytes([
            170,
            85]))
        self.retry = 0
    # WARNING: Decompyle incomplete


    def handle_state_3_1(self):
        st = 0
        i = 0
        self.send_command(b'AT+BOOT=3,64,')
        chunk = self.file_da[st:st + 64]
        self.ser.write(chunk)
        self.ser.write(bytes([
            170,
            85]))
        logger1.info('Sent first data chunk of 64 bytes')
        st += 64
        self.cmd = True
        self.data = ''
        self.page.controls[4].value = str(int(self.p * (i + 1)))
        i += 1
        self.data_event.clear()
    # WARNING: Decompyle incomplete


    def handle_state_4(self):
        if 'AT+DONE' in self.data:
            print('got at+done after sending last data')
            self.send_command(b'AT+BOOT=4\r\n')
            self.ser.write(bytes([
                170,
                85]))
            logger1.info('Case 4: Sent AT+BOOT=4 and terminator')
            self.data_event.wait(0.3)
            self.state = 5
            self.data = ''
            self.cmd = True
            self.handle_state_5()
            return None


    def handle_state_5(self):
        pass
    # WARNING: Decompyle incomplete


    def crc_cal(self):
        crc = 0
        for byte in self.file_da:
            crc += byte
            logger1.info('CRC calculated: %d', crc)
            return crc


    def file_red(self):
        pass
    # WARNING: Decompyle incomplete
