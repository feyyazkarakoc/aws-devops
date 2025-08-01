
# 1 - Kullanıcıdan input ile iki veri alın. Alınan değerler aynı uzunlukta ise True döndüren algoritmayı yazınız.

veri1 = input("Birinci veriyi giriniz: ")
veri2 = input("İkinci veriyi giriniz: ")
sonuc = len(veri1) == len(veri2)
print(sonuc)

veri1 = input("Birinci veriyi giriniz: ")
veri2 = input("İkinci veriyi giriniz: ")
print(len(veri1) == len(veri2))

print(len(input("Birinci veriyi giriniz: ")) == len(input("İkinci veriyi giriniz: ")))

veri1 = input("Birinci veriyi giriniz: ")
veri2 = input("İkinci veriyi giriniz: ")
sonuc = True if len(veri1) == len(veri2) else False
print(sonuc)

veri1 = input("Birinci veriyi giriniz: ")
veri2 = input("İkinci veriyi giriniz: ")
if len(veri1) == len(veri2) :
    print(True)
else :
    print(False)

# 2 - Kullanıcıdan bir sayı isteyin. Sayı tek ise iki katını çift ise karesini yazdırın.
sayi = int(input("Bir sayı giriniz: "))
if sayi % 2 == 0 :
    print(f"Girdiğiniz sayı : {sayi}, Sonuç : {sayi ** 2}")
else :
    print(f"Girdiğiniz sayı : {sayi}, Sonuç : {sayi * 2}")

# 3 - Kullanıcıdan iki tam sayı isteyin. Sayılar eşitse veya sayıların farkı 5'in katı ise True döndüren algoritmayı yazınız.
sayi1 = int(input("Birinci tam sayıyı giriniz: "))
sayi2 = int(input("İkinci tam sayıyı giriniz: "))

if sayi1 == sayi2 or (sayi1 - sayi2) % 5 == 0 :
    print(f"Girdiğiniz sayılar : {sayi1, sayi2} Sonuç : ", True)
else :
    print(f"Girdiğiniz sayılar : {sayi1, sayi2} sonuç : ", False)


print(True if (sayi1 == sayi2) or ((sayi1 - sayi2) % 5 == 0) else False)

# abs() içine verilen ifadenin mutlak değerini döndürür

print(True if sayi1 == sayi2 or abs(sayi1 - sayi2) % 5 == 0 else False)


# 4 - Vücut kitle indexini hesaplayan fonksiyonu yazınız. Hesapladığınız değerin hangi kategoride olduğunu belirtiniz. 
"""
(vki = kilo / (boy ** 2))
VKI Aralıkları:
18.5'in altı: Zayıf
- 18.5 24.9: Normal kilolu
- 25 - 29.9: Fazla kilolu
- 30 - 39.9: Obez
- 40 ve üzeri: Aşırı obez """

def vki_hesapla(kilo, boy) :
    vki = kilo / (boy ** 2)
    if vki < 18.5 :
        aralik =  "Zayıf"
    elif 18.5 <= vki <= 24.9 :
        aralik = "Normal kilolu"
    elif 25 <= vki <= 29.9 :
        aralik =  "Fazla kilolu"
    elif 30 <= vki <= 39.9 :
        aralik =  "Obez"
    elif vki >= 40 :
        aralik =  "Aşırı obez"
    
    return vki, aralik
    
kilo = float(input("Kilonuzu giriniz (kg): "))
boy =  float(input("Boyunuzu giriniz (m): "))

vki, aralık = vki_hesapla(kilo, boy)
print(f"Vücut kitle indeksiniz: {vki: .2f} - Kategori : {aralık}")

"""
Python'da aralik değişkeni yalnızca if, elif blokları içinde tanımlanıyor gibi görünüyor. Ama yine de return vki,
aralik satırında bu değişkene ulaşılıyor. Peki bu nasıl oluyor?
Python'da if-elif-else Bloklarının Scope'u (Kapsamı):
Python'da:
if, elif, else, for, while gibi blokların kendilerine özel bir scope'u yoktur.
Yani, bu bloklarda tanımlanan değişkenler, bulundukları fonksiyonun içinde geçerli olur.
Burada aralik değişkeni tüm if-elif bloklarında tanımlanıyor ama fonksiyonun genel kapsamına ait. 
Yani fonksiyon çalıştırıldığında ve bir koşul sağlandığında aralik atanıyor ve sonrasında return ile birlikte döndürülebiliyor.
Potansiyel Risk:
Eğer hiçbir if veya elif bloğu çalışmazsa, aralik hiç tanımlanmamış olur ve return kısmında:
UnboundLocalError: local variable 'aralik' referenced before assignment
hatası alırsın.

Ama senin koşulların tüm olası vki değerlerini kapsadığı için bu sorun çıkmaz. Yine de güvenli olması için else eklemek iyi bir pratiktir:
    else:
        aralik = "Bilinmeyen"

Kısaca Özet:
Python'da if, elif, else gibi bloklar yeni bir scope oluşturmaz.
Bloklarda tanımlanan değişkenler, fonksiyon kapsamı içinde tanımlanmış sayılır.
Ama hiçbir blok çalışmazsa ve değişken tanımlanmazsa, UnboundLocalError hatası alırsın.
Güvenli kod için mutlaka bir else veya başlangıçta aralik = None gibi varsayılan değer belirlemek iyi bir uygulamadır.
"""


