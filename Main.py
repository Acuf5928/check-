#!/usr/bin/env python3

#Questo programma visualizza la banda totale in Download e in Upload occupata oltre alla potenza del segnale 4G
#Il programma è pensato per modem Linkem che usano tecnologia 4G per la navigazione
#Il programma è stato testato su Ubuntu ma dovrebbe funzionare senza problemi anche su Windows
#Fai ciò che vuoi con questo programma, se puoi citami.

import requests, time
from PyQt5 import Qt
import sys

x=0

app = Qt.QApplication(sys.argv)
systemtray_icon = Qt.QSystemTrayIcon(Qt.QIcon(""))
systemtray_icon.show()
systemtray_icon.showMessage("Check!", "Avvio")


while x<1:
     dati=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
     volte=0
     num=0
     indice=0

     response = requests.get("http://192.168.1.1/cgi-bin/sysconf.cgi?page=ajax.asp&action=status_wanInfo&time=1481306924884&_=1481306924884") #Questa è la pagine contenente tutte le statistiche del modem
     pagina = response.text

     for a in range(0, len(pagina)):
             if pagina[a] == "\t" or pagina[a] == ";":
                     indice = indice + 1
                     num = num + 1

             else:
                     dati[indice] = dati[indice] + pagina[num]
                     num = num + 1
     dati[0]='a'
	 
     if pagina[0] != 'S' and volte <= 3:
             app = Qt.QApplication(sys.argv)
             systemtray_icon = Qt.QSystemTrayIcon(Qt.QIcon("/usr/share/notify-osd/icons/Humanity/scalable/status/notification-gsm-full.svg"))
             systemtray_icon.show()
             systemtray_icon.showMessage("Check!", "Connessione Linkem non funzionante")
             volte = volte + 1

     elif pagina[0] == 'S' and volte != 0:
             
             app = Qt.QApplication(sys.argv)
             systemtray_icon = Qt.QSystemTrayIcon(Qt.QIcon("/usr/share/notify-osd/icons/Humanity/scalable/status/notification-gsm-disconnected.svg"))
             systemtray_icon.show()
             systemtray_icon.showMessage("Check!", "Connessione Linkem funzionante")
             volte = 0
     
     print (" Download",dati[32],"Kbs\n","Upload",dati[29],"Kbs\n","Intensita' del segnale",dati[22],"dBm\n","Qualita' segnale",dati[21],"dB\n\n")

     time.sleep(1)
