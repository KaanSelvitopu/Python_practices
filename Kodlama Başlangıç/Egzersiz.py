print("""*******************
Kullanıcı Girişi
""")
sys_kullanıcı_adı ="Kaan"
sys_parola ="12345"

kullanıcı_adı = input("Kullanıcı Adı:")
parola = input("Parola:")

if (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
    print("Şifre Hatalı")
elif(kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
    print("Kullanıcı Adı Hatalı")
elif(kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
    print("Kullanıcı Adı ve Şifre HATALI")
else:
    print("Giriş Başarılı")