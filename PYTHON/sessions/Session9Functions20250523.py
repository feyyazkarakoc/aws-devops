
# Functions

# def fonksiyon_ismi(parametre) :
#    işlemler

"""
Temel Yapı:
def fonksiyon_adi(parametre1, parametre2, ...):
    # Fonksiyonun yaptığı işlemler üçlü çift tırnak (""" """ veya ''' ''') içinde, docstring formatında açıkça yazılır
    return değer  # opsiyonel
"""

"""
 Python’da bir fonksiyon tanımlamak için def anahtar kelimesi her zaman zorunludur  (lambda dışında).
"""

"""
Docstring'in Faydaları:
help() komutuyla bu açıklamaya erişebilirsin.
IDE'ler (VS Code, PyCharm, vb.) imleci fonksiyon üstüne getirince docstring’i gösterir.
Daha okunabilir ve sürdürülebilir kod sağlar.
Otomatik dökümantasyon araçları (Sphinx, pdoc, vs.) docstring üzerinden çalışır.
Python'da fonksiyonların içine docstring yazmak çok yaygındır,
Profesyonel projelerde neredeyse her fonksiyon, sınıf, modül böyle belgelenir.
Özellikle açık kaynak projelerde bu bir zorunluluk gibi uygulanır.


"""


def kare_al(x) : # docstring şeklinde fonksiyonun tanımı yazılır
    '''
    Girilen sayının karesini alan fonksiyon 
    '''
    return x ** x


print(kare_al(2)) # 4

help(kare_al)
"""
Help on function kare_al in module __main__:

kare_al(x)
    girilen sayının karesini alan fonksiyon

"""

def kare_al2(x) :
    print(x ** 2) 
# Bu satır ekrana karesini yazdırır ama  bu fonksiyon return kullanmadığı için, otomatik olarak None döner.


print(kare_al2(9))
"""
81
None

Fonksiyonlarda print → ekrana yazar.
return → çağırana değer döner.
"""

# return yok, bu çıktıyı bir yerde kullanamam
x = 5 + kare_al2(2) # TypeError: unsupported operand type(s) for +: 'int' and 'NoneType', print none döndürür
print(x)

x = 5 + kare_al(2)
print(x) # 9 

print(type(print())) # <class 'NoneType'> 
# Fonksiyonlarda çıktının kullanılabilir olması için print yerine return tercih edilir

def topla(a, b) : # burda girilen parametrelere argüman deniliyor
    return a + b


print(topla(70, 100)) # 170

print(topla()) # TypeError: topla() missing 2 required positional arguments: 'a' and 'b' , argüaman girmediğimizde hata veriyor

def topla(a = 2, b = 3) : # default değerler verebiliyoruz
    return a + b

print(topla()) # 5 

print(topla(23, 32)) # 55 # default değerleri olan fonksiyona yeni değerler de verebiliriz

def kare_topla(a = 5, b = 3) :
    return a ** 2 + b ** 2

print(kare_topla()) # 34 defaullt değerlerin karesini aldı

print(kare_topla(2, 3)) # 13

def hesap_makinesi(x, opr, y) :
    """Bu fonksiyon dört işlem yapabilmek için oluşturulmuştur."""
    if opr == "+" :
        return x + y
    elif opr == "-" :
        return x - y
    elif opr == "*" :
        return x * y
    elif opr == "/" :
        if y != 0 :
            return x / y
        else :
            return "Sayı sıfıra bölünemez!!!"
    else :
        return "Geçersiz işlem!!!"
    
print(hesap_makinesi(4, "*", 12)) # 48

print(hesap_makinesi("a", "+", "b")) # ab

print(hesap_makinesi("a", "+", 5)) # TypeError: can only concatenate str (not "int") to str

print(hesap_makinesi(4, 15, "+")) # Geçersiz işlem # fonksiyona verdiğimiz tuple tipindeki argümanlara pozisyonel argüman denir ve sıralama önemlidir
"""
Yani Fonksiyonun parametrelerine değer verirken sıralamaya (pozisyona) dikkat etmeliyiz. Sıralama yanlış olursa, fonksiyon beklenen şekilde çalışmaz.
"""

print(hesap_makinesi(5, "/", 0)) # Sayı sıfıra bölünemez!!!

