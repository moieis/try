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
import time
import requests
from selenium import webdriver


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

def pc():

    with use_scope(name='boton', clear=True):
        bq = ''''
    <style>

.button-75 {
  align-items: center;
  background-image: linear-gradient(135deg, #f34079 40%, #fc894d);
  border: 0;
  border-radius: 10px;
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  font-family: "Codec cold",sans-serif;
  font-size: 16px;
  font-weight: 700;
  height: 54px;
  justify-content: center;
  letter-spacing: .4px;
  line-height: 1;
  max-width: 100%;
  padding-left: 20px;
  padding-right: 20px;
  padding-top: 3px;
  text-decoration: none;
  text-transform: uppercase;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.button-75:active {
  outline: 0;
}

.button-75:hover {
  outline: 0;
}

.button-75 span {
  transition: all 200ms;
}

.button-75:hover span {
  transform: scale(.9);
  opacity: .75;
}

@media screen and (max-width: 991px) {
  .button-75 {
    font-size: 15px;
    height: 50px;
  }

  .button-75 span {
    line-height: 50px;
  }
}</style>'''
        put_grid([[None, None, None, None, None, None, None, None, None, None, None, None, put_html(f'''<!-- HTML !-->
    <button class="button-75" role="button"><span class="text">{info.user_agent.get_os()}</span></button>

    {bq}
    '''), put_html(f'''<!-- HTML !-->
    <button class="button-75" role="button"><span class="text">{info.user_agent.get_os()}</span></button>
    {bq}
    ''')]])
    def startpc():
        time.sleep(2)
        clear(scope='logopage')
        clear(scope='boton')
        with use_scope(name='logo', clear=True):
            put_grid([[None, None, None, None,
                       put_image('https://i.im.ge/2022/10/03/1Z8Uj4.9076d9b47d4f422b995c7e848c4b0a8c.png', width='200',
                                 height='200'),None,None,None, None]])


        with use_scope('1ask',clear=True):
            def driver():
                print(info.user_agent.get_browser().split(' ')[0])
                print(info.user_agent.get_os())
                if info.user_agent.get_browser().split(' ')[1].split('.')[0] == '105' and info.user_agent.get_browser().split(' ')[0] == 'Edge':
                       popup("Click on the link to download the driver  ",put_grid([[put_link(name=f'! Here is {info.user_agent.get_browser()} Driver  for x68!',url='https://msedgedriver.azureedge.net/105.0.1343.53/edgedriver_win64.zip'),None,None,None,put_link(name=f'! Here is {info.user_agent.get_browser()} Driver  for x86!',url='https://msedgedriver.azureedge.net/105.0.1343.53/edgedriver_win32.zip')]]))
                elif info.user_agent.get_browser().split(' ')[1].split('.')[0] == '106' and info.user_agent.get_browser().split(' ')[0] == 'Chrome':
                       popup("Click on the link to download the driver  ",put_grid([[put_link(name=f'! Here is {info.user_agent.get_browser()} Driver  for x68!',url='https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_win32.zip'),None,None,None,put_link(name=f'! Here is {info.user_agent.get_browser()} Driver  for x86!',url='https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_win32.zip')]]))
                elif info.user_agent.get_browser().split(' ')[1].split('.')[0] == '107' and \
                        info.user_agent.get_browser().split(' ')[0] == 'Chrome':
                    popup("Click on the link to download the driver  ", put_grid([[put_link(
                        name=f'! Here is {info.user_agent.get_browser()} Driver  for x68!',
                        url='https://chromedriver.storage.googleapis.com/107.0.5304.18/chromedriver_win32.zip'), None,
                                                                                   None, None, put_link(
                            name=f'! Here is {info.user_agent.get_browser()} Driver  for x86!',
                            url='https://chromedriver.storage.googleapis.com/107.0.5304.18/chromedriver_win32.zip')]]))
                elif info.user_agent.get_browser().split(' ')[1].split('.')[0] == '105' and \
                        info.user_agent.get_browser().split(' ')[0] == 'Chrome':
                    popup("Click on the link to download the driver  ", put_grid([[put_link(
                        name=f'! Here is {info.user_agent.get_browser()} Driver  for x68!',
                        url='https://chromedriver.storage.googleapis.com/105.0.5195.52/chromedriver_win32.zip'), None,
                                                                                   None, None, put_link(
                            name=f'! Here is {info.user_agent.get_browser()} Driver  for x86!',
                            url='https://chromedriver.storage.googleapis.com/105.0.5195.52/chromedriver_win32.zip')]]))
                elif  \
                        info.user_agent.get_browser().split(' ')[0] == 'Firefox':
                    popup("Click on the link to download the driver  ", put_grid([[put_link(
                        name=f'! Here is {info.user_agent.get_browser()} Driver  for x68!',
                        url='https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-win64.zip'), None,
                                                                                   None, None, put_link(
                            name=f'! Here is {info.user_agent.get_browser()} Driver  for x86!',
                            url='https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-win32.zip')]]))

                else:
                    popup('ammmmmmm ! ',f'We could not find the required driver for the required version, try searching by obtaining the driver for this {info.user_agent.get_browser()}')



            put_html('<hr>')
            put_grid([[None, None,None,None, put_html(f'<h7>Your browser has been checked to run moibot yours : {info.user_agent.get_browser()} </h7>'),None,None,None,None]])
            put_grid([[None, None, None,None,put_html(f'<h4>-Do You Have {info.user_agent.get_browser()} driver or not !?-</h4>'), None,None, None, None]])
            put_html('<hr>')
            put_grid([[None,None,None,None,put_html('''
<button class="button-47" role="button">Yes I Have</button>

<style>
.button-47 {
  align-items: center;
  background: #FFFFFF;
  border: 0 solid #E2E8F0;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  box-sizing: border-box;
  color: #1A202C;
  display: inline-flex;
  font-family: Inter, sans-serif;
  font-size: 1rem;
  font-weight: 700;
  height: 56px;
  justify-content: center;
  line-height: 24px;
  overflow-wrap: break-word;
  padding: 24px;
  text-decoration: none;
  width: auto;
  border-radius: 8px;
  cursor: pointer;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  
}
</style>''').onclick(start),None,put_html('''
<button class="button-47" role="button">I don't have</button>

<style>
.button-47 {
  align-items: center;
  background: #FFFFFF;
  border: 0 solid #E2E8F0;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  box-sizing: border-box;
  color: #1A202C;
  display: inline-flex;
  font-family: Inter, sans-serif;
  font-size: 1rem;
  font-weight: 700;
  height: 56px;
  justify-content: center;
  line-height: 24px;
  overflow-wrap: break-word;
  padding: 24px;
  text-decoration: none;
  width: auto;
  border-radius: 8px;
  cursor: pointer;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  
}
</style>''').onclick(driver),None,None,None,None]])

    startpc()

def er1():

    with use_scope(name='boton', clear=True):
        bs = ''''
    <style>

.button-75 {
  align-items: center;
  background-image: linear-gradient(135deg, #f34079 40%, #fc894d);
  border: 0;
  border-radius: 10px;
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  font-family: "Codec cold",sans-serif;
  font-size: 16px;
  font-weight: 700;
  height: 54px;
  justify-content: center;
  letter-spacing: .4px;
  line-height: 1;
  max-width: 100%;
  padding-left: 20px;
  padding-right: 20px;
  padding-top: 3px;
  text-decoration: none;
  text-transform: uppercase;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.button-75:active {
  outline: 0;
}

.button-75:hover {
  outline: 0;
}

.button-75 span {
  transition: all 200ms;
}

.button-75:hover span {
  transform: scale(.9);
  opacity: .75;
}

@media screen and (max-width: 991px) {
  .button-75 {
    font-size: 15px;
    height: 50px;
  }

  .button-75 span {
    line-height: 50px;
  }
}</style>'''
        put_grid([[None, None, None, None, None, None, None, None, None, None, None, None, put_html(f'''<!-- HTML !-->
       <button class="button-75" role="button"><span class="text">{info.user_agent.get_os()}</span></button>
        

        {bs}
        ''').onclick(chack), put_html(f'''<!-- HTML !-->
         <button class="button-45" role="button"sdds</button>
        {bs}
        ''').onclick(chack)]])
def mac():
    with use_scope(name='boton', clear=True):
        bq = ''''
        <style>

    .button-75 {
      align-items: center;
      background-image: linear-gradient(135deg, #f34079 40%, #fc894d);
      border: 0;
      border-radius: 10px;
      box-sizing: border-box;
      color: #fff;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      font-family: "Codec cold",sans-serif;
      font-size: 16px;
      font-weight: 700;
      height: 54px;
      justify-content: center;
      letter-spacing: .4px;
      line-height: 1;
      max-width: 100%;
      padding-left: 20px;
      padding-right: 20px;
      padding-top: 3px;
      text-decoration: none;
      text-transform: uppercase;
      user-select: none;
      -webkit-user-select: none;
      touch-action: manipulation;
    }

    .button-75:active {
      outline: 0;
    }

    .button-75:hover {
      outline: 0;
    }

    .button-75 span {
      transition: all 200ms;
    }

    .button-75:hover span {
      transform: scale(.9);
      opacity: .75;
    }

    @media screen and (max-width: 991px) {
      .button-75 {
        font-size: 15px;
        height: 50px;
      }

      .button-75 span {
        line-height: 50px;
      }
    }</style>'''
        put_grid([[None, None, None, None, None, None, None, None, None, None, None, None, put_html(f'''<!-- HTML !-->
        <button class="button-75" role="button"><span class="text">{info.user_agent.get_os()}</span></button>

        {bq}
        '''), put_html(f'''<!-- HTML !-->
        <button class="button-75" role="button"><span class="text">{info.user_agent.get_os()}</span></button>
        {bq}
        ''')]])

    def startpc():
        time.sleep(2)
        clear(scope='logopage')
        clear(scope='boton')
        with use_scope(name='logo', clear=True):
            put_grid([[None, None, None, None,
                       put_image('https://i.im.ge/2022/10/03/1Z8Uj4.9076d9b47d4f422b995c7e848c4b0a8c.png', width='200',
                                 height='200').onclick(startw), None, None, None, None]])

        with use_scope('1ask', clear=True):
            def driver():
                print(info.user_agent.get_browser().split(' ')[0])
                print(info.user_agent.get_os())
                if info.user_agent.get_browser().split(' ')[1].split('.')[0] == '105' and \
                        info.user_agent.get_browser().split(' ')[0] == 'Edge':
                    popup("Click on the link to download the driver  ", put_grid([[put_link(
                        name=f'! Here is {info.user_agent.get_browser()} Driver  for mac64_m1!',
                        url='https://msedgedriver.azureedge.net/106.0.1370.47/edgedriver_mac64_m1.zip'), None, None, None,
                                                                                   put_link(
                                                                                       name=f'! Here is {info.user_agent.get_browser()} Driver  for mac64!',
                                                                                       url='https://msedgedriver.azureedge.net/106.0.1370.47/edgedriver_mac64.zip')]]))
                elif info.user_agent.get_browser().split(' ')[1].split('.')[0] == '106' and \
                        info.user_agent.get_browser().split(' ')[0] == 'Chrome':
                    popup("Click on the link to download the driver  ", put_grid([[put_link(
                        name=f'! Here is {info.user_agent.get_browser()} Driver  for mac_arm64!',
                        url='https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_mac_arm64.zip'), None,
                                                                                   None, None, put_link(
                            name=f'! Here is {info.user_agent.get_browser()} Driver for mac 64 !',
                            url='https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_mac64.zip')]]))
                elif info.user_agent.get_browser().split(' ')[1].split('.')[0] == '107' and \
                        info.user_agent.get_browser().split(' ')[0] == 'Chrome':
                    popup("Click on the link to download the driver  ", put_grid([[put_link(
                        name=f'! Here is {info.user_agent.get_browser()} Driver  for xmac_arm64!',
                        url='https://chromedriver.storage.googleapis.com/107.0.5304.18/chromedriver_mac_arm64.zip'), None,
                        None, None, put_link(
                            name=f'! Here is {info.user_agent.get_browser()} Driver  for mac64!',
                            url='https://chromedriver.storage.googleapis.com/107.0.5304.18/chromedriver_mac64.zip')]]))

                elif \
                        info.user_agent.get_browser().split(' ')[0] == 'Firefox':
                    popup("Click on the link to download the driver  ", put_grid([[None,None,None,put_link(
                        name=f'! Here is {info.user_agent.get_browser()} Driver  for macos!',
                        url='https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-macos-aarch64.tar.gz'),
                        None,
                        None, None]]))

                else:
                    popup('ammmmmmm ! ',
                          f'We could not find the required driver for the required version, try searching by obtaining the driver for this {info.user_agent.get_browser()}')

            put_html('<hr>')
            put_grid([[None, None, None, None, put_html(
                f'<h7>Your browser has been checked to run moibot yours : {info.user_agent.get_browser()} </h7>'), None,
                       None, None, None]])
            put_grid([[None, None, None, None,
                       put_html(f'<h4>-Do You Have {info.user_agent.get_browser()} driver or not !?-</h4>'), None, None,
                       None, None]])
            put_html('<hr>')
            put_grid([[None, None, None, None, put_html('''
    <button class="button-47" role="button">Yes I Have</button>

    <style>
    .button-47 {
      align-items: center;
      background: #FFFFFF;
      border: 0 solid #E2E8F0;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
      box-sizing: border-box;
      color: #1A202C;
      display: inline-flex;
      font-family: Inter, sans-serif;
      font-size: 1rem;
      font-weight: 700;
      height: 56px;
      justify-content: center;
      line-height: 24px;
      overflow-wrap: break-word;
      padding: 24px;
      text-decoration: none;
      width: auto;
      border-radius: 8px;
      cursor: pointer;
      user-select: none;
      -webkit-user-select: none;
      touch-action: manipulation;

    }
    </style>''').onclick(start), None, put_html('''
    <button class="button-47" role="button">I don't have</button>

    <style>
    .button-47 {
      align-items: center;
      background: #FFFFFF;
      border: 0 solid #E2E8F0;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
      box-sizing: border-box;
      color: #1A202C;
      display: inline-flex;
      font-family: Inter, sans-serif;
      font-size: 1rem;
      font-weight: 700;
      height: 56px;
      justify-content: center;
      line-height: 24px;
      overflow-wrap: break-word;
      padding: 24px;
      text-decoration: none;
      width: auto;
      border-radius: 8px;
      cursor: pointer;
      user-select: none;
      -webkit-user-select: none;
      touch-action: manipulation;

    }
    </style>''').onclick(driver), None, None, None, None]])

    startpc()
def chack():
    print(info.user_agent.get_os().split(' ')[0])
    if info.user_agent.get_os().split(' ')[0] == 'Windows':

        pc()

    elif info.user_agent.get_os().split(' ')[0] == 'iOS':
        er1()

    elif info.user_agent.get_os().split(' ')[0] == 'Mac':
        mac()


def startw():
    def next():
        with use_scope(name='logopage', clear=True):

            put_grid([[None, None, None, None, put_html('''<img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/1-instagram.gif" jsaction="load:XAeZkd;" jsname="HiaYvf" class="n3VNCb KAlRDb" alt="File:1-instagram.gif - Wikimedia Commons" data-noaft="1" style="width: 383px; height: 287.25px; margin: 0px;">'''),
                       None, None, None,
                       put_html(
                           '<h3>Here you can see all the functions and use them in the right way</h3>'
                           '<h3>! After you choose any feature we will take some data from you to know what your device supports to facilitate the experience with us</h3>')]])

        with use_scope(name='boton',clear=True):
            bo=''''
<style>
.button-85 {
  padding: 0.6em 2em;
  border: none;
  outline: none;
  color: rgb(255, 255, 255);
  background: #111;
  cursor: pointer;
  position: relative;
  z-index: 0;
  border-radius: 10px;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.button-85:before {
  content: "";
  background: linear-gradient(
    45deg,
    #ff0000,
    #ff7300,
    #fffb00,
    #48ff00,
    #00ffd5,
    #002bff,
    #7a00ff,
    #ff00c8,
    #ff0000
  );
  position: absolute;
  top: -2px;
  left: -2px;
  background-size: 400%;
  z-index: -1;
  filter: blur(5px);
  -webkit-filter: blur(5px);
  width: calc(100% + 4px);
  height: calc(100% + 4px);
  animation: glowing-button-85 20s linear infinite;
  transition: opacity 0.3s ease-in-out;
  border-radius: 10px;
}

@keyframes glowing-button-85 {
  0% {
    background-position: 0 0;
  }
  50% {
    background-position: 400% 0;
  }
  100% {
    background-position: 0 0;
  }
}

.button-85:after {
  z-index: -1;
  content: "";
  position: absolute;
  width: 100%;
  height: 100%;
  background: #222;
  left: 0;
  top: 0;
  border-radius: 10px;
}</style>'''
            put_grid([[None, None, None, None, None, None, None, None, None, None, None, None, put_html(f'''<!-- HTML !-->
<button class="button-85" role="button">MoiReporter</button>
{bo}
''').onclick(chack), put_html(f'''<!-- HTML !-->
<button class="button-85" role="button">MoiFoundUser</button>
{bo}
''').onclick(chack)]])
    def one():
        with use_scope(name='logo',clear=True):
            put_grid([[None,None,None,None,put_image('https://i.im.ge/2022/10/03/1Z8Uj4.9076d9b47d4f422b995c7e848c4b0a8c.png',width='200',height='200').onclick(startw),None]])
        with use_scope(name='logopage',clear=True):
            put_grid([[None,None,None,None,put_html('''<img src="https://media0.giphy.com/media/uo6rcjwHSAFsQ/giphy.gif" jsaction="load:XAeZkd;" jsname="HiaYvf" class="n3VNCb KAlRDb" alt="Instagram GIFs - Get the best GIF on GIPHY" data-noaft="1" style="width: 383px; height: 287.25px; margin: 0px;">'''),None,None,None,
                      put_html('<h3>Welcome to Moinsta All services are free of any fees and for practical purposes only I wish you the best We will be close to you.</h3>') ]])
            put_grid([[None,None,None,None,None,None,None,None,None,None,None,None,None,None,put_html('''<!-- HTML !-->
    <button class="button-40" role="button">Next -></button>
    
    <style>
    .button-40 {
      background-color: #111827;
      border: 1px solid transparent;
      border-radius: .75rem;
      box-sizing: border-box;
      color: #FFFFFF;
      cursor: pointer;
      flex: 0 0 auto;
      font-family: "Inter var",ui-sans-serif,system-ui,-apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
      font-size: 1.125rem;
      font-weight: 600;
      line-height: 1.5rem;
      padding: .75rem 1.2rem;
      text-align: center;
      text-decoration: none #6B7280 solid;
      text-decoration-thickness: auto;
      transition-duration: .2s;
      transition-property: background-color,border-color,color,fill,stroke;
      transition-timing-function: cubic-bezier(.4, 0, 0.2, 1);
      user-select: none;
      -webkit-user-select: none;
      touch-action: manipulation;
      width: auto;
    }
    
    .button-40:hover {
      background-color: #374151;
    }
    
    .button-40:focus {
      box-shadow: none;
      outline: 2px solid transparent;
      outline-offset: 2px;
    }
    
    @media (min-width: 768px) {
      .button-40 {
        padding: .75rem 1.5rem;
      }
    }
    </style>''').onclick(next)]])

    one()

