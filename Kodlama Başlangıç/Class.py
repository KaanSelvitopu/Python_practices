import random
import time

class Kumanda():


    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["Trt"],kanal = "Trt"):
        self.tv_durum =tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):

        if(self.tv_durum == "Açık"):
            print("Tv Zaten Açık")
        else:
            print("Tv Açılıyor")
            self.tv_durum = "Açık"
    def tv_kapat(self):
        if(self.tv_durum == "Kapalı"):
            print("Tv Zaten Kapalı")
        else:
            print("Tv Kapanıyor")
            self.tv_durum = "Kapalı"
    def ses_ayarları(self):

        while True:
            cevap = input("Sesi azalt: '<'\nSesi artır: '>'\nÇıkış:exit ")
            if(cevap == "<"):
                if(self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses",self.tv_ses)
            elif(cevap == ">"):
                if(self.tv_ses != 32):
                    self.tv_ses +=1
                    print("ses",self.tv_ses)
            else:
                print("ses güncellendi",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal Ekleniyor....")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi...")
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şuanki Kanal",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv durumu : {}\nTv ses :{}\nKanal listesi :{}\nŞu anki kanal :{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = Kumanda()
print(""" 



Televizyon Uygulaması

1. Tv aç
2. Tv kapat
3.Ses Ayarları
4.Kanal ekle
5.Kanal sayısını öğrenme
6.Rastgele Kanal geçme
7.Televizyon bilgileri


Çıkmak için 'q' ya basınız.
""")

while True:
    işlem = input("işlemi seçiniz:")

    if(işlem == "q"):
        print("program sonlandırılıyor...")
        break
    elif(işlem == "1"):
        kumanda.tv_ac()
    elif(işlem == "2"):
        kumanda.tv_kapat()
    elif(işlem == "3"):
        kumanda.ses_ayarları()
    elif(işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak giriniz")
        kanal_listesi= kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif(işlem =="5"):
            print("kanal sayısı:",len(kumanda))
    elif(işlem == "6"):
        kumanda.rastgele_kanal()
    elif(işlem == "7"):
        print(kumanda)
    else:
        print("Geçersiz işlem")