def hesap_makinesi() :
    """Bu fonksiyon dört işlem yapabilmek için oluşturulmuştur."""
    x = int(input("Birinci sayıyı giriniz: "))
    y = int(input("İkinci sayıyı giriniz: ")) 
    opr = input("Yapmak istediğiniz işlemi giriniz (+, -, *, /): ")
    if opr == "+" :
        return x + y
    elif opr == "-" :
        return x - y
    elif opr == "*" :
        return x * y
    elif opr == "/" :
        if y != 0 :
            return x / y
        else :
            return "Sayı sıfıra bölünemez!!!"
    else :
        return "Geçersiz işlem!!!"

print(hesap_makinesi()) # Bu fonksiyon kullanıcıdan veri alır ve işlemi yapar

def my_len(iter) :
    """Girilen ifadedeki eleman sayısını döndürür."""
    sayac = 0
    for i in iter :
        sayac += 1
    return sayac

print(my_len("techpro")) # 6

print(my_len([3, 2, 1, 3, 5, 6])) # 6

print(my_len({"key1" : "value1", "key2": "value2"})) # 2

print(my_len(1234)) # TypeError: 'int' object is not iterable, 1234 iterable olmadığı için hata verdi 

print(len(1234)) # TypeError: object of type 'int' has no len()
"""
len() hangi türleri kabul etmez?
Şu türlerde len() hata verir çünkü uzunluğu yoktur:
int
float
bool
None
"""

help(my_len)
"""
Help on function my_len in module __main__:

my_len(iter)
    Girilen ifadedeki eleman sayısını döndürür.
"""

# Fonksiyona eklediğimiz string ifadeyi döndüren bir metot var:
my_len.__doc__  # 'Girilen ifadedeki eleman sayısını döndürür.' # docstring'i döndürür

hesap_makinesi.__doc__  # 'Bu fonksiyon dört işlem yapabilmek için oluşturulmuştur.' # docstring'i döndürür

"""
Python'da __doc__ ve benzeri iki alt çizgiyle (__) başlayan ve biten yapılar özel metotlardır ve bunlara dondur
(dunder = double underscore) metodları denir. Bunlar built-in (gömülü) ve özelleştirilebilir davranışları temsil eder.
Bunlar built-in mıdır?
Evet, bunların tamamı Python'da gömülüdür (built-in) ama istersen sen de bu metotları override edebilir (yeniden tanımlayabilir)
ve sınıflarına özel davranışlar kazandırabilirsin.
"""

# int bir sayının lenini bulan bir fonksiyon yazalım
def len_int(sayi) :
    """Bu fonksiyon integer ifadelerin uzunluğunu döndürür."""
    return len(str(sayi))

print(len_int(1234)) # 4

print(len_int("Hello World")) # 11

print(len_int([1, 2, 4, 4, 6, 7])) # 18
print(len([1, 2, 4, 4, 6, 7])) # 6 

print(len_int(356.86432)) # 9

print(len_int(-234)) # 4

def len_int(sayi) :
    """Bu fonksiyon integer ifadelerin uzunluğunu döndürür."""
    if type(sayi) != int :
        return "Lütfen bir integer ifade giriniz."
    sayac = 0
    for i in str(sayi) :
        sayac += 1
    return sayac
print(len_int(123456789)) # 9

# Kullanıcının verdiği liste içerisinden yine kullanıcının istediği tek veya çift sayılar listesini döndüren bir fonksiyon yazalım
def tek_cift_sayilar(liste, secenek) :
    """Bu fonksiyon verilen listeden tek veya çift sayıları döndürür."""
    if type(liste) != list :
        return "Lütfen bir liste giriniz."
    tek_sayialr = []
    cift_sayilar = []
    for j in liste :
        if j %2 == 0 :
            cift_sayilar.append(j)
        else :
            tek_sayialr.append(j)
    if secenek == "tek" :
        return tek_sayialr
    elif secenek =="cift" :
        return cift_sayilar
    
print(tek_cift_sayilar([1, 2, 3, 4, 5, 6], "tek")) # [1, 3, 5]
print(tek_cift_sayilar([1, 2, 3, 7, 8, 10, 55, 22], "cift")) # [2, 8, 10, 22]

# Bu fonksiyona default olarak bir değer verebiliriz
def tek_cift_sayilar(liste, secenek = "tek") : # Kullanıcı seçenek girmediğinde  tek sayıları getirir
    """Bu fonksiyon verilen listeden tek veya çift sayıları döndürür."""
    if type(liste) != list :
        return "Lütfen bir liste giriniz."
    tek_sayialr = []
    cift_sayilar = []
    for j in liste :
        if j %2 == 0 :
            cift_sayilar.append(j)
        else :
            tek_sayialr.append(j)
    if secenek == "tek" :
        return tek_sayialr
    elif secenek =="cift" :
        return cift_sayilar
    
    print(tek_cift_sayilar([1, 2, 3, 4, 5, 6])) # [1, 3, 5] default olarak tek sayıları döndürdü, tek çift diye belirtmedik

