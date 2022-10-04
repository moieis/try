import itranslate as t
from pywebio.output  import *
from pywebio.input import *
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
    pass
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
            put_grid([[None,None,None,None,put_image('https://i.im.ge/2022/10/03/1Z8Uj4.9076d9b47d4f422b995c7e848c4b0a8c.png',width='200',height='200'),None]])
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

        with use_scope(name='chose',clear=True):
            put_html('<hr>')

            put_grid([[None,None,None,put_html('''<h5>Choose your favorite browser :</h5>'''),None,None,None,None]])
            put_grid([[None, None, None, None, put_select('se',options=[None,'Chrome','Firefox','Safari','Edge',]), None, None, None,None]])
            while True:
                pin_wait_change('se')
                cho.append(pin.se)
                if pin.se == 'Chrome' or 'Firefox' or 'Safari' or 'Edge':

                    break


        with use_scope(name='chose',clear=True):
            put_html('<hr>')
            with use_scope(name='info',clear=True):
                put_info('There is no withdrawal of any of your data. You can see the details of the algorithm. You are in our protection !')
                time.sleep(2)
            put_grid([[None,put_text('Your InstUser :'),put_input('myuser',type=TEXT),None,None,None]])
            put_grid([[None,put_text('Your InstPassword :'),put_input('mypass',type=PASSWORD),None,None,None]])
            put_html('<hr>')
            def userofr():
                def noon():



                    try:
                                def ch():
                                    clear(scope='chose')
                                    toast('please wait  .....')
                                    with use_scope('info',clear=True):
                                        put_success('getting the thigs ready to controll ...')

                                    driver = webdriver.Chrome(loc[-1])
                                    with use_scope('info',clear=True):
                                        put_success('catching the driver  waiting for 10 open instaweb.....')
                                    time.sleep(10)
                                    driver.get('https://www.instagram.com/')
                                    with use_scope('info',clear=True):
                                        put_success('catching the cokies returns ...')
                                    time.sleep(9)
                                    try:
                                        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]').click()
                                        with use_scope('info', clear=True):

                                            put_success('catching the cokies returns Sucsess without any problem...')
                                    except:
                                        with use_scope('info', clear=True):
                                            put_error('trying to get cookise return wait ....')
                                            driver.find_element(By.XPATH,'/html/body/div[4]/div/div/button[2]').click()
                                            time.sleep(2)
                                            put_success('i found it .!')
                                            pass


                                    time.sleep(2)
                                    with use_scope('info', clear=True):
                                        put_success(f'retun  your user [{myuse[-1]}] ..... ')
                                    us = driver.find_element(By.XPATH,
                                                             '//*[@id="loginForm"]/div/div[1]/div/label/input')

                                    us.clear()
                                    us.send_keys(str(myuse[-1]))
                                    with use_scope('info', clear=True):
                                        put_success(f' [{myuse[-1]}] writed Done !..... ')
                                    with use_scope('info', clear=True):
                                        put_success(f' retun  your passowrd [{mypas[-1]}] .....  ')
                                    p = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
                                    p.clear()
                                    p.send_keys(str(mypas[-1]))
                                    with use_scope('info', clear=True):
                                        put_success(f' [{mypas[-1]}] writed Done !..... ')

                                    time.sleep(2)

                                    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
                                    with use_scope('info', clear=True):
                                        put_success(f'pressing to the botton  ')
                                    time.sleep(2)

                                    for i in range(int(rang[-1])):
                                        if i != 10:
                                            try:


                                                driver.get(f'https://www.instagram.com/{user[-1]}/')
                                                time.sleep(4)
                                                driver.find_element(By.XPATH,
                                                                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[2]/button').click()
                                                driver.find_element(By.XPATH,
                                                                    '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]').click()
                                                time.sleep(0.6)
                                                driver.find_element(By.XPATH,
                                                                    '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]').click()
                                                time.sleep(1)
                                                driver.find_element(By.XPATH,
                                                                    '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[1]').click()
                                                time.sleep(0.3)
                                                driver.find_element(By.XPATH,
                                                                    '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[1]').click()
                                                time.sleep(1)
                                                driver.find_element(By.XPATH,
                                                                    '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div[4]/button').click()
                                                print(f'we are on the {i}')
                                            except:
                                                pass
                                        else:
                                            print(f"seucses o this time{i} ")
                                            break




                                # path of driver ____________________________________________!!

                                if pin.se == "Chrome":
                                    print('sdds')

                                    ch()


                                elif pin.se == "Edge":

                                    driver = webdriver.Edge(pin.dr)
                                    pass

                                elif pin.se == "Firefox":
                                    driver = webdriver.Firefox(pin.dr)
                                    pass
                                elif pin.se == "Safari":
                                    driver = webdriver.Safari(pin.dr)
                                    pass
                    except:
                                if len(pin.d) < 3:
                                    toast(f"We can't find the driver on this path {pin.f}", color='#F81D05')



                def chack2():
                    user.append(pin.user)
                    print(pin.user)
                    with use_scope("u",clear=True):
                        dat =confirm(f'Here we go for this {user[-1]}? ')
                        if dat == True:
                                put_grid([[None, None, None, None, put_html(f'<h3> ATTACK  THIS USER {user[-1]}  👨🏻‍🎤‍ </h3>'), None,
                                       None, None, None]])

                                with use_scope(name='chose',clear=True):
                                    def tim():
                                        rang.append(pin.w)


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

                                noon()


                with use_scope(name='chose',clear=True):
                    put_html("<hr>")
                    with use_scope(name="u",clear=True):


                            put_grid([[None,None,None,None,put_html('<h3> ATTACK  THIS USER 👨🏻‍🎤‍ </h3>'),None,None,None,None]])
                    put_html('<hr>')
                    put_grid([[None, None, None, None, put_input('user',type=TEXT), None, None, None,
                               None]])
                    put_html('<hr>')
                    put_grid([[None,None,None,None,None,None,put_html("""<button>Start</button>
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


                    dat =confirm(f'are you shoir this Your user is : [{pin.myuser}] and Your pass is :[{pin.mypass}]')
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












if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(startw, port=args.port,debug=True,max_payload_size='10000000',reconnect_timeout=4)

