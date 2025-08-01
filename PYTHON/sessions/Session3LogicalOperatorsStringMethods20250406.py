
# Comparison Operators
# Karşılaştırma opratörleri boolean döndürür.

print(5 == 5)

print(9 == 2)

print(1 != 8)

print(2 != 2)

print(2 > 3)

print(2 < 5)

print(3 >= 2)

print(4 <= 3)

# Logical Operators
# Mantıksal operatörler boolean döndürür.
# and, or, not
# işlem önceliği: not > and > or

print(1 is not False) # True 
print(1 is True) # False # is operatörü nesne kimliğini (yani bellekteki yerini) karşılaştırır. 1 ve True eşit değerde olabilir ama aynı nesne değildirler.

print(1 == True) # True # == operatörü değerleri karşılaştırır. 1 ve True (1) değer olarak eşittirler.
print(1 != False) # True # != operatörü değerleri karşılaştırır. 1 ve False (0) eşit değerde değildirler.

print(0 is not False) # True is not operatörü nesne kimliğini (yani bellekteki yerini) karşılaştırır. 0 ve False eşit değerde olabilir ama aynı nesne değildirler.

print(2 and 3 ) # 3 # Hepsi True olduğunda en sonuncuyu döndürür.
print(0 and 1000) # 0 # Gördüğü ilk False değeri yazdırır.
"""and ifadesi, bool sonucu döndürmek zorunda değildir. x and y ifadesi:
Eğer x False ise, sonucu x olur.
Eğer x True ise, sonucu y olur."""

print(1 and False and 0 and 5) # False

print(0 or 1) # İlk gördüğü True değeri döndürür. # 1
print(None or 5 or 0) # 5 # None False olarak döner
print(0 or False or None) # None # Hepsi False ise sonuncuyu döndürür.
print(None or 0) # 0 Önemli

print(2 or 0 or 9) # 2 # İlk gördüğü True ifadedeyi döndürür.

print("Bilsen" or [] and 0) # Bilsen # işlem önceliği: and > or

print(False or 9 and not 0) # True # işlem önceliği: not > and > or önemli

print([] or not 1 and 0) # False # işlem önceliği: not > and > or önemli

print(True or False and not 0 and 8 or False) # True # işlem önceliği: not > and > or 

print(not 0) # True # not önüne geldiği ifadenin tersini döndürür. 
print(not 1) # False # not operatörü, True ve False değerlerini tersine çevirir.

print('Mukaddes' or []) # Mukaddes

print('To be' or not 'To be') # To be # not 'To be' ifadesi False döner. False or 'To be' ifadesi 'To be' döner.

print(0 != 0) # False # != operatörü değerleri karşılaştırır. 0 ve 0 eşit değerdedirler.

print(0 is not False) # True # is not operatörü nesne kimliğini (yani bellekteki yerini) karşılaştırır. 0 ve False eşit değerde olabilir ama aynı nesne değildirler.




# String methods

# input() fonksiyonu, kullanıcıdan bir girdi alır ve çıktısı str olur.

input("Adınızı giriniz :")

isim = input("Adınızı yazınız : ")
print(isim)

yas = input("Yaşınızı yazınız : ")
print(type(yas)) # str döner.
print(yas) # str döner.

#10 yıl sonra kaç yaşında olacaksınız?
yas_10 = int(yas) + 10
print(f"Bugünkü yaşınız {yas}, 10 yıl sonra {yas_10} yaşında olacaksınız.") # int() fonksiyonu, str'i int'e çevirir. 
# f string metodu ile değişkenleri string içerisinde kullanabiliyoruz.

# Girilen sayının karesini hesaplayın
sayi = input("Bir sayı giriniz : ")
sayi = int(sayi)
karesi = sayi ** 2 
print(f"Girdiğiniz sayı {sayi}, bu sayının karesi {karesi}")

sayi_1 = float(input("Numara giriniz : "))
print(type(sayi_1)) # float döner.
print(sayi_1)

yas_1 = int(input("Yaşınızı giriniz : "))
print(f"Yaşınız {yas_1}, 10 yıl sonra {yas_1 + 10} yaşında olacaksınız.")


# lower()  metodu, stringi küçük harfe çevirir.

print("FEYYAZ".lower())

isim = "Miyase"
print(isim)
print(isim.lower())

x = "TECHPRO Education"
print(x.lower())
print(x)

"""String immutable olması şöyle düşünebilirsin:
Bir kağıda HELLO yazdın, ama o kağıda bir daha yazı yazamazsın.
Yeni bir kağıda hello yazarsın, sonra elindekini değiştirirsin."""

