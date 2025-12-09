# Source Generated with Decompyle++
# File: log.pyc (Python 3.11)

import logging
import os
import csv
from logging.handlers import RotatingFileHandler
documents_folder = os.path.expanduser('~/Desktop')
emo_log_folder = os.path.join(documents_folder, 'Emo_log_Folder')
os.makedirs(emo_log_folder, exist_ok = True)
log_file_path = os.path.join(emo_log_folder, 'emo_app.log')
handler = RotatingFileHandler(log_file_path, maxBytes = 10485760, backupCount = 10, encoding = 'utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)
csv_file_path = os.path.join(emo_log_folder, 'Error_index.csv')
Error_index = [
    [
        'Error Index',
        'Error Name'],
    [
        '0',
        'SD Card Error'],
    [
        '1',
        'AFE Error'],
    [
        '2',
        'Mosfet Error'],
    [
        '3',
        'DT Warning'],
    [
        '4',
        'Open Wire Error'],
    [
        '5',
        'Short Circuit'],
    [
        '6',
        'Over Current'],
    [
        '7',
        'Thermal Runaway'],
    [
        '8',
        'Over temperature'],
    [
        '9',
        'Cell Over Volt'],
    [
        '10',
        'Pack Over Volt'],
    [
        '11',
        'Cell Under Volt'],
    [
        '12',
        'Pack Under Volt'],
    [
        '13',
        'Fan Status'],
    [
        '14',
        'Reserved'],
    [
        '15',
        'Reserved'],
    [
        '16',
        'Over Current Warining'],
    [
        '17',
        'Over temp warning'],
    [
        '18',
        'Error Fuse'],
    [
        '19',
        'Reserved'],
    [
        '20',
        'Error Pre_charge']]
# WARNING: Decompyle incomplete
