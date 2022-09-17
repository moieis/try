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
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon



def page():
    put_button(label='hi',onclick=o)
def o():

        class App(QWidget):

            def __init__(self):
                super().__init__()
                self.title = 'PyQt5 file dialogs - pythonspot.com'
                self.left = 10
                self.top = 10
                self.width = 640
                self.height = 480
                self.initUI()

            def initUI(self):
                self.setWindowTitle(self.title)
                self.setGeometry(self.left, self.top, self.width, self.height)

                self.openFileNameDialog()
                self.openFileNamesDialog()
                self.saveFileDialog()

                self.show()

            def openFileNameDialog(self):
                options = QFileDialog.Options()
                options |= QFileDialog.DontUseNativeDialog
                fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                          "All Files (*);;Python Files (*.py)", options=options)
                if fileName:
                    print(fileName)

            def openFileNamesDialog(self):
                options = QFileDialog.Options()
                options |= QFileDialog.DontUseNativeDialog
                files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                        "All Files (*);;Python Files (*.py)", options=options)
                if files:
                    print(files)

            def saveFileDialog(self):
                options = QFileDialog.Options()
                options |= QFileDialog.DontUseNativeDialog
                fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                          "All Files (*);;Text Files (*.txt)", options=options)
                if fileName:
                    print(fileName)


        if __name__ == '__main__':
            app = QApplication(sys.argv)
            ex = App()
            sys.exit(app.exec_())




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(page, port=args.port,debug=True,max_payload_size='10000000',reconnect_timeout=4)

