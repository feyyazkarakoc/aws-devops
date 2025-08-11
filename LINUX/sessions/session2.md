
# Linux’ta man pages (“manual pages” = kılavuz sayfaları)
her komutun, fonksiyonun, dosya formatının veya yapılandırma dosyasının detaylı kullanım dökümanıdır.

Temel mantık:
Terminalde bir komutun ne işe yaradığını, hangi parametreleri aldığını ve nasıl kullanılacağını doğrudan Linux’un kendi içinden öğrenmek için kullanılır.

1. Nasıl kullanılır?
man komut_adi
Örnek:
man ls
ls komutunun açıklamasını, seçeneklerini, örneklerini gösterir.
Okumayı bitirmek için q tuşuna basılır.

2. Man page bölümleri
Her man sayfası genellikle şu başlıklarla gelir:

Bölüm	Açıklama
NAME	Komutun/fonksiyonun adı ve kısa açıklaması
SYNOPSIS	Kullanım şekli (komut + parametreler)
DESCRIPTION	Detaylı açıklama
OPTIONS	Parametreler ve anlamları
EXAMPLES	Kullanım örnekleri
SEE ALSO	Benzer komut veya dokümanlar

3. Man page kategorileri (section’lar)
Man sayfaları konu türüne göre numaralandırılır:

User Commands – Normal komutlar (ls, cp, mv)

System Calls – Kernel sistem çağrıları

Library Functions – C kütüphane fonksiyonları

Special Files – /dev altındaki özel cihaz dosyaları

File Formats – Konfigürasyon dosyalarının formatları

Games – Oyunlar ve eğlence programları

Miscellaneous – Çeşitli bilgiler

Admin Commands – Sadece root’un çalıştırabileceği komutlar

Örnek:
man 5 passwd
Bu, /etc/passwd dosyasının formatını (section 5) gösterir.

Kısacası:
Man pages = Linux’un kendi içindeki “offline Google” gibi. İnternete gerek kalmadan, her komutun resmi açıklamasını verir.

# Linux’taki info pages (veya GNU info pages), komutlar, programlar ve kütüphaneler hakkında ayrıntılı belgeler sunan bir dokümantasyon sistemidir.

Temel Özellikleri
man pages gibi komutların nasıl çalıştığını anlatır, fakat daha detaylı ve dallanmış menüler şeklindedir.

GNU yazılımlarının çoğu (örn. coreutils, gcc, bash) info formatında ek belgelerle birlikte gelir.

Sayfalar hyperlink mantığıyla bağlanmıştır — bir konudan başka bir konuya atlayabilirsiniz.

man sayfaları kısa referans gibi, info sayfaları ise daha çok “kitap” gibidir.

Kullanımı
Bir komutun info sayfasını açmak için:
info komut_adi
Örneğin:
info ls
Info içinde gezinme:

n → next (sonraki bölüm)

p → previous (önceki bölüm)

u → up (üst menüye çık)

q → quit (çıkış)

Farkı — man vs info
Özellik	man pages	info pages
İçerik	Kısa ve doğrudan	Daha detaylı, açıklamalı
Format	Tek parça metin	Bölümlere ayrılmış, linklerle geçiş var
Kullanım Amacı	Hızlı referans	Ayrıntılı kılavuz
Hedef Kitlesi	Komutu bilen ama söz dizimini hatırlamayan	Komutu derinlemesine öğrenmek isteyen

# Relative path (göreceli yol) ve absolute path (mutlak yol) kavramlarını dosya/dizin konumlarını belirtirken kullanırız.

1. Absolute Path (Mutlak Yol)
Kök dizinden (/ — root) başlayarak dosyanın/dizinin tam adresini yazar.

Başında her zaman / olur.

Nerede olursan ol, o dosyaya ulaşmak için aynı yolu kullanırsın.

Örnek (Linux):
/home/feyyaz/Documents/notes.txt
/etc/nginx/nginx.conf

Örnek (Windows):
C:\Users\Feyyaz\Documents\notes.txt
D:\Projects\Java\Main.java

Avantajı: Her zaman kesin adres verir.
Dezavantajı: Uzun olabilir.

2. Relative Path (Göreceli Yol)
Bulunduğun mevcut dizine (current working directory) göre dosyanın yolunu verir.

/ ile başlamaz (Linux’ta).

Kısa ve pratiktir, ama çalıştığın konuma bağlıdır.

Örnek:
Varsayalım şu an /home/feyyaz dizinindesin:
Documents/notes.txt
Yukarıdaki yol, aslında şu absolute path’e karşılık gelir:

/home/feyyaz/Documents/notes.txt
Göreceli yol özel kısayollar:

. → Bulunduğun dizin (current directory)

.. → Bir üst dizin (parent directory)

Örnek:
./notes.txt      → bulunduğun dizindeki notes.txt
../notes.txt     → bir üst dizindeki notes.txt
../../file.txt   → iki üst dizindeki file.txt
Kısaca Fark
Özellik	Absolute Path	Relative Path
Nereden başlar	Kök dizinden (/ veya C:\)	Mevcut çalışma dizininden
/ ile başlar?	Evet (Linux’ta)	Hayır
Bağımsız mı?	Evet	Hayır (konuma bağlı)
Kullanım amacı	Kesin adres vermek	Kısa ve pratik erişim

Absolute path: /home/user/documents/pictures → her zaman kökten başlar.

Relative path: pictures veya ../downloads → bulunduğun yerden başlar.