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
import os

import pandas as pd
from pywebio.input import file_upload
from pywebio.output import put_file,put_text
def page():

        form = file_upload('sdf')
        fi = str(form['filename'])
        if fi:
            # This code will strip the leading absolute path from your file-name
            fil = os.path.basename(fi)

            # open for reading & writing the file into the server
            a=open(fi, 'wb').write(form['content'])
            b=open(fi,'rb').read()

            put_text(pd.read_csv(fi))
            put_file(fi,b)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(page, port=args.port,debug=True,max_payload_size='10000000',reconnect_timeout=4)

