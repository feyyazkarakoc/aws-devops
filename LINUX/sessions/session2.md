
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