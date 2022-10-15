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












        with use_scope(name='chose',clear=True):
            put_html('<hr>')

            put_grid([[None,None,None,put_html('''<h5>Choose your favorite browser :</h5>'''),None,None,None,None]])
            put_grid([[None, None, None, None, put_select('se',options=[None,'Chrome','Firefox','Safari','Edge',]), None, None, None,None]])
            while True:
                pin_wait_change('se')
                cho.append(pin.se)
                if pin.se == 'Chrome' :
                    break
                elif pin.se == 'Firefox':
                    break
                elif pin.se == 'safari':
                    break
                elif pin.se == 'edge':
                    break


















    











if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(startw, port=args.port,debug=True,max_payload_size='10000000',reconnect_timeout=4)

