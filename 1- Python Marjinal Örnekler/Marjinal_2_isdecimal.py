veri = "Egitim 101"
egitim = list(veri)
harf_sayici = 0
rakam_sayici = 0
for i in egitim:
    if str(i).isdecimal():
        rakam_sayici +=1
    else:
        harf_sayici +=1
print("Rakam sayisi: ", rakam_sayici)
print("Harf sayisi: ", harf_sayici)