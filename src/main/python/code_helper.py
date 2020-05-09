import requests


def foundValue():
    try:
        response = requests.get(
            "http://192.168.1.1/cgi-bin/sysconf.cgi?page=ajax.asp&action=status_wanInfo&time=1481306924884&_=1481306924884",
            timeout=2)  # Questa è la pagine contenente tutte le statistiche del modem
        pagina = response.text

        pagina = pagina.split("\t")

        pagina[27] = pagina[27].split(";")
        return pagina[30], pagina[27][1], pagina[21], pagina[20]

    except Exception:
        return "Error", "Error", "Error", "Error"
    # (" Download",pagina[30],"Kbps\n","Upload",pagina[27][1],"Kbps\n","Intensita' del segnale",pagina[21],"dBm\n","Qualita' segnale",pagina[20],"dB\n\n")
