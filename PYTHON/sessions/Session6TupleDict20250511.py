"""
Python'da bir nesne for döngüsüyle dolaşılabiliyorsa, ona iterable denir.
Örnek iterable'lar:
list, tuple, set, dict, str
range(10)
file nesneleri
Teknik olarak:
Bir nesne __iter__() metoduna sahipse (veya __getitem__()), Python onu iterable olarak kabul eder.

Java'da Iterable ne demek?
Tanım:
Java'da Iterable bir arayüzdür (interface) ve foreach döngüsünde kullanılabilen nesneleri tanımlar.
List sınıfı Iterable arayüzünü uygular. Bu yüzden for-each döngüsüyle gezilebilir.
Java’da iterable olan şeyler:
List, Set, Queue, Map.keySet()

Kendi sınıfını da implements Iterable diyerek iterable yapabilirsin.
public class MyIterable implements Iterable<String> {
    @Override
    public Iterator<String> iterator() {
        return List.of("x", "y", "z").iterator();
    }
}

Java’da Bir Sınıfın Iterable Olması İçin Ne Gerekir?
Bir sınıfın for-each döngüsünde kullanılabilmesi (yani iterable olması) için:
Iterable<T> arayüzünü implements etmelisin 
iterator() metodunu override etmelisin
"""







# Tuples: Türkçe demet
# () ile kullanılır
# tuple() metodu da var
# Değiştirilemez (immutable) veri yapısıdır.
# iterable'dır. Yani elemanlarına for döngüsü ile tek tek ulaşılabilir.

my_tuple = (1, 2, "3", "Hello", True)
print(my_tuple) # (1, 2, '3', 'Hello', True)
print(type(my_tuple)) # <class 'tuple'>

print(tuple("techpro education")) # ('t', 'e', 'c', 'h', 'p', 'r', 'o', ' ', 'e', 'd', 'u', 'c', 'a', 't', 'i', 'o', 'n')

name = "İbrahim"
print(tuple(name)) # ('İ', 'b', 'r', 'a', 'h', 'i', 'm')

print(tuple(1453)) # TypeError: 'int' object is not iterable önemli
# tuple() metodu iterable argüman alır (örneğin string, list, tuple, set, dict gibi)

print(tuple([1, 2, 3, 4])) # (1, 2, 3, 4) içine liste aldı tuple'a dönüştürdü

a = [1, 2, 3, 4]

b = tuple(a)

print(b) # (1, 2, 3, 4) listeyi tuple'a dönüştürdü

print(a[0]) # 1 list indexlenebilir
print(b[0]) # 1 tuple indexlenebilir
a[0] = 5
print(a) # [5, 2, 3, 4] list mutable

b[0] = 5 # tuple immutable # TypeError: 'tuple' object does not support item assignment

print(tuple(range(1, 20, 5))) # (1, 6, 11, 16) range() fonksiyonu ile tuple oluşturma

x = (1)
print(type(x)) # <class 'int'>

x = (1,)
print(type(x)) # <class 'tuple'>

print(tuple("techpro")) # ('t', 'e', 'c', 'h', 'p', 'r', 'o')

tuple_1 = "x", "y", 3, 1.5
print(tuple_1) # ('x', 'y', 3, 1.5) parantez kullanılmadığında da python tuple olareak olarak algılar
print(type(tuple_1)) # <class 'tuple'>

print(type(("hello",))) # <class 'tuple'>
print(type(("hello"))) # <class 'str'>

print(("Ayşe", "Uluğbek", "Mukaddes") + ("Ali",)) # ('Ayşe', 'Uluğbek', 'Mukaddes', 'Ali')
# Listelerde olduğu gibi toplama operatörü tuple'da da concat işlemi yapıyor.

print(("Ayşe", "Uluğbek", "Mukaddes") * 2) # ('Ayşe', 'Uluğbek', 'Mukaddes', 'Ayşe', 'Uluğbek', 'Mukaddes')


# Indexing

tuple_2 = (7, 8, "max", False, 234, [1 ,2 ,3], [5, 6, 7])

print(tuple_2[2]) # max
print(tuple_2[2][1]) # a

print(tuple_2[-1][2]) # 7

print("ali", "mehmet" + "ali") # ali mehmetali
print(type("ali", "mehmet" + "ali")) # TypeError: type() takes 1 or 3 arguments


