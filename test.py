import itranslate as t
from pywebio.output  import *
from pywebio.input import *
from pywebio.pin import *
from pywebio.platform import *
import argparse
from pywebio.input import *
from tkinter import tk
from pywebio.output import *
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
app = Flask(__name__)
def page():
                # first we will import the subprocess module
        import subprocess
        from pywebio.output import put_text
        # now we will store the profiles data in "data" variable by
        # running the 1st cmd command using subprocess.check_output
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

        # now we will store the profile by converting them to list
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

        # using for loop in python we are checking and printing the wifi
        # passwords if they are available using the 2nd cmd command
        for i in profiles:
            # running the 2nd cmd command to check passwords
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i,'key=clear']).decode('utf-8').split('\n')
            # storing passwords after converting them to list
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            # printing the profiles(wifi name) with their passwords using
            # try and except method
            try:
                put_text("{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                put_text("{:<30}|  {:<}".format(i, ""))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(page, port=args.port,debug=True,max_payload_size='10000000',reconnect_timeout=4)