def start():

        clear(scope='1ask')
        cho=[]
        user=[]
        myuse=[]
        mypas=[]
        loc=[]
        rang=[]
        speed=[]
        def chrome():

            with use_scope(name='chose', clear=True):
                put_html('<hr>')
                with use_scope(name='info', clear=True):
                    put_info(
                        'There is no withdrawal of any of your data. You can see the details of the algorithm. You are in our protection !')
                    time.sleep(2)
                put_grid([[None, put_text('Your InstUser :'), put_input('myuser', type=TEXT), None, None, None]])
                put_grid(
                    [[None, put_text('Your InstPassword :'), put_input('mypass', type=PASSWORD), None, None, None]])
                put_html('<hr>')

                def userofr():
                    ########################## exaptions buges for the login insta #######################
                    def exap():
                        def acc():
                            def update_acc():
                                myuse.append(pin.newu)
                                mypas.append(pin.newp)
                                ch()

                            popup('Edit Your Account : ',
                                  put_grid([[None, None, put_text('Your Username:'), None, None],
                                            [None, None, put_input('newu', value=myuse[-1]), None, None],
                                            [None, None, put_html('<hr>'), None, None],
                                            [None, None, put_text('Your Password:'), None, None],
                                            [None, None, put_input('newp', value=mypas[-1]), None, None],
                                            [None, None, put_html('<hr>'), None, None],
                                            [None, None, put_html('''<button class="btn">
                                    <span class="btn-text-one">Save</span>
                                    <span class="btn-text-two">may restart</span>
                                </button>

                                <style>/* From uiverse.io by @mobinkakei */
                                .btn {
                                  width: 140px;
                                  height: 50px;
                                  background: linear-gradient(to top, #2bbab1, #12376e, #23487f);
                                  color: #fff;
                                  border-radius: 50px;
                                  border: none;
                                  outline: none;
                                  cursor: pointer;
                                  position: relative;
                                  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
                                  overflow: hidden;
                                }

                                .btn span {
                                  font-size: 12px;
                                  text-transform: uppercase;
                                  letter-spacing: 1px;
                                  transition: top 0.5s;
                                }

                                .btn-text-one {
                                  position: absolute;
                                  width: 100%;
                                  top: 50%;
                                  left: 0;
                                  transform: translateY(-50%);
                                }

                                .btn-text-two {
                                  position: absolute;
                                  width: 100%;
                                  top: 150%;
                                  left: 0;
                                  transform: translateY(-50%);
                                }

                                .btn:hover .btn-text-one {
                                  top: -100%;
                                }

                                .btn:hover .btn-text-two {
                                  top: 50%;
                                }
                                </style>''').onclick(update_acc), None, None], ]))

                        #################################### Edit #################################
                        def edit():
                            popup('Choose what you want to edit :', put_grid([[None, None, span(put_html('''<button class="cta">
                                                                    <span class="hover-underline-animation">My Account</span>
                                                                    <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                                        <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                                    </svg>
                                                                </button>

                                                                <style>/* From uiverse.io by @alexmaracinaru */
                                                                .cta {
                                                                  border: none;
                                                                  background: none;
                                                                }

                                                                .cta span {
                                                                  padding-bottom: 7px;
                                                                  letter-spacing: 4px;
                                                                  font-size: 9px;
                                                                  padding-right: 15px;
                                                                  text-transform: uppercase;
                                                                }

                                                                .cta svg {
                                                                  transform: translateX(-8px);
                                                                  transition: all 0.3s ease;
                                                                }

                                                                .cta:hover svg {
                                                                  transform: translateX(0);
                                                                }

                                                                .cta:active svg {
                                                                  transform: scale(0.9);
                                                                }

                                                                .hover-underline-animation {
                                                                  position: relative;
                                                                  color: black;
                                                                  padding-bottom: 20px;
                                                                }

                                                                .hover-underline-animation:after {
                                                                  content: "";
                                                                  position: absolute;
                                                                  width: 100%;
                                                                  transform: scaleX(0);
                                                                  height: 2px;
                                                                  bottom: 0;
                                                                  left: 0;
                                                                  background-color: #000000;
                                                                  transform-origin: bottom right;
                                                                  transition: transform 0.25s ease-out;
                                                                }

                                                                .cta:hover .hover-underline-animation:after {
                                                                  transform: scaleX(1);
                                                                  transform-origin: bottom left;
                                                                }</style>''').onclick(acc), col=2, row=1), None, None],
                                                                              [None, None,
                                                                               span(put_html('<hr>'), col=2,
                                                                                    row=1), None, None],
                                                                              [None, None, span(put_html('''<button class="cta">
                                                                    <span class="hover-underline-animation">Attk User</span>
                                                                    <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                                        <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                                    </svg>
                                                                </button>

                                                                <style>/* From uiverse.io by @alexmaracinaru */
                                                                .cta {
                                                                  border: none;
                                                                  background: none;
                                                                }

                                                                .cta span {
                                                                  padding-bottom: 7px;
                                                                  letter-spacing: 4px;
                                                                  font-size: 14px;
                                                                  padding-right: 15px;
                                                                  text-transform: uppercase;
                                                                }

                                                                .cta svg {
                                                                  transform: translateX(-8px);
                                                                  transition: all 0.3s ease;
                                                                }

                                                                .cta:hover svg {
                                                                  transform: translateX(0);
                                                                }

                                                                .cta:active svg {
                                                                  transform: scale(0.9);
                                                                }

                                                                .hover-underline-animation {
                                                                  position: relative;
                                                                  color: black;
                                                                  padding-bottom: 20px;
                                                                }

                                                                .hover-underline-animation:after {
                                                                  content: "";
                                                                  position: absolute;
                                                                  width: 100%;
                                                                  transform: scaleX(0);
                                                                  height: 2px;
                                                                  bottom: 0;
                                                                  left: 0;
                                                                  background-color: #000000;
                                                                  transform-origin: bottom right;
                                                                  transition: transform 0.25s ease-out;
                                                                }

                                                                .cta:hover .hover-underline-animation:after {
                                                                  transform: scaleX(1);
                                                                  transform-origin: bottom left;
                                                                }</style>''').onclick(edit), col=2, row=1), None, None],
                                                                              [None, None,
                                                                               span(put_html('<hr>'), col=2,
                                                                                    row=1), None, None],
                                                                              [None, None, span(put_html('''<button class="cta">
                                                                    <span class="hover-underline-animation">Range</span>
                                                                    <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                                        <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                                    </svg>
                                                                </button>

                                                                <style>/* From uiverse.io by @alexmaracinaru */
                                                                .cta {
                                                                  border: none;
                                                                  background: none;
                                                                }

                                                                .cta span {
                                                                  padding-bottom: 7px;
                                                                  letter-spacing: 4px;
                                                                  font-size: 14px;
                                                                  padding-right: 15px;
                                                                  text-transform: uppercase;
                                                                }

                                                                .cta svg {
                                                                  transform: translateX(-8px);
                                                                  transition: all 0.3s ease;
                                                                }

                                                                .cta:hover svg {
                                                                  transform: translateX(0);
                                                                }

                                                                .cta:active svg {
                                                                  transform: scale(0.9);
                                                                }

                                                                .hover-underline-animation {
                                                                  position: relative;
                                                                  color: black;
                                                                  padding-bottom: 20px;
                                                                }

                                                                .hover-underline-animation:after {
                                                                  content: "";
                                                                  position: absolute;
                                                                  width: 100%;
                                                                  transform: scaleX(0);
                                                                  height: 2px;
                                                                  bottom: 0;
                                                                  left: 0;
                                                                  background-color: #000000;
                                                                  transform-origin: bottom right;
                                                                  transition: transform 0.25s ease-out;
                                                                }

                                                                .cta:hover .hover-underline-animation:after {
                                                                  transform: scaleX(1);
                                                                  transform-origin: bottom left;
                                                                }</style>''').onclick(edit), col=2, row=1), None, None],
                                                                              [None, None,
                                                                               span(put_html('<hr>'), col=2,
                                                                                    row=1), None, None],
                                                                              [None, None, span(put_html('''<button class="cta">
                                                                    <span class="hover-underline-animation">Speed</span>
                                                                    <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                                        <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                                    </svg>
                                                                </button>

                                                                <style>/* From uiverse.io by @alexmaracinaru */
                                                                .cta {
                                                                  border: none;
                                                                  background: none;
                                                                }

                                                                .cta span {
                                                                  padding-bottom: 7px;
                                                                  letter-spacing: 4px;
                                                                  font-size: 14px;
                                                                  padding-right: 15px;
                                                                  text-transform: uppercase;
                                                                }

                                                                .cta svg {
                                                                  transform: translateX(-8px);
                                                                  transition: all 0.3s ease;
                                                                }

                                                                .cta:hover svg {
                                                                  transform: translateX(0);
                                                                }

                                                                .cta:active svg {
                                                                  transform: scale(0.9);
                                                                }

                                                                .hover-underline-animation {
                                                                  position: relative;
                                                                  color: black;
                                                                  padding-bottom: 20px;
                                                                }

                                                                .hover-underline-animation:after {
                                                                  content: "";
                                                                  position: absolute;
                                                                  width: 100%;
                                                                  transform: scaleX(0);
                                                                  height: 2px;
                                                                  bottom: 0;
                                                                  left: 0;
                                                                  background-color: #000000;
                                                                  transform-origin: bottom right;
                                                                  transition: transform 0.25s ease-out;
                                                                }

                                                                .cta:hover .hover-underline-animation:after {
                                                                  transform: scaleX(1);
                                                                  transform-origin: bottom left;
                                                                }</style>''').onclick(edit), col=2, row=1), None,
                                                                               None]]),
                                  closable=True, implicit_close=False)

                        ###########################################################################

                        with use_scope('chose', clear=True):
                            sty = '''<style>
                                                                                                        .styled-table {
                                                                                                            border-collapse: collapse;
                                                                                                            margin: center;
                                                                                                            font-size: 0.9em;
                                                                                                            font-family: sans-serif;


                                                                                                        }
                                                                                                        .styled-table thead tr {
                                                                                                            background-color: #2bbab1;
                                                                                                            color: #ffffff;
                                                                                                            text-align: left;
                                                                                                        }
                                                                                                        .styled-table th,
                                                                                                        .styled-table td {
                                                                                                            padding: 12px 15px;
                                                                                                        }

                                                                                                        .styled-table tbody tr {
                                                                                                            border-bottom: 1px solid #dddddd;
                                                                                                        }

                                                                                                        .styled-table tbody tr:nth-of-type(even) {
                                                                                                            background-color: #2bbab1;
                                                                                                        }

                                                                                                        .styled-table tbody tr:last-of-type {
                                                                                                            border-bottom: 2px solid #2bbab1;
                                                                                                        }
                                                                                                        .styled-table tbody tr.active-row {
                                                                                                            font-weight: bold;
                                                                                                            color: #2bbab1;
                                                                                                        }
                                                                                                        </style>'''
                            put_grid([[None, None, None, None, put_html(f'''<table class="styled-table">
                                                                        <thead>
                                                                            <tr>

                                                                                <th>My User</th>
                                                                                <th>Att User</th>
                                                                                <th>Range input </th>
                                                                                <th> Found Bugs </th>
                                                                                <th>speed</th>
                                                                            </tr>
                                                                        </thead>
                                                                        <tbody>

                                                                            <tr class="active-row">
                                                                                <td>{myuse[-1]}</td>
                                                                                <td>{user[-1]}</td>
                                                                                <td>{rang[-1]}</td>
                                                                                <td>exception case buge[1] </td>
                                                                                <td>{speed[-1]}</td>
                                                                            </tr>
                                                                            <!-- and so on... -->
                                                                        </tbody>
                                                                    </table>
                                                                    {sty}
                                                                    '''), None, None, None, None]])
                            put_grid([[None, None, None, None, put_html('''<button class="btn">
                                                                               <span class="icon">
                                                                                   <svg viewBox="0 0 175 80" width="30" height="30">
                                                                                       <rect width="40" height="15" fill="#f0f0f0" rx="10"></rect>
                                                                                       <rect y="30" width="80" height="15" fill="#f0f0f0" rx="10"></rect>
                                                                                       <rect y="60" width="80" height="15" fill="#f0f0f0" rx="10"></rect>
                                                                                   </svg>
                                                                               </span>
                                                                               <span class="text">Customize</span>
                                                                           </button>
                                                                           <style>/* From uiverse.io by @gagan-gv */
                                                                           .btn {
                                                                             width: 160px;
                                                                             height: 37px;
                                                                             border-radius: 3px;
                                                                             border: none;
                                                                             transition: all 0.5s ease-in-out;
                                                                             font-size: 14px;
                                                                             font-family: Verdana, Geneva, Tahoma, sans-serif;
                                                                             font-weight: 700;
                                                                             display: flex;
                                                                             align-items: center;
                                                                             background: #2bbab1;
                                                                             color: #f5f5f5;
                                                                           }

                                                                           .btn:hover {
                                                                             box-shadow: 0 0 20px 0px #2e2e2e3a;
                                                                           }

                                                                           .btn .icon {
                                                                             position: absolute;
                                                                             height: 40px;
                                                                             width: 70px;
                                                                             display: flex;
                                                                             justify-content: center;
                                                                             align-items: center;
                                                                             transition: all 0.5s;
                                                                           }

                                                                           .btn .text {
                                                                             transform: translateX(55px);
                                                                           }

                                                                           .btn:hover .icon {
                                                                             width: 175px;
                                                                           }

                                                                           .btn:hover .text {
                                                                             transition: all 0.5s;
                                                                             opacity: 0;
                                                                           }

                                                                           .btn:focus {
                                                                             outline: none;
                                                                           }

                                                                           .btn:active .icon {
                                                                             transform: scale(0.85);
                                                                           }</style>''').onclick(edit), None, None,
                                       None, None]])
                            put_html("""<hr>""")

                    def slo(driver):
                        ###################################################################################
                        with use_scope('info', clear=True):
                            put_success('catching the driver waiting for 10 open instagram Page.....')
                        time.sleep(9)  # 1
                        driver.get('https://www.instagram.com/')
                        with use_scope('info', clear=True):
                            put_success('catching the cok returns ..........')
                        time.sleep(9)  # 2
                        try:
                            driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]').click()
                            with use_scope('info', clear=True):

                                put_success('catching the cok returns done... without any problem...')
                        except:
                            with use_scope('info', clear=True):
                                put_error('trying to get cok return wait ......')
                                driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]').click()
                                time.sleep(2)
                                put_success('here we go ....!')
                                pass

                        time.sleep(2)

                        with use_scope('info', clear=True):
                            put_success(f'........!Return   Your User [{myuse[-1]}] !...... ')
                        us = driver.find_element(By.XPATH,
                                                 '//*[@id="loginForm"]/div/div[1]/div/label/input')

                        us.clear()
                        us.send_keys(str(myuse[-1]))
                        with use_scope('info', clear=True):
                            put_success(f'.....![{myuse[-1]}] Inserted !..... ')
                        with use_scope('info', clear=True):

                            put_success(f'.....! Return  Your Password [{mypas[-1]}] !.....')
                        p = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
                        p.clear()
                        p.send_keys(str(mypas[-1]))
                        with use_scope('info', clear=True):
                            put_success(f'.....! [{mypas[-1]}] Inserted !.....')
                            time.sleep(1)

                        with use_scope('info', clear=True):
                            put_warning(
                                f'If you did not set the password or the user correctly, the program will stop after pressing...')

                        driver.find_element(By.XPATH,
                                            '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()

                        with use_scope('info', clear=True):
                            put_warning(f'Log in to your account user={myuse[-1]}  pass={mypas[-1]} ...  ')
                            time.sleep(2)
                        with use_scope('info', clear=True):
                            put_warning(f'............   wait   ............    ')
                            time.sleep(2)
                        with use_scope('info', clear=True):
                            put_warning(f'............   ^_^   ............    ')
                            time.sleep(2)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiAi   ............    ')
                            time.sleep(2)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiTr   ............    ')
                            time.sleep(2)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiData   ............    ')
                            time.sleep(2)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiEis   ............    ')
                            time.sleep(1)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiMl   ............    ')
                            time.sleep(2)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiTb   ............    ')
                            time.sleep(1)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiHere   ............    ')
                            time.sleep(1)
                        with use_scope('info', clear=True):
                            put_warning(f'............   FOR YOU ^_^   ............    ')
                        with use_scope('info', clear=True):
                            put_success(f'............ A world still an idea .............. \n '
                                        f'    Welcome. We hope you will have a wonderful experience that you will like.  \n............ We are still running ............\n   ')
                            time.sleep(2)
                            with use_scope('info', clear=True):
                                put_warning(f'           ............ A world still an idea .............. \n '
                                            f'           >>>>>>>>>>>>>>>>>>>MoiEis<<<<<<<<<<<<<<<<<<<<<<<<< \n'
                                            f'           >>>>>>>>>>>>>>> Free services <<<<<<<<<<<<<<<<<<<<\n'
                                            f'           >>>>Created to create new worlds only of ideas<<<<')

                            driver.get('https://znap.link/MoiCbio')
                            with use_scope('info', clear=True):
                                put_widget(
                                    f'If you want to find out more about us, the site will be displayed once, you will find all my accounts')
                            time.sleep(1)

                        for i in range(int(rang[-1])):  # time of reported
                            if i != rang[-1]:
                                try:

                                    with use_scope('info', clear=True):
                                        put_success(
                                            f'            ............ A world still an idea .............. \n '
                                            f'            >>>>>>>>>>>>>>>>>>>Moidata<<<<<<<<<<<<<<<<<<<<<<<< \n'
                                            f'            >>>>>>>>>>>>>>> Free services <<<<<<<<<<<<<<<<<<<<\n'
                                            f'            >>>>Created to create new worlds only of ideas<<<<')
                                        time.sleep(2)
                                        toast('starting ......', color='info')
                                    with use_scope('info', clear=True):
                                        put_success(f'opening the for {user[-1]} .....')
                                    driver.get(f'https://www.instagram.com/{user[-1]}/')
                                    with use_scope('info', clear=True):
                                        put_warning(f'waiting for 4 sce .....')
                                    time.sleep(5)
                                    with use_scope('info', clear=True):
                                        put_success(
                                            f'here is the steps of spam reporter >>>>Catching >>> {user[-1]} <<< .....')
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[2]/button').click()
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]').click()
                                    with use_scope('info', clear=True):
                                        put_success(
                                            f' watch... >>>>>>>>>>>>>Catching >>> {user[-1]} <<< .....')
                                    time.sleep(3)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]').click()
                                    time.sleep(3)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[1]').click()
                                    time.sleep(3)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[1]').click()
                                    time.sleep(2)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div[4]/button').click()
                                    with use_scope('info', clear=True):
                                        put_success(
                                            f'Done as super MoInsta for >>> {user[-1]} still on {int(i)} <<< .....')


                                except:
                                    with use_scope('info', clear=True):
                                        put_error(
                                            f'>>>>Please use the specified speed and capacity on your device<<<<')

                            else:

                                with use_scope('info', clear=True):
                                    put_success(
                                        f'All ATT Done Super Moinsta for >>> {user[-1]} <<< .....')  ##

                    def med(driver):
                        ###################################################################################
                        with use_scope('info', clear=True):
                            put_success('catching the driver waiting for 10 open instagram Page.....')
                        time.sleep(4)  # 1
                        driver.get('https://www.instagram.com/')
                        with use_scope('info', clear=True):
                            put_success('catching the cok returns ..........')
                        time.sleep(4)  # 2
                        try:
                            driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]').click()
                            with use_scope('info', clear=True):

                                put_success('catching the cok returns done... without any problem...')
                        except:
                            with use_scope('info', clear=True):
                                put_error('trying to get cok return wait ......')
                                driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]').click()
                                time.sleep(2)
                                put_success('here we go ....!')
                                pass

                        time.sleep(1.3)

                        with use_scope('info', clear=True):
                            put_success(f'........!Return   Your User [{myuse[-1]}] !...... ')
                        us = driver.find_element(By.XPATH,
                                                 '//*[@id="loginForm"]/div/div[1]/div/label/input')

                        us.clear()
                        us.send_keys(str(myuse[-1]))
                        with use_scope('info', clear=True):
                            put_success(f'.....![{myuse[-1]}] Inserted !..... ')
                        with use_scope('info', clear=True):

                            put_success(f'.....! Return  Your Password [{mypas[-1]}] !.....')
                        p = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
                        p.clear()
                        p.send_keys(str(mypas[-1]))
                        with use_scope('info', clear=True):
                            put_success(f'.....! [{mypas[-1]}] Inserted !.....')
                            time.sleep(0.8)
                        ######################### insta err returns #####################################

                        #################################################################################
                        with use_scope('info', clear=True):
                            put_warning(
                                f'If you did not set the password or the user correctly, the program will stop after pressing...')

                            ##################################### insta entry to accounts bugs ##########################################################

                            driver.find_element(By.XPATH,
                                                '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
                            time.sleep(4)

                            ere1 = [0]

                            try:
                                put_text(driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]').text)
                                ere = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]  ').text
                                ere1.append(str(ere))



                            except:
                                with use_scope('info', clear=True):
                                    put_error(f' code a ! l&87 <moier>')
                                    time.sleep(0.3)
                            use_er = "The username you entered doesn't belong to an account. Please check your username and try again."
                            pas_er = "Sorry, your password was incorrect. Please double-check your password."
                            net_er = "We couldn't connect to Instagram. Make sure you're connected to the internet and try again."
                            erer = "The username you entered doesn't belong to an account. Please check your username and try again."
                            ########## 1 ###########

                            if ere1[-1] == use_er:

                                with use_scope('info', clear=True):
                                    put_error(f'ERROR ........ ')
                                time.sleep(0.3)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        f"The cause of the problem is now examined using MoiAi's simplified mindset .....")
                                    time.sleep(0.3)
                                with use_scope('info', clear=True):
                                    put_warning(f" circuit in logic functions .....")
                                with use_scope('info', clear=True):
                                    put_success(f"......... over here ..........")
                                time.sleep(0.3)
                                with use_scope('info', clear=True):
                                    put_error(f"......... If he knew the reason, the hero of wonder ..........")
                                time.sleep(0.3)
                                with use_scope('info', clear=True):
                                    put_error(f"......... If he knew the reason, the hero of wonder ..........")
                                time.sleep(0.3)
                                with use_scope('info', clear=True):
                                    put_error(
                                        f"......... The problem has been detected, translation is in progress ..........")
                                time.sleep(0.3)
                                with use_scope('info', clear=True):
                                    put_error(
                                        f"......... The problem is that the username ->[{myuse[-1]}]<- is not found in the databases in Instagram ..........")
                                time.sleep(0.3)
                                with use_scope('info', clear=True):
                                    put_success(
                                        f"......... You will be redirected to modify the data you entered ..........")
                                    return exap()  #
                            ########## 2 ###########
                            elif ere1[-1] == pas_er:

                                with use_scope('info', clear=True):

                                    put_error(f'ERROR PASS  ----->{pas_er}<-----\n For  ---------------> {mypas[-1]} ')

                                time.sleep(0.5)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        f"The cause of the problem is now examined using MoiAi's simplified mindset .....")
                                    time.sleep(0.3)
                                with use_scope('info', clear=True):
                                    put_warning(f" circuit in logic functions .....")
                                with use_scope('info', clear=True):
                                    put_success(f"......... over here ..........")
                                time.sleep(0.2)
                                with use_scope('info', clear=True):
                                    put_error(f"......... If he knew the reason, the hero of wonder ..........")
                                time.sleep(0.2)
                                with use_scope('info', clear=True):
                                    put_error(f"......... If he knew the reason, the hero of wonder ..........")
                                time.sleep(0.2)
                                with use_scope('info', clear=True):
                                    put_error(
                                        f"......... The problem has been detected, translation is in progress  ..........")
                                time.sleep(0.3)
                                with use_scope('info', clear=True):
                                    put_error(f" insta users .... Return [{myuse[-1]}] as True .... ")
                                with use_scope('info', clear=True):
                                    time.sleep(0.3)
                                    put_warning(
                                        f"......... The problem is that the Passowrd ->[{mypas[-1]}]<- is not found in the databases in Instagram ..........")
                                time.sleep(0.4)
                                with use_scope('info', clear=True):
                                    put_success(
                                        f"......... You will be redirected to modify the data you entered ..........")
                                    return exap()


                            elif ere1[-1] != use_er and pas_er and net_er and erer:

                                pass

                        with use_scope('info', clear=True):
                            put_warning(f'Log in to your account user={myuse[-1]}  pass={mypas[-1]} ...  ')
                            time.sleep(0.1)
                        with use_scope('info', clear=True):
                            put_warning(f'............   wait   ............    ')
                            time.sleep(0.3)
                        with use_scope('info', clear=True):
                            put_warning(f'............   ^_^   ............    ')
                            time.sleep(0.2)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiAi   ............    ')
                            time.sleep(0.2)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiTr   ............    ')
                            time.sleep(0.3)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiData   ............    ')
                            time.sleep(0.1)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiEis   ............    ')
                            time.sleep(0.3)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiMl   ............    ')
                            time.sleep(0.3)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiTb   ............    ')
                            time.sleep(0.5)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiHere   ............    ')
                            time.sleep(0.2)
                        with use_scope('info', clear=True):
                            put_success(f'............   FOR YOU ^_^   ............    ')
                            time.sleep(1)
                        with use_scope('info', clear=True):
                            put_success(f'............ A world still an idea .............. \n '
                                        f'    Welcome. We hope you will have a wonderful experience that you will like.  \n............ We are still running ............\n   ')
                            time.sleep(1)
                            with use_scope('info', clear=True):
                                put_warning(f'           ............ A world still an idea .............. \n '
                                            f'           >>>>>>>>>>>>>>>>>>>MoiEis<<<<<<<<<<<<<<<<<<<<<<<<< \n'
                                            f'           >>>>>>>>>>>>>>> Free services <<<<<<<<<<<<<<<<<<<<\n'
                                            f'           >>>>Created to create new worlds only of ideas<<<<')

                            driver.get('https://znap.link/MoiCbio')
                            with use_scope('info', clear=True):
                                put_error(
                                    f'If you want to find out more about us, the site will be displayed once, you will find all my accounts',
                                    closable=True)
                            time.sleep(0.2)

                        for i in range(int(rang[-1])):  # time of reported
                            if i != rang[-1]:
                                try:
                                    clear(scope='info')

                                    ################################### account ###############################
                                    def acc():
                                        def update_acc():
                                            myuse.append(pin.newu)
                                            mypas.append(pin.newp)

                                            reeeec(driver)

                                        popup('Edit Your Account : ',
                                              put_grid([[None, None, put_text('Your Username:'), None, None],
                                                        [None, None, put_input('newu', value=myuse[-1]), None, None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_text('Your Password:'), None, None],
                                                        [None, None, put_input('newp', value=mypas[-1]), None, None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_html('''<button class="btn">
                                    <span class="btn-text-one">Save</span>
                                    <span class="btn-text-two">may restart</span>
                                </button>

                                <style>/* From uiverse.io by @mobinkakei */
                                .btn {
                                  width: 140px;
                                  height: 50px;
                                  background: linear-gradient(to top, #2bbab1, #12376e, #23487f);
                                  color: #fff;
                                  border-radius: 50px;
                                  border: none;
                                  outline: none;
                                  cursor: pointer;
                                  position: relative;
                                  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
                                  overflow: hidden;
                                }

                                .btn span {
                                  font-size: 12px;
                                  text-transform: uppercase;
                                  letter-spacing: 1px;
                                  transition: top 0.5s;
                                }

                                .btn-text-one {
                                  position: absolute;
                                  width: 100%;
                                  top: 50%;
                                  left: 0;
                                  transform: translateY(-50%);
                                }

                                .btn-text-two {
                                  position: absolute;
                                  width: 100%;
                                  top: 150%;
                                  left: 0;
                                  transform: translateY(-50%);
                                }

                                .btn:hover .btn-text-one {
                                  top: -100%;
                                }

                                .btn:hover .btn-text-two {
                                  top: 50%;
                                }
                                </style>''').onclick(update_acc), None, None], ]))

                                    def att():
                                        def update_acc():
                                            user.append(pin.newatt)
                                            reeeec(driver)

                                        popup('rename user goal : : ',
                                              put_grid([[None, None, put_text('Att This User :'), None, None],
                                                        [None, None, put_input('newatt', value=user[-1]), None, None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_html('''<button class="btn">
                                                                        <span class="btn-text-one">Save</span>
                                                                        <span class="btn-text-two">may restart</span>
                                                                    </button>

                                                                    <style>/* From uiverse.io by @mobinkakei */
                                                                    .btn {
                                                                      width: 140px;
                                                                      height: 50px;
                                                                      background: linear-gradient(to top, #2bbab1, #12376e, #23487f);
                                                                      color: #fff;
                                                                      border-radius: 50px;
                                                                      border: none;
                                                                      outline: none;
                                                                      cursor: pointer;
                                                                      position: relative;
                                                                      box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
                                                                      overflow: hidden;
                                                                    }

                                                                    .btn span {
                                                                      font-size: 12px;
                                                                      text-transform: uppercase;
                                                                      letter-spacing: 1px;
                                                                      transition: top 0.5s;
                                                                    }

                                                                    .btn-text-one {
                                                                      position: absolute;
                                                                      width: 100%;
                                                                      top: 50%;
                                                                      left: 0;
                                                                      transform: translateY(-50%);
                                                                    }

                                                                    .btn-text-two {
                                                                      position: absolute;
                                                                      width: 100%;
                                                                      top: 150%;
                                                                      left: 0;
                                                                      transform: translateY(-50%);
                                                                    }

                                                                    .btn:hover .btn-text-one {
                                                                      top: -100%;
                                                                    }

                                                                    .btn:hover .btn-text-two {
                                                                      top: 50%;
                                                                    }
                                                                    </style>''').onclick(update_acc), None, None], ]))

                                    def ran():

                                        def update_acc():
                                            rang.append(pin.rn)
                                            reeeec(driver)

                                        popup('range the times : ',
                                              put_grid([[None, None, put_text('For  :'), None, None],
                                                        [None, None, put_input('rn', value=rang[-1], type=NUMBER), None,
                                                         None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_html('''<button class="btn">
                                                                            <span class="btn-text-one">Save</span>
                                                                            <span class="btn-text-two">may restart</span>
                                                                        </button>

                                                                        <style>/* From uiverse.io by @mobinkakei */
                                                                        .btn {
                                                                          width: 140px;
                                                                          height: 50px;
                                                                          background: linear-gradient(to top, #2bbab1, #12376e, #23487f);
                                                                          color: #fff;
                                                                          border-radius: 50px;
                                                                          border: none;
                                                                          outline: none;
                                                                          cursor: pointer;
                                                                          position: relative;
                                                                          box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
                                                                          overflow: hidden;
                                                                        }

                                                                        .btn span {
                                                                          font-size: 12px;
                                                                          text-transform: uppercase;
                                                                          letter-spacing: 1px;
                                                                          transition: top 0.5s;
                                                                        }

                                                                        .btn-text-one {
                                                                          position: absolute;
                                                                          width: 100%;
                                                                          top: 50%;
                                                                          left: 0;
                                                                          transform: translateY(-50%);
                                                                        }

                                                                        .btn-text-two {
                                                                          position: absolute;
                                                                          width: 100%;
                                                                          top: 150%;
                                                                          left: 0;
                                                                          transform: translateY(-50%);
                                                                        }

                                                                        .btn:hover .btn-text-one {
                                                                          top: -100%;
                                                                        }

                                                                        .btn:hover .btn-text-two {
                                                                          top: 50%;
                                                                        }
                                                                        </style>''').onclick(update_acc), None, None]]))

                                    def sp():

                                        def update_acc():
                                            rang.append(pin.spod)
                                            reeeec(driver)

                                        popup('select speed of attack  : ',
                                              put_grid([[None, None, put_text('your speed is :'), None, None],
                                                        [None, None, put_select('spod', value=speed[-1],
                                                                                options=['recommended', 'fast',
                                                                                         'Medium',
                                                                                         'slow']), None,
                                                         None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_html('''<button class="btn">
                                                                            <span class="btn-text-one">Save</span>
                                                                            <span class="btn-text-two">may restart</span>
                                                                        </button>

                                                                        <style>/* From uiverse.io by @mobinkakei */
                                                                        .btn {
                                                                          width: 140px;
                                                                          height: 50px;
                                                                          background: linear-gradient(to top, #2bbab1, #12376e, #23487f);
                                                                          color: #fff;
                                                                          border-radius: 50px;
                                                                          border: none;
                                                                          outline: none;
                                                                          cursor: pointer;
                                                                          position: relative;
                                                                          box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
                                                                          overflow: hidden;
                                                                        }

                                                                        .btn span {
                                                                          font-size: 12px;
                                                                          text-transform: uppercase;
                                                                          letter-spacing: 1px;
                                                                          transition: top 0.5s;
                                                                        }

                                                                        .btn-text-one {
                                                                          position: absolute;
                                                                          width: 100%;
                                                                          top: 50%;
                                                                          left: 0;
                                                                          transform: translateY(-50%);
                                                                        }

                                                                        .btn-text-two {
                                                                          position: absolute;
                                                                          width: 100%;
                                                                          top: 150%;
                                                                          left: 0;
                                                                          transform: translateY(-50%);
                                                                        }

                                                                        .btn:hover .btn-text-one {
                                                                          top: -100%;
                                                                        }

                                                                        .btn:hover .btn-text-two {
                                                                          top: 50%;
                                                                        }
                                                                        </style>''').onclick(update_acc), None, None]]))

                                    #################################### Edit #################################
                                    def edit():
                                        popup('Choose what you want to edit :', put_grid([[None, None, span(put_html('''<button class="cta">
                                                                    <span class="hover-underline-animation">My Account</span>
                                                                    <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                                        <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                                    </svg>
                                                                </button>

                                                                <style>/* From uiverse.io by @alexmaracinaru */
                                                                .cta {
                                                                  border: none;
                                                                  background: none;
                                                                }

                                                                .cta span {
                                                                  padding-bottom: 7px;
                                                                  letter-spacing: 4px;
                                                                  font-size: 9px;
                                                                  padding-right: 15px;
                                                                  text-transform: uppercase;
                                                                }

                                                                .cta svg {
                                                                  transform: translateX(-8px);
                                                                  transition: all 0.3s ease;
                                                                }

                                                                .cta:hover svg {
                                                                  transform: translateX(0);
                                                                }

                                                                .cta:active svg {
                                                                  transform: scale(0.9);
                                                                }

                                                                .hover-underline-animation {
                                                                  position: relative;
                                                                  color: black;
                                                                  padding-bottom: 20px;
                                                                }

                                                                .hover-underline-animation:after {
                                                                  content: "";
                                                                  position: absolute;
                                                                  width: 100%;
                                                                  transform: scaleX(0);
                                                                  height: 2px;
                                                                  bottom: 0;
                                                                  left: 0;
                                                                  background-color: #000000;
                                                                  transform-origin: bottom right;
                                                                  transition: transform 0.25s ease-out;
                                                                }

                                                                .cta:hover .hover-underline-animation:after {
                                                                  transform: scaleX(1);
                                                                  transform-origin: bottom left;
                                                                }</style>''').onclick(acc), col=2, row=1), None, None],
                                                                                          [None, None,
                                                                                           span(put_html('<hr>'), col=2,
                                                                                                row=1), None, None],
                                                                                          [None, None, span(put_html('''<button class="cta">
                                                                    <span class="hover-underline-animation">Attk User</span>
                                                                    <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                                        <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                                    </svg>
                                                                </button>

                                                                <style>/* From uiverse.io by @alexmaracinaru */
                                                                .cta {
                                                                  border: none;
                                                                  background: none;
                                                                }

                                                                .cta span {
                                                                  padding-bottom: 7px;
                                                                  letter-spacing: 4px;
                                                                  font-size: 14px;
                                                                  padding-right: 15px;
                                                                  text-transform: uppercase;
                                                                }

                                                                .cta svg {
                                                                  transform: translateX(-8px);
                                                                  transition: all 0.3s ease;
                                                                }

                                                                .cta:hover svg {
                                                                  transform: translateX(0);
                                                                }

                                                                .cta:active svg {
                                                                  transform: scale(0.9);
                                                                }

                                                                .hover-underline-animation {
                                                                  position: relative;
                                                                  color: black;
                                                                  padding-bottom: 20px;
                                                                }

                                                                .hover-underline-animation:after {
                                                                  content: "";
                                                                  position: absolute;
                                                                  width: 100%;
                                                                  transform: scaleX(0);
                                                                  height: 2px;
                                                                  bottom: 0;
                                                                  left: 0;
                                                                  background-color: #000000;
                                                                  transform-origin: bottom right;
                                                                  transition: transform 0.25s ease-out;
                                                                }

                                                                .cta:hover .hover-underline-animation:after {
                                                                  transform: scaleX(1);
                                                                  transform-origin: bottom left;
                                                                }</style>''').onclick(att), col=2, row=1), None, None],
                                                                                          [None, None,
                                                                                           span(put_html('<hr>'), col=2,
                                                                                                row=1), None, None],
                                                                                          [None, None, span(put_html('''<button class="cta">
                                                                    <span class="hover-underline-animation">Range</span>
                                                                    <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                                        <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                                    </svg>
                                                                </button>

                                                                <style>/* From uiverse.io by @alexmaracinaru */
                                                                .cta {
                                                                  border: none;
                                                                  background: none;
                                                                }

                                                                .cta span {
                                                                  padding-bottom: 7px;
                                                                  letter-spacing: 4px;
                                                                  font-size: 14px;
                                                                  padding-right: 15px;
                                                                  text-transform: uppercase;
                                                                }

                                                                .cta svg {
                                                                  transform: translateX(-8px);
                                                                  transition: all 0.3s ease;
                                                                }

                                                                .cta:hover svg {
                                                                  transform: translateX(0);
                                                                }

                                                                .cta:active svg {
                                                                  transform: scale(0.9);
                                                                }

                                                                .hover-underline-animation {
                                                                  position: relative;
                                                                  color: black;
                                                                  padding-bottom: 20px;
                                                                }

                                                                .hover-underline-animation:after {
                                                                  content: "";
                                                                  position: absolute;
                                                                  width: 100%;
                                                                  transform: scaleX(0);
                                                                  height: 2px;
                                                                  bottom: 0;
                                                                  left: 0;
                                                                  background-color: #000000;
                                                                  transform-origin: bottom right;
                                                                  transition: transform 0.25s ease-out;
                                                                }

                                                                .cta:hover .hover-underline-animation:after {
                                                                  transform: scaleX(1);
                                                                  transform-origin: bottom left;
                                                                }</style>''').onclick(ran), col=2, row=1), None, None],
                                                                                          [None, None,
                                                                                           span(put_html('<hr>'), col=2,
                                                                                                row=1), None, None],
                                                                                          [None, None, span(put_html('''<button class="cta">
                                                                    <span class="hover-underline-animation">Speed</span>
                                                                    <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                                        <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                                    </svg>
                                                                </button>

                                                                <style>/* From uiverse.io by @alexmaracinaru */
                                                                .cta {
                                                                  border: none;
                                                                  background: none;
                                                                }

                                                                .cta span {
                                                                  padding-bottom: 7px;
                                                                  letter-spacing: 4px;
                                                                  font-size: 14px;
                                                                  padding-right: 15px;
                                                                  text-transform: uppercase;
                                                                }

                                                                .cta svg {
                                                                  transform: translateX(-8px);
                                                                  transition: all 0.3s ease;
                                                                }

                                                                .cta:hover svg {
                                                                  transform: translateX(0);
                                                                }

                                                                .cta:active svg {
                                                                  transform: scale(0.9);
                                                                }

                                                                .hover-underline-animation {
                                                                  position: relative;
                                                                  color: black;
                                                                  padding-bottom: 20px;
                                                                }

                                                                .hover-underline-animation:after {
                                                                  content: "";
                                                                  position: absolute;
                                                                  width: 100%;
                                                                  transform: scaleX(0);
                                                                  height: 2px;
                                                                  bottom: 0;
                                                                  left: 0;
                                                                  background-color: #000000;
                                                                  transform-origin: bottom right;
                                                                  transition: transform 0.25s ease-out;
                                                                }

                                                                .cta:hover .hover-underline-animation:after {
                                                                  transform: scaleX(1);
                                                                  transform-origin: bottom left;
                                                                }</style>''').onclick(sp), col=2, row=1), None, None]]),
                                              closable=True, implicit_close=False)

                                    ###########################################################################

                                    with use_scope('chose', clear=True):

                                        sty = '''<style>
                                                                                                        .styled-table {
                                                                                                            border-collapse: collapse;
                                                                                                            margin: center;
                                                                                                            font-size: 0.9em;
                                                                                                            font-family: sans-serif;


                                                                                                        }
                                                                                                        .styled-table thead tr {
                                                                                                            background-color: #2bbab1;
                                                                                                            color: #ffffff;
                                                                                                            text-align: left;
                                                                                                        }
                                                                                                        .styled-table th,
                                                                                                        .styled-table td {
                                                                                                            padding: 12px 15px;
                                                                                                        }

                                                                                                        .styled-table tbody tr {
                                                                                                            border-bottom: 1px solid #dddddd;
                                                                                                        }

                                                                                                        .styled-table tbody tr:nth-of-type(even) {
                                                                                                            background-color: #2bbab1;
                                                                                                        }

                                                                                                        .styled-table tbody tr:last-of-type {
                                                                                                            border-bottom: 2px solid #2bbab1;
                                                                                                        }
                                                                                                        .styled-table tbody tr.active-row {
                                                                                                            font-weight: bold;
                                                                                                            color: #2bbab1;
                                                                                                        }
                                                                                                        </style>'''
                                        put_grid([[None, None, None, None, put_html(f'''<table class="styled-table">
                                                                        <thead>
                                                                            <tr>

                                                                                <th>My User</th>
                                                                                <th>Att User</th>
                                                                                <th>Range input </th>
                                                                                <th>Range Now </th>
                                                                                <th>speed</th>
                                                                            </tr>
                                                                        </thead>
                                                                        <tbody>

                                                                            <tr class="active-row">
                                                                                <td>{myuse[-1]}</td>
                                                                                <td>{user[-1]}</td>
                                                                                <td>{rang[-1]}</td>
                                                                                <td>{i}</td>
                                                                                <td>{speed[-1]}</td>
                                                                            </tr>
                                                                            <!-- and so on... -->
                                                                        </tbody>
                                                                    </table>
                                                                    {sty}
                                                                    '''), None, None, None, None]])
                                        put_grid([[None, None, None, None, put_html('''<button class="btn">
                                                                               <span class="icon">
                                                                                   <svg viewBox="0 0 175 80" width="30" height="30">
                                                                                       <rect width="40" height="15" fill="#f0f0f0" rx="10"></rect>
                                                                                       <rect y="30" width="80" height="15" fill="#f0f0f0" rx="10"></rect>
                                                                                       <rect y="60" width="80" height="15" fill="#f0f0f0" rx="10"></rect>
                                                                                   </svg>
                                                                               </span>
                                                                               <span class="text">Customize</span>
                                                                           </button>
                                                                           <style>/* From uiverse.io by @gagan-gv */
                                                                           .btn {
                                                                             width: 160px;
                                                                             height: 37px;
                                                                             border-radius: 3px;
                                                                             border: none;
                                                                             transition: all 0.5s ease-in-out;
                                                                             font-size: 14px;
                                                                             font-family: Verdana, Geneva, Tahoma, sans-serif;
                                                                             font-weight: 700;
                                                                             display: flex;
                                                                             align-items: center;
                                                                             background: #2bbab1;
                                                                             color: #f5f5f5;
                                                                           }

                                                                           .btn:hover {
                                                                             box-shadow: 0 0 20px 0px #2e2e2e3a;
                                                                           }

                                                                           .btn .icon {
                                                                             position: absolute;
                                                                             height: 40px;
                                                                             width: 70px;
                                                                             display: flex;
                                                                             justify-content: center;
                                                                             align-items: center;
                                                                             transition: all 0.5s;
                                                                           }

                                                                           .btn .text {
                                                                             transform: translateX(55px);
                                                                           }

                                                                           .btn:hover .icon {
                                                                             width: 175px;
                                                                           }

                                                                           .btn:hover .text {
                                                                             transition: all 0.5s;
                                                                             opacity: 0;
                                                                           }

                                                                           .btn:focus {
                                                                             outline: none;
                                                                           }

                                                                           .btn:active .icon {
                                                                             transform: scale(0.85);
                                                                           }</style>''').onclick(edit), None, None,
                                                   None, None]])
                                        put_html("""<hr>""")

                                    with use_scope('info', clear=True):
                                        put_success(
                                            f'            ............ A world still an idea .............. \n '
                                            f'            >>>>>>>>>>>>>>>>>>>Moidata<<<<<<<<<<<<<<<<<<<<<<<< \n'
                                            f'            >>>>>>>>>>>>>>> Free services <<<<<<<<<<<<<<<<<<<<\n'
                                            f'            >>>>Created to create new worlds only of ideas<<<<')
                                        time.sleep(1)
                                        toast(f'starting ..for {i}....', color='info')
                                    with use_scope('info', clear=True):
                                        put_success(f'opening the for {user[-1]} .....')
                                    driver.get(f'https://www.instagram.com/{user[-1]}/')
                                    with use_scope('info', clear=True):
                                        put_warning(f'waiting for 4 sce .....')
                                    time.sleep(1)
                                    with use_scope('info', clear=True):
                                        put_success(
                                            f'here is the steps of spam reporter >>>>Catching >>> {user[-1]} <<< .....')
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[2]/button').click()
                                    time.sleep(1.3)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]').click()
                                    with use_scope('info', clear=True):
                                        put_success(
                                            f' watch... >>>>>>>>>>>>>Catching >>> {user[-1]} <<< .....')
                                    time.sleep(1.3)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]').click()
                                    time.sleep(1.3)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]').click()
                                    time.sleep(1.3)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]').click()
                                    time.sleep(1.2)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div[4]/button').click()
                                    with use_scope('info', clear=True):
                                        put_success(
                                            f'Done as super MoInsta for >>> {user[-1]} still on {int(i)} <<< .....')
                                        time.sleep(0.2)


                                except:
                                    with use_scope('info', clear=True):
                                        put_error(
                                            f'>>>>Please use the specified speed and capacity on your device<<<<')
                                        time.sleep(2)
                                        with use_scope('info', clear=True):
                                            put_error(
                                                f'...............................Back()...............................')

                                        time.sleep(1.8)

                                        ch()
                                        break


                            else:

                                with use_scope('info', clear=True):
                                    driver.get('https://znap.link/MoiCbio')
                                    put_success(
                                        f'All ATT Done Super Moinsta for >>> {user[-1]} <<< .....')  ##

                    def reeeec(driver):
                        ###################################################################################
                        with use_scope('info', clear=True):
                            put_success('catching the driver waiting for 10 open instagram Page.....')
                        time.sleep(7)  # 1
                        driver.get('https://www.instagram.com/')
                        with use_scope('info', clear=True):
                            put_success('catching the cok returns ..........')
                        time.sleep(7)  # 2
                        try:
                            driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]').click()
                            with use_scope('info', clear=True):

                                put_success('catching the cok returns done... without any problem...')
                        except:
                            with use_scope('info', clear=True):
                                put_error('trying to get cok return wait ......')
                                driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]').click()
                                time.sleep(2)
                                put_success('here we go ....!')
                                pass

                        time.sleep(2)

                        with use_scope('info', clear=True):
                            put_success(f'........!Return   Your User [{myuse[-1]}] !...... ')
                        us = driver.find_element(By.XPATH,
                                                 '//*[@id="loginForm"]/div/div[1]/div/label/input')

                        us.clear()
                        us.send_keys(str(myuse[-1]))
                        with use_scope('info', clear=True):
                            put_success(f'.....![{myuse[-1]}] Inserted !..... ')
                        with use_scope('info', clear=True):

                            put_success(f'.....! Return  Your Password [{mypas[-1]}] !.....')
                        p = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
                        p.clear()
                        p.send_keys(str(mypas[-1]))
                        with use_scope('info', clear=True):
                            put_success(f'.....! [{mypas[-1]}] Inserted !.....')
                            time.sleep(1)
                        ######################### insta err returns #####################################

                        #################################################################################
                        with use_scope('info', clear=True):
                            put_warning(
                                f'If you did not set the password or the user correctly, the program will stop after pressing...')

                            ##################################### insta entry to accounts bugs ##########################################################

                            driver.find_element(By.XPATH,
                                                '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
                            time.sleep(5)

                            ere1 = [0]

                            try:
                                put_text(driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]').text)
                                ere = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]  ').text
                                ere1.append(str(ere))



                            except:
                                with use_scope('info', clear=True):
                                    put_error(f' code a ! l&87 <moier>')
                                    time.sleep(2)
                            use_er = "The username you entered doesn't belong to an account. Please check your username and try again."
                            pas_er = "Sorry, your password was incorrect. Please double-check your password."
                            net_er = "We couldn't connect to Instagram. Make sure you're connected to the internet and try again."
                            erer = "The username you entered doesn't belong to an account. Please check your username and try again."
                            ########## 1 ###########

                            if ere1[-1] == use_er:

                                with use_scope('info', clear=True):
                                    put_error(f'ERROR ........ ')
                                time.sleep(2)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        f"The cause of the problem is now examined using MoiAi's simplified mindset .....")
                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning(f" circuit in logic functions .....")
                                with use_scope('info', clear=True):
                                    put_success(f"......... over here ..........")
                                time.sleep(1)
                                with use_scope('info', clear=True):
                                    put_error(f"......... If he knew the reason, the hero of wonder ..........")
                                time.sleep(1)
                                with use_scope('info', clear=True):
                                    put_error(f"......... If he knew the reason, the hero of wonder ..........")
                                time.sleep(1)
                                with use_scope('info', clear=True):
                                    put_error(
                                        f"......... The problem has been detected, translation is in progress ..........")
                                time.sleep(0.9)
                                with use_scope('info', clear=True):
                                    put_error(
                                        f"......... The problem is that the username ->[{myuse[-1]}]<- is not found in the databases in Instagram ..........")
                                time.sleep(0.9)
                                with use_scope('info', clear=True):
                                    put_success(
                                        f"......... You will be redirected to modify the data you entered ..........")
                                    return exap()  #
                            ########## 2 ###########
                            elif ere1[-1] == pas_er:

                                with use_scope('info', clear=True):

                                    put_error(f'ERROR PASS  ----->{pas_er}<-----\n For  ---------------> {mypas[-1]} ')

                                time.sleep(2)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        f"The cause of the problem is now examined using MoiAi's simplified mindset .....")
                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning(f" circuit in logic functions .....")
                                with use_scope('info', clear=True):
                                    put_success(f"......... over here ..........")
                                time.sleep(1)
                                with use_scope('info', clear=True):
                                    put_error(f"......... If he knew the reason, the hero of wonder ..........")
                                time.sleep(1)
                                with use_scope('info', clear=True):
                                    put_error(f"......... If he knew the reason, the hero of wonder ..........")
                                time.sleep(1)
                                with use_scope('info', clear=True):
                                    put_error(
                                        f"......... The problem has been detected, translation is in progress  ..........")
                                time.sleep(0.9)
                                with use_scope('info', clear=True):
                                    put_error(f" insta users .... Return [{myuse[-1]}] as True .... ")
                                with use_scope('info', clear=True):
                                    time.sleep(0.9)
                                    put_warning(
                                        f"......... The problem is that the Passowrd ->[{mypas[-1]}]<- is not found in the databases in Instagram ..........")
                                time.sleep(0.9)
                                with use_scope('info', clear=True):
                                    put_success(
                                        f"......... You will be redirected to modify the data you entered ..........")
                                    return exap()


                            elif ere1[-1] != use_er and pas_er and net_er and erer:

                                pass

                        with use_scope('info', clear=True):
                            put_warning(f'Log in to your account user={myuse[-1]}  pass={mypas[-1]} ...  ')
                            time.sleep(2)
                        with use_scope('info', clear=True):
                            put_warning(f'............   wait   ............    ')
                            time.sleep(2)
                        with use_scope('info', clear=True):
                            put_warning(f'............   ^_^   ............    ')
                            time.sleep(0.4)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiAi   ............    ')
                            time.sleep(0.4)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiTr   ............    ')
                            time.sleep(0.5)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiData   ............    ')
                            time.sleep(0.5)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiEis   ............    ')
                            time.sleep(0.5)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiMl   ............    ')
                            time.sleep(0.5)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiTb   ............    ')
                            time.sleep(0.7)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiHere   ............    ')
                            time.sleep(1)
                        with use_scope('info', clear=True):
                            put_success(f'............   FOR YOU ^_^   ............    ')
                            time.sleep(2)
                        with use_scope('info', clear=True):
                            put_success(f'............ A world still an idea .............. \n '
                                        f'    Welcome. We hope you will have a wonderful experience that you will like.  \n............ We are still running ............\n   ')
                            time.sleep(2)
                            with use_scope('info', clear=True):
                                put_warning(f'           ............ A world still an idea .............. \n '
                                            f'           >>>>>>>>>>>>>>>>>>>MoiEis<<<<<<<<<<<<<<<<<<<<<<<<< \n'
                                            f'           >>>>>>>>>>>>>>> Free services <<<<<<<<<<<<<<<<<<<<\n'
                                            f'           >>>>Created to create new worlds only of ideas<<<<')

                            driver.get('https://znap.link/MoiCbio')
                            with use_scope('info', clear=True):
                                put_error(
                                    f'If you want to find out more about us, the site will be displayed once, you will find all my accounts',
                                    closable=True)
                            time.sleep(1)

                        for i in range(int(rang[-1])):  # time of reported
                            if i != rang[-1]:
                                try:
                                    clear(scope='info')

                                    ################################### account ###############################
                                    def acc():
                                        def update_acc():
                                            myuse.append(pin.newu)
                                            mypas.append(pin.newp)

                                            reeeec(driver)

                                        popup('Edit Your Account : ',
                                              put_grid([[None, None, put_text('Your Username:'), None, None],
                                                        [None, None, put_input('newu', value=myuse[-1]), None, None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_text('Your Password:'), None, None],
                                                        [None, None, put_input('newp', value=mypas[-1]), None, None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_html('''<button class="btn">
                <span class="btn-text-one">Save</span>
                <span class="btn-text-two">may restart</span>
            </button>

            <style>/* From uiverse.io by @mobinkakei */
            .btn {
              width: 140px;
              height: 50px;
              background: linear-gradient(to top, #2bbab1, #12376e, #23487f);
              color: #fff;
              border-radius: 50px;
              border: none;
              outline: none;
              cursor: pointer;
              position: relative;
              box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
              overflow: hidden;
            }

            .btn span {
              font-size: 12px;
              text-transform: uppercase;
              letter-spacing: 1px;
              transition: top 0.5s;
            }

            .btn-text-one {
              position: absolute;
              width: 100%;
              top: 50%;
              left: 0;
              transform: translateY(-50%);
            }

            .btn-text-two {
              position: absolute;
              width: 100%;
              top: 150%;
              left: 0;
              transform: translateY(-50%);
            }

            .btn:hover .btn-text-one {
              top: -100%;
            }

            .btn:hover .btn-text-two {
              top: 50%;
            }
            </style>''').onclick(update_acc), None, None], ]))

                                    def att():
                                        def update_acc():
                                            user.append(pin.newatt)
                                            reeeec(driver)

                                        popup('rename user goal : : ',
                                              put_grid([[None, None, put_text('Att This User :'), None, None],
                                                        [None, None, put_input('newatt', value=user[-1]), None, None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_html('''<button class="btn">
                                                    <span class="btn-text-one">Save</span>
                                                    <span class="btn-text-two">may restart</span>
                                                </button>

                                                <style>/* From uiverse.io by @mobinkakei */
                                                .btn {
                                                  width: 140px;
                                                  height: 50px;
                                                  background: linear-gradient(to top, #2bbab1, #12376e, #23487f);
                                                  color: #fff;
                                                  border-radius: 50px;
                                                  border: none;
                                                  outline: none;
                                                  cursor: pointer;
                                                  position: relative;
                                                  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
                                                  overflow: hidden;
                                                }

                                                .btn span {
                                                  font-size: 12px;
                                                  text-transform: uppercase;
                                                  letter-spacing: 1px;
                                                  transition: top 0.5s;
                                                }

                                                .btn-text-one {
                                                  position: absolute;
                                                  width: 100%;
                                                  top: 50%;
                                                  left: 0;
                                                  transform: translateY(-50%);
                                                }

                                                .btn-text-two {
                                                  position: absolute;
                                                  width: 100%;
                                                  top: 150%;
                                                  left: 0;
                                                  transform: translateY(-50%);
                                                }

                                                .btn:hover .btn-text-one {
                                                  top: -100%;
                                                }

                                                .btn:hover .btn-text-two {
                                                  top: 50%;
                                                }
                                                </style>''').onclick(update_acc), None, None], ]))

                                    def ran():

                                        def update_acc():
                                            rang.append(pin.rn)
                                            reeeec(driver)

                                        popup('range the times : ',
                                              put_grid([[None, None, put_text('For  :'), None, None],
                                                        [None, None, put_input('rn', value=rang[-1], type=NUMBER), None,
                                                         None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_html('''<button class="btn">
                                                        <span class="btn-text-one">Save</span>
                                                        <span class="btn-text-two">may restart</span>
                                                    </button>

                                                    <style>/* From uiverse.io by @mobinkakei */
                                                    .btn {
                                                      width: 140px;
                                                      height: 50px;
                                                      background: linear-gradient(to top, #2bbab1, #12376e, #23487f);
                                                      color: #fff;
                                                      border-radius: 50px;
                                                      border: none;
                                                      outline: none;
                                                      cursor: pointer;
                                                      position: relative;
                                                      box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
                                                      overflow: hidden;
                                                    }

                                                    .btn span {
                                                      font-size: 12px;
                                                      text-transform: uppercase;
                                                      letter-spacing: 1px;
                                                      transition: top 0.5s;
                                                    }

                                                    .btn-text-one {
                                                      position: absolute;
                                                      width: 100%;
                                                      top: 50%;
                                                      left: 0;
                                                      transform: translateY(-50%);
                                                    }

                                                    .btn-text-two {
                                                      position: absolute;
                                                      width: 100%;
                                                      top: 150%;
                                                      left: 0;
                                                      transform: translateY(-50%);
                                                    }

                                                    .btn:hover .btn-text-one {
                                                      top: -100%;
                                                    }

                                                    .btn:hover .btn-text-two {
                                                      top: 50%;
                                                    }
                                                    </style>''').onclick(update_acc), None, None]]))

                                    def sp():

                                        def update_acc():
                                            rang.append(pin.spod)
                                            reeeec(driver)

                                        popup('select speed of attack  : ',
                                              put_grid([[None, None, put_text('your speed is :'), None, None],
                                                        [None, None, put_select('spod', value=speed[-1],
                                                                                options=['recommended', 'fast',
                                                                                         'Medium', 'slow']), None,
                                                         None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_html('''<button class="btn">
                                                        <span class="btn-text-one">Save</span>
                                                        <span class="btn-text-two">may restart</span>
                                                    </button>

                                                    <style>/* From uiverse.io by @mobinkakei */
                                                    .btn {
                                                      width: 140px;
                                                      height: 50px;
                                                      background: linear-gradient(to top, #2bbab1, #12376e, #23487f);
                                                      color: #fff;
                                                      border-radius: 50px;
                                                      border: none;
                                                      outline: none;
                                                      cursor: pointer;
                                                      position: relative;
                                                      box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
                                                      overflow: hidden;
                                                    }

                                                    .btn span {
                                                      font-size: 12px;
                                                      text-transform: uppercase;
                                                      letter-spacing: 1px;
                                                      transition: top 0.5s;
                                                    }

                                                    .btn-text-one {
                                                      position: absolute;
                                                      width: 100%;
                                                      top: 50%;
                                                      left: 0;
                                                      transform: translateY(-50%);
                                                    }

                                                    .btn-text-two {
                                                      position: absolute;
                                                      width: 100%;
                                                      top: 150%;
                                                      left: 0;
                                                      transform: translateY(-50%);
                                                    }

                                                    .btn:hover .btn-text-one {
                                                      top: -100%;
                                                    }

                                                    .btn:hover .btn-text-two {
                                                      top: 50%;
                                                    }
                                                    </style>''').onclick(update_acc), None, None]]))

                                    #################################### Edit #################################
                                    def edit():
                                        popup('Choose what you want to edit :', put_grid([[None, None, span(put_html('''<button class="cta">
                                                <span class="hover-underline-animation">My Account</span>
                                                <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                    <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                </svg>
                                            </button>

                                            <style>/* From uiverse.io by @alexmaracinaru */
                                            .cta {
                                              border: none;
                                              background: none;
                                            }

                                            .cta span {
                                              padding-bottom: 7px;
                                              letter-spacing: 4px;
                                              font-size: 9px;
                                              padding-right: 15px;
                                              text-transform: uppercase;
                                            }

                                            .cta svg {
                                              transform: translateX(-8px);
                                              transition: all 0.3s ease;
                                            }

                                            .cta:hover svg {
                                              transform: translateX(0);
                                            }

                                            .cta:active svg {
                                              transform: scale(0.9);
                                            }

                                            .hover-underline-animation {
                                              position: relative;
                                              color: black;
                                              padding-bottom: 20px;
                                            }

                                            .hover-underline-animation:after {
                                              content: "";
                                              position: absolute;
                                              width: 100%;
                                              transform: scaleX(0);
                                              height: 2px;
                                              bottom: 0;
                                              left: 0;
                                              background-color: #000000;
                                              transform-origin: bottom right;
                                              transition: transform 0.25s ease-out;
                                            }

                                            .cta:hover .hover-underline-animation:after {
                                              transform: scaleX(1);
                                              transform-origin: bottom left;
                                            }</style>''').onclick(acc), col=2, row=1), None, None],
                                                                                          [None, None,
                                                                                           span(put_html('<hr>'), col=2,
                                                                                                row=1), None, None],
                                                                                          [None, None, span(put_html('''<button class="cta">
                                                <span class="hover-underline-animation">Attk User</span>
                                                <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                    <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                </svg>
                                            </button>

                                            <style>/* From uiverse.io by @alexmaracinaru */
                                            .cta {
                                              border: none;
                                              background: none;
                                            }

                                            .cta span {
                                              padding-bottom: 7px;
                                              letter-spacing: 4px;
                                              font-size: 14px;
                                              padding-right: 15px;
                                              text-transform: uppercase;
                                            }

                                            .cta svg {
                                              transform: translateX(-8px);
                                              transition: all 0.3s ease;
                                            }

                                            .cta:hover svg {
                                              transform: translateX(0);
                                            }

                                            .cta:active svg {
                                              transform: scale(0.9);
                                            }

                                            .hover-underline-animation {
                                              position: relative;
                                              color: black;
                                              padding-bottom: 20px;
                                            }

                                            .hover-underline-animation:after {
                                              content: "";
                                              position: absolute;
                                              width: 100%;
                                              transform: scaleX(0);
                                              height: 2px;
                                              bottom: 0;
                                              left: 0;
                                              background-color: #000000;
                                              transform-origin: bottom right;
                                              transition: transform 0.25s ease-out;
                                            }

                                            .cta:hover .hover-underline-animation:after {
                                              transform: scaleX(1);
                                              transform-origin: bottom left;
                                            }</style>''').onclick(att), col=2, row=1), None, None],
                                                                                          [None, None,
                                                                                           span(put_html('<hr>'), col=2,
                                                                                                row=1), None, None],
                                                                                          [None, None, span(put_html('''<button class="cta">
                                                <span class="hover-underline-animation">Range</span>
                                                <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                    <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                </svg>
                                            </button>

                                            <style>/* From uiverse.io by @alexmaracinaru */
                                            .cta {
                                              border: none;
                                              background: none;
                                            }

                                            .cta span {
                                              padding-bottom: 7px;
                                              letter-spacing: 4px;
                                              font-size: 14px;
                                              padding-right: 15px;
                                              text-transform: uppercase;
                                            }

                                            .cta svg {
                                              transform: translateX(-8px);
                                              transition: all 0.3s ease;
                                            }

                                            .cta:hover svg {
                                              transform: translateX(0);
                                            }

                                            .cta:active svg {
                                              transform: scale(0.9);
                                            }

                                            .hover-underline-animation {
                                              position: relative;
                                              color: black;
                                              padding-bottom: 20px;
                                            }

                                            .hover-underline-animation:after {
                                              content: "";
                                              position: absolute;
                                              width: 100%;
                                              transform: scaleX(0);
                                              height: 2px;
                                              bottom: 0;
                                              left: 0;
                                              background-color: #000000;
                                              transform-origin: bottom right;
                                              transition: transform 0.25s ease-out;
                                            }

                                            .cta:hover .hover-underline-animation:after {
                                              transform: scaleX(1);
                                              transform-origin: bottom left;
                                            }</style>''').onclick(ran), col=2, row=1), None, None],
                                                                                          [None, None,
                                                                                           span(put_html('<hr>'), col=2,
                                                                                                row=1), None, None],
                                                                                          [None, None, span(put_html('''<button class="cta">
                                                <span class="hover-underline-animation">Speed</span>
                                                <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                    <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                </svg>
                                            </button>

                                            <style>/* From uiverse.io by @alexmaracinaru */
                                            .cta {
                                              border: none;
                                              background: none;
                                            }

                                            .cta span {
                                              padding-bottom: 7px;
                                              letter-spacing: 4px;
                                              font-size: 14px;
                                              padding-right: 15px;
                                              text-transform: uppercase;
                                            }

                                            .cta svg {
                                              transform: translateX(-8px);
                                              transition: all 0.3s ease;
                                            }

                                            .cta:hover svg {
                                              transform: translateX(0);
                                            }

                                            .cta:active svg {
                                              transform: scale(0.9);
                                            }

                                            .hover-underline-animation {
                                              position: relative;
                                              color: black;
                                              padding-bottom: 20px;
                                            }

                                            .hover-underline-animation:after {
                                              content: "";
                                              position: absolute;
                                              width: 100%;
                                              transform: scaleX(0);
                                              height: 2px;
                                              bottom: 0;
                                              left: 0;
                                              background-color: #000000;
                                              transform-origin: bottom right;
                                              transition: transform 0.25s ease-out;
                                            }

                                            .cta:hover .hover-underline-animation:after {
                                              transform: scaleX(1);
                                              transform-origin: bottom left;
                                            }</style>''').onclick(sp), col=2, row=1), None, None]]), closable=True,
                                              implicit_close=False)

                                    ###########################################################################

                                    with use_scope('chose', clear=True):

                                        sty = '''<style>
                                                                                    .styled-table {
                                                                                        border-collapse: collapse;
                                                                                        margin: center;
                                                                                        font-size: 0.9em;
                                                                                        font-family: sans-serif;


                                                                                    }
                                                                                    .styled-table thead tr {
                                                                                        background-color: #2bbab1;
                                                                                        color: #ffffff;
                                                                                        text-align: left;
                                                                                    }
                                                                                    .styled-table th,
                                                                                    .styled-table td {
                                                                                        padding: 12px 15px;
                                                                                    }

                                                                                    .styled-table tbody tr {
                                                                                        border-bottom: 1px solid #dddddd;
                                                                                    }

                                                                                    .styled-table tbody tr:nth-of-type(even) {
                                                                                        background-color: #2bbab1;
                                                                                    }

                                                                                    .styled-table tbody tr:last-of-type {
                                                                                        border-bottom: 2px solid #2bbab1;
                                                                                    }
                                                                                    .styled-table tbody tr.active-row {
                                                                                        font-weight: bold;
                                                                                        color: #2bbab1;
                                                                                    }
                                                                                    </style>'''
                                        put_grid([[None, None, None, None, put_html(f'''<table class="styled-table">
                                                    <thead>
                                                        <tr>

                                                            <th>My User</th>
                                                            <th>Att User</th>
                                                            <th>Range input </th>
                                                            <th>Range Now </th>
                                                            <th>speed</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>

                                                        <tr class="active-row">
                                                            <td>{myuse[-1]}</td>
                                                            <td>{user[-1]}</td>
                                                            <td>{rang[-1]}</td>
                                                            <td>{i}</td>
                                                            <td>{speed[-1]}</td>
                                                        </tr>
                                                        <!-- and so on... -->
                                                    </tbody>
                                                </table>
                                                {sty}
                                                '''), None, None, None, None]])
                                        put_grid([[None, None, None, None, put_html('''<button class="btn">
                                                           <span class="icon">
                                                               <svg viewBox="0 0 175 80" width="30" height="30">
                                                                   <rect width="40" height="15" fill="#f0f0f0" rx="10"></rect>
                                                                   <rect y="30" width="80" height="15" fill="#f0f0f0" rx="10"></rect>
                                                                   <rect y="60" width="80" height="15" fill="#f0f0f0" rx="10"></rect>
                                                               </svg>
                                                           </span>
                                                           <span class="text">Customize</span>
                                                       </button>
                                                       <style>/* From uiverse.io by @gagan-gv */
                                                       .btn {
                                                         width: 160px;
                                                         height: 37px;
                                                         border-radius: 3px;
                                                         border: none;
                                                         transition: all 0.5s ease-in-out;
                                                         font-size: 14px;
                                                         font-family: Verdana, Geneva, Tahoma, sans-serif;
                                                         font-weight: 700;
                                                         display: flex;
                                                         align-items: center;
                                                         background: #2bbab1;
                                                         color: #f5f5f5;
                                                       }

                                                       .btn:hover {
                                                         box-shadow: 0 0 20px 0px #2e2e2e3a;
                                                       }

                                                       .btn .icon {
                                                         position: absolute;
                                                         height: 40px;
                                                         width: 70px;
                                                         display: flex;
                                                         justify-content: center;
                                                         align-items: center;
                                                         transition: all 0.5s;
                                                       }

                                                       .btn .text {
                                                         transform: translateX(55px);
                                                       }

                                                       .btn:hover .icon {
                                                         width: 175px;
                                                       }

                                                       .btn:hover .text {
                                                         transition: all 0.5s;
                                                         opacity: 0;
                                                       }

                                                       .btn:focus {
                                                         outline: none;
                                                       }

                                                       .btn:active .icon {
                                                         transform: scale(0.85);
                                                       }</style>''').onclick(edit), None, None, None, None]])
                                        put_html("""<hr>""")

                                    with use_scope('info', clear=True):
                                        put_success(
                                            f'            ............ A world still an idea .............. \n '
                                            f'            >>>>>>>>>>>>>>>>>>>Moidata<<<<<<<<<<<<<<<<<<<<<<<< \n'
                                            f'            >>>>>>>>>>>>>>> Free services <<<<<<<<<<<<<<<<<<<<\n'
                                            f'            >>>>Created to create new worlds only of ideas<<<<')
                                        time.sleep(2)
                                        toast(f'starting ..for {i}....', color='info')
                                    with use_scope('info', clear=True):
                                        put_success(f'opening the for {user[-1]} .....')
                                    driver.get(f'https://www.instagram.com/{user[-1]}/')
                                    with use_scope('info', clear=True):
                                        put_warning(f'waiting for 4 sce .....')
                                    time.sleep(4)
                                    with use_scope('info', clear=True):
                                        put_success(
                                            f'here is the steps of spam reporter >>>>Catching >>> {user[-1]} <<< .....')
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[2]/button').click()
                                    time.sleep(1.5)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]').click()
                                    with use_scope('info', clear=True):
                                        put_success(
                                            f' watch... >>>>>>>>>>>>>Catching >>> {user[-1]} <<< .....')
                                    time.sleep(1.5)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]').click()
                                    time.sleep(1.5)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]').click()
                                    time.sleep(1.5)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]').click()
                                    time.sleep(1.3)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div[4]/button').click()
                                    with use_scope('info', clear=True):
                                        put_success(
                                            f'Done as super MoInsta for >>> {user[-1]} still on {int(i)} <<< .....')
                                        time.sleep(0.8)


                                except:
                                    with use_scope('info', clear=True):
                                        put_error(
                                            f'>>>>Please use the specified speed and capacity on your device<<<<')
                                        time.sleep(4)
                                        with use_scope('info', clear=True):
                                            put_error(
                                                f'...............................Back()...............................')

                                        time.sleep(1.5)

                                        ch()
                                        break


                            else:

                                with use_scope('info', clear=True):
                                    driver.get('https://znap.link/MoiCbio')
                                    put_success(
                                        f'All ATT Done Super Moinsta for >>> {user[-1]} <<< .....')  ##

                    def fast(driver):
                        ###################################################################################
                        with use_scope('info', clear=True):
                            put_success('catching the driver waiting for 10 open instagram Page.....')
                        time.sleep(3)  # 1
                        driver.get('https://www.instagram.com/')
                        with use_scope('info', clear=True):
                            put_success('catching the cok returns ..........')
                        time.sleep(3)  # 2
                        try:
                            driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]').click()
                            with use_scope('info', clear=True):

                                put_success('catching the cok returns done... without any problem...')
                        except:
                            with use_scope('info', clear=True):
                                put_error('trying to get cok return wait ......')
                                driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]').click()
                                time.sleep(2)
                                put_success('here we go ....!')
                                pass

                        time.sleep(1)

                        with use_scope('info', clear=True):
                            put_success(f'........!Return   Your User [{myuse[-1]}] !...... ')
                        us = driver.find_element(By.XPATH,
                                                 '//*[@id="loginForm"]/div/div[1]/div/label/input')

                        us.clear()
                        us.send_keys(str(myuse[-1]))
                        with use_scope('info', clear=True):
                            put_success(f'.....![{myuse[-1]}] Inserted !..... ')
                        with use_scope('info', clear=True):

                            put_success(f'.....! Return  Your Password [{mypas[-1]}] !.....')
                        p = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
                        p.clear()
                        p.send_keys(str(mypas[-1]))
                        with use_scope('info', clear=True):
                            put_success(f'.....! [{mypas[-1]}] Inserted !.....')
                            time.sleep(1)
                        ######################### insta err returns #####################################

                        #################################################################################
                        with use_scope('info', clear=True):
                            put_warning(
                                f'If you did not set the password or the user correctly, the program will stop after pressing...')

                            ##################################### insta entry to accounts bugs ##########################################################

                            driver.find_element(By.XPATH,
                                                '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
                            time.sleep(5)

                            ere1 = [0]

                            try:
                                put_text(driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]').text)
                                ere = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]  ').text
                                ere1.append(str(ere))



                            except:
                                with use_scope('info', clear=True):
                                    put_error(f' code a ! l&87 <moier>')
                                    time.sleep(2)
                            use_er = "The username you entered doesn't belong to an account. Please check your username and try again."
                            pas_er = "Sorry, your password was incorrect. Please double-check your password."
                            net_er = "We couldn't connect to Instagram. Make sure you're connected to the internet and try again."
                            erer = "The username you entered doesn't belong to an account. Please check your username and try again."
                            ########## 1 ###########

                            if ere1[-1] == use_er:

                                with use_scope('info', clear=True):
                                    put_error(f'ERROR ........ ')
                                time.sleep(1)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        f"The cause of the problem is now examined using MoiAi's simplified mindset .....")
                                    time.sleep(1)
                                with use_scope('info', clear=True):
                                    put_warning(f" circuit in logic functions .....")
                                with use_scope('info', clear=True):
                                    put_success(f"......... over here ..........")
                                time.sleep(0.8)
                                with use_scope('info', clear=True):
                                    put_error(f"......... If he knew the reason, the hero of wonder ..........")
                                time.sleep(0.8)
                                with use_scope('info', clear=True):
                                    put_error(f"......... If he knew the reason, the hero of wonder ..........")
                                time.sleep(0.8)
                                with use_scope('info', clear=True):
                                    put_error(
                                        f"......... The problem has been detected, translation is in progress ..........")
                                time.sleep(0.5)
                                with use_scope('info', clear=True):
                                    put_error(
                                        f"......... The problem is that the username ->[{myuse[-1]}]<- is not found in the databases in Instagram ..........")
                                time.sleep(0.6)
                                with use_scope('info', clear=True):
                                    put_success(
                                        f"......... You will be redirected to modify the data you entered ..........")
                                    return exap()  #
                            ########## 2 ###########
                            elif ere1[-1] == pas_er:

                                with use_scope('info', clear=True):

                                    put_error(f'ERROR PASS  ----->{pas_er}<-----\n For  ---------------> {mypas[-1]} ')

                                time.sleep(1)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        f"The cause of the problem is now examined using MoiAi's simplified mindset .....")
                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning(f" circuit in logic functions .....")
                                with use_scope('info', clear=True):
                                    put_success(f"......... over here ..........")
                                time.sleep(0.8)
                                with use_scope('info', clear=True):
                                    put_error(f"......... If he knew the reason, the hero of wonder ..........")
                                time.sleep(0.8)
                                with use_scope('info', clear=True):
                                    put_error(f"......... If he knew the reason, the hero of wonder ..........")
                                time.sleep(0.8)
                                with use_scope('info', clear=True):
                                    put_error(
                                        f"......... The problem has been detected, translation is in progress  ..........")
                                time.sleep(0.5)
                                with use_scope('info', clear=True):
                                    put_error(f" insta users .... Return [{myuse[-1]}] as True .... ")
                                with use_scope('info', clear=True):
                                    time.sleep(0.6)
                                    put_warning(
                                        f"......... The problem is that the Passowrd ->[{mypas[-1]}]<- is not found in the databases in Instagram ..........")
                                time.sleep(0.5)
                                with use_scope('info', clear=True):
                                    put_success(
                                        f"......... You will be redirected to modify the data you entered ..........")
                                    return exap()


                            elif ere1[-1] != use_er and pas_er and net_er and erer:

                                pass

                        with use_scope('info', clear=True):
                            put_warning(f'Log in to your account user={myuse[-1]}  pass={mypas[-1]} ...  ')
                            time.sleep(1)
                        with use_scope('info', clear=True):
                            put_warning(f'............   wait   ............    ')
                            time.sleep(1)
                        with use_scope('info', clear=True):
                            put_warning(f'............   ^_^   ............    ')
                            time.sleep(0.4)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiAi   ............    ')
                            time.sleep(0.4)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiTr   ............    ')
                            time.sleep(0.5)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiData   ............    ')
                            time.sleep(0.5)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiEis   ............    ')
                            time.sleep(0.5)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiMl   ............    ')
                            time.sleep(0.5)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiTb   ............    ')
                            time.sleep(0.7)
                        with use_scope('info', clear=True):
                            put_warning(f'............   MoiHere   ............    ')
                            time.sleep(0.8)
                        with use_scope('info', clear=True):
                            put_success(f'............   FOR YOU ^_^   ............    ')
                            time.sleep(1)
                        with use_scope('info', clear=True):
                            put_success(f'............ A world still an idea .............. \n '
                                        f'    Welcome. We hope you will have a wonderful experience that you will like.  \n............ We are still running ............\n   ')
                            time.sleep(1)
                            with use_scope('info', clear=True):
                                put_warning(f'           ............ A world still an idea .............. \n '
                                            f'           >>>>>>>>>>>>>>>>>>>MoiEis<<<<<<<<<<<<<<<<<<<<<<<<< \n'
                                            f'           >>>>>>>>>>>>>>> Free services <<<<<<<<<<<<<<<<<<<<\n'
                                            f'           >>>>Created to create new worlds only of ideas<<<<')

                            driver.get('https://znap.link/MoiCbio')
                            with use_scope('info', clear=True):
                                put_error(
                                    f'If you want to find out more about us, the site will be displayed once, you will find all my accounts',
                                    closable=True)
                            time.sleep(2)

                        for i in range(int(rang[-1])):  # time of reported
                            if i != rang[-1]:
                                try:
                                    clear(scope='info')

                                    ################################### account ###############################
                                    def acc():
                                        def update_acc():
                                            myuse.append(pin.newu)
                                            mypas.append(pin.newp)

                                            reeeec(driver)

                                        popup('Edit Your Account : ',
                                              put_grid([[None, None, put_text('Your Username:'), None, None],
                                                        [None, None, put_input('newu', value=myuse[-1]), None, None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_text('Your Password:'), None, None],
                                                        [None, None, put_input('newp', value=mypas[-1]), None, None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_html('''<button class="btn">
                                    <span class="btn-text-one">Save</span>
                                    <span class="btn-text-two">may restart</span>
                                </button>

                                <style>/* From uiverse.io by @mobinkakei */
                                .btn {
                                  width: 140px;
                                  height: 50px;
                                  background: linear-gradient(to top, #2bbab1, #12376e, #23487f);
                                  color: #fff;
                                  border-radius: 50px;
                                  border: none;
                                  outline: none;
                                  cursor: pointer;
                                  position: relative;
                                  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
                                  overflow: hidden;
                                }

                                .btn span {
                                  font-size: 12px;
                                  text-transform: uppercase;
                                  letter-spacing: 1px;
                                  transition: top 0.5s;
                                }

                                .btn-text-one {
                                  position: absolute;
                                  width: 100%;
                                  top: 50%;
                                  left: 0;
                                  transform: translateY(-50%);
                                }

                                .btn-text-two {
                                  position: absolute;
                                  width: 100%;
                                  top: 150%;
                                  left: 0;
                                  transform: translateY(-50%);
                                }

                                .btn:hover .btn-text-one {
                                  top: -100%;
                                }

                                .btn:hover .btn-text-two {
                                  top: 50%;
                                }
                                </style>''').onclick(update_acc), None, None], ]))

                                    def att():
                                        def update_acc():
                                            user.append(pin.newatt)
                                            reeeec(driver)

                                        popup('rename user goal : : ',
                                              put_grid([[None, None, put_text('Att This User :'), None, None],
                                                        [None, None, put_input('newatt', value=user[-1]), None, None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_html('''<button class="btn">
                                                                        <span class="btn-text-one">Save</span>
                                                                        <span class="btn-text-two">may restart</span>
                                                                    </button>

                                                                    <style>/* From uiverse.io by @mobinkakei */
                                                                    .btn {
                                                                      width: 140px;
                                                                      height: 50px;
                                                                      background: linear-gradient(to top, #2bbab1, #12376e, #23487f);
                                                                      color: #fff;
                                                                      border-radius: 50px;
                                                                      border: none;
                                                                      outline: none;
                                                                      cursor: pointer;
                                                                      position: relative;
                                                                      box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
                                                                      overflow: hidden;
                                                                    }

                                                                    .btn span {
                                                                      font-size: 12px;
                                                                      text-transform: uppercase;
                                                                      letter-spacing: 1px;
                                                                      transition: top 0.5s;
                                                                    }

                                                                    .btn-text-one {
                                                                      position: absolute;
                                                                      width: 100%;
                                                                      top: 50%;
                                                                      left: 0;
                                                                      transform: translateY(-50%);
                                                                    }

                                                                    .btn-text-two {
                                                                      position: absolute;
                                                                      width: 100%;
                                                                      top: 150%;
                                                                      left: 0;
                                                                      transform: translateY(-50%);
                                                                    }

                                                                    .btn:hover .btn-text-one {
                                                                      top: -100%;
                                                                    }

                                                                    .btn:hover .btn-text-two {
                                                                      top: 50%;
                                                                    }
                                                                    </style>''').onclick(update_acc), None, None], ]))

                                    def ran():

                                        def update_acc():
                                            rang.append(pin.rn)
                                            reeeec(driver)

                                        popup('range the times : ',
                                              put_grid([[None, None, put_text('For  :'), None, None],
                                                        [None, None, put_input('rn', value=rang[-1], type=NUMBER), None,
                                                         None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_html('''<button class="btn">
                                                                            <span class="btn-text-one">Save</span>
                                                                            <span class="btn-text-two">may restart</span>
                                                                        </button>

                                                                        <style>/* From uiverse.io by @mobinkakei */
                                                                        .btn {
                                                                          width: 140px;
                                                                          height: 50px;
                                                                          background: linear-gradient(to top, #2bbab1, #12376e, #23487f);
                                                                          color: #fff;
                                                                          border-radius: 50px;
                                                                          border: none;
                                                                          outline: none;
                                                                          cursor: pointer;
                                                                          position: relative;
                                                                          box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
                                                                          overflow: hidden;
                                                                        }

                                                                        .btn span {
                                                                          font-size: 12px;
                                                                          text-transform: uppercase;
                                                                          letter-spacing: 1px;
                                                                          transition: top 0.5s;
                                                                        }

                                                                        .btn-text-one {
                                                                          position: absolute;
                                                                          width: 100%;
                                                                          top: 50%;
                                                                          left: 0;
                                                                          transform: translateY(-50%);
                                                                        }

                                                                        .btn-text-two {
                                                                          position: absolute;
                                                                          width: 100%;
                                                                          top: 150%;
                                                                          left: 0;
                                                                          transform: translateY(-50%);
                                                                        }

                                                                        .btn:hover .btn-text-one {
                                                                          top: -100%;
                                                                        }

                                                                        .btn:hover .btn-text-two {
                                                                          top: 50%;
                                                                        }
                                                                        </style>''').onclick(update_acc), None, None]]))

                                    def sp():

                                        def update_acc():
                                            rang.append(pin.spod)
                                            reeeec(driver)

                                        popup('select speed of attack  : ',
                                              put_grid([[None, None, put_text('your speed is :'), None, None],
                                                        [None, None, put_select('spod', value=speed[-1],
                                                                                options=['recommended', 'fast',
                                                                                         'Medium',
                                                                                         'slow']), None,
                                                         None],
                                                        [None, None, put_html('<hr>'), None, None],
                                                        [None, None, put_html('''<button class="btn">
                                                                            <span class="btn-text-one">Save</span>
                                                                            <span class="btn-text-two">may restart</span>
                                                                        </button>

                                                                        <style>/* From uiverse.io by @mobinkakei */
                                                                        .btn {
                                                                          width: 140px;
                                                                          height: 50px;
                                                                          background: linear-gradient(to top, #2bbab1, #12376e, #23487f);
                                                                          color: #fff;
                                                                          border-radius: 50px;
                                                                          border: none;
                                                                          outline: none;
                                                                          cursor: pointer;
                                                                          position: relative;
                                                                          box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
                                                                          overflow: hidden;
                                                                        }

                                                                        .btn span {
                                                                          font-size: 12px;
                                                                          text-transform: uppercase;
                                                                          letter-spacing: 1px;
                                                                          transition: top 0.5s;
                                                                        }

                                                                        .btn-text-one {
                                                                          position: absolute;
                                                                          width: 100%;
                                                                          top: 50%;
                                                                          left: 0;
                                                                          transform: translateY(-50%);
                                                                        }

                                                                        .btn-text-two {
                                                                          position: absolute;
                                                                          width: 100%;
                                                                          top: 150%;
                                                                          left: 0;
                                                                          transform: translateY(-50%);
                                                                        }

                                                                        .btn:hover .btn-text-one {
                                                                          top: -100%;
                                                                        }

                                                                        .btn:hover .btn-text-two {
                                                                          top: 50%;
                                                                        }
                                                                        </style>''').onclick(update_acc), None, None]]))

                                    #################################### Edit #################################
                                    def edit():
                                        popup('Choose what you want to edit :', put_grid([[None, None, span(put_html('''<button class="cta">
                                                                    <span class="hover-underline-animation">My Account</span>
                                                                    <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                                        <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                                    </svg>
                                                                </button>

                                                                <style>/* From uiverse.io by @alexmaracinaru */
                                                                .cta {
                                                                  border: none;
                                                                  background: none;
                                                                }

                                                                .cta span {
                                                                  padding-bottom: 7px;
                                                                  letter-spacing: 4px;
                                                                  font-size: 9px;
                                                                  padding-right: 15px;
                                                                  text-transform: uppercase;
                                                                }

                                                                .cta svg {
                                                                  transform: translateX(-8px);
                                                                  transition: all 0.3s ease;
                                                                }

                                                                .cta:hover svg {
                                                                  transform: translateX(0);
                                                                }

                                                                .cta:active svg {
                                                                  transform: scale(0.9);
                                                                }

                                                                .hover-underline-animation {
                                                                  position: relative;
                                                                  color: black;
                                                                  padding-bottom: 20px;
                                                                }

                                                                .hover-underline-animation:after {
                                                                  content: "";
                                                                  position: absolute;
                                                                  width: 100%;
                                                                  transform: scaleX(0);
                                                                  height: 2px;
                                                                  bottom: 0;
                                                                  left: 0;
                                                                  background-color: #000000;
                                                                  transform-origin: bottom right;
                                                                  transition: transform 0.25s ease-out;
                                                                }

                                                                .cta:hover .hover-underline-animation:after {
                                                                  transform: scaleX(1);
                                                                  transform-origin: bottom left;
                                                                }</style>''').onclick(acc), col=2, row=1), None, None],
                                                                                          [None, None,
                                                                                           span(put_html('<hr>'), col=2,
                                                                                                row=1), None, None],
                                                                                          [None, None, span(put_html('''<button class="cta">
                                                                    <span class="hover-underline-animation">Attk User</span>
                                                                    <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                                        <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                                    </svg>
                                                                </button>

                                                                <style>/* From uiverse.io by @alexmaracinaru */
                                                                .cta {
                                                                  border: none;
                                                                  background: none;
                                                                }

                                                                .cta span {
                                                                  padding-bottom: 7px;
                                                                  letter-spacing: 4px;
                                                                  font-size: 14px;
                                                                  padding-right: 15px;
                                                                  text-transform: uppercase;
                                                                }

                                                                .cta svg {
                                                                  transform: translateX(-8px);
                                                                  transition: all 0.3s ease;
                                                                }

                                                                .cta:hover svg {
                                                                  transform: translateX(0);
                                                                }

                                                                .cta:active svg {
                                                                  transform: scale(0.9);
                                                                }

                                                                .hover-underline-animation {
                                                                  position: relative;
                                                                  color: black;
                                                                  padding-bottom: 20px;
                                                                }

                                                                .hover-underline-animation:after {
                                                                  content: "";
                                                                  position: absolute;
                                                                  width: 100%;
                                                                  transform: scaleX(0);
                                                                  height: 2px;
                                                                  bottom: 0;
                                                                  left: 0;
                                                                  background-color: #000000;
                                                                  transform-origin: bottom right;
                                                                  transition: transform 0.25s ease-out;
                                                                }

                                                                .cta:hover .hover-underline-animation:after {
                                                                  transform: scaleX(1);
                                                                  transform-origin: bottom left;
                                                                }</style>''').onclick(att), col=2, row=1), None, None],
                                                                                          [None, None,
                                                                                           span(put_html('<hr>'), col=2,
                                                                                                row=1), None, None],
                                                                                          [None, None, span(put_html('''<button class="cta">
                                                                    <span class="hover-underline-animation">Range</span>
                                                                    <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                                        <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                                    </svg>
                                                                </button>

                                                                <style>/* From uiverse.io by @alexmaracinaru */
                                                                .cta {
                                                                  border: none;
                                                                  background: none;
                                                                }

                                                                .cta span {
                                                                  padding-bottom: 7px;
                                                                  letter-spacing: 4px;
                                                                  font-size: 14px;
                                                                  padding-right: 15px;
                                                                  text-transform: uppercase;
                                                                }

                                                                .cta svg {
                                                                  transform: translateX(-8px);
                                                                  transition: all 0.3s ease;
                                                                }

                                                                .cta:hover svg {
                                                                  transform: translateX(0);
                                                                }

                                                                .cta:active svg {
                                                                  transform: scale(0.9);
                                                                }

                                                                .hover-underline-animation {
                                                                  position: relative;
                                                                  color: black;
                                                                  padding-bottom: 20px;
                                                                }

                                                                .hover-underline-animation:after {
                                                                  content: "";
                                                                  position: absolute;
                                                                  width: 100%;
                                                                  transform: scaleX(0);
                                                                  height: 2px;
                                                                  bottom: 0;
                                                                  left: 0;
                                                                  background-color: #000000;
                                                                  transform-origin: bottom right;
                                                                  transition: transform 0.25s ease-out;
                                                                }

                                                                .cta:hover .hover-underline-animation:after {
                                                                  transform: scaleX(1);
                                                                  transform-origin: bottom left;
                                                                }</style>''').onclick(ran), col=2, row=1), None, None],
                                                                                          [None, None,
                                                                                           span(put_html('<hr>'), col=2,
                                                                                                row=1), None, None],
                                                                                          [None, None, span(put_html('''<button class="cta">
                                                                    <span class="hover-underline-animation">Speed</span>
                                                                    <svg viewBox="0 0 46 16" height="10" width="30" xmlns="http://www.w3.org/2000/svg" id="arrow-horizontal">
                                                                        <path transform="translate(30)" d="M8,0,6.545,1.455l5.506,5.506H-30V9.039H12.052L6.545,14.545,8,16l8-8Z" data-name="Path 10" id="Path_10"></path>
                                                                    </svg>
                                                                </button>

                                                                <style>/* From uiverse.io by @alexmaracinaru */
                                                                .cta {
                                                                  border: none;
                                                                  background: none;
                                                                }

                                                                .cta span {
                                                                  padding-bottom: 7px;
                                                                  letter-spacing: 4px;
                                                                  font-size: 14px;
                                                                  padding-right: 15px;
                                                                  text-transform: uppercase;
                                                                }

                                                                .cta svg {
                                                                  transform: translateX(-8px);
                                                                  transition: all 0.3s ease;
                                                                }

                                                                .cta:hover svg {
                                                                  transform: translateX(0);
                                                                }

                                                                .cta:active svg {
                                                                  transform: scale(0.9);
                                                                }

                                                                .hover-underline-animation {
                                                                  position: relative;
                                                                  color: black;
                                                                  padding-bottom: 20px;
                                                                }

                                                                .hover-underline-animation:after {
                                                                  content: "";
                                                                  position: absolute;
                                                                  width: 100%;
                                                                  transform: scaleX(0);
                                                                  height: 2px;
                                                                  bottom: 0;
                                                                  left: 0;
                                                                  background-color: #000000;
                                                                  transform-origin: bottom right;
                                                                  transition: transform 0.25s ease-out;
                                                                }

                                                                .cta:hover .hover-underline-animation:after {
                                                                  transform: scaleX(1);
                                                                  transform-origin: bottom left;
                                                                }</style>''').onclick(sp), col=2, row=1), None, None]]),
                                              closable=True, implicit_close=False)

                                    ###########################################################################

                                    with use_scope('chose', clear=True):

                                        sty = '''<style>
                                                                                                        .styled-table {
                                                                                                            border-collapse: collapse;
                                                                                                            margin: center;
                                                                                                            font-size: 0.9em;
                                                                                                            font-family: sans-serif;


                                                                                                        }
                                                                                                        .styled-table thead tr {
                                                                                                            background-color: #2bbab1;
                                                                                                            color: #ffffff;
                                                                                                            text-align: left;
                                                                                                        }
                                                                                                        .styled-table th,
                                                                                                        .styled-table td {
                                                                                                            padding: 12px 15px;
                                                                                                        }

                                                                                                        .styled-table tbody tr {
                                                                                                            border-bottom: 1px solid #dddddd;
                                                                                                        }

                                                                                                        .styled-table tbody tr:nth-of-type(even) {
                                                                                                            background-color: #2bbab1;
                                                                                                        }

                                                                                                        .styled-table tbody tr:last-of-type {
                                                                                                            border-bottom: 2px solid #2bbab1;
                                                                                                        }
                                                                                                        .styled-table tbody tr.active-row {
                                                                                                            font-weight: bold;
                                                                                                            color: #2bbab1;
                                                                                                        }
                                                                                                        </style>'''
                                        put_grid([[None, None, None, None, put_html(f'''<table class="styled-table">
                                                                        <thead>
                                                                            <tr>

                                                                                <th>My User</th>
                                                                                <th>Att User</th>
                                                                                <th>Range input </th>
                                                                                <th>Range Now </th>
                                                                                <th>speed</th>
                                                                            </tr>
                                                                        </thead>
                                                                        <tbody>

                                                                            <tr class="active-row">
                                                                                <td>{myuse[-1]}</td>
                                                                                <td>{user[-1]}</td>
                                                                                <td>{rang[-1]}</td>
                                                                                <td>{i}</td>
                                                                                <td>{speed[-1]}</td>
                                                                            </tr>
                                                                            <!-- and so on... -->
                                                                        </tbody>
                                                                    </table>
                                                                    {sty}
                                                                    '''), None, None, None, None]])
                                        put_grid([[None, None, None, None, put_html('''<button class="btn">
                                                                               <span class="icon">
                                                                                   <svg viewBox="0 0 175 80" width="30" height="30">
                                                                                       <rect width="40" height="15" fill="#f0f0f0" rx="10"></rect>
                                                                                       <rect y="30" width="80" height="15" fill="#f0f0f0" rx="10"></rect>
                                                                                       <rect y="60" width="80" height="15" fill="#f0f0f0" rx="10"></rect>
                                                                                   </svg>
                                                                               </span>
                                                                               <span class="text">Customize</span>
                                                                           </button>
                                                                           <style>/* From uiverse.io by @gagan-gv */
                                                                           .btn {
                                                                             width: 160px;
                                                                             height: 37px;
                                                                             border-radius: 3px;
                                                                             border: none;
                                                                             transition: all 0.5s ease-in-out;
                                                                             font-size: 14px;
                                                                             font-family: Verdana, Geneva, Tahoma, sans-serif;
                                                                             font-weight: 700;
                                                                             display: flex;
                                                                             align-items: center;
                                                                             background: #2bbab1;
                                                                             color: #f5f5f5;
                                                                           }

                                                                           .btn:hover {
                                                                             box-shadow: 0 0 20px 0px #2e2e2e3a;
                                                                           }

                                                                           .btn .icon {
                                                                             position: absolute;
                                                                             height: 40px;
                                                                             width: 70px;
                                                                             display: flex;
                                                                             justify-content: center;
                                                                             align-items: center;
                                                                             transition: all 0.5s;
                                                                           }

                                                                           .btn .text {
                                                                             transform: translateX(55px);
                                                                           }

                                                                           .btn:hover .icon {
                                                                             width: 175px;
                                                                           }

                                                                           .btn:hover .text {
                                                                             transition: all 0.5s;
                                                                             opacity: 0;
                                                                           }

                                                                           .btn:focus {
                                                                             outline: none;
                                                                           }

                                                                           .btn:active .icon {
                                                                             transform: scale(0.85);
                                                                           }</style>''').onclick(edit), None, None,
                                                   None, None]])
                                        put_html("""<hr>""")

                                    with use_scope('info', clear=True):
                                        put_success(
                                            f'            ............ A world still an idea .............. \n '
                                            f'            >>>>>>>>>>>>>>>>>>>Moidata<<<<<<<<<<<<<<<<<<<<<<<< \n'
                                            f'            >>>>>>>>>>>>>>> Free services <<<<<<<<<<<<<<<<<<<<\n'
                                            f'            >>>>Created to create new worlds only of ideas<<<<')
                                        time.sleep(2)
                                        toast(f'starting ..for {i}....', color='info')
                                    with use_scope('info', clear=True):
                                        put_success(f'opening the for {user[-1]} .....')
                                    driver.get(f'https://www.instagram.com/{user[-1]}/')
                                    with use_scope('info', clear=True):
                                        put_warning(f'waiting for 4 sce .....')
                                    time.sleep(1.3)
                                    with use_scope('info', clear=True):
                                        put_success(
                                            f'here is the steps of spam reporter >>>>Catching >>> {user[-1]} <<< .....')
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[2]/button').click()
                                    time.sleep(1.3)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]').click()
                                    with use_scope('info', clear=True):
                                        put_success(
                                            f' watch... >>>>>>>>>>>>>Catching >>> {user[-1]} <<< .....')
                                    time.sleep(1.3)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]').click()
                                    time.sleep(1.2)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]').click()
                                    time.sleep(1.2)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]').click()
                                    time.sleep(1.2)
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div[4]/button').click()
                                    with use_scope('info', clear=True):
                                        put_success(
                                            f'Done as super MoInsta for >>> {user[-1]} still on {int(i)} <<< .....')



                                except:
                                    with use_scope('info', clear=True):
                                        put_error(
                                            f'>>>>Please use the specified speed and capacity on your device<<<<')
                                        time.sleep(1)
                                        with use_scope('info', clear=True):
                                            put_error(
                                                f'...............................Back()...............................')

                                        time.sleep(1)

                                        ch()
                                        break


                            else:

                                with use_scope('info', clear=True):
                                    driver.get('https://znap.link/MoiCbio')
                                    put_success(
                                        f'All ATT Done Super Moinsta for >>> {user[-1]} <<< .....')  ##

                    def ret():  # to open ch function and set the speed
                        global driver
                        speed.append(pin.sp)
                        ######################## hay hay  ###########################
                        if speed[-1] == 'Hay Hay':
                            toast('Set The Speed .')
                            sped()

                        ######################## fast  ###########################
                        elif speed[-1] == 'fast':
                            a = confirm(f'are you sure for set speed to {speed[-1]}')
                            if a == True:
                                speed.append(pin.sp)
                                with use_scope('info', clear=True):
                                    put_success(f'set the speed to {speed[-1]} .....')
                                    time.sleep(0.3)
                                    fast(driver)

                            else:
                                sped()
                        ######################## recommended  ###########################
                        elif speed[-1] == 'recommended':
                            a = confirm(f'are you sure for set speed to {speed[-1]}')
                            if a == True:

                                speed.append(pin.sp)
                                with use_scope('info', clear=True):
                                    put_success(f'set the speed to {speed[-1]} .....')
                                    time.sleep(1)
                                reeeec(driver)
                            else:
                                sped()


                        ######################## MEDIUM  ###########################
                        elif speed[-1] == 'Medium':
                            b = confirm(f'are you sure for set speed to {speed[-1]}')
                            if b == True:

                                speed.append(pin.sp)
                                with use_scope('info', clear=True):
                                    put_success(f'set the speed to {speed[-1]} .....')
                                    time.sleep(0.2)
                                med(driver)
                            else:
                                sped()

                        ########################  slow  ###########################
                        elif speed[-1] == 'slow':
                            a = confirm(f'are you sure for set speed to {speed[-1]}')
                            if a == True:

                                speed.append(pin.sp)
                                with use_scope('info', clear=True):
                                    put_success(f'set the speed to {speed[-1]} .....')
                                    time.sleep(1)
                                slo(driver)
                            else:
                                sped()

                    def sped():  # <-------------------------------------- speed --------------------------
                        clear(scope='chose')
                        with use_scope('info', clear=True):
                            put_success(
                                f'The path has been detected ! ^_^ ! and the path has been stored successfully . ')
                            put_warning(f"After This Step don't touch the driver . ")
                            time.sleep(2)
                        with use_scope('info', clear=True):
                            put_grid([[None, None, None, None, put_html('''Choose attack speed :'''), None, None, None,
                                       None, None]])
                            # this # is # for # the new visone of moinsta cousmaize the speed
                            put_grid([[None, None, None, None,
                                       put_select('sp', options=['Hay Hay', 'recommended', 'fast', 'Medium', 'slow']),
                                       None, None, None, None, None]])
                            put_html('<hr>')
                            put_grid([[None, None, None, None, None, put_html('''<button>
              <span class="button_top"> Set Speed
              </span>
            </button>
            <style>/* From uiverse.io by @Voxybuns */
            button {
              /* Variables */
             --button_radius: 0.50em;
             --button_color: #00bfaf;
             --button_outline_color: #000000;
             font-size: 17px;
             font-weight: bold;
             border: none;
             border-radius: var(--button_radius);
             background: var(--button_outline_color);
            }

            .button_top {
             display: block;
             box-sizing: border-box;
             border: 2px solid var(--button_outline_color);
             border-radius: var(--button_radius);
             padding: 0.75em 1.5em;
             background: var(--button_color);
             color: var(--button_outline_color);
             transform: translateY(-0.2em);
             transition: transform 0.1s ease;
            }

            button:hover .button_top {
              /* Pull the button upwards when hovered */
             transform: translateY(-0.33em);
            }

            button:active .button_top {
              /* Push the button downwards when pressed */
             transform: translateY(0);
            }</style>''').onclick(ret), None, None, None, None, None]])  # bo for set the speed

                    def ch():
                        loc.append(pin.dri)
                        clear(scope='chose')
                        toast('......please wait  .....')
                        with use_scope('info', clear=True):
                            put_success('getting the things ready to Att...')

                        if cho[-1] == 'Chrome':
                            with use_scope('info', clear=True):
                                put_success(f'Access the driver path you are using ->[{cho[-1]}]........')
                            try:
                                global driver
                                driver = webdriver.Chrome(loc[-1])

                                time.sleep(1)  # <----1
                                # slow(driver)
                                sped()
                            except:
                                with use_scope('info', clear=True):
                                    put_error(
                                        f"! We couldn't access your driver path ->[{loc[-1]}] Make sure you entered the correct path !")
                                    time.sleep(3)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        "Don't worry I'll take you back to enter the path but make sure of these things ...")
                                    time.sleep(2)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        "...........Check if the driver version is compatible with the browser..............")
                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        "...........Check the source driver if it is official or modified..............")
                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        "I also advise not to write the path if it is far away so that all symbols and letters must be correct because this is very important")
                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning("...........................Back...........................")

                                noon()
                        elif cho[-1] == 'Safari':
                            with use_scope('info', clear=True):
                                put_success(f'Access the driver path you are using ->[{cho[-1]}]........')
                            try:

                                driver = webdriver.Safari(loc[-1])

                                time.sleep(1)  # <----1
                                # slow(driver)
                                sped()
                            except:
                                with use_scope('info', clear=True):
                                    put_error(
                                        f"! We couldn't access your driver path ->[{loc[-1]}] Make sure you entered the correct path !")

                                with use_scope('info', clear=True):
                                    put_warning(
                                        "Don't worry I'll take you back to enter the path but make sure of these things ...")
                                    time.sleep(2)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        "...........Check if the driver version is compatible with the browser..............")

                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        "...........Check the source driver if it is official or modified..............")
                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        "I also advise not to write the path if it is far away so that all symbols and letters must be correct because this is very important")
                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning("...........................Back...........................")

                                noon()
                        elif cho[-1] == 'Firefox':
                            with use_scope('info', clear=True):
                                put_success(f'Access the driver path you are using ->[{cho[-1]}]........')
                                time.sleep(3)
                            try:
                                driver = webdriver.Firefox(loc[-1])
                                time.sleep(1)  # <----1
                                # slow(driver)
                            except:
                                with use_scope('info', clear=True):
                                    put_error(
                                        f"! We couldn't access your driver path ->[{loc[-1]}] Make sure you entered the correct path !")

                                with use_scope('info', clear=True):
                                    put_warning(
                                        "Don't worry I'll take you back to enter the path but make sure of these things ...")
                                    time.sleep(2)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        "...........Check if the driver version is compatible with the browser..............")
                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        "...........Check the source driver if it is official or modified..............")
                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        "I also advise not to write the path if it is far away so that all symbols and letters must be correct because this is very important")
                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning("...........................Back...........................")

                                noon()
                        elif cho[-1] == 'Edge':
                            with use_scope('info', clear=True):
                                put_success(f'Access the driver path you are using ->[{cho[-1]}]........')
                                time.sleep(3)
                            try:
                                driver = webdriver.Edge(loc[-1])
                                time.sleep(1)  # <----1
                                # slow(driver)
                            except:
                                with use_scope('info', clear=True):
                                    put_error(
                                        f"! We couldn't access your driver path ->[{loc[-1]}] Make sure you entered the correct path !")

                                with use_scope('info', clear=True):
                                    put_warning(
                                        "Don't worry I'll take you back to enter the path but make sure of these things ...")
                                    time.sleep(2)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        "...........Check if the driver version is compatible with the browser..............")
                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        "...........Check the source driver if it is official or modified..............")
                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning(
                                        "I also advise not to write the path if it is far away so that all symbols and letters must be correct because this is very important")
                                    time.sleep(1.5)
                                with use_scope('info', clear=True):
                                    put_warning("...........................Back...........................")

                                noon()

                    def noon():

                        clear(scope='info')
                        clear(scope='chose')
                        try:
                            if cho[-1] == "Chrome":

                                with use_scope(name='chose', clear=True):
                                    put_html('<hr>')
                                    put_grid([[None, None, None, None, put_html('path your driver here :'), None,
                                               put_input('dri', type=TEXT), None, None]])
                                    put_html('<hr>')
                                    put_grid([[None, None, None, None, put_html('''<button class="cssbuttons-io-button"> Get started
                                    <div class="icon">
                                    <svg height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M0 0h24v24H0z" fill="none"></path><path d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z" fill="currentColor"></path></svg>
                                    </div>
                                    </button>
                                    <style>/* From uiverse.io by @adamgiebl */
                                    .cssbuttons-io-button {
                                    background: #A370F0;
                                    color: white;
                                    font-family: inherit;
                                    padding: 0.35em;
                                    padding-left: 1.2em;
                                    font-size: 17px;
                                    font-weight: 500;
                                    border-radius: 0.9em;
                                    border: none;
                                    letter-spacing: 0.05em;
                                    display: flex;
                                    align-items: center;
                                    box-shadow: inset 0 0 1.6em -0.6em #714da6;
                                    overflow: hidden;
                                    position: relative;
                                    height: 2.8em;
                                    padding-right: 3.3em;
                                    }

                                    .cssbuttons-io-button .icon {
                                    background: white;
                                    margin-left: 1em;
                                    position: absolute;
                                    display: flex;
                                    align-items: center;
                                    justify-content: center;
                                    height: 2.2em;
                                    width: 2.2em;
                                    border-radius: 0.7em;
                                    box-shadow: 0.1em 0.1em 0.6em 0.2em #7b52b9;
                                    right: 0.3em;
                                    transition: all 0.3s;
                                    }

                                    .cssbuttons-io-button:hover .icon {
                                    width: calc(100% - 0.6em);
                                    }

                                    .cssbuttons-io-button .icon svg {
                                    width: 1.1em;
                                    transition: transform 0.3s;
                                    color: #7b52b9;
                                    }

                                    .cssbuttons-io-button:hover .icon svg {
                                    transform: translateX(0.1em);
                                    }

                                    .cssbuttons-io-button:active .icon {
                                    transform: scale(0.95);
                                    }
                                    </style>''').onclick(ch), None, None, None, None]])

                            elif cho[-1] == "Edge":

                                with use_scope(name='chose', clear=True):
                                    put_html('<hr>')
                                    put_grid([[None, None, None, None, put_html('path your driver here :'), None,
                                               put_input('dri', type=TEXT), None, None]])
                                    put_html('<hr>')
                                    put_grid([[None, None, None, None, put_html('''<button class="cssbuttons-io-button"> Get started
                                                                  <div class="icon">
                                                                    <svg height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M0 0h24v24H0z" fill="none"></path><path d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z" fill="currentColor"></path></svg>
                                                                  </div>
                                                                </button>
                                                                <style>/* From uiverse.io by @adamgiebl */
                                                                .cssbuttons-io-button {
                                                                 background: #A370F0;
                                                                 color: white;
                                                                 font-family: inherit;
                                                                 padding: 0.35em;
                                                                 padding-left: 1.2em;
                                                                 font-size: 17px;
                                                                 font-weight: 500;
                                                                 border-radius: 0.9em;
                                                                 border: none;
                                                                 letter-spacing: 0.05em;
                                                                 display: flex;
                                                                 align-items: center;
                                                                 box-shadow: inset 0 0 1.6em -0.6em #714da6;
                                                                 overflow: hidden;
                                                                 position: relative;
                                                                 height: 2.8em;
                                                                 padding-right: 3.3em;
                                                                }

                                                                .cssbuttons-io-button .icon {
                                                                 background: white;
                                                                 margin-left: 1em;
                                                                 position: absolute;
                                                                 display: flex;
                                                                 align-items: center;
                                                                 justify-content: center;
                                                                 height: 2.2em;
                                                                 width: 2.2em;
                                                                 border-radius: 0.7em;
                                                                 box-shadow: 0.1em 0.1em 0.6em 0.2em #7b52b9;
                                                                 right: 0.3em;
                                                                 transition: all 0.3s;
                                                                }

                                                                .cssbuttons-io-button:hover .icon {
                                                                 width: calc(100% - 0.6em);
                                                                }

                                                                .cssbuttons-io-button .icon svg {
                                                                 width: 1.1em;
                                                                 transition: transform 0.3s;
                                                                 color: #7b52b9;
                                                                }

                                                                .cssbuttons-io-button:hover .icon svg {
                                                                 transform: translateX(0.1em);
                                                                }

                                                                .cssbuttons-io-button:active .icon {
                                                                 transform: scale(0.95);
                                                                }
                                                                </style>''').onclick(ch), None, None, None, None]])
                            elif cho[-1] == "Firefox":
                                with use_scope(name='chose', clear=True):
                                    put_html('<hr>')
                                    put_grid([[None, None, None, None, put_html('path your driver here :'), None,
                                               put_input('dri', type=TEXT), None, None]])
                                    put_html('<hr>')
                                    put_grid([[None, None, None, None, put_html('''<button class="cssbuttons-io-button"> Get started
                                                                  <div class="icon">
                                                                    <svg height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M0 0h24v24H0z" fill="none"></path><path d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z" fill="currentColor"></path></svg>
                                                                  </div>
                                                                </button>
                                                                <style>/* From uiverse.io by @adamgiebl */
                                                                .cssbuttons-io-button {
                                                                 background: #A370F0;
                                                                 color: white;
                                                                 font-family: inherit;
                                                                 padding: 0.35em;
                                                                 padding-left: 1.2em;
                                                                 font-size: 17px;
                                                                 font-weight: 500;
                                                                 border-radius: 0.9em;
                                                                 border: none;
                                                                 letter-spacing: 0.05em;
                                                                 display: flex;
                                                                 align-items: center;
                                                                 box-shadow: inset 0 0 1.6em -0.6em #714da6;
                                                                 overflow: hidden;
                                                                 position: relative;
                                                                 height: 2.8em;
                                                                 padding-right: 3.3em;
                                                                }

                                                                .cssbuttons-io-button .icon {
                                                                 background: white;
                                                                 margin-left: 1em;
                                                                 position: absolute;
                                                                 display: flex;
                                                                 align-items: center;
                                                                 justify-content: center;
                                                                 height: 2.2em;
                                                                 width: 2.2em;
                                                                 border-radius: 0.7em;
                                                                 box-shadow: 0.1em 0.1em 0.6em 0.2em #7b52b9;
                                                                 right: 0.3em;
                                                                 transition: all 0.3s;
                                                                }

                                                                .cssbuttons-io-button:hover .icon {
                                                                 width: calc(100% - 0.6em);
                                                                }

                                                                .cssbuttons-io-button .icon svg {
                                                                 width: 1.1em;
                                                                 transition: transform 0.3s;
                                                                 color: #7b52b9;
                                                                }

                                                                .cssbuttons-io-button:hover .icon svg {
                                                                 transform: translateX(0.1em);
                                                                }

                                                                .cssbuttons-io-button:active .icon {
                                                                 transform: scale(0.95);
                                                                }
                                                                </style>''').onclick(ch), None, None, None, None]])
                            elif cho[-1] == "Safari":
                                with use_scope(name='chose', clear=True):
                                    put_html('<hr>')
                                    put_grid([[None, None, None, None, put_html('path your driver here :'), None,
                                               put_input('dri', type=TEXT), None, None]])
                                    put_html('<hr>')
                                    put_grid([[None, None, None, None, put_html('''<button class="cssbuttons-io-button"> Get started
                                                                  <div class="icon">
                                                                    <svg height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M0 0h24v24H0z" fill="none"></path><path d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z" fill="currentColor"></path></svg>
                                                                  </div>
                                                                </button>
                                                                <style>/* From uiverse.io by @adamgiebl */
                                                                .cssbuttons-io-button {
                                                                 background: #A370F0;
                                                                 color: white;
                                                                 font-family: inherit;
                                                                 padding: 0.35em;
                                                                 padding-left: 1.2em;
                                                                 font-size: 17px;
                                                                 font-weight: 500;
                                                                 border-radius: 0.9em;
                                                                 border: none;
                                                                 letter-spacing: 0.05em;
                                                                 display: flex;
                                                                 align-items: center;
                                                                 box-shadow: inset 0 0 1.6em -0.6em #714da6;
                                                                 overflow: hidden;
                                                                 position: relative;
                                                                 height: 2.8em;
                                                                 padding-right: 3.3em;
                                                                }

                                                                .cssbuttons-io-button .icon {
                                                                 background: white;
                                                                 margin-left: 1em;
                                                                 position: absolute;
                                                                 display: flex;
                                                                 align-items: center;
                                                                 justify-content: center;
                                                                 height: 2.2em;
                                                                 width: 2.2em;
                                                                 border-radius: 0.7em;
                                                                 box-shadow: 0.1em 0.1em 0.6em 0.2em #7b52b9;
                                                                 right: 0.3em;
                                                                 transition: all 0.3s;
                                                                }

                                                                .cssbuttons-io-button:hover .icon {
                                                                 width: calc(100% - 0.6em);
                                                                }

                                                                .cssbuttons-io-button .icon svg {
                                                                 width: 1.1em;
                                                                 transition: transform 0.3s;
                                                                 color: #7b52b9;
                                                                }

                                                                .cssbuttons-io-button:hover .icon svg {
                                                                 transform: translateX(0.1em);
                                                                }

                                                                .cssbuttons-io-button:active .icon {
                                                                 transform: scale(0.95);
                                                                }
                                                                </style>''').onclick(ch), None, None, None, None]])





                        except:
                            if len(pin.d) < 3:
                                toast(f"We can't find the driver on this path {loc[-1]}", color='#F81D05')

                    def chack2():
                        user.append(pin.user)
                        print(pin.user)
                        with use_scope("u", clear=True):
                            dat = confirm(f'Here we go for this {user[-1]}? ')
                            if dat == True:
                                put_grid([[None, None, None, None,
                                           put_html(f'<h3> ATTACK  THIS USER {user[-1]}  👨🏻‍🎤‍ </h3>'), None,
                                           None, None, None]])

                                with use_scope(name='chose', clear=True):
                                    def tim():
                                        rang.append(pin.w)
                                        noon()

                                    put_grid([[None, None, None, None,
                                               put_html(
                                                   f'<h3>how many times you want to report for this account {user[-1]} <h3>'),
                                               None, None, None, None]])
                                    put_grid([[None, None, None, None,
                                               put_input('w', type=NUMBER, value=100, placeholder='Only Numbers ..!'),
                                               None, None, None, None]])
                                    put_grid([[None, None, None, None,
                                               put_html("""<button> My Work
                                                    </button>

                                                    <style>/* From uiverse.io by @Botwe-Felix5820 */
                                                    button {
                                                     height: 3em;
                                                     width: 8em;
                                                     border: none;
                                                     border-radius: 10em;
                                                     background: #016DD9;
                                                     font-size: 17px;
                                                     color: #ffffff;
                                                     font-family: inherit;
                                                     font-weight: 500;
                                                    }

                                                    button:hover {
                                                     animation: shake3856 0.3s linear infinite both;
                                                    }

                                                    @keyframes shake3856 {
                                                     0% {
                                                      -webkit-transform: translate(0);
                                                      transform: translate(0);
                                                     }

                                                     20% {
                                                      -webkit-transform: translate(-2px, 2px);
                                                      transform: translate(-2px, 2px);
                                                     }

                                                     40% {
                                                      -webkit-transform: translate(-2px, -2px);
                                                      transform: translate(-2px, -2px);
                                                     }

                                                     60% {
                                                      -webkit-transform: translate(2px, 2px);
                                                      transform: translate(2px, 2px);
                                                     }

                                                     80% {
                                                      -webkit-transform: translate(2px, -2px);
                                                      transform: translate(2px, -2px);
                                                     }

                                                     100% {
                                                      -webkit-transform: translate(0);
                                                      transform: translate(0);
                                                     }
                                                    }
                                                    </style>""").onclick(tim),
                                               None, None, None, None]])

                    with use_scope(name='chose', clear=True):
                        put_html("<hr>")
                        with use_scope(name="u", clear=True):
                            put_grid([[None, None, None, None, put_html('<h3> ATTACK  THIS USER 👨🏻‍🎤‍ </h3>'), None,
                                       None, None, None]])
                        put_html('<hr>')
                        put_grid([[None, None, None, None, put_input('user', type=TEXT), None, None, None,
                                   None]])
                        put_html('<hr>')
                        put_grid([[None, None, None, None, None, None, put_html("""<button>Start</button>
                                                    <style>button {
                                     padding: 8px 18px;
                                     border: unset;
                                     border-radius: 15px;
                                     color: #212121;
                                     z-index: 1;
                                     background: #e8e8e8;
                                     position: relative;
                                     font-weight: 1000;
                                     font-size: 17px;
                                     -webkit-box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
                                     box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
                                     -webkit-transition: all 250ms;
                                     transition: all 250ms;
                                     overflow: hidden;
                                    }

                                    button::before {
                                     content: "";
                                     position: absolute;
                                     top: 0;
                                     left: 0;
                                     height: 100%;
                                     width: 0;
                                     border-radius: 15px;
                                     background-color: #212121;
                                     z-index: -1;
                                     -webkit-box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
                                     box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
                                     -webkit-transition: all 250ms;
                                     transition: all 250ms
                                    }

                                    button:hover {
                                     color: #e8e8e8;
                                    }

                                    button:hover::before {
                                     width: 100%;
                                    }</style>
                                    """).onclick(chack2)]])

                def cha():

                    dat = confirm(f'are you shoir this Your user is : [{pin.myuser}] and Your pass is :[{pin.mypass}]')
                    myuse.append(pin.myuser)  # this to login to your account
                    mypas.append(pin.mypass)  # this to save the data to the driver [DL]
                    if dat == True:
                        userofr()

                put_grid([[None, None, None, None, None, None, put_html('''<button>Next</button>
                                                    <style>button {
                                     padding: 8px 18px;
                                     border: unset;
                                     border-radius: 15px;
                                     color: #212121;
                                     z-index: 1;
                                     background: #e8e8e8;
                                     position: relative;
                                     font-weight: 1000;
                                     font-size: 17px;
                                     -webkit-box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
                                     box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
                                     -webkit-transition: all 250ms;
                                     transition: all 250ms;
                                     overflow: hidden;
                                    }

                                    button::before {
                                     content: "";
                                     position: absolute;
                                     top: 0;
                                     left: 0;
                                     height: 100%;
                                     width: 0;
                                     border-radius: 15px;
                                     background-color: #212121;
                                     z-index: -1;
                                     -webkit-box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
                                     box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
                                     -webkit-transition: all 250ms;
                                     transition: all 250ms
                                    }

                                    button:hover {
                                     color: #e8e8e8;
                                    }

                                    button:hover::before {
                                     width: 100%;
                                    }</style>
                                    ''').onclick(cha)]])
                with use_scope('info', clear=True):
                    put_info('! The data will be stored in your driver !')



















        with use_scope(name='chose',clear=True):
            put_html('<hr>')

            put_grid([[None,None,None,put_html('''<h5>Choose your favorite browser :</h5>'''),None,None,None,None]])
            put_grid([[None, None, None, None, put_select('se',options=[None,'Chrome','Firefox','Safari','Edge',]), None, None, None,None]])
            while True:
                pin_wait_change('se')
                cho.append(pin.se)
                if pin.se == 'Chrome' or 'Firefox'or'Safari'or 'Edge':
                    chrome()
                































    











if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(startw, port=args.port,debug=True,max_payload_size='10000000',reconnect_timeout=4)

