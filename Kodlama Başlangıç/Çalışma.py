print("********** KULLANICI GİRİŞİ **********")

sys_kullanıcı_adı = "Kaan"
sys_parola = "123456"
giriş_hakkı = 3
while True:
    kullanıcı_adı =input("Kullanıcı Adı:")
    parola = input("Parola:")
    if(sys_kullanıcı_adı == kullanıcı_adı and sys_parola != parola):
        print("Parola Hatalı Tekrar Deneyiniz...")
        giriş_hakkı -= 1
    elif(sys_kullanıcı_adı != kullanıcı_adı and sys_parola == parola):
        print("Kullanıcı Adı Hatalı Tekrar Deneyiniz...")
        giriş_hakkı -= 1
    elif(sys_kullanıcı_adı != kullanıcı_adı and sys_parola != parola):
        print("Kullanıcı Adı ve Şifre Hatalı Tekrar Deneyiniz...")
        giriş_hakkı -= 1
    else:
        print("Giriş Başarıyla Gerçekleştirildi")
        break
    if(giriş_hakkı == 0):
        print("Giriş Hakkı Kalmadı...")
        break