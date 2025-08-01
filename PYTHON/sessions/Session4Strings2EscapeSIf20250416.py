
# is ile başlayan string metotları

# isalnum() : alfanumerik  olup olmadığını sorgular.

name = "Techpro!"
print(name.isalnum()) # False ünlem işareti olduğu için False döner.

print("hello123".isalnum()) # Sadece numara ve harflerden oluştuğu için True döndürür.

print("369".isalnum()) # Sadece numara olduğu için True döndürür.

# isnumeric() : string ifadenin sadece sayılardan mı oluşuyor bunu kontrol eder.

print("369".isnumeric()) # True 

print("hello123".isnumeric()) # False çünkü içinde harf var.

print("12 56".isnumeric()) # False çünkü içinde boşluk var.

print("-5 -2j".isnumeric()) # False çünkü içinde - ve j var.

print("-5-2j".isnumeric()) # False çünkü içinde - ve j var.

print("-5".isnumeric()) # False çünkü içinde - var.

print("1.5".isnumeric()) # False çünkü içinde . var.

# isalpha() : string ifadenin sadece harflerden mi oluştuğunu kontrol eder.

print("hello".isalpha()) # True çünkü sadece harflerden oluşuyor.

print("hello123".isalpha()) # False çünkü içinde rakam var.

print("Merhaba Dünya".isalpha()) # False çünkü içinde boşluk var.


"""
 Python’da bu metotlar CamelCase değil,snake_case de değil,flatcase (hepsi küçük, arada alt çizgi yok)
Örneğin:
str.isalnum()
str.isnumeric()
str.islower()
Sebebi:
Bu metotlar Python’un C ile yazılmış standart kütüphanesinden geliyor. Python’un ilk sürümleri C dilinde yazıldığında, fonksiyon 
isimleri genelde bu tarzda (alt çizgisiz ve küçük harfli) tanımlanırdı. Bu alışkanlık string metodlarına da yansıdı.
Sen kendi fonksiyonlarını Python'da her zaman snake_case ile yazmalısın, çünkü bu PEP8 standardı.Ama isalpha() gibi hazır metodlar farklı — bu 
Python’un kendi stilinde istisna diyebiliriz.
Python’un hazır metotlarının büyük kısmı flatcase (yani tamamen küçük harf ve alt çizgi yok) olarak yazılmıştır ama bazıları snake_case şeklindedir.
Python'da kendi yazdığımız fonksiyonlarda ve modern API'de snake_case önerilir ama
hazır metotların büyük kısmı flatcase. 
"""

# islower() : string ifadenin sadece küçük harflerden mi oluştuğunu kontrol eder.

print("Selam".islower()) # False çünkü içinde büyük harf var.

print("merhaba".islower()) # True çünkü sadece küçük harflerden oluşuyor.

# isascii() : string ifadenin ASCII karakterlerden mi oluştuğunu kontrol eder.Türkçe karakter varsa false verir.

print("İstanbul".isascii()) # False çünkü İ ascii karakter değildir.

print("Istanbul".isascii()) # True 

# istitle() : string ifadenin baş harfi büyük mü kontrol eder.

print("İstanbul".istitle()) # True çünkü baş harfi büyük.


# count() : string ifadenin içinde bir bir alt dizenin kaç kez geçtiğini sayar.

print("Selam Naber Gelecek misiniz".count("e")) # 5 tane e var. Önemli

print("Selam Naber Gelecek misiniz".count("i")) # 3

print("Selam Naber Gelecek misiniz".count("el")) # 2

print("Siz bizim çekoslovakyalılalıştıramdıklarımızdan mısınız".count("a")) # 6

print("Hello , 123, 3.14".count("3")) # 2

# split() string ifadeyi bir alt dizeye ayırır. Bir şey vermezsek default olarak boşluklardan ayırır.
# split() metodu string ifadeyi bir listeye dönüştürür.
# maxsplit parametresi ayırma işlemini en fazla kaç tane yapacağını belirler.

