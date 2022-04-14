import requests
import subprocess
header={"X-ApiKeys": "accessKey=77687b4cdd16a30add699769d8af5d9272c279561dd6952c8d8514684d069a13; secretKey=815770509260a5baadcaa91f3faa36a5a125e16bb55f6dd8f501f4358bc96b08;"}
url = "https://127.0.0.1:8834/scans"
sonuc = requests.get(url=url,headers=header,verify=False)
for i in sonuc.json()["scans"]:
    scan_id = i["id"]
    url = "https://127.0.0.1:8834/scans/" + str(i["id"])
    sonuc = requests.get(url=url,headers=header,verify=False)
    for i in sonuc.json()["hosts"]:
        try:
            IP=i["hostname"]
            host_id=i["host_id"]
            print(IP)
            print(host_id)
            print("==================")
            url = "https://127.0.0.1:8834/scans/" + str(scan_id) + "/hosts/" + str(host_id) + "/plugins/11936"
            zafiyet = requests.get(url=url, headers=header, verify=False)
            plugin_output = zafiyet.json()["outputs"][0]["plugin_output"]
            if "Windows" in plugin_output:
                dizin = subprocess.check_output("dir", shell="True")
                if not "windows.txt" in str(dizin):
                    veri = str(IP)  +"\n"
                    dosya = open("windows.txt","w")
                    dosya.write(veri)
                    dosya.close()
                dosya = open("windows.txt","r")
                IP_kontrol = dosya.read()
                dosya.close()
                if not str(IP) in IP_kontrol:
                    veri = str(IP) + "\n"
                    dosya = open("windows.txt","a")
                    dosya.write(veri)
                    dosya.close()
        except:
            pass