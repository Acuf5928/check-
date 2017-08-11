#!/usr/bin/env python3

#Questo programma visualizza la banda totale in Download e in Upload occupata oltre alla potenza del segnale 4G
#Il programma è pensato per modem Linkem che usano tecnologia 4G per la navigazione
#Il programma è stato testato su Ubuntu ma dovrebbe funzionare senza problemi anche su Windows
#Fai ciò che vuoi con questo programma, se puoi citami.

import requests, time
import sys

x=0

while x<1:
     dati=[]
     volte=0
     num=0
     indice=0

     response = requests.get("http://192.168.1.1/cgi-bin/sysconf.cgi?page=ajax.asp&action=status_wanInfo&time=1481306924884&_=1481306924884") #Questa è la pagine contenente tutte le statistiche del modem
     pagina = response.text

     pagina = pagina.split("\t")

     pagina[27] = pagina[27].split(";")
     print (" Download",pagina[30],"Kbs\n","Upload",pagina[27][1],"Kbs\n","Intensita' del segnale",pagina[21],"dBm\n","Qualita' segnale",pagina[20],"dB\n\n")

     time.sleep(1)