print("Siz bizim çekoslovakyalılalıştıramdıklarımızdan mısınız".split())
# ['Siz', 'bizim', 'çekoslovakyalılalıştıramdıklarımızdan', 'mısınız']

print("Siz bizim çekoslovakyalılalıştıramdıklarımızdan mısınız".split(sep = "i", maxsplit = 5))
# ['S', 'z b', 'z', 'm çekoslovakyalılalıştıramdıklarımızdan mısınız'] 

print("Karaca ahmet".split(sep = "a", maxsplit = 3)) # ['K', 'r', 'c', ' ahmet']

print("Anlaşıldı hocam".split()) # ['Anlaşıldı', 'hocam']

print("Anlaşıldı hocam".split(sep = "ı")) # ['Anlaş', 'ld', ' hocam']


# strip() 

print("  Python çok eğlenceli    ".strip()) # Başta ve sondaki boşlukları siler.

print("Biz     de     sevmeye      başladık.".strip()) # Aradaki boşlukları silmez.
# Biz     de     sevmeye      başladık.

print("***  Hello   ***".strip("*")) # "  Hello   "     Baştaki ve sondaki yıldızları sildi, boşlukları silmedi.

# rstrip() 

print("    Hello     ".rstrip()) #     Hello  sadece sağdakini sildi

print("1299345999999999999".rstrip("9")) # 1299345

# lstrip()

print("      Hello     ".lstrip()) # "Hello     "  sadece soldakini sildi

print("123123456123".lstrip("123")) # 456123

print("123123456123".strip("123")) # 456

print("Techpro Education".strip("Teno")) # chpro Educati  DİKKAT: stripe girilen Stringteki sıralama önemli değil, harfler başta ve sonda varsa silinir

print("Goooooogle".strip("Go")) # gle    DİKKAT: stripe girilen Stringteki sıralama önemli değil, harfler başta ve sonda varsa silinir

print("1+5j+2+6j+5+5j+-3-3j-9j".strip("1+5j-9j")) # 2+6j+5+5j+-3-3

# Escape Sequences

print('I\'m a python teacher.') # \ önüne geldiği karakterin görevini iptal eder.
# I'm a python teacher.

print("Python programlama dilinin adı \"piton yılanından\" gelmez.")
# Python programlama dilinin adı "piton yılanından" gelmez.

print("Python programlama \ndilinin adı \npiton yılanından gelmez.")
"""Python programlama 
dilinin adı 
piton yılanından gelmez."""

# \t tab kadar boşluk koyar

print("Python \tprogramlama \tdilinin \tadı \tpiton \tyılanından \tgelmez.")
# Python  programlama     dilinin         adı     piton   yılanından      gelmez.

print("Python programlama", "dilinin adı", "piton yılanından gelmez.", sep = "\t")
# Python programlama      dilinin adı     piton yılanından gelmez.

print("Ptyhon", "Çok güzel\b", sep = "*****")

print("\a") # bip sesi verir

print("C:\aylar\nisan\toplam masraf")
"""C:ylar
isan    oplam masraf""" # \a, \n ve \t kaçış karakteri olarak algıladı. Dosya yolunu yanlış yorumladı. Bunun için "r" kullanılmalı.

print(r"C:\aylar\nisan\toplam masraf") # C:\aylar\nisan\toplam masraf   kaçış karakterlerini ascii elemanı olarak kullanılmasını sağlar.

# Ya da ters slash kullanabiliriz. Yukardaki örnekteki gibi ters slash önüne geldiği karaktewrin görevini iptal eder.
print("C:\\aylar\\nisan\\toplam masraf") # C:\aylar\nisan\toplam masraf


# if & elif & else

# if

x = 4
if x < 5:
    print("x 5'ten küçüktür.") 

x = 7
if x < 5:
    print("x 5'ten küçüktür.")

