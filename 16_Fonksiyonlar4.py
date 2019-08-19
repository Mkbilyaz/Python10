# a = 4
# def fonk():
#     global a
#     a = 8
#     print(a)
# fonk()
# print(a)


dosya = open("deneme.csv","r+")
Adi = input("Adınızı Giriniz")
Soyadi = input("Soyadinizi Giriniz")
Telefon = input("Telefonu Giriniz")
kayit = "{};{};{}".format(Adi,Soyadi,Telefon)
print(kayit)

