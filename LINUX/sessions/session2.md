
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

# mkdir ./techproeducation/lesson ./techproeducation/materials
mkdir → make directory (yeni klasör oluşturur).

. (nokta) → geçerli dizini ifade eder.

Senin örneğinde ./techproeducation demek:
“Şu anda bulunduğum dizinin altında techproeducation klasörüne git.” (Aslında gitmeden oluşturur. cd dememize gerek kalmadan oluşturur.)

./techproeducation/lesson → geçerli dizinin içinde techproeducation klasörünün altında lesson adında bir klasör oluşturur.

./techproeducation/materials → aynı şekilde techproeducation altında materials adında bir klasör oluşturur.

Dikkat:

Eğer techproeducation klasörü önceden yoksa, bu komut hata verir çünkü mkdir varsayılan olarak eksik ara klasörleri otomatik oluşturmaz.

Eksik ara klasörleri de oluşturmasını istersen -p parametresi gerekir:
mkdir -p ./techproeducation/lesson ./techproeducation/materials

# ping komutu, bir bilgisayar ile başka bir bilgisayar (veya sunucu) arasındaki ağ bağlantısını test etmek için kullanılır.
Nasıl çalışır?
ping, hedefe ICMP (Internet Control Message Protocol) Echo Request paketleri gönderir.

Hedef cihaz cevap verirse (Echo Reply), bağlantının çalıştığını ve ne kadar sürede cevap aldığını gösterir.

Bu süreye gecikme süresi (latency) denir.

Temel Kullanım
ping google.com
Bu komut, google.com adresine veri paketleri gönderir ve yanıt sürelerini milisaniye cinsinden gösterir.

Örnek çıktı
PING google.com (142.250.183.78) 56(84) bytes of data.
64 bytes from lhr25s05-in-f14.1e100.net (142.250.183.78): icmp_seq=1 ttl=117 time=22.4 ms
64 bytes from lhr25s05-in-f14.1e100.net (142.250.183.78): icmp_seq=2 ttl=117 time=23.1 ms
icmp_seq → Gönderilen paket numarası

ttl (time-to-live) → Paketin geçerli olacağı maksimum “atlama” sayısı

time → Yanıtın gelme süresi (ms)

Önemli kullanım amaçları
Ağ çalışıyor mu? — İnternete ya da başka bir cihazın IP’sine ulaşabiliyor musun?

Gecikme süresi ölçümü — Özellikle oyunlarda ve VoIP uygulamalarda önemli.

Paket kaybı testi — Eğer bazı paketler geri dönmezse bağlantı sorunları olabilir.

Not:
Bazı sunucular güvenlik amacıyla ICMP’yi kapatır, böylece ping yanıt vermez. Bu, mutlaka sunucunun kapalı olduğu anlamına gelmez.

# ssh komutu, uzak bir bilgisayara veya sunucuya güvenli bir şekilde bağlanmak için kullanılan bir komuttur.
Açılımı: Secure Shell (Güvenli Kabuk).

Ne işe yarar?
Bir uzak makinenin terminaline bağlanmanı sağlar.

Tüm veri transferi şifrelenir → Kullanıcı adı, parola, gönderilen komutlar güvenli olur.

DevOps, cloud, Linux sistem yönetimi, yazılım geliştirme gibi alanlarda sıkça kullanılır.

Temel kullanım şekli
ssh kullanıcı_adı@sunucu_ip_adresi
Örneğin:

ssh ec2-user@34.228.165.66
Bu komut, IP’si 34.228.165.66 olan sunucuya ec2-user kullanıcısıyla bağlanır.

Özel anahtar ile bağlanma
Bulut sistemlerde (AWS EC2, Google Cloud vb.) genellikle private key (.pem) dosyası kullanılır:

ssh -i ~/.ssh/mykey.pem ec2-user@34.228.165.66
-i → Kullanılacak özel anahtar dosyasını belirtir.

Örnek senaryo
AWS EC2 üzerinde bir Linux sunucu açtın.

Sana bir IP adresi ve .pem anahtar dosyası verildi.

Kendi bilgisayarından bu komutla bağlanırsın:

ssh -i ~/.ssh/mykey.pem ec2-user@EC2_IP_ADDRESS
Bağlandıktan sonra sanki o bilgisayarın başındaymış gibi komut yazabilirsin.

SSH, ping gibi sadece test etmez, direkt olarak kontrol imkanı sağlar.
Ping → Bağlantı var mı?
SSH → Bağlandım, artık komut çalıştırabilirim.

# wget komutu, internet üzerinden (HTTP, HTTPS, FTP) dosya indirmek için kullanılan bir komuttur.
Adı World Wide Web + Get kelimelerinden gelir.

Ne işe yarar?
İnternetteki bir dosyayı terminalden indirmeni sağlar.

Arka planda çalışabilir, bağlantı koptuğunda devam edebilir.

Otomasyon, script, sunucu kurulumu gibi işlerde çok kullanılır.

Basit kullanım
wget URL
Örneğin:
wget https://example.com/dosya.zip
Bu komut, dosya.zip dosyasını bulunduğun dizine indirir.

