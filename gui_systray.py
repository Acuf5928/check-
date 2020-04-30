import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

import time
import sys
import _thread
import code_helper


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.menu = QtWidgets.QMenu(parent)
        self.activated.connect(self.iconActivated)
        self.icon = icon
        self.setMenu()

    # Init sysTray
    def setMenu(self):
        self.menu.clear()

        self.download = self.menu.addAction("Download: Search...")
        self.download.setEnabled(False)
        self.upload = self.menu.addAction("Upload: Search...")
        self.upload.setEnabled(False)
        self.signal1 = self.menu.addAction("Intensita' del segnale: Search...")
        self.signal1.setEnabled(False)
        self.signal2 = self.menu.addAction("Qualita' segnale: Search...")
        self.signal2.setEnabled(False)

        self.menu.addSeparator()

        exitAction = self.menu.addAction("Exit")
        exitAction.triggered.connect(self.exit)

        self.setContextMenu(self.menu)

    def exit(self):
        sys.exit()

    # To here

    # Override click on systray icon fun
    def iconActivated(self, reason):
        super()
        if reason == 1:
            _thread.start_new_thread(self.updateInterface, ())

    # Download data from modem
    def updateInterface(self):
        for var in list(range(10)):
            download, upload, signal1, signal2 = code_helper.foundValue()
            print(download, upload, signal1, signal2)
            self.download.setText("Download: " + download)
            self.upload.setText("Upload: " + upload)
            self.signal1.setText("Intensita' del segnale: " + signal1)
            self.signal2.setText("Qualita' segnale: " + signal2)
            time.sleep(1)


# Start gui_sysTray
def main(image):
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon(image), w)
    trayIcon.show()
    sys.exit(app.exec_())
