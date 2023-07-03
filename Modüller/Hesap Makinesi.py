import math

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    return a / b

def karekok(a):
    return math.sqrt(a)

def usalma(a, b):
    return a ** b

def faktoriyel(a):
    return math.factorial(a)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def tan(a):
    return math.tan(math.radians(a))

def main():
    while True:
        print("Hesap Makinesi")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Karekök")
        print("6. Üs alma")
        print("7. Faktöriyel")
        print("8. Sinüs")
        print("9. Kosinüs")
        print("10. Tanjant")
        print("0. Çıkış")
        secim = int(input("Yapmak istediğiniz işlemi seçin: "))

        if secim == 0:
            print("Hesap makinesi kapatılıyor...")
            break
        elif secim == 1:
            a = float(input("Birinci sayıyı girin: "))
            b = float(input("İkinci sayıyı girin: "))
            print("Sonuç: ", toplama(a, b))
        elif secim == 2:
            a = float(input("Birinci sayıyı girin: "))
            b = float(input("İkinci sayıyı girin: "))
            print("Sonuç: ", cikarma(a, b))
        elif secim == 3:
            a = float(input("Birinci sayıyı girin: "))
            b = float(input("İkinci sayıyı girin: "))
            print("Sonuç: ", carpma(a, b))
        elif secim == 4:
            a = float(input("Birinci sayıyı girin: "))
            b = float(input("İkinci sayıyı girin: "))
            if b != 0:
                print("Sonuç: ", bolme(a, b))
            else:
                print("Hatalı giriş. Sıfıra bölme hatası!")
        elif secim == 5:
            a = float(input("Sayıyı girin: "))
            print("Sonuç: ", karekok(a))
        elif secim == 6:
            a = float(input("Taban sayıyı girin: "))
            b = float(input("Üs sayısını girin: "))
            print("Sonuç: ", usalma(a, b))
        elif secim == 7:
            a = int(input("Sayıyı girin: "))
            print("Sonuç: ", faktoriyel(a))
        elif secim == 8:
            a = float(input("Açıyı girin (derece cinsinden): "))
            print("Sonuç: ", sin(a))
        elif secim == 9:
            a = float(input("Açıyı girin (derece cinsinden): "))
            print("Sonuç: ", cos(a))
        elif secim == 10:
            a = float(input("Açıyı girin (derece cinsinden): "))
            print("Sonuç: ", tan(a))
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
main()

