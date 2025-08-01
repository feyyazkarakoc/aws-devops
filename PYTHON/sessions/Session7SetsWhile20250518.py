
# Sets
# Türkçesi kümeler
# Unique değerler içeren (tekrarlı elemanlar kabul etmez) (unique), sıralaması olmayan (unordered), indexlenmeyen (indeksle erişilemez), mutable bir veri yapısıdır
# {} ve  set() metodu ile oluşturulur
# set() Fonksiyonu Python’daki yerleşik (built-in) bir fonksiyondur. Herhangi bir iterable'ı (liste, string, tuple vs.) alır ve bir kümeye (set) çevirir.

print(set("hello")) # {'e', 'o', 'l', 'h'} # tekrar eden l'yi almadı, sıralama yok

"""
Set içinde sadece hashlenebilir (değiştirilemez) türler olabilir.”
Bu, bir set'in içindeki elemanların sabit (değiştirilemez) olması gerektiği anlamına gelir.
Python’da set, elemanlarını benzersizliğe göre saklar. Bunu yaparken elemanların hash() değerini kullanır.
hash() fonksiyonu değişmeyen (immutable) türlerde çalışır.
Set içine konabilecek türler:
int, float, str, bool, tuple (içinde değiştirilebilir bir şey yoksa)
Set içine konamayacak türler:
list, dict, set → çünkü bunlar değiştirilebilir (mutable) ve hashlenemez.
Örnek:
s = set()
s.add(10)       # int eklenebilir
s.add("abc")    # str eklenebilir
s.add((1, 2))   # tuple eklenebilir
s.add([1, 2])   # TypeError: unhashable type: 'list'

set yapısının kendisi değiştirilebilir (eleman eklenebilir, silinebilir),
ama içine konulan tek tek elemanlar değiştirilemez (sabit olmalı).
Yani:
set → değiştirilebilir (mutable)
içindeki elemanlar → değiştirilemez (immutable ve hashlenebilir)

Örnek:
s = set()
s.add("elma")    # ekledik
s.remove("elma") # çıkardık
# Ama içeriye liste koyamazsın çünkü list değişebilir:
s.add([1, 2])    # hata verir: çünkü list mutable

Kısaca Özet:
set yapısı	Değiştirilebilir (add, remove vs.)
Set’in içindeki elemanlar	Değiştirilemez ve hashlenebilir olmalı
Neden böyle?	Python set, elemanları hızlı karşılaştırmak için hash() kullanır
"""


"""
Python'da veri türleri, değiştirilebilir (mutable) ve değiştirilemez (immutable) olmak üzere iki gruba ayrılır. 
Bu ayrım, bir değişkenin bellekteki içeriğinin değiştirilip değiştirilemeyeceğini belirler.

Immutable (Değiştirilemez) Türler
Bu türlerde bir değer atandıktan sonra, içeriği değiştirilemez. Yeni bir değer vermek, aslında yeni bir nesne oluşturur.
Örnek immutable türler:
int (tam sayılar)
float (ondalıklı sayılar)
bool (True, False)
str (metinler)
tuple (demetler) – ama içindeki öğeler de immutable olmalı
frozenset (donmuş set)
bytes (byte dizisi)

Örnek:
x = 5
print(id(x))  # x'in bellekteki adresi
x = x + 1     # Yeni bir değer atandı
print(id(x))  # Farklı bir adres —> çünkü int immutable

Mutable (Değiştirilebilir) Türler
Bu türlerde, bir değişkene atanan veri yerinde (in-place) değiştirilebilir. Yeni nesne oluşturulmaz, aynı bellek adresinde değişiklik yapılır.
Örnek mutable türler:
list (liste)
dict (sözlük)
set (küme)
bytearray

Örnek:
my_list = [1, 2, 3]
print(id(my_list))  # Bellek adresi
my_list.append(4)
print(my_list)      # [1, 2, 3, 4]
print(id(my_list))  # Aynı adres —> çünkü liste mutable
"""

x = set()
print(x)
print(type(x)) # <class 'set'> # sadece set() ile boş bir set oluşturulur

y = {}
print(y)
print(type(y)) # <class 'dict'> # {} ile boş bir set oluşturulamaz, bu bir dict oluşturur

z = {1}
print(z)
print(type(z)) # <class 'set'> # 