# 5 - Kullanıcıdan bir cümle isteyin. Cümledeki büyük harf ve küçük harf sayısını hesaplayan bir program yazın.

def buyuk_kucuk_harf_say(cumle) :
    buyuk_harf, kucuk_harf = 0, 0
    for  harf in cumle :
        if harf.isupper() :
            buyuk_harf += 1
        elif harf.islower() :
            kucuk_harf += 1
    return buyuk_harf, kucuk_harf

cumle = input("Bir cümle giriniz: ")
print(buyuk_kucuk_harf_say(cumle))

cumle = input("Bir cümle giriniz: ")
kucuk_harf, buyuk_harf = 0, 0
for i in cumle :
    kucuk_harf += i.islower() # bu ifade True ise 1, False ise 0 döndürür
    buyuk_harf += i.isupper() # bu ifade True ise 1, False ise 0 döndürür
print(cumle)
print(f"Küçük har sayısı : {kucuk_harf}\nbüyük harf sayısı : {buyuk_harf}")
# f stringten önce format kullanılıyordu, şu an yaygın değil
print("Küçük harf sayısı : {0}\nBüyük harf sayısı : {1}".format(kucuk_harf, buyuk_harf))

# 5 - Kullanıcının girdiği kelimeyi tersten yazdıran bir fonksiyon yazınız

kelime = input("Bir kelime giriniz: ")
def my_reverse (kelime) :
    """Kullanıcının girdiği kelimeyi tersten yazdıran fonksiyon."""
    return kelime[::-1]

print(f"Girdiğiniz \"{kelime}\" kelimesinin tersi : {my_reverse(kelime)}")

# veya
kelime = input("Bir kelime giriniz: ")
print(f"Girdiğiniz \"{kelime}\" kelimesinin tersi : {''.join(reversed(kelime))}") # reversed() fonksiyonu, iterable döndürür bu yüzden join ile birleştirdik.
# join önünde "" kullanabiliriz, burada kullandığımızda pythonun kafası karışıyor, tek tırnak kullandık


# 5 - Girilen sayının faktöriyelini döndüren bir fonksiyon yazınız

def faktoriyel(sayi) :
    carpim = 1
    for i in range(1, sayi + 1) :
        carpim *= i
    return carpim

sayi = int(input("Bir sayı giriniz: "))
print(f"{sayi} sayısının faktöriyeli : {faktoriyel(sayi)}")

def faktöriyel(sayi) :
    carpim = 1
    while sayi > 1:
        carpim *= sayi
        sayi -= 1
    return carpim

sayi = int(input("Bir sayı giriniz: "))
print(f"{sayi} sayısının faktöriyeli : {faktöriyel(sayi)}")


def faktoriyel(n) :
    if n == 0 or n==1 :
        return 1
    elif n < 0 :
        return "Tanımsız"
    else :
        carpim = 1
        for i in range(1, n + 1) :
            carpim *= i
        return carpim
    
sayi = int(input("Bir sayı giriniz: "))
print(f"{sayi} sayısının faktöriyeli : {faktoriyel(sayi)}")


def faktoriyel_recursive(sayi) :
    if sayi < 0 :
        return "Tanımsız"
    elif sayi == 0 or sayi == 1 :
        return  1
    return sayi * faktoriyel_recursive(sayi - 1)

sayi = int(input("Bir sayı giriniz: "))
print(f"{sayi} sayısının faktöriyeli : {faktoriyel_recursive(sayi)}")

# 5 - Palindrome bulalım
def palindrome(ifade) :
    return ifade == ifade[::-1]

print(palindrome("ey edip adanada pide ye"))

def palindrome(ifade) :
    return ifade == "".join(reversed(ifade))

print(palindrome("ey edip adanada pide ye"))