sehir = input("Yaşadığınız şehir : ")
print(sehir)

sehir_1 = input("Yaşadığınız şehir : ").lower() 
print(sehir_1)


# upper() String ifadeleri büyük harfe çevirir.

sehir_2 = input("Bir şehir giriniz : ")
print(sehir_2)
print(sehir_2.upper()) # String ifadeleri büyük harfe dönüştürür.
print(sehir_2.lower())

print("İZMİR".lower())

print("izmir".upper()) # IZMIR   python büyüttüğü zaman İngilizce karaktere göre büyütür.


# title() metodu, her bir sözcüğün ilk harfini büyük yapar.

print("birazdan mola vereceğiz.".title()) # Birazdan Mola Vereceğiz.

# capitalize() metodu, cümlenin ilk harfini büyük harf yapar.

print("python öğrenmek çok eğlenceli".capitalize()) # Python öğrenmek çok eğlenceli 
print("python öğrenmek çok eğlenceli".title()) # Python Öğrenmek Çok Eğlenceli


# swapcase() metodu, büyük harfleri küçük, küçük harfleri büyük yapar.

print("pytHON".swapcase()) # PYThon



# Indexing and Slicing
# Karakterlere erişim sağlar.


"""
Veri Yapısı	         İndeksleme	       Dilimleme	       Not
str	                   E                  E                 -
list	               E                  E                 -
tuple	               E                  E                 Değiştirilemez
range	               E                  H                 Genelde list() ile
set	                   H                  H                 Sırasız
dict	               H                  H                 Sırasız ve anahtar-değer çiftleri ile erişilir.
numpy.array            E                  E                 Numpy dizileri için geçerli.
"""

name = "Techpro Education"
print(f"Hello my name is {name}.")
print(name[0])
print(name[8])
print(name[7])
print(name[16])
print(name[-1]) # Son karaktere erişim sağlar.
print(name[-5])

print("Techpro" + " " + "Education") # + operatörü string ifadelerle kullanılınca uç uca ekleme yani concat yapar

print("Techpro" * 3) # * operatörü string ifadeleri verilen sayı kadar uç uca ekler

print(name[4] + name[5] + name[6]) # pro

print(name[2] + name[-5] + name[-1]) # can

print(name[4:7]) # değişken[start : stop] start dahildir stop indexi dahil değildir

print(name[:4]) # 0'dan 4'e kadar olan karakterleri alır. 0 dahil 4 hariç.

print(name[ : ]) # Tüm karakterleri alır.

print(name[-2 : -5]) # boş string döndürdü, Python her zaman soldan sağa çalışır. Python sola doğru gitmez. 

print(name[-2:2]) # boş string döndürdü

print(name[-2:-1]) # o

print(name[-2:-5:-1]) # oit Eğer tersine gitmek istiyorsak step parametresi eklemek gerekir. -1 ile sağdan sola gidilir.

print(name[ : : -1]) # Tüm karakterleri ters çevirir.
# değişken[start : stop : step] step negatif girilirse tersten okur

"""step parametresi, Python’da slicing (dilimleme) işlemlerinde kaç adımda ilerleyeceğini belirler. 
Yani start ile stop arasında kaç adım atlayarak ilerleyeceğini söyler.
değişken[start : stop : step]
step için varsayılan değer 1’dir.
"""

print(name[-2::-5]) # ourT #-2'den başlar, 5'er 5'er atlayarak indeksleri getirir

# name = Techpro Education
print(name[3:-4:2]) # hr dc 3'ten başlar, -4'e kadar 2'şer atlayarak indeksleri getirir. 3, 5, 7, 9, 11 bitiş indeksi dahil edilmez -4 (13) dahil değil ÖNEMLİ ******

name_1 = name[3:7]
print(name_1) # hpro

print("Gülay"[:3]) # Gül 




# len() metodu, string ifadedeki eleman sayısını verir. indeks sayısından bir fazladır, 0'dan başlamaz.

print(len(name)) # 17 karakter var. boşluklar da sayılır.

print(len("Gülay")) # 5




# replace() metodu,verilen alt dizeyi yeni ifade ile değiştirir.

print(name.replace(" ","&")) # Techpro&Education
print(name) # Techpro Education
# Python stringleri immutable (değiştirilemez) olduğu için replace() yeni bir string döner, orijinali değiştirmez.

name_2 = "Dersimiz bitiyor."
print(name_2) # Dersimiz bitiyor.
print(name_2.replace("i","$")) # Ders$m$z b$t$yor.


