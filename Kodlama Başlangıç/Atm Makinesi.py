print("""****************************************

X BANK ATM

İşlemler;

1. Bakiye Sorgulama

2. para yatırma

3. Para çekme


Programdan çıkmak için 'q' ya basın. 
****************************************
""")

bakiye = 1000


while True:
    işlem = input("İşlemi Seçiniz:")

    if(işlem == "q"):
        print("yine bekleriz.")
        break
    elif(işlem == "1"):
        print("Bakiyeniz {} tl dir".format(bakiye))

    elif(işlem == "2"):
        miktar = int(input("Miktarı Giriniz:"))
        bakiye += miktar

    elif(işlem == "3"):
        miktar = int(input("Miktarı Giriniz:"))
        if(bakiye - miktar < 0):
            print("Böyle Bir miktar çekemezsiniz")
            continue
        bakiye -= miktar

    else:
        print("Geçersiz İşlem...")
