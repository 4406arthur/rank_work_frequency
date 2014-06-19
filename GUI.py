import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView

class TestWindow(QtGui.QWidget):
    def __init__(self, parent = None):
        super(TestWindow, self).__init__(parent)

        self.palette = QtGui.QPalette()
        self.gridLayout = QtGui.QGridLayout()
        self.centralWidget = QtGui.QWidget()
        self.button = QtGui.QPushButton("Click")
        self.setWindowTitle("UNIX")
        self.resize(1200,700)
        self.button.clicked.connect(self.clicked)
        self.b = QWebView()
        self.b.load(QUrl('http://www.google.com'))
        IEdit = QtGui.QLineEdit()
        self.Trans = QtGui.QTextEdit()

        self.gridLayout.addWidget(IEdit,0,0)
        self.gridLayout.addWidget(self.button,1,0)
        self.gridLayout.addWidget(self.b,2,0)
        self.gridLayout.addWidget(self.Trans,3,0)

        
        self.setLayout(self.gridLayout)


    def clicked(self):
            self.b.load(QUrl('http://yahoo.com.tw'))
            self.Trans.setText('HI')
            #for line in urlFile:
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = TestWindow()
    ex.show()
    sys.exit(app.exec_())