print(("ali", "mehmet" + "ali")) # ('ali', 'mehmetali')
print(type(("ali", "mehmet" + "ali"))) # <class 'tuple'>

print(tuple_2) # (7, 8, 'max', False, 234, [1, 2, 3], [5, 6, 7])

# list mutable, tuple immutable. tuple içerisindeki listeye eleman ekleyebilir miyiz?
tuple_2[5].append(4)
print(tuple_2) # (7, 8, 'max', False, 234, [1, 2, 3, 4], [5, 6, 7])
print(type(tuple_2[5])) # <class 'list'> 5. eleman liste, listenin özelliklerini taşır

del tuple_2[3] # TypeError: 'tuple' object doesn't support item deletion # tuple immutable'dır.

del tuple_2[5][0]
print(tuple_2) # (7, 8, 'max', False, 234, [2, 3, 4], [5, 6, 7]) # 1 silindi, liste mutable

# Ama tuple'ı tamamen silebiliriz
del tuple_2
print(tuple_2) # NameError: name 'tuple_2' is not defined # tuple_2 silindi


# len

tuple_3 = (2, 4, [1, 2, 3], "Ayşe", "Fatma")
print(len(tuple_3)) # 5

print(len(tuple_3[2])) # 3

# index()

tuple_3.index("Ayşe") # 3

print((1, 2, 2, 3, 3, 3, 1, 3, 2, 1, 5, 6).index(1)) # 0  # verilen elemanın ilk gördüğü yerdeki indexini verir

# count()
print((1, 2, 2, 3, 3, 3, 1, 3, 2, 1, 5, 6).count(3)) # 4 # verilen elemanın kaç tane olduğunu verir

# Kullanıcıdan 2 tane nesne isteyin, girilen nesneler int ise bunların toplamını veren programı yazın.


# isnumeric() ile, en kapsamlısı isnumeric()
input_1 = input("Birinci nesneyi giriniz: ")

input_2 = input("İkinci nesneyi giriniz: ")

if input_1.isnumeric() and input_2.isnumeric():
        print(int(input_1) + int(input_2))
else:
        print("Lütfen sayısal bir değer giriniz.")

# isdigit() ile
input_1 = input("Birinci nesneyi giriniz: ")

input_2 = input("İkinci nesneyi giriniz: ")

if input_1.isdigit() and input_2.isdigit():
        print(int(input_1) + int(input_2))
else:
        print("Lütfen sayısal bir değer giriniz.")

# isdecimal() ile
input_1 = input("Birinci nesneyi giriniz: ")

input_2 = input("İkinci nesneyi giriniz: ")

if input_1.isdecimal() and input_2.isdecimal():
        print(int(input_1) + int(input_2))
else:
        print("Lütfen sayısal bir değer giriniz.")


# ord()  sayısal (ordinal) karşılığı verir.

print(ord("a")) # 97


# chr() ASCII'deki  karşılığı verir.

print(chr(98)) # b


# Dictionaries 
# sözlük veya mapping ile karşımıza çıkıyor. {} ile kullanılır
# dict() metodu da var

"""
items() metodu, sözlükteki her bir key-value çiftini içeren tuple’lardan oluşan ve liste gibi görünen bir view object döndürür.
Bu nesne:
dict_items tipindedir.
İçerdiği her öğe: (key, value) şeklinde bir tuple’dır.
Görünüşte liste gibi davranır ama gerçek bir liste değildir (yani .append() gibi liste metodları yoktur).

view object Nedir?
Python'da sözlük metotları olan .items(), .keys() ve .values() birer view object döndürür.
View object, sözlüğün canlı (dynamic) bir görünümünü temsil eder.
Yani sözlük değiştiğinde view object de otomatik olarak değişir.
Örnek:
dict_1 = {"key1" : "value1", "key2": "value2"}
view = dict_1.items()
print(view)  # dict_items([('key1', 'value1'), ('key2', 'value2')])
dict_1["key3"] = "value3"
print(view)  # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
Görüldüğü gibi dict_1 değişince view de değişti.
Bu canlı yapıya view object denir.
Bu çıktıda:
dict_items(...) → view object
İçindeki her ('key', 'value') → tuple

dict_items(...)
Bu, view object’in türünü belirtir.
dict_1.items() ifadesi çalıştırıldığında dönen özel tiptir: dict_items

[...] → Köşeli parantez
İçeride bir liste (Python'da list) var.
Yani bu dict_items nesnesi, görünüşte bir liste gibi davranıyor.

'key1', 'value1') → Normal parantezler
Bu bir tuple’dır.
"""