print(set("techpro education")) # {'d', 'o', ' ', 'i', 'a', 'p', 'r', 'u', 'h', 't', 'n', 'c', 'e'} # tekrar eden harfleri almadı, 
# boşluk karakterini de aldı, unordered sıraladı

set1 = {"blue", "green", "white", "magenta", "blue", "blue"} # dictioary'de de {} kullanıyorduk, python bu farkı anahtar : değer ile anlıyor
print(set1) # {'green', 'white', 'blue', 'magenta'} # tekrar eden elemanları almadı, unordered sıraladı
print(len(set1)) # 4 # tekrar eden elemanları almadı, sadece bir tane blue aldı, unique olmalı

# set2 = {[1,2,3,5,4,2,3,4,7,9,8,6]} # TypeError: unhashable type: 'list' # list mutable olduğu için hata verir
set2 = set([1,2,3,5,4,2,3,4,7,9]) # set() ile listeyi set'e çeviriyoruz
print(set2) # {1, 2, 3, 4, 5, 7, 9} 
print(len(set2)) # 7

alfabe = "a b c d e f g".split() # defaultu boşluktu, boşluk karakterine göre ayırdık
print(alfabe) # ['a', 'b', 'c', 'd', 'e', 'f', 'g'] # liste oluşturduk
set3 = set(alfabe) # set'e çeviriyoruz
print(set3) # {'e', 'b', 'f', 'g', 'd', 'a', 'c'}

print(set([1, True, False, 0, 1.0 , 0.0])) # {False, 1}  # True ve 1 aynı şey, False ve 0 aynı şey, 1.0 ve 1 aynı şey

# union(), intersection(), difference()

a = set("malatya")
b = set("kayısı")
print(a, b, sep = "\n")
# {'y', 'l', 't', 'm', 'a'}
# {'ı', 'y', 'k', 's', 'a'}

print(a - b) # a'nın b'den farklı olan elemanlarını getirir # {'m', 'l', 't'}
print(a.difference(b)) # a'nın b'den farklı olan elemanlarını getirir # {'m', 'l', 't'}

print(b - a) # b'nin a'dan farklı olan elemanlarını getirir # {'k', 's', 'ı'}
print(b.difference(a)) # b'nin a'dan farklı olan elemanlarını getirir # {'k', 's', 'ı'}

print(a.intersection(b)) # a ve b'de ortak elemanları getirir # {'y', 'a'}
print(b.intersection(a)) # a ve b'nin kesişim kümesini getirir # {'y', 'a'}
print(a & b) # a ve b'de ortak elemanları getirir # {'y', 'a'}

print(a.union(b)) # a ve b'nin tüm elemanlarını getirir # {'ı', 'y', 'l', 'k', 't', 'm', 's', 'a'}
print(b.union(a)) # a ve b'nin tüm elemanlarını getirir # {'ı', 'y', 'l', 'k', 't', 'm', 's', 'a'}
print(a | b) # a ve b'nin tüm elemanlarını getirir # {'ı', 'y', 'l', 'k', 't', 'm', 's', 'a'}

c = set("fındık")
d = set("fıstık")
print(c, d, sep = "\n")
# {'ı', 'f', 'k', 'n', 'd'}
# {'ı', 'f', 'k', 't', 's'}
print(c - d) # {'d', 'n'}
print(d - c) # {'s', 't'}
print(c - d | d - c) # {'d', 's', 't', 'n'}
print((c | d) - (c & d)) # {'d', 's', 't', 'n'}

print(a, b, c, d, sep = "\n")
"""
{'y', 'l', 't', 'm', 'a'}
{'ı', 'y', 'k', 's', 'a'}
{'ı', 'f', 'k', 'n', 'd'}
{'ı', 'f', 'k', 't', 's'}
"""

print(c.intersection(d) - d.union(c)) # set()
# boş kümeyi göstermek için set() yazılır, {} değil. {} boş bir sözlük (dictionary) anlamına gelir.
print((d.union(c)) - (c.intersection(d))) # {'d', 's', 't', 'n'}

print(a.difference(b).difference(c)) # {'m', 'l', 't'}
print(a.difference(b).difference(d)) # {'m', 'l'}

# clear()

a.clear()
print(a) # set()

# remove()

print(b) # {'ı', 'y', 'k', 's', 'a'}
b.remove("a")
print(b) # {'ı', 'y', 'k', 's'}

