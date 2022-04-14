a_sinifi = ["Ahmet","Mehmet"]
b_sinifi = ["Ali","Ayse"]
isim = input("Kişi ismi: ")
if isim in a_sinifi:
    print("Kişi a sinifindadır.")
elif isim in b_sinifi:
    print("Kişi b sinifindadır.")
else:
    print("Kişi hiçbir sinifta bulunmamaktadır.")