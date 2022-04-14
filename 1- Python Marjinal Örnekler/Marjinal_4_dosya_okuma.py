dosya=open("sayilar.txt","r")
icerik = dosya.read()
dosya.close()
for i in icerik.splitlines():
    print(i)