print("""***************

FAKTÖRİYEL BULMA PROGRAMI

çıkmak için 'q' ya basınız
*************************""")

while True:
    sayı = input("Sayı:")

    if(sayı == "q"):
        print("Program Sonlandırılıyor.")
        break
    else:
        sayı = int(sayı)

        faktöriyel = 1

        for i in range(2,sayı+1):
            print("Faktöriyel",faktöriyel,"i:",i)
            faktöriyel *= i
        print("Faktöriyel",faktöriyel)