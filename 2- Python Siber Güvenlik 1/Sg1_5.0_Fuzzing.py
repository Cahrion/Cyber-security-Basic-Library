import requests
dosya = open("PSG_5.1_Fuzzing.txt","r")
icerik = dosya.read()
dosya.close()
header = {"Cookie": "security=low; PHPSESSID=a0b29e43b154e8cf261c3a93686bdd94"}
for i in icerik.split("\n"):
    print(i)
    url = "https://10.10.10.10"+ str(i)
    sonuc = requests.get(url=url, headers=header)
    if "200" in str(sonuc.status_code):
        print("Dosya veya dizin var: ", i)
    else:
        print("Dosya veya dizin yok: ",i)