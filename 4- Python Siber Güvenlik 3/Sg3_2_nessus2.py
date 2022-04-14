import requests
import subprocess
import datetime
import sqlite3
cikti = subprocess.check_output("dir", shell=True)
if not "port.db" in str(cikti):
    conn = sqlite3.connect("port.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE portlar (port text, ip text, zaman text)''')
    c.close()
header={"X-ApiKeys": "accessKey=77687b4cdd16a30add699769d8af5d9272c279561dd6952c8d8514684d069a13; secretKey=815770509260a5baadcaa91f3faa36a5a125e16bb55f6dd8f501f4358bc96b08;"}
url = "https://127.0.0.1:8834/scans"
sonuc = requests.get(url=url,headers=header,verify=False)
for i in sonuc.json()["scans"]:
    scan_id = i["id"]
    url = "https://127.0.0.1:8834/scans/" + str(i["id"])
    tarama = requests.get(url=url,headers=header,verify=False)
    for j in tarama.json()["hosts"]:
        try:
            host_id=j["host_id"]
            url = "https://127.0.0.1:8834/scans/" + str(scan_id) + "/hosts/" + str(host_id) + "/plugins/11936"
            IP = requests.get(url=url, headers=header, verify=False)
            for k in IP.json()["outputs"]:
                port = list(k["ports"].keys())[0]
                IP = j["hostname"]
                conn = sqlite3.connect("port.db")
                c = conn.cursor()
                cikti = c.execute("select * from portlar where port=? and ip=?", (port,IP))
                port_sayisi = len(cikti.fetchall())
                conn.close()
                if port_sayisi <1:
                    print("Yeni port: ",port, " IP:", IP)
                    conn = sqlite3.connect("port.db")
                    c = conn.cursor()
                    c.execute("INSERT INTO portlar VALUES (?, ?, ?)",(port,IP,str(datetime.datetime.now)))
                    conn.commit()
                    conn.close()
     except:
            pass