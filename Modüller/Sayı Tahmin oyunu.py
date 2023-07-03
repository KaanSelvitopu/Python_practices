import random
import time

print("""*********************

Sayı Tahmin Oyunu




1 ile 40 arasında sayıyı tahmin edin
**************************""")

rastgele_sayı=random.randint(1,40)
tahmin_hakkı=7
while True:
    tahmin=int(input("Tahmininiz:"))

    if(tahmin<rastgele_sayı):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Daha Yüksek Bir sayı söyleyin")
        tahmin_hakkı-=1
    elif(tahmin>rastgele_sayı):
        print("Bilgiler Sorgulanıyor.")
        time.sleep(1)
        print("Daha Düşük Bir Sayı söyleyiniz")
        tahmin_hakkı-=1
    else:
        print("Bilgiler Sorgunlanıyor...")
        time.sleep(1)
        print("Tebrikler Doğru Cevap",rastgele_sayı)
        break
    if(tahmin_hakkı==0):
        print("Tahmin Hakkınız Bitti")
        print("Sayımız:",rastgele_sayı)
        break
