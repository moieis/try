import random
import time
import tkinter.messagebox
import os
import sys
import numpy as np
import appdata
from pytube import *
from pywebio.output import *
from pywebio.input import *
from pywebio.platform import *
from pywebio.pin import *
import tkinter as tk
from tkinter import messagebox
from tkinter import *
@config(theme='minty')
def s():

         put_grid([[None,None,None,None,None,put_input('r',value=['sdasd'],type=COLOR),None,None,None,None,None]])

         while True:

            pin_wait_change('r')
            with use_scope('s',clear=True):

              if pin.r[1] != 'f':
                with use_scope('o',clear=True):
                   put_html(f'''<h1 style="color:{pin.r};">You like This color ---> {pin.r}</h1>''')
              elif pin.r[1] == 'f' or pin.r[0:3] == '#eb':
                  st='<style>body {background-color: #a26789;}</style>'
                  put_html(f'''{st}<h1 style="color:{pin.r};">You like This color ---> {pin.r}</h1>''')
                  put_button(label='fd',color='dark',onclick=False)


se=np.arange(3432,45334)
one=random.choice(se)
def y():
    try:

        s()


    except:
        def fix():
            messagebox.showinfo("How To Fix ", "press OK and open the app agine")
            p.destroy()





        tk.Label(text='Erorr press fix butten').pack()
        tk.Button(text='Fix it for me ',command=fix).pack()


p = tk.Tk()
p.title('Hash Color Moi ')
p.minsize(400,200)
t=tk.Button(text='start hashcolor',command=y,activebackground='red',activeforeground='black',
            background='red').pack()

p.mainloop()