# 8 - Virgülle ayrılmış sayılardan oluşan bir string dizesi giriniz. Bu dizedeki tek sayıların karesini virgülle ayırarak yazdırınız.
def tek_sayilarin_karesi(dize) :
    tek_kareler = []
    dize = dize.replace(",","")
    for i in dize :
        if int(i) % 2 == 1 :
           tek_kareler.append(int(i) ** 2)
    return tek_kareler

dize = input("Virgülle ayrılmış sayılardan oluşan bir dize giriniz: ")
print(tek_sayilarin_karesi(dize))

def tek_sayilarin_karesi(dize) :
    tek_kareler = []
    for i in dize.split(",") :
        if int(i) % 2 == 1 :
            tek_kareler.append(int(i) ** 2)
    return tek_kareler

dize = input("Virgülle ayrılmış sayılardan oluşan bir dize giriniz: ")
print(f"Girilen dizedeki tek sayıların karesinin listesi : {tek_sayilarin_karesi(dize)}")

# 9 - Girilen cümledeki çift indekslerdeki harfleri büyük diğerlerini küçük harf yapan fonksiyonu yazınız.

def buyuk_kucuk_indeks(cumle) :
    yeni_cumle = ""
    for i in  range(len(cumle)) :
        if i % 2 == 0  and cumle[i].isalpha() :
            yeni_cumle += cumle[i].upper()
        elif i % 2 == 1 and cumle[i].isalpha() :
            yeni_cumle += cumle[i].lower()
        else :
            yeni_cumle += cumle[i]
    return yeni_cumle

cumle = input("Bir cümle giriniz: ")
print(buyuk_kucuk_indeks(cumle))

# 10 - girilen öğrenci listesindeki tek indexteki isimleri ayrı listeye çift indexte olan isimleri ayrı listeye alan fonksiyonu yazınız. 
# Fakat bu iki liste tek bir liste olarak return olsun.

def ayristir(ogrenci_listesi) :
    tek_liste = []
    cift_liste = []
    for i in range(len(ogrenci_listesi)) :
        if i % 2 == 0 :
            cift_liste.append(ogrenci_listesi[i])
        else :
            tek_liste.append(ogrenci_listesi[i])
    return [cift_liste, tek_liste]

ogrenci_listesi = input("Öğrenci isimlerini virgülle ayırarak giriniz: ").split(",")
print(ayristir(ogrenci_listesi))

def divide_names(students) :
    grup = [[], []]
    for index, student in enumerate(students) :
        if index % 2 == 0 :
            grup[0].append(student)
        else :
            grup[1].append(student)
    return grup

ogrenci_listesi = "Zehra, Seda, Zeynep, Nur,Züleyha".split(",")
print(divide_names(ogrenci_listesi))


"""
Python'daki enumerate() fonksiyonu oldukça kullanışlı bir yerleşik (built-in) fonksiyondur. enumerate(), bir iterable (örneğin list, tuple, string) 
üzerindeki elemanlara indeks bilgisiyle birlikte döngü kurmamızı sağlar.
Söz Dizimi (Syntax):
enumerate(iterable, start=0)
iterable	Üzerinde döneceğimiz herhangi bir sıralı yapı (liste, demet, string vs.)
start	İndeksin kaçtan başlayacağı (varsayılan 0)
Döndürdüğü Değer:
Bir enumerate objesi döner. Bu nesne, her elemanı (indeks, değer) şeklinde bir tuple olan bir iterable'dır.
"""

# klasik
meyveler = ["elma", "armut", "muz"]
for i in range(len(meyveler)) :
    print(i, meyveler[i])

"""
0 elma 
1 armut
2 muz 
"""

# enumerate() 
meyveler = ["elma", "armut", "muz"]
for index, meyve in enumerate(meyveler) :
    print(index, meyve)

"""
0 elma
1 armut
2 muz
"""

# start parametresi ile:
meyveler = ["elma", "armut", "muz"]
for index, meyve in enumerate(meyveler, start = 1) :
    print(f"{index}. {meyve}")

"""
1. elma
2. armut
3. muz
"""

print(list(enumerate(["elma", "armut", "muz"]))) # [(0, 'elma'), (1, 'armut'), (2, 'muz')]  # enumerate, bir enumerate objesi döndürür, yazdırmak için list() kullanabiliriz


names = ["Zehra", "Seda", "Zeynep", "Nur", "Züleyha"]
print(enumerate(names)) # <enumerate object at 0x0000016198F611C0>   # enumerate, bir enumerate objesi döndürür, yazdırmak için for döngüsü kullanabiliriz

for i in enumerate(names) : # iterablle verileri numaralandırır ve object olarak döndürür
    print(i)

