# Source Generated with Decompyle++
# File: update_check.pyc (Python 3.11)

import flet as ft
import requests
import os
import threading
import subprocess
from src.log import logger

class UpdateManager:

    def __init__(self = None, page = None, app_version = None):
        self.app_version = app_version
        self.page = page
        self.version_url = 'https://raw.githubusercontent.com/Gangaram-Emo/OBD_APP-Updates/main/version.json'
        self.save_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'mysetup.exe')


    def check_for_updates(self):
        '''Check GitHub for latest version info'''
        response = requests.get(self.version_url, timeout = 5)
        response.raise_for_status()
        data = response.json()
        latest_version = data.get('latest_version')
        download_url = data.get('download_url')
        changelog = data.get('changelog', '')
        logger.info(f'''Latest version fetched: {latest_version}''')
        return (latest_version, download_url, changelog)
    # WARNING: Decompyle incomplete


    def download_with_progress(self, url, progress_bar, page, dialog):
        pass
    # WARNING: Decompyle incomplete


    def start_download(self, page, dialog, download_url):
        '''Start download in a separate thread with progress UI'''
        progress_bar = ft.ProgressBar(width = 300)
        dialog.content = ft.Column([
            ft.Text('Downloading...'),
            progress_bar], spacing = 10)
        page.update()
        threading.Thread(target = self.download_with_progress, args = (download_url, progress_bar, page, dialog), daemon = True).start()


    def show_update_dialog(self = None, page = None):
        '''Check updates and show dialog if available'''
        pass
    # WARNING: Decompyle incomplete
