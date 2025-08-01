
# Python Recap

"""
Python'daki farklı veri tipleri şunlardır:
1. Sayısal Veri Tipleri
int: Tam sayılar (örneğin, 5, -3)
float: Ondalık sayılar (örneğin, 3.14, -0.001) 
complex: Karmaşık sayılar (örneğin, 2 + 3j)

2. Diziler
str: Karakter dizileri (örneğin, "Merhaba")
list: Sıralı ve değiştirilebilir diziler (örneğin, [1, 2, 3])
tuple: Sıralı ancak değiştirilemeyen diziler (örneğin, (1, 2, 3))

3. Sözlükler
dict: Anahtar-değer çiftlerinden oluşan koleksiyonlar (örneğin, {"anahtar": "değer"})

4. Küme
set: Benzersiz öğelerden oluşan koleksiyonlar (örneğin, {1, 2, 3}) 
frozenset: Değiştirilemeyen set (örneğin, frozenset([1, 2, 3]))

5. Boolean
bool: Doğru veya yanlış değerleri (örneğin, True, False)

6. None
NoneType: Hiçbir değeri temsil eden özel bir veri tipi (örneğin, None)
"""

"""
Liste ile tuple arasındaki farkı açıklayınız.
Python'da liste (list) ile demet (tuple) arasındaki temel farklar şunlardır:

Özellik	                       Liste (list)	                         Demet (tuple)
Değiştirilebilirlik	  Değiştirilebilir (mutable)	            Değiştirilemez (immutable)
Söz dizimi	          [] köşeli parantez kullanılır	            () normal parantez kullanılır
Performans	          Daha yavaştır	                            Daha hızlıdır (değiştirilemez olduğu için)
Kullanım amacı	      Değişebilir veri kümeleri için uygundur	Sabit veri kümeleri için uygundur
Yöntem sayısı	      Daha fazla yerleşik metod içerir	        Daha az yerleşik metoda sahiptir
İç içe elemanlar	  İç içe listeler olabilir	                İç içe tuple'lar olabilir

Eğer veri zaman içinde değişecekse, list kullan.
Eğer veri sabit kalacaksa, tuple kullan (örneğin sabit koordinatlar, sabit ay adları gibi).
"""

my_list = [1, 2, 3]
print(my_list[0]) # 1  liste elemanlarına indeks ile erişebiliriz, iterable'dır
my_list[0] = 4
print(my_list) # [4, 2, 3]  listeyi değiştirebildik, listeler mutable(değiştirilebilir)

my_tuple = (1, 2, 3)
print(my_tuple[0]) # 1  tuple elemanlarına indeks ile erişebiliriz, iterable'dır
# my_tuple[0] = 4 # TypeError: 'tuple' object does not support item assignment
print(my_tuple) # (1, 2, 3)  tuple'ı değiştiremedik, tuple immutable(değiştirilemez)

# 3. swapcase() fpnksiyonu ne işe yarar?
# swapcase() fonksiyonu, bir string içindeki tüm harflerin büyük harflerini küçük harfe, küçük harflerini ise büyük harfe dönüştürür.

my_string = "Techpro Education"
print(my_string.swapcase())  # tECHPRO eDUCATION
print(my_string) # Techpro Education

# 4.Bir listedeki tekrarlı elemanları nasıl silersiniz?

demo_list = [3, 3, 4, 4, 2, 1, 6, 6, 9, 9, 9]
new_list = list(set(demo_list))  # set() ile tekrarlı elemanlar silinir, tekrar list'e dönüştürülür
print(new_list) # [1, 2, 3, 4, 6, 9] tekrarlı elemanlar silindi
print(demo_list) # [3, 3, 4, 4, 2, 1, 6, 6, 9, 9, 9] 

# 5. İki tuple nasıl birleştirilir?

tup1 = (1, 2, "a")
tup2 = (3, 4, "b")
tup3 = tup1 + tup2 # + operatörü ile iki tuple birleştirilebilir (concat)
print(tup1)  # (1, 2, 'a') 
print(tup2) # (3, 4, 'b')
print(tup3) # (1, 2, 'a', 3, 4, 'b')  yeni tuple oluşturuldu

