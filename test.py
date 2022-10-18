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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from datetime import datetime
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio_battery import *
from pywebio.platform import *
from pywebio.session import info
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdrivermanager.chrome import ChromeDriverManager

app = Flask(__name__)





def startw():
        

        driver = webdriver.Chrome(ChromeDriverManager().download_and_install())
        driver.get("http://www.python.org")







    











if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(startw, port=args.port,debug=True,max_payload_size='10000000',reconnect_timeout=4)