dict_1 = {"key1" : "value1", "key2": "value2", "key3": "value3"}
print(dict_1) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# dictionary'nin her bir öğesine item denir.
# items() metodu sözlükteki her bir öğeyi (key, value) şeklinde tuple olarak verir ve bu tuple'ları içeren bir view object döner.
# .items() çıktısı, doğrudan list() veya tuple() içine alınabilir.

print(dict_1.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])


"""
keys() metodu:
set-like object "Küme-benzeri nesne" demek. Yani bu nesne tıpkı bir set (küme) gibi davranır:
Tekrar eden elemanlar yok
Elemanlar sırasızdır
in operatörüyle sorgulama yapılabilir

providing a view on D's keys: "Sözlük D’nin anahtarlarına bir görünüm sağlar."
Bu, anahtarları kopyalamadan gösterdiğini anlatır. Yani bellek tasarrufu sağlar ve orijinal sözlük değişirse bu görünüm de güncellenir.      

dict.keys() ne döner?
dict_keys adlı özel bir nesne döner. Bu nesne:
set gibi davranır
iterable’dır (üzerinde döngü yapılabilir)
indexlenemez (örneğin d.keys()[0] yazılamaz, ama list(d.keys())[0] olur)
otomatik güncellenir (sözlük değişince bu görünüm de değişir)         

tam olarak bir set dönmez.
Ama set gibi davranan özel bir dict_keys nesnesi döner.
İstersen bunu sete dönüştürebilirsin:
set_of_keys = set(d.keys())  # artık gerçek bir set


dict.keys() ne döner?	dict_keys adında set-benzeri bir görünüm döner
Gerçek bir set mi?	Hayır, ama set(d.keys()) ile dönüştürülebilir
"""


print(dict_1.keys()) # dict_keys(['key1', 'key2', 'key3']) # sadece key'leri verir

print(dict_1.values()) # dict_values(['value1', 'value2', 'value3']) # sadece value'ları verir

print(dict_1[0]) # KeyError: 0 # dictinary'lerde indexleme yok, key ile erişim sağlanır

print(dict_1["key2"]) # value2 # key ile çağırdık
print(dict_1["value2"]) # KeyError: 'value2' # value ile key'e erişim yok, buraya sadece key yazılmalı

dict_2 = {False : 0, True : 1}
print(dict_2) # {False: 0, True: 1} 
print(dict_2[True]) # 1

dict_3 = {1 : ["a", "b", "c"], 2 : (3 , 4)}
print(dict_3) # {1: ['a', 'b', 'c'], 2: (3, 4)} # key'ler int, value'lar list ve tuple
print(dict_3[1]) # ['a', 'b', 'c'] # index değil key

dict_4 = {1 : ["a", "b", "c"], 1 : (3, 4)}
print(dict_4) # {1: (3, 4)} # Aynı key birden fazlaysa sonuncuyu kabul eder
print(len(dict_4)) # 1 # sadece bir tane key var, o yüzden 1 döner
"""
Python'da bir sözlük (dictionary) tanımlarken aynı key (anahtar) birden fazla kez kullanılırsa, sonuncusu geçerli olur. 
Çünkü bir sözlükte anahtarlar benzersiz olmalıdır.
Python bu durumda şunu yapar:
İlk 1: ["a", "b", "c"] kaydını sözlüğe ekler.
Sonra aynı anahtar olan 1: (3, 4) geldiğinde öncekini siler, yerine bunu yazar.
Neden bu böyle?
Çünkü sözlükler şöyle çalışır:
Her anahtar benzersiz olmalı (tıpkı bir kimlik numarası gibi).
Eğer birden fazla aynı anahtar varsa, sonuncusu "üstüne yazar".
Sözlükte veriye erişim O(1) sürede yapılır — bu performansı sağlayabilmek için anahtarların benzersiz olması gerekir.
"""

