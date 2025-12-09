# Source Generated with Decompyle++
# File: add_user.pyc (Python 3.11)

from flet import *
import requests

class Add_User:

    def __init__(self = None, page = None):
        self.page = page
        self.username = TextField(label = 'Username', hint_text = 'Enter username')
        self.useremail = TextField(label = 'Email', hint_text = 'Enter email')
        self.hrs = TextField(label = 'Hours', hint_text = 'Enter hours')
        self.password = TextField(label = 'Password', hint_text = 'Enter password', password = True, can_reveal_password = True)
        self.role = Dropdown(label = 'Role', hint_text = 'Select role', options = [
            dropdown.Option('admin'),
            dropdown.Option('user')])
        self.add_button = ElevatedButton('Add User', on_click = self.add_user)
        self.alert = SnackBar(Text('User added successfully!', size = 20), bgcolor = 'green', padding = padding.only(left = 550))
        self.grant_access = ElevatedButton('Grant Access', on_click = self.grant_access1)


    def get_id(self, id_token):
        global user_id
        user_id = id_token


    def add_user(self, e):
        pass
    # WARNING: Decompyle incomplete


    def grant_access1(self, e):
        pass
    # WARNING: Decompyle incomplete


    def build(self):
        return Column(controls = [
            Container(height = 150),
            Text('Add New User', size = 20, weight = FontWeight.BOLD),
            self.username,
            self.password,
            self.role,
            self.add_button,
            Text('Grant Access to normal users', size = 20, weight = FontWeight.BOLD),
            self.useremail,
            self.hrs,
            self.grant_access])
