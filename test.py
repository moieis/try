import itranslate as t
from pywebio.output  import *
from pywebio.input import *
import time
from pywebio.pin import *
from pywebio.platform import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import argparse
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio_battery import *
from pywebio.platform import *
from pywebio.session import info
app = Flask(__name__)
import os
import pandas as pd
from selenium import webdriver
from os import system, name
import chromedriver_binary
from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading
import chromedriver_autoinstaller


def pc():
        put_text('sdkd')
        chromedriver_autoinstaller.install()


        start = time()
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1024, 650)
        

    













if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(pc, port=args.port,debug=True,max_payload_size='10000000',reconnect_timeout=4)