dict_5 = dict(a = [1, 2, 3], b = "techpro", c = True)
print(dict_5) # {'a': [1, 2, 3], 'b': 'techpro', 'c': True} # dict() metodu ile dictionary oluşturma
print(dict_5.keys()) # dict_keys(['a', 'b', 'c']) # key'leri verir
print(dict_5.values()) # dict_values([[1, 2, 3], 'techpro', True]) # value'ları verir

"""
Farklı dict oluşturma yolları: 
Biçim	                Açıklama
dict()	              Boş sözlük
dict({'a': 1})	      Mapping (başka bir sözlük)
dict([('a', 1)])      Iterable (liste/tuple içinde çiftler)
dict(a=1, b=2)	      Keyword argümanlarla sözlük
"""

"""
kwargs Python'da fonksiyonlara anahtar-değer çifti olarak istediğin kadar argüman geçirebilmeni sağlayan bir yapıdır.
Tanım: **kwargs
kwargs → "keyword arguments" (anahtar kelime argümanları)
** operatörü ile kullanılır.
Fonksiyona istediğin sayıda isimli (anahtar=değer) argüman gönderirsin.
Bu argümanlar fonksiyonda bir sözlük (dict) olarak toplanır.
Örnek:

def selamla(**kwargs):
    print(kwargs)

selamla(isim="Ali", yas=25)
Çıktı:
{'isim': 'Ali', 'yas': 25}
Burada:
isim="Ali" ve yas=25 → keyword arguments
Bunlar kwargs isimli bir sözlüğe dönüşür.

*args ile farkı:
Yapı	   Ne toplar               Türü
*args	   Sırasız argümanlar	   tuple
**kwargs   Anahtar=değer çiftleri  dict

Sonuç
**kwargs = fonksiyona sınırsız sayıda isimli argüman verebilmeni sağlar.
İçeride bu argümanlar bir sözlük (dict) haline gelir ve işleyebilirsin.
"""

# print(dict(1 = "a", 2 = "b")) # SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
"""print(dict(1 = "a", 2 = "b"))    
Yasak çünkü:
1 ve 2 geçerli değişken isimleri (identifier) değildir.
key=value biçiminde kullanılacak key'ler Python değişkeni gibi yazılmalı.
Çözüm: ya dict([(1, "a"), (2, "b")]) kullan ya da dict(one="a") gibi string-key kullan. """
# print(dict("1" = "a", "2" = "b")) # SyntaxError: expression cannot contain assignment, perhaps you meant "=="?

print(dict(name1 = "Ayşe", name2 = "Betül")) # {'name1': 'Ayşe', 'name2': 'Betül'} # değişken ismine uygun key verildiğinde kabul ediyor

# dict_names = {name1 : "Uluğbek", name2 : "Ümit", name3 : "Burak", name4 : "Betül"} # NameError: name 'name1' is not defined 
"""
Burada name1, name2, name3, name4 Python’da tanımlı bir değişken değil.
Python bu name1 gibi ifadeleri string değil, değişken zanneder.
Ama bu değişkenler tanımlı olmadığı için NameError oluşur.
Çözüm:
Key’leri string yapmak gerekiyor:
"""
dict_names = {"name1" : "Uluğbek", "name2" : "Ümit", "name3" : "Burak", "name4" : "Betül"}
print(dict_names) # {'name1': 'Uluğbek', 'name2': 'Ümit', 'name3': 'Burak', 'name4': 'Betül'}

# dict mutable
# keylerin valuelerini (anahtarların değerlerini) değiştirebiliriz
dict_names["name4"] = "Ayşe"
print(dict_names) # {'name1': 'Uluğbek', 'name2': 'Ümit', 'name3': 'Burak', 'name4': 'Ayşe'}

person_info = {"name" : ["Ali", "Veli"], "age" : [25, 30]}
print(person_info) # {'name': ['Ali', 'Veli'], 'age': [25, 30]}
print(person_info["name"]) # ['Ali', 'Veli']
print(person_info["name"][1]) # Veli # "name" keyi için value list'tir. O halde list için indexleme ve list metotlarını kullanabiliriz
person_info["name"].append("Ayşe")
print(person_info["name"]) # ['Ali', 'Veli', 'Ayşe'] # list'e eleman ekledik
print(person_info) # {'name': ['Ali', 'Veli', 'Ayşe'], 'age': [25, 30]}
person_info["age"].append(25)
print(person_info) # {'name': ['Ali', 'Veli', 'Ayşe'], 'age': [25, 30, 25]}



