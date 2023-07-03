print(""" *************
Hesap Makinesi Programı

işlemler;

1. Toplama işlemi

2. Çıkarma işlemi

3. Çarpma işlemi

4. Bölme işlemi
**************
""")


a = int(input("Birinci Sayı:"))

b = int(input("İkinci Sayı:"))

işlem = input("İşlemi giriniz:")

if işlem == "1":
    print("{} ile {} toplamı {} dir".format(a,b,a+b))
elif işlem == "2":
    print("{} ile {} farkı {} dir".format(a,b,a-b))
elif işlem == "3":
    print("{} ile {} çarpımı {} dir".format(a,b,a*b))
elif işlem == "4":
    print("{} ile {} bölümü {} dir".format(a,b,a/b))
else:
    print("Geçersiz İşlem")