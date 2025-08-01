
# Tekrar

# Kullanıcıdan bir sayı alınız.
# Sayının pozitif, negatif veya sıfır olup olmadığını ekrana yazdırınız.

sayi = int(input("Bir sayı giriniz:"))
if sayi > 0:
    print(f"Girdiğiniz sayi ({sayi}) pozitiftir.")
elif sayi < 0:
    print(f"Girdiğiniz sayı ({sayi}) negatiftir.")
else:
    print("Girdiğiniz sayı 0'dır.")

# Kullanıcıdan bir sayı alınız.
# Sayının tek veya çift olup olmadığını ekrana yazdırınız.

sayi = int(input("Bir sayı giriniz:"))

if sayi % 2 == 0:
    print(f"Girdiğiniz sayı ({sayi}) çifttir.")
else:
    print("Girdiğiniz sayı ({sayi}) tektir.")


# Kullanıcıdan bir karakter alınız.
# Karakterin büyük harf, küçük harf veya rakam olup olmadığını kontrol ediniz.

karakter = input("Lütfen bir karakter giriniz:")
if karakter.islower():
    print(f"Girdiğiniz karakter ({karakter}) küçük bir harftir. ")
elif karakter.isupper():
    print(f"Girdiğiniz karakter ({karakter}) büyük bir harftir.")
elif karakter.isnumeric():
    print(f"Girdiğiniz karakter ({karakter})  bir rakamdır.")
else:
    print(f"Girdiğiniz karakter ({karakter}) rakam ya da harf değil.")

# List Methods

# string veriler iterable ve immutable
# liste tipi veriler iterable ve mutable
# iterable:  index ile elemanlarına ulaşabiliyoruz

""" Python listelerinin özellikleri:

Sıralıdır – Elemanlar eklenme sırasını korur.

Değiştirilebilirdir – Liste içeriği sonradan değiştirilebilir.

Farklı veri tipleri içerebilir – Aynı listede sayılar, string’ler ve başka listeler olabilir.

Tekrar eden elemanlara izin verir – Aynı değer birden fazla kez bulunabilir.

İndekslenebilir – Her elemana sıfırdan başlayan indekslerle ulaşılabilir.

Dilimlenebilir – Belirli aralıktaki elemanlar seçilebilir (liste[1:3]).

Negatif indeksleri destekler – Sondan başlayarak erişim mümkündür (liste[-1]).

Dinamik boyutludur – Listeye eleman eklenebilir veya çıkarılabilir.

Birçok yerleşik metodu vardır – append(), remove(), pop() gibi metotlar listelerle çalışmayı kolaylaştırır.

Kapsayıcı (container) bir veri tipidir – Diğer veri yapıları (tuple, list, dict) içerebilir."""

 
liste = [1, 3, True, [1, 2, 3], "1.5", "max"]

print(liste[0]) # 1

print(liste[-1]) # max

print(liste[3]) # [1, 2, 3]

print(liste[3][2]) # 3

liste[1] = 5 # listeler mutable
print(liste) # [1, 5, True, [1, 2, 3], '1.5', 'max']

print(type(liste)) # <class 'list'>


# list()
a = list() # listeyi list() metodo ile de tanımlayabiliriz.
print(a) # []

liste_1 = list("techpro") # str'yi listeye çevirdi
print(liste_1) # ['t', 'e', 'c', 'h', 'p', 'r', 'o']

b = "Hello"
print(list(b)) # ['H', 'e', 'l', 'l', 'o']

# print(list(256)) # HATA TypeError: 'int' object is not iterable, list() metodu içine iterable veri verilmeli, string ya da liste gibi 
# print(list("Hello","word")) # HATA TypeError: list expected at most 1 argument, got 2, list() metoduna 1 parametre verilmeli

# len()
print(len(liste)) # 6 liste içindeki listeyi tek bir elemean olarak sayıyor

print(liste_1) # ['t', 'e', 'c', 'h', 'p', 'r', 'o']
print(len(liste_1)) # 7

print(len("techpro")) # 7

# noktaya ulaşmak istiyoruz
print(liste[4][1]) # '1.5' tırnak içinde yazılmış demek ki türü string. O halde index kullanabiliriz.
print(list(liste[4])[1]) # ikinci yol

# 4. elemanı floata dönüştürelim
x = float(liste[4])
print(type(x)) # <class 'float'>

liste_2 = [1, 2, 1, 4, 3, 3, 5, 12, 35, 2, 7, 61]
print(liste_2[2:11:3]) # [1, 3, 35] start:stop:step start dahil, stop dahil değil

print(liste_2[::5]) # [1, 3, 7]

print(liste_2[5:8]) # [3, 5, 12]