# update() metodu ile bir sözlüğe yeni key-value ekleyebiliriz.
"""
update() metodu mevcut bir sözlüğü güncellemek için kullanılır. Yani başka bir sözlük veya anahtar-değer çiftleri verildiğinde,
bunları mevcut sözlüğe ekler veya günceller.
update() metodunun ikinci kullanım şekli:
Anahtar-değer çiftlerini keyword argument şeklinde de verebilirsin.
Örnek:
d.update(one="1", two="2")
Burada one ve two → string anahtarlar, "1" ve "2" → string değerlerdir.
Burada **kwargs: str demek:
Anahtarlar str olacak (zaten Python bunu zorunlu kılar), ve değerler de str olmalı
Bu metodun dönüş değeri yoktur. Yani None döner. update() metodu sözlüğü yerinde (in-place) değiştirir, yeni bir sözlük döndürmez.

Kısaca Özetlersek:
update() metodu, ya:
Bir sözlük gibi bir yapı alır (anahtar ve değerleri str türünde),
Veya key=value şeklinde keyword argümanları alır,
Ve mevcut sözlüğü yerinde günceller.
Dönüş değeri: None
"""

print(person_info.keys()) # dict_keys(['name', 'age'])

# Bir keyi nasıl değiştiriyorsak, aynı yöntemle yeni bir key ekleyebiliriz.
person_info["job"] = ["Teacher", "Doctor", "Devops Engineer"]
print(person_info) # {'name': ['Ali', 'Veli', 'Ayşe'], 'age': [25, 30, 25], 'job': ['Teacher', 'Doctor', 'Devops Engineer']}

print(dict_1) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
dict_1["key4"] = "value4"
print(dict_1) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

dict_1.update({"key5" : "value5", "key6" : "value6"}) # yeni bir dict ekler
print(dict_1) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5', 'key6': 'value6'}

# concat yapılmaz
print({1 : "bir", 2 : "iki"} + {3 : "üç", 4 : "dört"}) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

dict_1["key5", "key6"] = "value5", "value6"  # virgül ile verdiklerimizi tuple olarak algıladı, veya [] içine tuple girebiliriz
print(dict_1)
# {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5', 'key6': 'value6', ('key5', 'key6'): ('value5', 'value6')}

# clear() metodu ile dictionary'i temizleyebiliriz

dict_1.clear()
print(dict_1) # {} # dictionary'i temizledik

dict_5.clear()
print(dict_5) # {}

print(dict_3) # {1: ['a', 'b', 'c'], 2: (3, 4)} 
print(dict_2) # {False: 0, True: 1}

print(dict_2 |dict_3) # {False: 0, True: ['a', 'b', 'c'], 2: (3, 4)} # python 3.9 ve sonrası | operatörü ile birleştirme yapabilir
""" 
Python dict birleştirmede aynı hash ve eşitliğe sahip anahtarlar varsa:
Değer sağdakinden gelir
Anahtar tipi soldaki kalır
True ve 1 aynı anahtar olduğu için değer güncellenir, fakat ilk karşılaşılan anahtar olan True (bool) yazılmaya devam eder.
"""

dict_6 = {"İstanbul"  : "Yağışlı", "Ankara" : "Karlı"} |{"İzmir" : "Rüzgarlı", "Antalya" : "Güneşli"}
print(dict_6) # {'İstanbul': 'Yağışlı', 'Ankara': 'Karlı', 'İzmir': 'Rüzgarlı', 'Antalya': 'Güneşli'}

dict_6.update(dict_2)
print(dict_6) # {'İstanbul': 'Yağışlı', 'Ankara': 'Karlı', 'İzmir': 'Rüzgarlı', 'Antalya': 'Güneşli', False: 0, True: 1}


# pop() metodu ile dictionary'den bir key-value çiftini silebiliriz.

print(dict_6.pop("İstanbul")) # 'Yağışlı' # veriilen keyi siler ve valuesunu yazdırır
print(dict_6) # {'Ankara': 'Karlı', 'İzmir': 'Rüzgarlı', 'Antalya': 'Güneşli', False: 0, True: 1}