"""
(0, 'Zehra')
(1, 'Seda')
(2, 'Zeynep')
(3, 'Nur')
(4, 'Züleyha')
"""


# 11 - 10'a kadar olan çift sayıların karesini alarak bir sözlüğe ekleyin. Keyler orjinal değerler value'lar karesi alınmış değerler olsun.

dict_sayilar = {}
for i in range(10) :
    if i % 2 == 0 :
        dict_sayilar[i] = i ** 2
print(dict_sayilar) # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

dict_sayilar = {i : i ** 2 for i in range(10) if i % 2 == 0}
print(dict_sayilar) # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

dict_sayilar = {}
for i in range(10) :
    if i % 2 == 0 :
        dict_sayilar.update({i : i ** 2})
print(dict_sayilar) # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# 12 - Girilen sayının verilen aralıkta olup olmadığını kontrol eden bir fonksiyon yazınız.

def sayi_varmı(sayi, baslangic, bitis) :
    return baslangic < sayi < bitis

sayi = int(input("Bir sayı giriniz: "))
baslangic = int(input("Başlangıç değerini giriniz: "))
bitis = int(input("Bitiş değerini giriniz: "))
print(f"Girdiğiniz {sayi} sayısı {baslangic} ile {bitis} arasında mı? : {sayi_varmı(sayi, baslangic, bitis)}")

# 13 - zip() Fonksiyonu Nedir?
"""
zip(), birden fazla iterable (örneğin liste, tuple, string vb.) alır ve bu iterable’ların elemanlarını birlikte
gruplayarak bir iterator döndürür. Her gruplama, verilen iterable'lardaki aynı indeksli elemanlardan oluşur.
Söz Dizimi (Syntax):
zip(iterable1, iterable2, iterable3, ...)
"""


names = ["Zehra", "Seda", "Zeynep", "Nur", "Züleyha"]
ages = [25, 28, 30, 27, 31]

zipped = zip(names, ages)
print(zipped) # <zip object at 0x000002114C6BBF00>  # zip, bir zip objesi döndürür, yazdırmak için list() kullanabiliriz
print(list(zipped)) # [('Zehra', 25), ('Seda', 28), ('Zeynep', 30), ('Nur', 27), ('Züleyha', 31)]

"""
zip objesi bir kez kullanıldıktan sonra tekrar kullanılamaz, bu yüzden tekrar zip yapmalıyız.
list(zipped) çağrısı ile zipped içindeki tüm veriler bir kereye mahsus olarak tüketildi. Yani:
print(list(zipped))
Bu satır zipped içindeki tüm (name, age) çiftlerini tüketir.

Sonrasında şunu yazdığınızda:
for i in zipped:
    print(i)
Artık zipped içinde hiçbir şey kalmadığı için for döngüsü çalışmaz, çıktı vermez.
Eğer zipped'i birden fazla kez kullanmak istiyorsan, ya:
1. zip()'i yeniden oluştur:
zipped = zip(names, ages)
2. Veya ilk başta list()'e çevir, sonra çok kez kullan:
zipped_list = list(zip(names, ages))
Özet
zip() bir defalık kullanılan bir iterator döndürür.
list(zipped) yaptıktan sonra zipped boş kalır.
Tekrar kullanacaksan ya zip()'i yeniden çağır ya da başta list(zip(...)) olarak kaydet.

Neden zip() gibi yapılar tükenir?
Çünkü zip() fonksiyonu bir iterator (yineleyici) döndürür. Python'da iterator'lar şu şekilde çalışır:
Iterator’lar, verileri tek seferde, adım adım üretir.
Bellekte tüm listeyi saklamazlar, sadece sıradaki öğeyi verirler.
Bu nedenle bir kere döndürüldükten sonra, içinde bir şey kalmaz.
Bu davranış, verimlilik ve performans için yapılmıştır.
Avantajı Nedir?
Belleği boşa harcamaz.
Çok büyük veri kümeleriyle çalışırken verimli olur.
zip() gibi fonksiyonlar, büyük veri kümelerinde lazy evaluation (tembel değerlendirme) sağlar.
Örnek:
a = range(1_000_000_000)
b = range(1_000_000_000)
z = zip(a, b)  # Bellekte liste oluşmaz!
Eğer zip() direkt liste döndürseydi, bu kadar büyük veriyle belleğin dolmasına neden olurdu.


"""

zipped = zip(names, ages)
for i in zipped :
    print(i)

"""
('Zehra', 25)
('Seda', 28)
('Zeynep', 30)
('Nur', 27)
('Züleyha', 31)
"""




