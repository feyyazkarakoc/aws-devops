#  Kodunu çalıştırmadan önce Ctrl + S ile kaydetmeyi unutma.

"""
PowerShell:Bu, komut satırıdır (terminal).
VS Code’un kodu çalıştırmak için kullandığı alt yapı.
Senin Windows’un varsayılan terminali bu: PowerShell.
İstersen burayı CMD veya Git Bash gibi başka şeylerle değiştirebilirsin ama gerek yok şu an.
VS Code'da sen terminali seçebilirsin:
Menüden Terminal > Select Default Profile kısmına girip:
PowerShell
CMD
Git Bash hangisini istersen seçebilirsin.


Neden IDE’ler terminale ihtiyaç duyar?
Çünkü:
Kodun gerçekten çalışmasını sağlayan şey, IDE değil, işletim sistemin altındaki yorumlayıcı veya derleyicidir.
Nasıl çalışır?
Sen kodu IDE’de yazarsın (örneğin VS Code, IntelliJ, PyCharm vs.)
IDE bunu alır ve terminal üzerinden işletim sistemine komut verir:

python dosyam.py
javac Hello.java && java Hello
Bu komutlar, terminalde işletim sistemi tarafından çalıştırılır.

Çıktılar tekrar terminal üzerinden sana gösterilir.

İşletim sistemi mi çalıştırıyor?
IDE	Kodu yazmanı ve kolay çalıştırmanı sağlar (geliştirici arayüzüdür)
Terminal	Komutları işletim sistemine iletir
İşletim sistemi	Komutu alır, ilgili programı (Python, Java, C derleyici vs.) çalıştırır
Yorumlayıcı / Derleyici	Kodu çalıştırır ve çıktıyı üretir
 IDE neden kendi başına çalıştırmıyor?
Çünkü:
IDE bir editördür, bir programlama dili değildir.
Her dilin kendi çalıştırma mekanizması (yorumlayıcısı veya derleyicisi) vardır.
Bu yüzden IDE, sadece bu aracı çalıştırmak için terminali kullanır.

"Indentation (girinti) hatası", Python'da blok yapılarının yanlış girinti (boşluk veya tab) ile yazılması durumunda oluşan hatadır.
 Python’da süslü parantez {} gibi yapılar olmadığı için, hangi kod bloğunun hangi yapıya ait olduğunu girintiler (indentation) belirler.
Python’da girinti kuralları:
Her blok için 4 boşluk önerilir (PEP 8’e göre).
Aynı dosyada boşluk ve tab karıştırılmaz.
if, for, while, def, class gibi yapılar girinti gerektirir.

 Python’da tuple (okunuşu: tapıl), birden fazla veriyi tek bir değişkende saklamamıza yarayan sıralı ve değiştirilemez 
 (immutable) bir veri tipidir.
Parantez () ile tanımlanır.
Elemanlar sıralıdır (index ile erişilebilir).
Değiştirilemezler. Eleman ekleyemez, silemez, değiştiremezsin.
Farklı veri tipleri bir arada olabilir.
"""



