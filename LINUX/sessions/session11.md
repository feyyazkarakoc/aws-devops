
# öşeli parantezler [ ] - aralık belirtmek için kullanılan joker karakterdir.
Kullanım örnekleri:
Harf aralığı:
ls [a-z]*         # a-z ile başlayan dosyalar
ls [A-Z]*         # A-Z ile başlayan dosyalar  
ls [a-zA-Z]*      # Tüm harflerle başlayan dosyalar
Rakam aralığı:
ls [0-9]*         # 0-9 ile başlayan dosyalar
ls file[1-5].txt  # file1.txt, file2.txt, ..., file5.txt
ls *[0-9].log     # Rakamla biten .log dosyaları
Belirli karakterler:
ls [abc]*         # a, b veya c ile başlayan dosyalar
ls file[135].txt  # file1.txt, file3.txt, file5.txt
ls [!0-9]*        # Rakamla başlamayan dosyalar (ünlem = değil)
Karmaşık örnekler:
bashls [a-z][0-9]*    # Harf+rakam ile başlayan dosyalar
ls *[a-z][A-Z]*   # İçinde küçük+büyük harf olan dosyalar  
ls [!aeiou]*      # Sesli harfle başlamayan dosyalar

# [] köşeli parantezlerin anlamı.

Kural:

ls dosya[178] yazınca, [178] sadece tek bir karakter eşleştirir.

Bu, "1 ya da 7 ya da 8" olabilir demek.

Yani dosya1, dosya7, dosya8 eşleşir.

Ama dosya11, dosya15, dosya19, dosya76, dosya88 eşleşmez çünkü [] sadece tek karaktere bakar.

Senin örneğin:
ls dosya[178]


eşittir:

ls dosya1 dosya7 dosya8


O yüzden sadece tek haneli numaralar geldi.

Eğer 11, 15, 19, 76, 88 gibi birden fazla haneli sayılar de gelsin istiyorsan:

? kullanabilirsin → bu da tek karakter yerine "herhangi bir karakter" koyar:

ls dosya1?


→ dosya10, dosya11, ..., dosya19 gelir.

Rakam aralıkları için {} kullanabilirsin (brace expansion):

ls dosya{1,7,8}*


→ dosya1, dosya7, dosya8, dosya11, dosya17, dosya18 ... gibi hepsi gelir.

Daha net:

ls dosya{11,15,19,76,88}


sadece istediğin dosyaları listeler.

Özet:

[ ] → tek karakter eşleşmesi (1,7,8)

{ } → listeleme / aralık (11,15,19,...)

? → herhangi bir tek karakter

# [ec2-user@ip-172-31-18-98 ~]$ ls -l
total 0
drwxr-xr-x. 6 ec2-user ec2-user 52 Sep 19 14:28 project
1. total 0
Bu, dizindeki dosyaların disk üzerindeki toplam blok sayısını gösterir.

Yani "bu klasördeki içerikler ne kadar disk bloğu kullanıyor?" bilgisini verir.

Senin örneğinde 0 çünkü project sadece bir klasör (henüz içinde dosya yok).

2. drwxr-xr-x. (izinler + tür)
Bu ilk kolon dosya/klasör hakkında bilgi verir:

d → directory (klasör)

rwx → owner (sahip) izinleri: read, write, execute

r-x → group izinleri: read, execute (yazma yok)

r-x → others izinleri: read, execute

sondaki . → SELinux veya extended attributes olduğunu gösterir.

3. 6 (link sayısı)
Bu, o klasöre kaç adet hard link olduğunu gösterir.
Klasörler için bu sayı:

. (klasörün kendisi)

.. (ebeveyn klasör)

ve içerideki alt klasörlerin .. referansları.

Senin klasörde alt dizinler var → bu yüzden sayı 6.

4. ec2-user ec2-user
İki ayrı şey:

Birinci ec2-user → dosya/klasörün owner (sahibi)

İkinci ec2-user → dosya/klasörün group (grubu)

Yani bu klasörün sahibi ec2-user kullanıcısı ve grubu da ec2-user.

5. 52
Bu klasörün boyutu (bayt olarak).
Klasörler için bu sayı dizin tablosunun boyutunu gösterir (içindekilerin isimleri tutulur).

6. Sep 19 14:28
Klasörün oluşturulma/değiştirilme tarihi.

7. project
Dosya veya klasörün adı.

Özet:

total → dizindeki içeriklerin disk blok toplamı

drwxr-xr-x. → izinler ve tür (directory, owner okuma/yazma/çalıştırma)

6 → link sayısı

ec2-user → sahip kullanıcı

ec2-user → sahip grup

52 → boyut (byte)

Sep 19 14:28 → son değiştirilme zamanı

project → dosya/klasör adı

# mkdir komutunda -p (veya --parents) şu işe yarar:

1. Var olan dizin için hata verme

Normalde:

mkdir backup


Eğer backup zaten varsa:

mkdir: cannot create directory ‘backup’: File exists


Ama:

mkdir -p backup


Dizin zaten varsa sessizce devam eder, hata vermez.

2. Gerekirse ara dizinleri de oluşturur

