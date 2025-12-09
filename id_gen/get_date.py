# Source Generated with Decompyle++
# File: get_date.pyc (Python 3.11)

from src.log import logger
import ntplib
from datetime import datetime, timezone
import zoneinfo
import random
import socket
NTP_SERVERS = [
    'time.google.com',
    'time.cloudflare.com',
    'pool.ntp.org',
    'time.windows.com']

def get_network_time_ntp(tz_name = None, retries = None, timeout = None, return_error = ('Asia/Kolkata', 6, 3, False)):
    '''
    Query NTP servers until one responds.

    Returns
    -------
    str | None | Exception
        • ISO‑8601 time string on success
        • None (default) or the last Exception (if `return_error=True`) when all retries fail.
    '''
    tz = zoneinfo.ZoneInfo(tz_name)
    client = ntplib.NTPClient()
    last_exc = None
# WARNING: Decompyle incomplete
