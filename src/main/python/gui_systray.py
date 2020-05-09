
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

import sys
import _thread

from fbs_runtime.application_context.PyQt5 import ApplicationContext

import code_helper


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, ctx):
        super(SystemTrayIcon, self).__init__()
        self.menu = QtWidgets.QMenu()
        self.activated.connect(self.iconActivated)
        self.setIcon(QtGui.QIcon(ctx.icon()))
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
        download, upload, signal1, signal2 = code_helper.foundValue()

        if download != "Error":
            download = download.split(".")[0]
            download = int(download) / 100 / 8

        if upload != "Error":
            upload = upload.split(".")[0]
            upload = int(upload) / 100 / 8

        self.download.setText("Download: " + str(download) + " Mbps")
        self.upload.setText("Upload: " + str(upload) + " Mbps")
        self.signal1.setText("Intensita' del segnale: " + signal1)
        self.signal2.setText("Qualita' segnale: " + signal2)


# Start gui_sysTray
def main(image):
    appctxt = AppContext()
    trayIcon = SystemTrayIcon(appctxt)
    trayIcon.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)


class AppContext(ApplicationContext):
    def run(self):
        return self.app.exec_()

    def icon(self):
        return self.get_resource("images/icon.png")