print(dict_6.pop("Van")) # KeyError: 'Van' # olmayan bir keyi silmeye çalıştık

print(dict_6.pop(0)) # 0 # False'ı 0 olarak görür, bu nedenle 0 verdiğimizde False: 0 çiftini siler


# get() metodu ile dictionary'den bir key'in value'sunu alabiliriz.

print(dict_6.get("İzmir")) # Rüzgarlı # verilen keyin value'sunu verir
print(dict_6["İzmir"]) # Rüzgarlı # aynı işlemi [] ile de yapabiliriz


# nested dicts

myFamily = {
        "child1" : {
                "name" : "John",
                "year" : 2004
        },
        "child2" : {
                "name" : "Jane",
                "year" : 2006
        },
        "child3" : {
                "name" : "Jim",
                "year" : 2008
        }
}

print(myFamily) # {'child1': {'name': 'John', 'year': 2004}, 'child2': {'name': 'Jane', 'year': 2006}, 'child3': {'name': 'Jim', 'year': 2008}}

print(myFamily.items()) # dict_items([('child1', {'name': 'John', 'year': 2004}), ('child2', {'name': 'Jane', 'year': 2006}), ('child3', {'name': 'Jim', 'year': 2008})])

print(myFamily.get("child1")) # {'name': 'John', 'year': 2004} # child1 keyinin value'sunu verir

print(myFamily.get("child2").get("name")) # Jane # child2 keyinin value'sunun name keyinin value'sunu verir

myFamily.get("child3").update({"gender" : "male"})
print(myFamily) # {'child1': {'name': 'John', 'year': 2004}, 'child2': {'name': 'Jane', 'year': 2006}, 'child3': {'name': 'Jim', 'year': 2008, 'gender': 'male'}}

# not, not in

"""
in ve not in Python'da operatördür, yani bir fonksiyon gibi değil, dil yapısı (syntax) olarak tanımlıdır — bu yüzden üstüne gelince imza (signature) çıkmaz.

in Operatörü Kullanımı:
element in iterable
Anlamı:
Soldaki öğe (element), sağdaki yapının (iterable, yani üzerinde dolaşılabilen veri yapısı: liste, string, tuple, set, sözlük vs.) içinde var mı?
Sonuç: True ya da False döner.

not in Operatörü Kullanımı:
element not in iterable
Anlamı:
Soldaki öğe, sağdaki yapının içinde yok mu?
Yani not (element in iterable) ile aynıdır.
"""

print("e" in "hello") # True # "e" harfi hello kelimesinde var mı

print("a" in "hello") # False # "a" harfi hello kelimesinde var mı

print("l" not in "hello") # False # "l" harfi hello kelimesinde yok mu

print(1 in [1, 2, 3]) # True # 1 sayısı listede var mı

print("child1" in myFamily) # True # "child1" keyi myFamily dictionary'sinde var mı

print("name" in myFamily) # False # "name" keyi myFamily dictionary'sinde var mı

print(myFamily.values()) # dict_values([{'name': 'John', 'year': 2004}, {'name': 'Jane', 'year': 2006}, {'name': 'Jim', 'year': 2008, 'gender': 'male'}])
print("name" in myFamily.values()) # False # "name" value'su myFamily dictionary'sinde var mı

print("name" in myFamily["child1"]) # True # "name" keyi child1 dictionary'sinde var mı

print(myFamily["child1"].values()) # dict_values(['John', 2004])
print("John" not in myFamily["child2"].values()) # True # "John" value'su child2 dictionary'sinde yok mu
print("John" in myFamily["child1"].values()) # True # "John" value'su child1 dictionary'sinde var mı

print(myFamily.get("child3")) # {'name': 'Jim', 'year': 2008, 'gender': 'male'}
print("name" in myFamily.get("child3")) # True # "name" keyi child3 dictionary'sinde var mı

print(myFamily.get("child3").values()) # dict_values(['Jim', 2008, 'male'])
print("Jim" not in myFamily.get("child3").values()) # False 

print(list(myFamily.get("child3").values())) # ['Jim', 2008, 'male'] list yapısında
print(list(myFamily.get("child3").keys())) # ['name', 'year', 'gender'] list yapısında