Örnek:

mkdir project/src/scripts


Eğer project yoksa, hata alırsın:

mkdir: cannot create directory ‘project/src/scripts’: No such file or directory


Ama:

mkdir -p project/src/scripts


project, src yoksa hepsini tek seferde zincirleme oluşturur.

3. Best practice sebebi

Scriptlerde mkdir -p kullanmak daha güvenli.

Çünkü dizin zaten varsa sorun çıkarmaz,

yoksa da gerekli tüm parent dizinleriyle birlikte oluşturur.

Kısaca:
-p hem idempotent (tekrar tekrar çalıştırabilirsin, hata vermez)
hem de ebeveyn dizinleri otomatik oluşturur.

# cat $FILE | grep bekir | grep Terminate | grep -Eo "i-[a-zA-Z0-9]{17}" | sort | uniq > /tmp/result.txt
1. grep -Eo "i-[a-zA-Z0-9]{17}" kısmı
grep normalde bir satırın tamamını döndürür.

-E : Extended regex kullan demek, yani {17} gibi ileri regex özelliklerini destekler.

-o : sadece eşleşen kısmı göster, yani satırın tamamını değil sadece pattern’e uyan kısmı döndür.

"i-[a-zA-Z0-9]{17}" :

i- ile başlayan

sonrasında 17 karakterlik alfanümerik (a-z, A-Z, 0-9) bir dize.

Örnek: i-0c127ab5cdf997cf4

Bu sayede satırdaki uzun loglardan sadece instance id’leri çekilmiş oluyor.

2. Neden /tmp/result.txt?
/tmp Linux sistemlerinde geçici dosyalar için kullanılır.

Script’ler genellikle log veya geçici çıktı dosyalarını /tmp altında tutar, böylece sistemin home dizinini karıştırmaz.

Eğer kalıcı olarak saklamak istersen ~/result.txt gibi bir dizin kullanabilirsin.

3. Best practice mi?
Genel olarak iyi bir çözüm: grep -Eo ile sadece id’leri çekmek, sort | uniq ile tekrar edenleri kaldırmak mantıklı.

Ama birkaç iyileştirme yapılabilir:

cat $FILE | grep ... yerine doğrudan grep ile dosya okuma (grep bekir "$FILE" | ...) daha temizdir.

cat $FILE | grep ... bir “UUOC” (useless use of cat) örneği.

/tmp kullanmak iyi ama eğer script kullanıcıya kalıcı dosya istiyorsa, ~/result.txt daha iyi.

Örnek iyileştirilmiş versiyon:
grep bekir "$FILE" | grep Terminate | grep -Eo "i-[a-zA-Z0-9]{17}" | sort -u > ~/result.txt
echo "Your result is ready under ~/result.txt"
sort -u hem sıralar hem uniq yapar, tek komutla halledersin.


Şunu dedin:
normalde instance id 19 haneli biz oraya neden {17} yazdık

AWS EC2 Instance ID’leri genellikle i- ile başlar ve toplam uzunlukları 19 karakter olur.

Örnek: i-0c127ab5cdf997cf4

Ama regex’te "i-[a-zA-Z0-9]{17}" yazıyoruz. Neden 17?

Adım adım:

"i-" zaten 2 karakter (i ve -) kapsıyor.

Sonrasında {17} demek, 2 karakter + 17 karakter = toplam 19 karakter.

Yani {17} sadece i- kısmı hariç kalan 17 karakterlik alfanümerik kısmı temsil ediyor.
Bu şekilde toplam uzunluk 19’a eşit oluyor. 

Özet: {17} → i- hariç alfanümerik kısmın uzunluğu. i- ile birlikte 19 karakter oluyor.

# Bash’te karşılaştırma operatörleri, kullanılan bağlama göre değişir.

1. = ve == → String karşılaştırma
if [[ $a = "hello" ]]
if [[ $a == "hello" ]]


İkisi de string eşitliğini test eder.

[[ ... ]] içinde hem = hem de == geçerlidir.

== ayrıca pattern matching (joker karakterlerle eşleşme) de yapabilir:

x="file.txt"
if [[ $x == *.txt ]]; then
  echo "Bu bir txt dosyası"
fi


Yani == string eşitliği yanında joker eşleşme de sağlar.
= sadece eşitlik karşılaştırması yapar.

2. -eq, -ne, -lt, -gt → Sayısal karşılaştırma
if [[ $num -eq 5 ]]   # eşitse
if [[ $num -ne 5 ]]   # eşit değilse
if [[ $num -lt 10 ]]  # küçükse
if [[ $num -gt 10 ]]  # büyükse


Bunlar sadece integer değerler için çalışır.
Eğer string verirsen hata alırsın.

3. Özet

= → string karşılaştırma

== → string karşılaştırma + pattern matching

-eq, -ne, -lt, -gt → sayısal karşılaştırma

Senin örneğin:

if [[ $FILE == '' ]]


Doğru, burada string boş mu diye bakıyorsun.
Ama daha best practice olan yol şu:

if [[ -z $FILE ]]


-z → string uzunluğu sıfır mı (boş mu) diye kontrol eder.