# Kullanıcının girdiği listeden yine kullanıcının verdiği uzunluktaki isimleri döndüren bir fonksiyon yazalım
def  kelime_secme(liste, uzunluk) :
    sonuc = []
    for isim in liste :
        if len(isim) == uzunluk :
            sonuc.append(isim)
    return sonuc

print(kelime_secme(["Ali", "Veli", "Ayşe", "Betül", "Gülay", "Feyza", "İbrahim", "Uluğbek"], 5)) # ['Betül', 'Gülay', 'Feyza']

def kelime_secme(liste, uzunluk) :
    return [isim for isim in liste if len(isim) == uzunluk]

print(kelime_secme(["Ali", "Veli", "Ayşe", "Betül", "Gülay", "Feyza", "İbrahim", "Uluğbek"], 4)) # ['Veli', 'Ayşe']

print(kelime_secme(["Ali", "Veli", "Ayşe", "Betül", "Gülay", "Feyza", "İbrahim", "Uluğbek"], 7)) # ['İbrahim', 'Uluğbek']
     
print(kelime_secme(["Ali", "Veli", "Ayşe", "Betül", "Gülay", "Feyza", "İbrahim", "Uluğbek"], 5)) # ['Betül', 'Gülay', 'Feyza']

x = kelime_secme(["Ali", "Veli", "Ayşe", "Betül", "Gülay", "Feyza", "İbrahim", "Uluğbek"], 5)
x.sort()
print(x) # ['Betül', 'Feyza', 'Gülay'] # sort() metodu listeyi yerinde sıraladı

"""
list.sort() Metodu Nedir?
Python'da sort() metodu, bir listeyi yerinde (in-place) sıralar. Yani orijinal listeyi değiştirir ve hiçbir şey döndürmez (None).
In-place sorting: Listeyi doğrudan değiştirir, yeni bir liste oluşturmaz.
Stable sort (kararlı sıralama): Aynı değerlere sahip öğeler, listede bulundukları sıraya göre yer değiştirmez.
Bu, örneğin birden fazla kritere göre sıralama yaparken önemlidir.
key parametresi: Öğeleri sıralamak için dönüş değeri kullanılacak özel bir fonksiyon belirtebilirsin.
Not:
sort() metodu sadece listeler için geçerlidir.
Listeyi değiştirmek istemiyorsan, sorted() fonksiyonunu kullanabilirsin:
"""

# Sonucu sıralanmış olarak istersek
def kelime_secme(liste, uzunluk) :
    sonuc = []
    for isim in liste :
        if len(isim) == uzunluk :
            sonuc.append(isim)
    sonuc.sort()
    return sonuc

print(kelime_secme(["Ali", "Veli", "Ayşe", "Betül", "Gülay", "Feyza", "İbrahim", "Uluğbek"], 5)) # ['Betül', 'Feyza', 'Gülay']

# sıralanmış olarak listeyi getir sorted() versiyon 
def kelime_seçme(liste, uzunluk):
    sonuc = []
    for isim in liste :
        if len(isim) == uzunluk :
            sonuc.append(isim)
    return sorted(sonuc)  
print(kelime_seçme(["Ali", "Veli", "Ayşe", "Betül", "Gülay", "Feyza", "İbrahim", "Uluğbek"], 5)) # ['Betül', 'Feyza', 'Gülay']
"""
Yerleşik (built-in) fonksiyondur. 
sorted() fonksiyonu, Python'da sıralama yaparken orijinal veriyi bozmadan, yeni bir sıralı liste döndürmek için kullanılır.
sorted() herhangi bir sıralanabilir veri tipi ile çalışır (liste, tuple, sözlük, set, vs.).
Yeni bir liste döner, orijinal veri değişmez.
key parametresiyle özel sıralama yapılabilir.
reverse=True ile azalan sıralama yapılabilir.
Not:
list.sort() → listeyi yerinde değiştirir ve None döner.
sorted() → değiştirmeden yeni sıralı liste döner.
"""

print(kelime_seçme(["Ali", "Veli", "Ayşe", "Betül", "Gülay", "Feyza", "İbrahim", "Uluğbek"], 4)) # ['Ayşe', 'Veli']

print(kelime_seçme(["Ali", "Veli", "Ayşe", "Betül", "Gülay", "Feyza", "ibrahim", "Uluğbek"], 7)) # ['Uluğbek', 'ibrahim'] # ASCII değerlerine göre sıraladı