"""if 2 != 3:
print("Girinti önemli")""" # IndentationError: expected an indented block after 'if' statement on line 1

"""if 4 > 1
    print(": önemli") """ # SyntaxError: expected ':'

if "Uluğbek":
    print("Sizce bu kod çalışır mı") # Sizce bu kod çalışır mı

# else

if 5 > 4:
    print("if kısmı çalıştı.")
else:   # değilse
    print("else kısmı çalıştı.")
# if kısmı çalıştı.

if 3 > 4 :
    print("if kısmı çalıştı.")
else:
    print("else kısmı çalıştı") 
# else kısmı çalıştı

# elif (else if'in kısaltılmışı), çok sayıda elif bloğu kullanılabilir

x = 8
if x < 2:
    print("if bloğu çalıştı.")
elif x < 9:
    print("elif bloğu çalıştı.")
# elif bloğu çalıştı.

x = 2
if x < 2:
    print("if bloğu çalıştı.")
elif x < 9:
    print("1. elif bloğu çalıştı.")
elif x == 2:
    print("2. elif bloğu çalıştı.")
# 1. elif bloğu çalıştı.
# Python yukarıdan aşağı kodları çalıştırır. if bloğu içerisindeki koşullardan ilk true olan koşulu yazdırır. 

x = 8
if x < 2:
    print("if kısmı çalıştı.")
elif x > 9:
    print("elif kısmı çalıştı.")
else:
    print("else kısmı çalıştı.")

# else kısmı çalıştı.


if True:
    print("Bu if bloğu hep çalışır.")
    print(2 * 5)
    print(5 / 3)

"""Bu if bloğu hep çalışır.
10
1.6666666666666667"""


if 5 > 3 :
    print("5 3'ten büyüktür.")
if 4 > 2 :
    print("4 2'den büyüktür.")
# 5 3'ten büyüktür.
# 4 2'den büyüktür.

if 4 and False:
    print("Sizce bu çıktıyı yazar mı?")
else:
    print("Yoksa else kısmı mı çalışır.")
# Yoksa else kısmı mı çalışır.

"""
1- input ile kullanıcıdan yaşını öğrenin.
2- Eğer yaşı 31'un altındaysa "Çok gençsin" yazdırın
3. Eğer yaşı 31 (dahil) - 60 (dahil) aralığındaysa "Olgunlaşmışsın" yazdırın
4- Eğer yaşı 60'dan büyükse "Yaşlısın" yazdırın """


yas = int(input("Yaşınızı giriniz:")) # input str döndürür



if yas>0 and yas < 31: # javadan farklı olarak 0 < yas < 31
    print("Çok gençsin")
elif yas >= 31 and yas <= 60: # javadan farklı olarak 31 =< yas <= 60
    print("Olgunlaşmışsın")
elif yas > 60 and yas <=100: # javadan farklı olarak 60 < yas <= 100
    print("Yaşlısın")
else:
    print("Hatalı giriş")



if 0 < yas < 31:
     print("Çok gençsin")
elif 31 <= yas <= 60:
      print("Olgunlaşmışsın")
elif 60 < yas < 100:
     print("Yaşlısın")
else:
    print("Hatalı giriş")




# nested if

if x < 9:
    if 5 > 8:
        print("This is true")
    else:
        print("this is false")
elif 4 > 9:
    print("This is elif")

# Kullanıcıdan input ile notunu öğrenin.Harf sistemine göre bu notun karşılığını veren python programını yazınız.

puan = float(input("Puanınızı giriniz:"))
if puan >= 90:
    notun = 'A'
elif puan >= 80:
    notun ='B'
elif puan >= 70:
    notun = 'C'
elif puan >= 60:
    notun = 'D'
else:
    notun = 'E'
print(f"Girdiğiniz puan : {puan}, Harf notunuz : {notun}")




# Ternary operator
x = 4
result = "x 5'ten büyük değildir" if x < 5 else "x 5'ten büyük değildir."
print(result)

