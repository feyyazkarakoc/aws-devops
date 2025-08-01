
# For Loop
# in operatörü True veya False döndürür

print(2 in [1, 2, 3]) # True

print(6 in [1, 2, 3]) # False

# For döngüsü

# liste
for i in  [1, 2, 3, 4] : # i sağındaki iterable yapının her bir elemanını dolaşır, buradaki collection type iterable olmalı
    print(i ** 2) 
"""
1
4
9
16
"""

"""
 Python'da for döngüsü, bir collection (koleksiyon) (liste, demet, dize, set, sözlük vb.) elemanları üzerinde sırayla gezinmek için kullanılır
 for değişken in koleksiyon:
     Yapılacak işlemler

for harf in "merhaba":
    print(harf)

meyveler = ["elma", "armut", "kiraz"]
for meyve in meyveler:
    print(meyve)

range() ile Sayılar Üzerinde
for i in range(5):  # 0'dan 4'e kadar
    print(i)

for ile Sözlük Üzerinde
ogrenci = {"ad": "Ali", "yas": 20}

for key in ogrenci:
    print(key)  # Sadece anahtarları verir

for key, value in ogrenci.items():
    print(key, value)
"""

# string
for harf in "trigonometri" :
    print(harf) # end parametresi hiç bişey verilmezse ("\n") 
"""
t
r
i
g
o
n
o
m
e
t
r
i
"""

for harf in "trigonometri" :
    print(harf, end = " * ") # t * r * i * g * o * n * o * m * e * t * r * i *

# tuple
for i in (1, 2, 2, 3) :
    i += 5
    print(i)

"""
6
7
7
8
"""


# set
for i in {1, 2, 3, 4} :
    print(i * 2)  
"""
2
4
6
8
"""

# int
for i in 1234 : # collection type iterable olmalı
    print(i) # TypeError: 'int' object is not iterable

# range
for i in range(1, 19, 3) :
    print(i)
"""
1
4
7
10
13
16
"""

# for döngüsü ile while döngüsü arasındaki fark

for i in [1, 2, 3, 4, 5] :
    print(i ** 2)
"""
1
4
9
16
25
"""

liste = [1, 2, 3, 4, 5]
index = 0
while index < len(liste) :
    print(liste[index] ** 2)
    index += 1
"""
1
4
9
16
25
"""

for i in ["merve", "bilsen", "yıldırım", "uluğbek", "ibrahim"] :
    print(i.title(), end = " - ")
# Merve - Bilsen - Yıldırım - Uluğbek - Ibrahim -

# dictionary
dict_1 = {"name" : "Mukaddes", "age" : 23, "job" : "aws_devops" }
print(dict_1) # {'name': 'Mukaddes', 'age': 23, 'job': 'aws_devops'}
for i in dict_1 :
    print(i) # keyler yazılır
"""
name
age
job
"""

for i in dict_1.values() :
    print(i) # value'lar yazılır
"""
Mukaddes
23
aws_devops
"""

for i in dict_1.items() :
    print(i) # key, value çiftleri yazılır
"""
('name', 'Mukaddes')
('age', 23)
('job', 'aws_devops')
"""

# for döngüsü sonsuz döngüye girebilir
liste = ["for ile sonsuza gitme"]
for i in liste :
    print(i)
    liste.append(i)

i = 0
for i in range(5) :
    print(i)
    i = 0
    print(i)
"""
0
0
1
0
2
0
3
0
4
0

Sayaç değiştirilebilir mi? Değiştirsen bile, Python arka planda range listesinden sıradaki sayıyı yine atar.
i = 1 etkili mi? Hayır, bir sonraki turda i tekrar range’den gelir.burada for döngüsü range(5) ifadesi üzerinden
iterasyona dayanır. Bu, i = 0 satırıyla i değişkenini değiştirmiş olsan bile, Python'un döngü kontrol mekanizması, 
range(5)'ten gelen sıradaki değeri her seferinde otomatik olarak i'ye atamaya devam eder. range(5) şu sayıları üretir: 0, 1, 2, 3, 4
Python for döngüsü, bu dizinin her elemanını sırayla alır ve i'ye atar.
Sen i = 1 yazsan bile, bir sonraki iterasyonda Python tekrar sıradaki değeri i'ye atar. Yani senin yaptığın i = 1, döngünün akışını etkilemez.
"""

# kullanıcıdan alınan sayı için çarpım tablosu oluşturan python kodunu yazınız

# while ile
sayi = int(input("1 ile 10 arasında bir sayı giriniz : "))
if 1 <= sayi <= 10 :
    x = 1
    while  x <= 10 :
        print(f"{sayi}   *   {x}   = ", sayi*x)
        x += 1
else :
    print("Sayı 1 ile 10 arasında olmalıdır!!!")


# for loop ile 
sayi = int(input("1 ile 10 arasında bir sayı giriniz : "))
if 1 <= sayi <=10 :
    for i in range(1, 11) :
        print(f"{sayi} * {i} = {sayi*i}")
else :
    print("Sayı 1 ile 10 arasında olmalıdır!!!")