a = [1, 3, 5]
b = [2, 4, 6]
print(a + b) # [1, 3, 5, 2, 4, 6]

int(a[0]) + int(b[0]) # 3

a[1] + b[1] # 7


# append()

sayılar = [1, 2, 3, 4, 5, 6]
sayılar.append(7) # liste sonuna eleman ekler
print(sayılar) # [1, 2, 3, 4, 5, 6, 7]

# sayılar.append(8, 9) # TypeError: list.append() takes exactly one argument (2 given) sadece bir argüman alır
#  bir eleman ekler, listenin sonuna ekler
print(sayılar)

sayılar.append([8,9]) # Bir eleman olarak algılar
print(sayılar) # [1, 2, 3, 4, 5, 6, 7, [8, 9]]
print(len(sayılar)) # 8


# extend()

sayılar.extend([8, 9])
print(sayılar) # [1, 2, 3, 4, 5, 6, 7, [8, 9], 8, 9] extend metodu iterable olan her
# türlü veriyi alıp her elemanını ayrı ayrı listeye ekler
# extend liste olarak değil, tek tek ekler, birden fazla eleman olarak ekler

sayılar.extend("techpro")
print(sayılar) # [1, 2, 3, 4, 5, 6, 7, [8, 9], 8, 9, 't', 'e', 'c', 'h', 'p', 'r', 'o']

# insert()

sayılar.insert(2, 0)  # verilen indexe bir eleman ekler, indexteki elemanı sağa kaydırır
print(sayılar) # [1, 2, 0, 3, 4, 5, 6, 7, [8, 9], 8, 9, 't', 'e', 'c', 'h', 'p', 'r', 'o']

sayılar.insert(0, "Logaritma")
print(sayılar) # ['Logaritma', 1, 2, 0, 3, 4, 5, 6, 7, [8, 9], 8, 9, 't', 'e', 'c', 'h', 'p', 'r', 'o']

liste.insert(3, False)
print(liste) # [1, 3, True, False, [1, 2, 3], '1.5', 'max']

# count()

print(liste_2.count(1)) # 2 içerisine verilen elemanın listede kaç defa geçtiğini sayar

print(liste_2.count(2)) # 2

print(liste_1.count("t")) # 1


# sort()

"""Listeyi kalıcı olarak sıralar (in-place).
Yeni bir liste döndürmez, mevcut listeyi değiştirir.
Geriye None döner."""

liste_3 = [34, 55, 21, 3, 5, 1, 0, 2]
liste_3.sort()
print(liste_3)

liste_3.sort(reverse=True)
print(liste_3) # [55, 34, 21, 5, 3, 2, 1, 0]

liste_1.sort()
print(liste_1) # ['c', 'e', 'h', 'o', 'p', 'r', 't']

x = list("Merve")
x.sort()
print(x) # ['M', 'e', 'e', 'r', 'v'] stringleri ASCII tablosuna göre sıralar

# join

"""Listeyi değiştirmez
Listeyi birleştirip bir string döndürür.
Orijinal liste aynen kalır."""

print(liste_1) # ['c', 'e', 'h', 'o', 'p', 'r', 't']
print(",".join(liste_1)) # 'c,e,h,o,p,r,t'
print(liste_1) # ['c', 'e', 'h', 'o', 'p', 'r', 't']

a = ['s', 'e', 'l', 'a', 'm']

print(" ".join(a)) # s e l a m
print(a) # ['s', 'e', 'l', 'a', 'm']

print("*".join(a)) # s*e*l*a*m

print("".join(a)) # selam

print("".join(["py", "thon"])) # python


# index()

print(sayılar) # ['Logaritma', 1, 2, 0, 3, 4, 5, 6, 7, [8, 9], 8, 9, 't', 'e', 'c', 'h', 'p', 'r', 'o']

print(sayılar.index("t")) # 12 verilen elemanın indexini yazdırır

print(liste_2) # [1, 2, 1, 4, 3, 3, 5, 12, 35, 2, 7, 61]

print(liste_2.index(2)) # 1 ilk gördüğü 2'nin indexini getirdi. python soldan sağa okur

# remove()

renk = ["kırmızı", "beyaz", "magenta", "cyan"]
renk.remove("kırmızı") # verilen elemanı listede ilk gördüğü yerde siler
print(renk) # ['beyaz', 'magenta', 'cyan']

renk.append("beyaz")
print(renk) # ['beyaz', 'magenta', 'cyan', 'beyaz']
renk.remove("beyaz") # ilk gördüğü beyazı siler
print(renk) # ['magenta', 'cyan', 'beyaz']

# pop()

print(renk.pop()) # beyaz sondaki elemanı sildi ve çıktı olarak verdi
# default olarak son indexi siler