# b.remove("i") # KeyError: 'i' # remove() verilen eleman yoksa hata verir
# bu hatayı almamak için discard() kullanabiliriz
b.discard("i") # verilen eleman yoksa hata vermez
print(b) # {'ı', 'y', 's'} 

# pop()

set1 = set("selam")
print(set1) # {'e', 'l', 'm', 's', 'a'}
print(set1.pop()) # s  # 'e' # set'ten rastgele bir eleman siler ve o elemanı döner
print(set1) # {'l', 'e', 'm', 'a'}

help(set.pop)
"""
Help on method_descriptor:

pop(...) unbound builtins.set method
    Remove and return an arbitrary set element.
    Raises KeyError if the set is empty.
"""
help(list.pop)
"""
Help on method_descriptor:

pop(self, index=-1, /) unbound builtins.list method
    Remove and return item at index (default last).

    Raises IndexError if list is empty or index is out of range.
"""

# add()

print(set1) # {'e', 'm', 'l', 'a'}   
set1.add("s")
print(set1) # {'s', 'e', 'm', 'l', 'a'}

set1.add("b", "c") # TypeError: set.add() takes exactly one argument (2 given)

set1.add((1, 2, 3)) # set'e tuple ekleyebiliriz
print(set1) # {'s', 'e', (1, 2, 3), 'm', 'l', 'a'}

set1.add([4, 5, 6]) # TypeError: unhashable type: 'list' # set'e liste ekleyemeyiz # set verileri içerisinde liste tipini tutmazlar

set1.add({"a" : 1, "b": 2}) # TypeError: unhashable type: 'dict' # set'e dict ekleyemeyiz # set verileri içerisinde dict tipini tutmazlar

set1.add("hello")
print(set1) # {'s', 'hello', 'e', (1, 2, 3), 'm', 'l', 'a'}

a = set("hello")
b = set("world")
a.update(b) # a.union(b) ile aynı işlevi görmüş oldu
print(a) # {'w', 'e', 'o', 'h', 'd', 'l', 'r'}

# While Loop
# while döngüsü, bir koşul doğru olduğu sürece döngüyü çalıştırır
# while koşul : # koşul True ise alttaki kod bloğu çalışır. Koşul False olana kadar kod bloğu çalışır
    #... code ...
"""
x = 5 
while 10 > x :
    print("Bu döngü sonsuza kadar çalışacak...") # sonsuz döngü

"""

x = 5 
while 10 > x :
    print("Bu döngü ne zaman biter?")
    x = x + 1 # x += 1
print("Döngü bitti.")

x = 1
while x < 10 :
    print(x)
    x += 1
    print("x'e 1 ekledik")
print("Döngü bitti.")

liste = ["Malatya", "Konya", "İzmir", "İstanbul", "Ankara"]
x = 0
while x < len(liste) :
    print(liste[x])
    x += 1
print("\nDöngü bitti.")

y = -3
while -5 < y < -1 :
    print(y)
    print("Her zaman pozitif ol")
    y += 1

"""
while True :
        print("Sonsuz döngü!")
"""

while False :
    print("Bu satır çalışmayacak")

y = True
while y :
    print("while döngüsü koşul False olana kadar çalışır.")
    y = False

x = 0
while x < 11 :
    print(x, end = " * ")
    x += 2
    print(x, end = " # ")



# 1'den 200'e kadar asal sayıları yazdırabilir miyiz?

x = 1
asal_sayilar = []
while x < 201:
    if x > 1 :
        y = 2
        while y <= x :
            if x % y == 0:
                break
            y += 1
        if y == x :
            asal_sayilar.append(x)
    x += 1
print(asal_sayilar)

"""
x = 1 
asal_sayilar = []
while x < 201 :
    if x > 1 :
        y = 2
        while y <= x :
            if x % y == 0:
                break
            y += 1
        if y == x :
            asal_sayilar.append(x)
    x += 1
print(asal_sayilar)
"""


x = 1
asal_sayilar = []
while x < 201:
    if x > 1 :
        asal = True
        y = 2
        while y * y <= x  :
            if x % y == 0 :
                asal = False
                break
            y += 1
        if asal :
            asal_sayilar.append(x)
    x += 1
print(asal_sayilar)