# 1'den 50'ye kadar olan sayıların toplamını veren py kodunu yazınız
# 1. yol
toplam = 0
for i in range(1, 51) :
    toplam += i 
print(toplam)

# 2. yol
print(sum(range(1, 51)))



# continue

# 1'den 10' akadar olan sayılardan 3'e bölünebilenlerin toplamını veren kodu yazınız.
toplam = 0
for i in range(1, 11) :
    if i % 3 == 0 :
        toplam += i
print(toplam)



toplam = 0
for i in range(1, 11) :
    if i % 3 != 0 :
        continue
    else:
        toplam += i
print(toplam)

toplam = 0
for i in range(1, 11) :
    if i % 3 != 0 :
        continue
    toplam += i
print(toplam)


# break

# 28. sayıya kadar tek ve çif sayıları ayrı ayrı listele
liste_2 = [1, 15, 2, 8, 9, 32, 65, 41, 14, 18, 22, 28, 71, 85, 98, 91]
cift = []
tek = []
for i in liste_2 :
    if i == 28:
        break
    elif i % 2 == 0 :
        cift.append(i)
    else:
        tek.append(i)
print(cift, tek) # [2, 8, 32, 14, 18, 22] [1, 15, 9, 65, 41]


# list comprehension
# for döngüsünü tek satırda yazabiliriz
# [ifade for öğe in koleksiyon if koşul]

# klsaik yöntem
for i in [1, 2, 3] :
    if i % 2 == 0:
        print(i ** 2)
    else :
        print(i)

# list comprehension
[i ** 2 for i in [1, 2, 3] if i % 2 == 0]

[i if i % 2 == 1 else i ** 2 for i in [1, 2, 3]] # else ile beraber kullanılırsa if başa alınır

liste = [1, 2, 3, 4, 5]
yeni_liste = []
for i in liste :
    yeni_liste.append(i ** 2)
print(yeni_liste)
# list comprehension
[i ** 2 for i in [1, 2, 3, 4, 5]]

liste = [1, 2, 3, 4, 5]
yeni_liste = []
for i in liste :
    if i % 2 == 0 :
        yeni_liste.append(i ** 2)
print(yeni_liste)
# list comprehension
[i ** 2 for  i in liste if i % 2 == 0 ]

liste = [1, 2, 3, 4, 5]
yeni_liste = []
for i in liste :
    if i % 2 == 0 :
        yeni_liste.append(i)
    else :
        yeni_liste.append(i ** 2)
print(yeni_liste)
# list comprehension
[i if i % 2 == 0 else i ** 2 for i in liste]


# listedeki min ve max sayılar arasındaki kayıp sayıları bulunuz
# klasik yöntem
num = [48, 10, 11, 21, 36, 5, 6, 52, 28, 29,
       53, 54, 45, 19, 20, 47, 55, 39, 41, 7,
       9, 17, 26, 27, 42, 22, 37, 51, 46, 18,
       44, 30, 34, 13, 15, 35, 33, 16, 50, 24]
kayıp_sayilar = []
for i in range(min(num), max(num)+1) :
    if  i not in num :
        kayıp_sayilar.append(i)
print(kayıp_sayilar)
# list comprehension
num = [48, 10, 11, 21, 36, 5, 6, 52, 28, 29,
       53, 54, 45, 19, 20, 47, 55, 39, 41, 7,
       9, 17, 26, 27, 42, 22, 37, 51, 46, 18,
       44, 30, 34, 13, 15, 35, 33, 16, 50, 24]
[i for i in range(min(num), max(num) + 1) if i not in num ]
# continue ile
num = [48, 10, 11, 21, 36, 5, 6, 52, 28, 29,
       53, 54, 45, 19, 20, 47, 55, 39, 41, 7,
       9, 17, 26, 27, 42, 22, 37, 51, 46, 18,
       44, 30, 34, 13, 15, 35, 33, 16, 50, 24]
kayıp_sayilar = []
for i in range(min(num), max(num) + 1) :
    if i in num :
        continue
    kayıp_sayilar.append(i)
print(kayıp_sayilar)


# Kullanıcıdan aldığınız 3 sayının en büyüğünü yazdırınız
sayi_1 = int(input("Birinci sayıyı giriniz : "))
sayi_2 = int(input("İkinci sayıyı giriniz : "))
sayi_3 = int(input("Üçüncü sayıyı giriniz : "))
sayilar = [sayi_1, sayi_2, sayi_3]
print(f"En büyük sayı : {max(sayilar)}")

sayi_1 = int(input("Birinci sayıyı giriniz : "))
sayi_2 = int(input("İkinci sayıyı giriniz : "))
sayi_3 = int(input("Üçüncü sayıyı giriniz : "))
sayilar = [sayi_1, sayi_2, sayi_3]
max = sayilar[0]
for i in sayilar :
    if  i > max :
        max = i
print(i)

sayilar = []
for i in range(3) :
    sayi = int(input("Sayı giriniz : "))
    sayilar.append(sayi)
print(max(sayilar))










