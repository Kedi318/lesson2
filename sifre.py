import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
karakter_sayisi = int(input("Şifrede kaç karakter olacak? "))
sifre = ""
for i in range(karakter_sayisi):
    sifre += random.choice(karakterler)
print(sifre)