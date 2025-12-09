# Source Generated with Decompyle++
# File: calibration.pyc (Python 3.11)

'''
Single Point BMS Current Calibration Script

This script calculates calibration parameters from just ONE current value.
Useful for quick calibration or when you only have one test point.

Usage:
    # For CSV format with single current value
    python single_calibration.py test_data.csv --actual-current 40

    # For Excel format
    python single_calibration.py input_file.xlsx

The script outputs:
    #define CURRENT_GAIN_CALIBRATION X.XXXX
    #define CURRENT_OFFSET_CALIBRATION 0.0000
'''
from src.log import logger
import pandas as pd
import numpy as np
import sys
import argparse
from pathlib import Path

def calculate_single_point_from_csv(csv_file, actual_current, mode = ('discharge',)):
    '''
    Process CSV file for single current value calibration

    Expected CSV format:
    BMS_ID,Pack_ID,Date,Time,Current,Mode,Voltage,...
    '''
    logger.info(f'''Reading CSV file: {csv_file}''')
    df = pd.read_csv(csv_file, low_memory = False)
    logger.info(f'''Data loaded successfully with {len(df)} rows''')
    if 'Current' not in df.columns:
        logger.error("Error: 'Current' column not found in CSV file")
        logger.error(f'''Available columns: {list(df.columns)}''')
        return (None, None)
    None.info('Data Summary:')
    logger.info(f'''Total rows: {len(df)}''')
    logger.info(f'''Pack ID(s): {df['Pack_ID'].unique() if 'Pack_ID' in df.columns else 'N/A'}''')
    logger.info(f'''BMS ID(s): {df['BMS_ID'].unique() if 'BMS_ID' in df.columns else 'N/A'}''')
# WARNING: Decompyle incomplete


def process_single_current_level(data, actual_current, mode_name):
    logger.info(f'''\n{mode_name} Single Point Analysis:''')
    logger.info('----------------------------------------')
    tolerance = max(1, actual_current * 0.2)
    matching_readings = data[(data['Current'] >= actual_current - tolerance) & (data['Current'] <= actual_current + tolerance)]['Current'].values
    logger.info(f'''Found matching readings: {len(matching_readings)}''')
    if len(matching_readings) < 5:
        logger.error(f'''Not enough readings found for {actual_current}A''')
        logger.error(f'''Found only {len(matching_readings)} readings (need at least 5)''')
        logger.error(f'''Tolerance range: {actual_current - tolerance:.1f}A to {actual_current + tolerance:.1f}A''')
        return (None, None)
    if None(matching_readings) > 10:
        sorted_readings = np.sort(matching_readings)
        trim_count = max(1, int(len(sorted_readings) * 0.1))
        stable_readings = sorted_readings[trim_count:-trim_count]
    else:
        stable_readings = matching_readings
    avg_measured = np.mean(stable_readings)
    std_measured = np.std(stable_readings)
    logger.info(f'''Actual current: {actual_current:.1f}A''')
    logger.info(f'''Measured current: {avg_measured:.2f}A ± {std_measured:.2f}A''')
    logger.info(f'''Stable readings used: {len(stable_readings)}''')
    logger.info(f'''Current offset: {actual_current - avg_measured:.2f}A''')
    logger.info(f'''Error percentage: {((actual_current - avg_measured) / actual_current) * 100:.1f}%''')
    gain = actual_current / avg_measured if avg_measured != 0 else 1
    offset = 0
    logger.info(f'''\n{mode_name} Calibration:''')
    logger.info(f'''CURRENT_GAIN_CALIBRATION = {gain:.4f}''')
    logger.info(f'''CURRENT_OFFSET_CALIBRATION = {offset:.4f}''')
    corrected_current = gain * avg_measured + offset
    error = actual_current - corrected_current
    logger.info('\nValidation:')
    logger.info(f'''After calibration: {corrected_current:.2f}A (Target: {actual_current:.1f}A)''')
    logger.info(f'''Remaining error: {abs(error):.3f}A''')
    error_percent = (abs(error) / actual_current) * 100
    if error_percent < 1:
        quality = 'Excellent'
        status = '✅'
    elif error_percent < 3:
        quality = 'Good'
        status = '✅'
    elif error_percent < 5:
        quality = 'Acceptable'
        status = '⚠️'
    else:
        quality = 'Poor'
        status = '❌'
    logger.info(f'''Calibration Quality: {status} {quality}''')
    return (gain, offset)
# WARNING: Decompyle incomplete


def calculate_single_point_from_excel(excel_file):
    '''
    Process Excel file for single point calibration

    Expected Excel format:
    | Pack ID  | Actual Current | Current Offset |
    | ZENE2143 | 40             | 5.2           |
    '''
    logger.info(f'''Reading Excel file: {excel_file}''')
    df = pd.read_excel(excel_file)
    required_columns = [
        'Actual Current',
        'Current Offset']
    for col in required_columns:
        if col not in df.columns:
            logger.error(f'''Error: Column \'{col}\' not found in Excel file''')
            logger.error(f'''Available columns: {list(df.columns)}''')
            return (None, None)
        actual_current_avg = df['Actual Current'].mean()
        current_offset_avg = df['Current Offset'].mean()
        measured_current_avg = actual_current_avg - current_offset_avg
        logger.info('\nExcel Data Analysis:')
        logger.info('----------------------------------------')
        logger.info(f'''Data points: {len(df)}''')
        logger.info(f'''Average actual current: {actual_current_avg:.2f}A''')
        logger.info(f'''Average current offset: {current_offset_avg:.2f}A''')
        logger.info(f'''Average measured current: {measured_current_avg:.2f}A''')
    gain = actual_current_avg / measured_current_avg if measured_current_avg != 0 else 1
    offset = 0
    logger.info('\nSingle Point Calibration:')
    logger.info(f'''CURRENT_GAIN_CALIBRATION = {gain:.4f}''')
    logger.info(f'''CURRENT_OFFSET_CALIBRATION = {offset:.4f}''')
    corrected_current = gain * measured_current_avg + offset
    error = actual_current_avg - corrected_current
    logger.info('\nValidation:')
    logger.info(f'''After calibration: {corrected_current:.2f}A (Target: {actual_current_avg:.1f}A)''')
    logger.info(f'''Remaining error: {abs(error):.3f}A''')
    return (gain, offset)
# WARNING: Decompyle incomplete


def run(input_file, actual_current, mode, output_file = (None, 'discharge', None)):
    file_path = Path(input_file)
    file_extension = file_path.suffix.lower()
    if file_extension == '.xlsx':
        (gain, offset) = calculate_single_point_from_excel(input_file)
# WARNING: Decompyle incomplete


def quick_calculate(actual_current, measured_current):
    '''
    Quick calculation for when you have just two values
    '''
    gain = actual_current / measured_current if measured_current != 0 else 1
    offset = 0
    logger.info('Quick Single Point Calibration:')
    logger.info(f'''Actual: {actual_current}A, Measured: {measured_current}A''')
    logger.info(f'''CURRENT_GAIN_CALIBRATION = {gain:.4f}''')
    logger.info(f'''CURRENT_OFFSET_CALIBRATION = {offset:.4f}''')
    return (gain, offset)