print(4 % 2)  # Modulus operator
print(4 ** 2)  # Exponentiation operator
print(4 // 2) # Floor division operator
print(4 / 2)  # Division operator
print((2 +3) ** 2 / 5) # Order of operations

# Data Types
# int

x = 5
print(type(x))  # <class 'int'>

y = 2,5
print(type(y)) # <class 'tuple'>

y = 2.5
print(type(y))  # <class 'float'>

z = 1 + 2j
print(type(z))  # <class 'complex'>
print(z.real)  # 1.0
print(z.imag)  # 2.0
print(z.conjugate())  # (1-2j)

# zz = 1 + j # j'nin önünde sayı olmalı
# print(type(zz)) # name 'j' is not defined

a = 0
print(type(a)) # <class 'int'>

n = ""
print(type(n)) # <class 'str'>

b = 1
print(type(b)) # <class 'int'>

c = True
print(type(c)) # <class 'bool'>

print(type(a), type(n), type(b), type(c)) # <class 'int'> <class 'str'> <class 'int'> <class 'bool'>
print(a, n, b, c) # 0  1 True



# Sequences 
# str 
s =  "I'm a python instructor."
# s = 'I'm a python instructor.' # SyntaxError: invalid syntax

a = "Selam"
b = "Naber?"
print( a + b ) # Concat


print(a[0]) # S
print(a[:3]) # Sel # a'nın ilk 3 indexini alır

# string veriler immutable'dır.
# a[0] = "A" 
print(a) # 'str' object does not support item assignment


# list
l = [1, 2, 3, 4, 5]
print(type(l)) # <class 'list'>

my_list = [1, 2, [2, 3, 4]]
print(my_list[2][1]) # 3

# listeler mutable'dır.
my_list[1] = 0
print(my_list) # [1, 0, [2, 3, 4]]

yeni_liste = ['Uluğbek', 'Buse', 'İbrahim' ]
print(type(yeni_liste)) # <class 'list'>
print(yeni_liste[0])
print(yeni_liste[0][4])
yeni_liste[0] = 'Sabina'
print(yeni_liste) # ['Sabina', 'Buse', 'İbrahim']


# tuple
# Tuple'lar parantez () ile tanımlanır.
t = (1, 2, 3)
print(type(t)) # <class 'tuple'>

# tuple'lar immutable'dır.
# t[0] = 5 # 'tuple' object does not support item assignment
print(t) # (1, 2, 3)

t_2 = (False, True, 2 ,'Ayşe')
print(type(t_2)) # <class 'tuple'>
# t_2[0] = 3
print(t_2) # 'tuple' object does not support item assignment


l_2 = [False, True, 2 ,'Ayşe']
print(type(l_2)) # <class 'list'>

# Madem her ikisi de farklı türler alıyor. Neden hem tuple hem list var. Çünkü listeler mutable'dır, tuple'lar immutable'dır.
# Tuple'lar hafızada daha az yer tutuyor.

print(t_2[3]) # Ayşe
print(type(t_2[3])) # <class 'str'>


# NoneType
l = [None, 1, 2, 3]
print(type(l[0])) # <class 'NoneType'>

print(2, 3, True) # sep: str | None = " "
print('Hello') # end: str | None = "\n" (alt satıra geçer)
"""
2 3 True
Hello
"""

"""
print() fonksiyonunun parametreleri:

sep: separator (ayraç)
print() içine birden fazla şey yazarsan, aralarına ne konacağını belirler.
Varsayılan: " " yani bir boşluk

 end: end-of-line (satır sonu)
print() sonunda neyle bitsin diye belirler.
Varsayılan: "\n" yani yeni satır

"""

print('Hello')
print('World')
"""Hello
World"""

print('Hello', end = ' ')
print('World') # Hello World

print('Hello', 'World', sep = ' * ') # Hello * World

# Type Conversion (Tür Dönüşümü)

# str()

# String Türkçesi Karakter dizisi veya metin.

sayi = 365
str_sayi = str(sayi) # '365' # int to str
print(sayi, end = ' * * * ')
print(str_sayi, end = ' # # # ')
print(type(sayi))
print(type(str_sayi))
"""365 * * * 365 # # # <class 'int'>
<class 'str'>"""

print(str(2.5)) # '2.5' # float to str

print(str(False)) # 'False'  # bool to str

print("Boolean veriler : ", False, True, sep = "\n")
"""Boolean veriler :
False
True"""

a = 'False'
print(type(a)) # <class 'str'>

a = False
print(type(a)) # <class 'bool'>

# a =  false
print(type(a)) # NameError: name 'false' is not defined. Did you mean: 'False'?

# int()
"""
int() → hiç argüman verilmezse 0 döner
int(x) → x sayıya çevrilebiliyorsa onu int'e çevirir
int(x, base=10) → x bir string ise, belirtilen tabana göre dönüştürür"""

print(int()) # 0

print(int(2.5)) # 2 # float to int (küsuratı atar) Ondalıklı sayıları sıfıra doğru yuvarlar

print(int(2.9)) # 2 # float to int (küsuratı atar) Ondalıklı sayıları sıfıra doğru yuvarlar

print(int("123")) # 123 # str to int (string sayıyı int'e çevirir)

x = '345'
y = int(x)
print(type(x), type(y), sep = '\n')
"""
<class 'str'>
<class 'int'>
"""
print(x)
print(y)

# print(int('Techpro')) # ValueError: invalid literal for int() with base 10: 'Techpro'

# print(int(2,3)) # TypeError: int() can't convert non-string with explicit base, önemli

print(int(2.3)) # 2 # float to int (küsuratı atar) Ondalıklı sayıları sıfıra doğru yuvarlar

print(int(True)) # 1 # bool to int (True'nun karşılığı 1'dir)

print(int(False)) # 0 # bool to int (False'un karşılığı 0'dır)

# print(int(1 + 2j)) #  TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex', önemli

# print(int(2j)) TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex', önemli

x, y, z = 'python', 3.14, 9
print(x, y, z) # python 3.14 9
print("x : ", x, "y : ",y,"z : ",z)

# float()

print(float()) # hiç argüman verilmezse 0.0 döner, önemli

print(float(3)) # 3.0 # int to float (tam sayıyı float'a çevirir)

print("3.14") # 3.14 # str to float (string sayıyı float'a çevirir)

print(float(5/8)) # 0.625 # float to float (float'ı float'a çevirir)

# print(float("selam")) # ValueError: could not convert string to float: 'selam'

print(float(True)) # 1.0 # bool to float (True'nun karşılığı 1'dir)

print(float(False)) # 0.0 # bool to float (False'un karşılığı 0'dır)

print(int(float(True))) # 1 


# dictionary data type
# Dictionary'ler süslü parantez {} ile tanımlanır.
# Dictionary'ler key-value çiftleri ile çalışır.
# Dictionary'ler mutable'dır.

x = {'ad' : 'Ahmet',  'soyad' : "Kaya", 'yas' : 42}
print(type(x)) # <class 'dict'>
print(x)

y = dict(ad = 'Ahmet',  soyad = "Kaya", yas =  42)
print(y)

print(x.keys()) # dict_keys(['ad', 'soyad', 'yas'])
print(x.values()) # dict_values(['Ahmet', 'Kaya', 42])

print(y.keys()) # dict_keys(['ad', 'soyad', 'yas'])
print(y.values) # dict_values(['Ahmet', 'Kaya', 42])

# set data type
# Set'ler süslü parantez {} ile tanımlanır.
# Set'ler sırasız ve değiştirilebilir (mutable) veri tipidir.

a = {'Elma', 'Armut', 'Kiraz'}
print(type(a)) # <class 'set'>
print(a) # {'Elma', 'Armut', 'Kiraz'}
# print(a[0]) # TypeError: 'set' object is not subscriptable (set'ler sırasızdır, index ile erişemezsin)

liste =  [1, 2, 3, 3, 4, 4, 1, 5, 2]
temiz_liste = set(liste) # set() ile tekrar eden elemanları temizler
print(liste) # [1, 2, 3, 3, 4, 4, 1, 5, 2]
print(temiz_liste) # {1, 2, 3, 4, 5}
print(type(liste)) # <class 'list'>
print(type(temiz_liste)) # <class 'set'>

liste_2 = list(temiz_liste) # tekrar listeye dönüştürmek için list() kullanılır
print(liste_2) # [1, 2, 3, 4, 5]
print(type(liste_2)) # <class 'list'>

# Yarıçapı 7 olan bir dairenin alanını bulan python kodunu yazınız.
pi = 3.14
r = 7
dairenin_alanı = pi * r ** 2
print(dairenin_alanı)  # 153.86