# 6. Bir string ifadeyi nasıl küçük harfe çevirirsiniz?

my_string2 = "TECHPRO EDUCATION"
print(my_string2.lower())  # techpro education
print(my_string2) # TECHPRO EDUCATION 
print(my_string2.lower().upper()) # TECHPRO EDUCATION

# 7. Pythonda bir listenin belirli bir indexine nasıl elaman yerleştirirsiniz?

my_list2 = [1, 2, 3, "beyaz", "kalem"]
my_list2.insert(3, "siyah")
print(my_list2)  # [1, 2, 3, 'siyah', 'beyaz', 'kalem']  index 3'e "siyah" eklendi

# 8. Negatif index nedir ne için kullanılır?
# Negatif index, bir dizinin sonundan başlayarak elemanlara erişmek için kullanılır.

print(my_list2)  # [1, 2, 3, 'siyah', 'beyaz', 'kalem']
print(my_list2[-2]) # beyaz 

# 9. Bir sayıyı nasıl string'e çevirirsiniz?

sayi = 123
str_sayi = str(sayi)
print(str_sayi)  # "123" 
print(sayi)  # 123 
print(type(sayi))  # <class 'int'>
print(type(str_sayi))  # <class 'str'> 

print(type(f"{sayi}")) # <class 'str'>  # f-string ile de string'e çevrilebilir

# 10. İki ayrı print() yazdırırken çıktıların aynı satırda olmasını nasıl sağlarsınız?

print("Merhaba", end = " ") 
print("Dünya") # Merhaba Dünya

# Aynı print içinde iki farklı ifadenin alt alta yazılmasını istersek, sep parameteresini kullanabiliriz.
print("Merhaba", "Dünya", sep  = "\n")
# Merhaba
# Dünya
print("Merhaba\nDünya")
# Merhaba
# Dünya

# 11. Bir ifadedeki boşlukları nasıl silersiniz?

ifade = "   Merhaba    "
ifade2 = ifade.strip()  # strip() ile baştaki ve sondaki boşluklar silinir
print(ifade2) # Merhaba

metin = "Hello      World!"
metin2 = metin.replace(" ","")  # replace() ile tüm boşluklar silinir
print(metin2)  # HelloWorld!

print(metin.split())  # ['Hello', 'World!']  split() ile boşluklara göre ayırır, liste döner
metin3 = "".join(metin.split())
print(metin3)


# 12. Verilen iki sayı listesini sayılar küçükten büyüğe olacak şekilde birleştirin.

liste_1 = [1, 6, 4, 56, 90, 78, 21]
liste_2 = [2, 32, 43, 56, 9, 6]

liste_3 = sorted(liste_1 + liste_2)
print(liste_3) # [1, 2, 4, 6, 6, 9, 21, 32, 43, 56, 56, 78, 90]



# 13. Pythonda append() ve extend() arasındaki farkı açıklayınız.
# append() metodu, bir listeye tek eleman ekler.
# extend() metodu ise, bir listeye birden fazla eleman ekler.

print(liste_2) # [2, 32, 43, 56, 9, 6]

liste_2.append(57)
print(liste_2) # [2, 32, 43, 56, 9, 6, 57] 

liste_2.extend([1 ,2 ,3])
print(liste_2) # [2, 32, 43, 56, 9, 6, 57, 1, 2, 3]

liste_2.append([4, 5, 6])
print(liste_2) # [2, 32, 43, 56, 9, 6, 57, 1, 2, 3, [4, 5, 6]] append() ile listeyi tek bir eleman olarak ekledik

# 14. Verilen bir sayının palindrom olup olmadığını veren paython kodunu yazınız.

def is_palindrome(num) :
    return num == int(str(num)[::-1])

print(is_palindrome(121))  # True
print(is_palindrome(123)) # False

num = int(input("Bir sayı giriniz: "))
if is_palindrome(num) :
    print(f"Girdiğiniz {num} sayısı polindrom bir sayıdır.")
else :
    print(f"Girdiğiniz {num} sayısı  polindrom bir sayı değildir.")