Önemli parametreler
Parametre	Açıklama
-O dosya_adi	İndirilen dosyayı farklı bir adla kaydeder.
-c	Yarım kalmış indirmeyi devam ettirir.
-b	Arka planda indirir (background).
--limit-rate=200k	İndirme hızını sınırlar.
-r	Web sitesini recursive (tüm alt bağlantılarla) indirir.

Örnekler
1. Farklı adla kaydetme
wget -O kurs.pdf https://example.com/egitim.pdf
egitim.pdf olarak gelen dosyayı kurs.pdf adıyla kaydeder.

2. Yarım kalan indirmeye devam etme
wget -c https://example.com/dosya.zip

3. Arka planda indirme
wget -b https://example.com/video.mp4
wget, DevOps’ta sunucuya internetten paket veya script çekmek için çok kullanılır.
Mesela EC2’da bir kurulum script’ini doğrudan indirip çalıştırabilirsin:

wget https://example.com/install.sh && bash install.sh

# curl komutu, internet üzerinden veri indirmek veya göndermek için kullanılan, çok yönlü bir komuttur.
Adı Client URL kelimelerinden gelir.

wget daha çok “dosya indirme” odaklıyken, curl hem indirme hem de API istekleri gibi veri gönderme/çekme işlemlerinde kullanılır.

Ne işe yarar?
HTTP, HTTPS, FTP, SFTP, SCP gibi birçok protokolü destekler.

Web sitelerinden dosya indirir.

API’lere GET, POST, PUT, DELETE istekleri gönderebilir.

Header bilgilerini inceleyebilir.

Form verisi gönderebilir.

Basit kullanım
curl URL
Örneğin:
curl https://example.com
Web sayfasının HTML içeriğini ekrana basar.

Önemli parametreler
Parametre	Açıklama
-o dosya	Çıktıyı ekrana değil, dosyaya yazar.
-O	İndirilen dosyayı orijinal adıyla kaydeder.
-L	Yönlendirmeleri takip eder.
-I	Sadece HTTP header bilgilerini alır.
-d	POST isteği ile veri gönderir.
-X	HTTP metodu belirtir (GET, POST, PUT, DELETE).

Örnekler
1. Dosya indirme

curl -O https://example.com/dosya.zip

2. Yönlendirmeleri takip ederek indirme

curl -L -O https://example.com/dosya.zip

3. HTTP header bilgilerini görüntüleme

curl -I https://example.com

4. Bir API’ye POST isteği atma

curl -X POST -d "kullanici=ali&parola=1234" https://example.com/login

5. JSON veri gönderme

curl -X POST -H "Content-Type: application/json" \
-d '{"ad":"Ali","yas":25}' https://api.example.com/kullanicilar

curl, özellikle DevOps ve Cloud ortamlarında, API testi, web servisleri ile konuşma ve otomasyon scriptleri için vazgeçilmezdir.
wget sadece dosya indirirken iş görürken, curl veri alışverişinin “İsviçre çakısı” gibidir. 

# unzip komutu

Ne yapar?
.zip uzantılı dosyaları açar (içeriğini çıkarır).

Temel kullanım

unzip dosya.zip


Bu komut dosya.zip içindeki dosyaları bulunduğun klasöre açar.

Örnekler

unzip dosya.zip -d hedef_klasor


→ .zip dosyasını hedef_klasor içine çıkarır.

unzip -l dosya.zip


→ Sadece içeriği listeler, açmaz.

Not:
unzip komutu Linux’ta her zaman yüklü gelmeyebilir.
Ubuntu/Debian’da yüklemek için:

sudo apt install unzip

# tar komutu

Ne yapar?
tar aslında bir arşivleme komutudur (ZIP gibi ama daha çok Linux’ta kullanılır).
Tek başına sıkıştırmaz, ama genellikle gzip (.tar.gz) veya bzip2 (.tar.bz2) ile birlikte çalışır.

Temel parametreler:

c → create (oluştur)

x → extract (çıkart)

v → verbose (açık açık listele)

f → file (dosya adı belirt)

z → gzip ile sıkıştır / aç

j → bzip2 ile sıkıştır / aç

Örnekler

Arşiv oluşturma

tar -cvf arsiv.tar klasor/


→ klasor/ içeriğini arsiv.tar dosyasına toplar (sıkıştırmaz).

Gzip ile sıkıştırma

tar -czvf arsiv.tar.gz klasor/


→ klasor/ içeriğini gzip ile sıkıştırılmış .tar.gz dosyası yapar.

Arşivi açma

tar -xvf arsiv.tar


→ .tar dosyasını çıkarır.

Gzip’li arşivi açma

tar -xzvf arsiv.tar.gz


→ .tar.gz dosyasını çıkarır.

Not:
.tar.gz dosyası hem arşiv hem sıkıştırma içerir; .tar ise sadece arşivdir.

Kısaca fark:

unzip → sadece .zip dosyaları açar.

tar → .tar, .tar.gz, .tar.bz2 gibi Linux’ta sık kullanılan arşivleri yönetir.