"""
x = 1
asal_sayilar = []
while x < 201 :
    if x > 1 :
        asal = True
        y = 2
        while y * y <= x :
            if x % y == 0 :
                asal = False
                break
            y += 1
        if asal :
            asal_sayilar.append(x)
    x += 1
print(asal_sayilar)
"""

x = 1
asal_sayilar = []
while x < 201 :
    bolen = 1
    bolen_sayisi = 0
    while bolen <= x :
        if x % bolen == 0 :
            bolen_sayisi += 1
        bolen += 1
    if bolen_sayisi == 2 :
        asal_sayilar.append(x)
    x += 1
print(asal_sayilar)

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 5, 245, 22, 65, 21]
tek_sayilar = []
cift_sayilar = []  
index = 0
len_liste = len(sayilar)
while index < len_liste :
    if  sayilar[index] % 2 == 0 :
        cift_sayilar.append(sayilar[index])
    else:
        tek_sayilar.append(sayilar[index])
    index += 1
print(cift_sayilar, tek_sayilar, sep = "\n")

while [] :
    print("Bu satır çalışmayacak") # boş liste False olduğu için çalışmaz
print("Döngü bitti")

x = int(input("Bir sayı girin: "))
while x : # x 0 olduğunda döngü biter, 0 False olarak kabul edilir
    print(x * 3)
    x -= 1
print("Döngü bitti.")

sayi = 25
while True :
    tahmin = int(input("1 - 100 arasında bir sayı giriniz :"))
    if tahmin < sayi :
        print("Daha büyük bir sayı giriniz.")
    elif tahmin > sayi :
        print("Daha küçük bir sayı giriniz.")
    else :
        print("Tebrikler! Doğru tahmin ettiniz.")
        break # break döngüden çıkmamızı sağlar



# random modülü
# pip install "kütüphane adını yazarız"

"""
Python’daki random bir modüldür, yani bir kütüphanenin parçası olan dosyadır. Python’un standart modüllerinden biridir (yani ek kurulum gerekmez).
Python’un standart kütüphanesinde (standard library) yer alır ve rastgele sayı üretme işlemleri için kullanılır.
 Modül mü, Kütüphane mi?
Modül: .py uzantılı bir Python dosyasıdır. random.py gibi.
Kütüphane (Library): Birden fazla modülün bulunduğu büyük yapıdır (örneğin math, datetime, unittest gibi modüller Python Standard Library içindedir).
Bu bağlamda random, standart kütüphanenin bir modülüdür.
"""

"""
pip install Nedir?
pip install, Python paketlerini (kütüphaneleri) yüklemek için kullanılan bir komuttur. Terminal (komut satırı) veya IDE'nin terminal penceresinde kullanılır.
PIP = "Pip Installs Packages" (kendini referanslayan eğlenceli bir kısaltma)
Eski kaynaklarda: "Preferred Installer Program" olarak da geçer.
Ne işe yarar?
Python diliyle yazılmış, başka geliştiriciler tarafından yayınlanmış paketleri Python Package Index (PyPI)'den indirip yükler.
Nerede Kullanılır?
Aşağıdaki gibi terminalde (CMD, Bash, PowerShell ya da VSCode/IDEA terminali) çalıştırılır:
pip install requests
Bu örnek, requests adındaki HTTP kütüphanesini indirip yükler.

pip ile yüklenen paketler nereye gider?
Varsayılan olarak:
Sanal ortam (virtualenv) varsa: sanal ortama yüklenir.
Yoksa: sistem genelindeki Python kurulumuna yüklenir.
"""

# random modülünü install etmemize gerek yok, eğer gömülü bir modül ise/veya daha önce install edilmişse  doğrudan import edebiiliriz.

import random

print(random.random()) # 0.0 ile 1.0 arasında rastgele bir float sayısı döner
print(random.randint(1, 200)) # 1 ile 200 arasında rastgele bir int sayısı döner

sayi = random.randint(1, 200)
count = 0
while True :
    tahmin = int(input("1 - 200 arasında bir sayı giriniz :"))
    count += 1
    if tahmin < sayi :
        print("Daha büyük bir sayı giriniz.")
    elif tahmin > sayi :
        print("Daha küçük bir sayı giriniz.")
    else :
        print("Tebrikler! Doğru tahmin ettiniz.")
        print(f"Toplam {count} denemede doğru tahmin ettiniz")
        break