print(liste_1) # ['c', 'e', 'h', 'o', 'p', 'r', 't']
print(liste_1.pop(0)) # c içerisine index verebiliyoruz, verdiğimiz indexteki elemanı siler, sildiği elemanı döndürür
# remove() içine silmek istediğimiz elemanı veriyorduk, remove o elemanı siler, ama elemanı döndürmez

# clear()

print(liste_1) # ['e', 'h', 'o', 'p', 'r', 't']

liste_1.clear() # Listedeki tüm elemanları siler
print(liste_1) # []

# del() 

del liste_1 # liste değişkenini tamamen siler, kullanımı farklı
# print(liste_1) # NameError: name 'liste_1' is not defined. Did you mean: 'liste_2'?

del liste_2
# print(liste_2) # NameError: name 'liste_2' is not defined. Did you mean: 'liste_3'?

# copy()

print(liste) # [1, 3, True, False, [1, 2, 3], '1.5', 'max']

yeni_liste = liste.copy()
print(yeni_liste) # [1, 3, True, False, [1, 2, 3], '1.5', 'max']

# extend()
yeni_liste.extend("selam")
print(yeni_liste) # [1, 3, True, False, [1, 2, 3], '1.5', 'max', 's', 'e', 'l', 'a', 'm']
print("-"*20)
print(liste) # [1, 3, True, False, [1, 2, 3], '1.5', 'max']


# max(), min(), sum()

liste_4 = [1, 2, 3, 4, 5]
print(max(liste_4)) # 5
print(min(liste_4)) # 1
print(sum(liste_4)) # 15 elemanlar int olmalıdır

"""Python'da:
max()
min()
sum()
hepsi yerleşik fonksiyonlardır (built-in functions).
Python bu fonksiyonları, __builtins__ isimli özel bir modül içinde otomatik olarak yükler.
Yani Python çalışır çalışmaz, bu fonksiyonlar kullanılabilir hâle gelir.
Java ile kıyaslarsak:
Java'da Math.max(a, b) gibi sınıf adıyla çağırırsın çünkü statictir.
Python'da max(a, b) der geçersin çünkü built-in'dir; otomatik olarak tanımlanmıştır, sınıf adı gerekmez.
"""

# range() bu bir liste metodu değil, gömülü bir fonksiyondur.

liste_5 = range(1 ,11)
print(liste_5) # range(1, 11) aralık verir
liste_5 = list(liste_5)
print(liste_5) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] start dahil, stop dahil değil

a = list(range(-3, 12))
print(a) # [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

b = list(range(0, 100, 20)) # start, stop, step adım sayısını verebiliriz
print(b) # [0, 20, 40, 60, 80]

c = list(range(10 , 0, -1))
print(c) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Practice

# 1'den 100'e kadar olan sayılardan çift olanları bir listeye, tek olanları başka bir listeye atayın.

cift_sayılar = list(range(0, 101, 2))
cift_sayılar.pop(0)
print(cift_sayılar)

tek_sayılar = list(range(1, 100, 2))
print(tek_sayılar)

# Kullanıcıdan bir cümle alarak, bu cümledeki kelime sayısını bulunuz.

print(len(input("Lütfen bir cümle giriniz:").split()))

# veya
cumle = input("Lütfen bir cümle giriniz:")
kelimeler = cumle.split()
kelime_sayısı = len(kelimeler)
print(f"Girilen cümlede {kelime_sayısı} tane kelime var.")

# Listedeki elemanların ortalamasını bulunuz

lis = [3, 5, 8, 9]

ort = sum(lis)/len(lis)
print(ort) # 6.25

# Kullanıcıdan bir yıl alınız ve yılın artık yıl olup olmadığını kontrol mediniz.
# (Artık yıllar 4'e tam bölünen, ancak 100' tam bölünemeyen veya 400'e tam bölünen yıllardır.)

yıl = int(input("Lütfen bir yıl giriniz: "))

if yıl % 400 == 0:
    print(f"Girdiğiniz yıl ({yıl}) artık yıldır.")
elif yıl % 100 == 0:
    print(f"Girdiğiniz yıl ({yıl}) artık yıl değildir.")
elif yıl % 4 == 0:
  print(f"Girdiğiniz yıl ({yıl}) artık yıldır.")
else:
    print(f"Girdiğiniz yıl ({yıl}) artık yıl değildir.")


# veya
yıl = int(input("Bir yıl giriniz: "))

if (yıl % 4 == 0 and yıl % 100 != 0) or (yıl % 400 == 0):
    print(f"Girdiğiniz yıl ({yıl}) artık yıldır.")
else:
    print(f"Girdiğiniz yıl ({yıl}) artık yıl değildir.")








