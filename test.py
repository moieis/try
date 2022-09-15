import itranslate as t
from pywebio.output  import *
from pywebio.input import *
from pywebio.pin import *
from pywebio.platform import *
import argparse
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
app = Flask(__name__)
import subprocess

def page():
        # using the check_output() for having the network term retrieval
        devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])

        # decode it to strings
        devices = devices.decode('ascii')

        s = devices.replace("\r", "")

        # displaying the information
        nearby = [x[x.find(':') + 1:].replace('\r', '').strip() for x in devices.split('\n') if "SSID" in x]

        meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

        # decoding meta data
        data = meta_data.decode('utf-8', errors="backslashreplace")

        # splitting data by line by line
        data = data.split('\n')

        # creating a list of profiles
        profiles = []

        # traverse the data
        for i in data:

            # find "All User Profile" in each item
            if "All User Profile" in i:
                # if found
                # split the item
                i = i.split(":")

                # item at index 1 will be the wifi name
                i = i[1]

                # formatting the name
                # first and last character is use less
                i = i[1:-1]

                # appending the wifi name in the list
                profiles.append(i)

        # printing heading
        put_text("{:<30}| {:<30} | {:<20}".format("Wi-Fi Name", "Password", "Nearby Network"))
        put_text("-" * 80)

        # traversing the profiles
        for i in profiles:

            # try catch block begins
            # try block
            try:
                # getting meta data with password using wifi name
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'])

                # decoding and splitting data line by line
                results = results.decode('utf-8', errors="backslashreplace")
                results = results.split('\n')

                # finding password from the result list
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

                # if there is password it will print the pass word
                try:
                    nearbyFlag = i in nearby
                    put_text("{:<30}| {:<30} | {:<20}".format(i, results[0], "Y" if nearbyFlag else "N"))

                # else it will print blank in front of pass word
                except IndexError:
                    put_text("{:<30}| {:<}".format(i, ""))

            # called when this process get failed
            except subprocess.CalledProcessError:
                print("Encoding Error Occured")




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(page, port=args.port,debug=True,max_payload_size='10000000',reconnect_timeout=4)

