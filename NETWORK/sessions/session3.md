
# Ethernet Protokolü Nedir?

Ethernet, bir ağ iletişim standardıdır.

Özellikle yerel alan ağlarında (LAN) en çok kullanılan teknolojidir.

IEEE 802.3 standardı altında tanımlanmıştır.

Görevi: Aynı ağdaki cihazların (bilgisayar, yazıcı, switch, modem) birbirine veri göndermesini sağlar.

Yani Ethernet = "LAN’da veri nasıl paketlenecek, adreslenecek ve iletilecek" kurallarının tamamıdır.

Ethernet’in Temel Özellikleri

Katmanı:

OSI modelinde 2. katman (Veri İletim Katmanı) protokolüdür.

Fiziksel bağlantıyı da içerdiği için 1. katmanla da yakından ilişkilidir.

Adresleme:

Cihazları tanımak için MAC adresi (48 bit, benzersiz donanım adresi) kullanır.

Her cihazın ağ kartında (NIC) yazılıdır.

Çalışma Mantığı:

Veri frame (çerçeve) adı verilen yapılara bölünür.

Frame içinde: hedef MAC, kaynak MAC, veri, hata kontrol kodu bulunur.

Cihazlar bu çerçeveleri okuyarak doğru hedefe gönderir.

Hızları:

İlk Ethernet: 10 Mbps

Fast Ethernet: 100 Mbps

Gigabit Ethernet: 1 Gbps

10/40/100 Gbps Ethernet → günümüzde veri merkezlerinde

Ortam:

Genelde UTP kablo (bakır, RJ-45 uçlu)

Ya da fiber optik kablo üzerinden çalışır.

Ethernet Protokolünün Görevleri

Aynı ağdaki cihazları adreslemek (MAC ile)

Veriyi frame’lere bölmek ve göndermek

Hedefe ulaşmayan/kayan veriyi hata kontrolü ile tespit etmek (CRC)

Çakışma (collision) durumlarını yönetmek (özellikle eski hub tabanlı ağlarda)

Basit Bir Örnek

Sen bilgisayarından yazıcıya dosya gönderiyorsun.

Ethernet protokolü:

Senin PC’nin MAC adresini kaynak olarak ekler.

Yazıcının MAC adresini hedef olarak ekler.

Dosyayı küçük frame’lere böler.

Switch bu frame’leri alır, hedef MAC adresine göre yönlendirir.

Yazıcı doğru veriyi alır ve yazdırır.

Bu süreç hep Ethernet protokolünün kuralları ile yapılır.

Özet:
Ethernet protokolü, LAN içindeki cihazların MAC adresleriyle birbirini tanıyıp, veriyi frame’ler halinde göndermesini sağlayan, IEEE 802.3 standardı ile tanımlanmış en yaygın ağ iletişim protokolüdür.

# Ethernet protokolü hem bilgisayara hem switche hem yazıcıya mı tanımlanmış?
Ethernet protokolü “sadece bilgisayarda çalışıyor” ya da “sadece switch biliyor” gibi bir şey değil.
Ağa bağlı olan tüm cihazların ortak dili.

Ethernet protokolü kimlerde “var”?

Bilgisayar / Laptop / Telefon

Hepsinin içinde bir NIC (Network Interface Card) yani ağ kartı vardır.

Bu kartta Ethernet protokolü donanım + sürücü ile uygulanmıştır.

Dolayısıyla bilgisayar Ethernet frame’lerini oluşturur ve gönderir.

Switch

Switch, Ethernet çerçevelerini (frame) okur, hedef MAC adresine bakar, doğru porta yollar.

Yani switch de Ethernet protokolünü bilir, çünkü onun işi frame yönlendirmektir.

Yazıcı (Network printer)

Ağ bağlantısı varsa, içinde ağ arabirimi (Ethernet kartı veya Wi-Fi modülü) vardır.

Bu arabirim de Ethernet protokolünü konuşur.

Böylece bilgisayardan gelen frame’i alır, “bu benim MAC adresim” der, içindeki veriyi çıkarıp işler.

Modem / Router

Onlarda da Ethernet portları vardır.

Ethernet frame’lerini alıp işleyebilir, yönlendirebilir.

Yani Ethernet Protokolü:

Tüm cihazlara “ortak kural kitabı” olarak tanımlanmıştır.

Bilgisayar frame hazırlar.

Switch yönlendirir.

Yazıcı alır ve işler.

Hepsi aynı dili konuştuğu için iletişim sorunsuz olur.

Özet:
Ethernet protokolü sadece tek bir cihaza özel değildir.
Ağa bağlı her cihazda (bilgisayar, switch, modem, yazıcı, kamera, IoT cihazı vs.) uygulanmıştır. Bu sayede herkes aynı dili konuşur.

# Ethernet protokolünü OSI modeli kapsamında detaylıca açıklayayım:
Ethernet ve OSI Modeli
Ethernet OSI Layer 2 (Data Link Layer) ve Layer 1 (Physical Layer)'da çalışır.
1. Çerçeveleme (Framing)
Ethernet verileri frame (çerçeve) halinde paketler:
Ethernet Frame Yapısı (64-1518 byte):
┌─────────────┬─────────┬────────┬──────────┬─────┬─────┐
│  Preamble   │Dest MAC │Src MAC │Type/Len  │Data │ FCS │
│   8 byte    │ 6 byte  │6 byte  │ 2 byte   │46-  │4byte│
│             │         │        │          │1500 │     │
└─────────────┴─────────┴────────┴──────────┴─────┴─────┘
Frame Alanları:

Preamble: Senkronizasyon için
Destination MAC: Hedef MAC adresi
Source MAC: Kaynak MAC adresi
Type/Length: Protokol türü veya veri uzunluğu
Data: Gerçek veri (IP paketi vs.)
FCS: Hata kontrolü (Frame Check Sequence)

2. Fiziksel Ortam Erişimi
Layer 1 (Physical) özellikleri:
Ethernet Türleri:
10BASE-T    → 10 Mbps,  UTP kablo
100BASE-TX  → 100 Mbps, UTP kablo  
1000BASE-T  → 1 Gbps,   UTP kablo
10GBASE-T   → 10 Gbps,  UTP kablo
Sinyal türleri:

Elektriksel: UTP/STP kablolar
Optik: Fiber optik kablolar

3. MAC Adreslemesi
48-bit fiziksel adres:
javaMAC Adresi: AA:BB:CC:DD:EE:FF
           │    │         │
           │    │         └── Device Unique ID (24 bit)
           └────┴── Vendor ID (24 bit)

Örnek: 
08:00:27:12:34:56
│
└── VirtualBox vendor ID
MAC Address özellikleri:

Globally unique (dünya çapında benzersiz)
Layer 2 iletişim için kullanılır
Switch'ler MAC tablosu tutar

4. CSMA/CD (Collision Detection)

Eski Ethernet'te kullanılan çoklu erişim yöntemi:
javaCSMA/CD Algoritması:

1. LISTEN: "Hat boş mu?" kontrol et
2. SEND: Boşsa veriyi gönder  
3. MONITOR: Gönderirken çakışma var mı?
4. COLLISION?: 
   - Varsa → JAM signal gönder
   - Random backoff bekle
   - Tekrar dene
   - Yoksa → İletim başarılı
Modern Ethernet'te:

Full-duplex kullanılır
Switch tabanlı
CSMA/CD artık gereksiz (çakışma olmaz)

5. Hız ve Esneklik
Ethernet evrim sürecinde:
1980'ler → 10 Mbps   (10BASE-T)
1990'lar → 100 Mbps  (Fast Ethernet)  
2000'ler → 1 Gbps    (Gigabit Ethernet)
2010'lar → 10 Gbps   (10 Gigabit)
2020'ler → 100+ Gbps (Ultra-high speed)
Auto-negotiation: Cihazlar otomatik en yüksek hızı belirler.

6. Standartlar ve Uyumluluk
IEEE 802.3 Standart Ailesi:
802.3      → Original Ethernet (10 Mbps)
802.3u     → Fast Ethernet (100 Mbps)
802.3ab    → Gigabit over UTP
802.3ae    → 10 Gigabit Ethernet
802.3bz    → 2.5G/5G over existing UTP

7. Yaygın Kullanım ve Uygulamalar

LAN Ağları:
Tipik ofis ağı
Switch ← Ethernet → PC/Laptop
Switch ← Ethernet → Server  
Switch ← Ethernet → Printer
Switch ← Ethernet → Access Point
Veri Merkezi:

Server-to-server iletişim
Storage network bağlantıları
High-performance computing

OSI Katmanlarıyla İlişki:
Layer 7 (Application)  → HTTP, FTP, etc.
Layer 6 (Presentation) → SSL/TLS
Layer 5 (Session)      → TCP Sessions  
Layer 4 (Transport)    → TCP/UDP
Layer 3 (Network)      → IP Protocol
Layer 2 (Data Link)    → ETHERNET ←←← Ana katman
Layer 1 (Physical)     → ETHERNET ←←← Fiziksel medya

Ethernet'in başarı faktörleri:

Basit ve güvenilir
Maliyet etkin
Geniş vendor desteği
Geriye uyumluluk
Sürekli hız artışı

Ethernet, LAN ağlarının %90'ından fazlasında kullanılan dominant teknolojidir.

# TCP Nedir? - Günlük Hayat Benzetmesi
TCP = Güvenilir Posta Sistemi gibi
Normal posta göndermek vs Kayıtlı/Taahhütlü posta göndermek arasındaki fark gibi düşünün:

UDP = Normal posta (attın gitti, gelip gelmediğini bilmiyorsun)
TCP = Taahhütlü posta (alındı belgesi alıyorsun, güvenilir)

1. Güvenilir Protokoldür. 
Mektup Gönderme Örneği:
Ali'den Veli'ye uzun bir mektup gönderiyorsun:

Normal POST (UDP gibi):
- Mektubu attın
- Gitti mi, gelmedi mi bilmiyorsun
- Kaybolursa haberin olmaz

TCP POST (Güvenilir):  
- Mektubu parçalara böl (sayfa numarası ver)
- Her parça için "alındı" belgesi iste
- Kaybolanları tekrar gönder
Bilgisayarda Nasıl Çalışır:
Büyük dosya gönderiyorsun
"Merhaba Dünya Bu Çok Uzun Bir Mesaj"

TCP bunu böyle parçalar:
Parça 1: "Merhaba Dünya" (Numara: 1)
Parça 2: "Bu Çok Uzun"   (Numara: 2)  
Parça 3: "Bir Mesaj"     (Numara: 3)

Her parça için onay bekler:
Gönder → Parça 1 → "Aldım 1. parçayı"
Gönder → Parça 2 → "Aldım 2. parçayı"
Gönder → Parça 3 → CEVAP YOK!
Tekrar Gönder → Parça 3 → "Aldım 3. parçayı"

2. Akış Kontrolü  sağlar.
Su Muslugu Örneği:
Musluktan su akan → Kovaya dolduruluyor

Kova dolmaya başlıyor:
"Yavaşla, kova dolacak!" 

Kova neredeyse dolu:
"Dur, kova dolu!"

Kova boşaltıldı:
"Tamam, devam edebilirsin"
Bilgisayarda:
Gönderen: "1000 byte gönderiyorum!"
Alıcı: "Dur! Sadece 500 byte alan kaldı"
Gönderen: "Tamam, 500 byte gönderiyorum"

Alıcı işledi, boşaldı:
Alıcı: "1500 byte daha alabilirim"
Gönderen: "Harika! Kalan verileri gönderiyorum"

3. Bağlantı Tabanlı (Connection-Oriented) protokoldür.
Telefon Görüşmesi Örneği:
SMS (UDP gibi):           Telefon Görüşmesi (TCP gibi):
- Mesaj gönder            - Numarayı çevir  
- Gitti mi bilmiyorsun    - "Alo?" "Alo Ali, ben Veli"
- Tek yönlü              - "Merhaba Veli!"
                         - Konuşma başlar
                         - "Hoşçakal" "Hoşçakal"
                         - Telefonu kapat
Bilgisayarda:
TCP Bağlantı kurma
Client: "Bağlanmak istiyorum"
Server: "Tamam, bağlan"  
Client: "Teşekkürler, bağlandım"
→ Artık konuşabilirler

// Veri alışverişi
Client: "Merhaba"
Server: "Merhaba, nasılsın?"
Client: "İyiyim, sen?"

// Bağlantı kapama  
Client: "Kapatalım bağlantıyı"
Server: "Tamam, kapatıyorum"
Client: "Ben de kapattım"

4. Üçlü El Sıkışma Yöntemini Kullanır.(three way handshake)
Restaurant'ta Rezervasyon:
1. Sen: "Akşam 8'de masa istiyorum" (SYN)
2. Restaurant: "Tamam, 8'de masa ayırttım, gelecek misin?" (SYN-ACK)  
3. Sen: "Evet, kesinlikle geliyorum" (ACK)
→ Rezervasyon tamamlandı!
Bilgisayarda Adım Adım:
java// 1. Adım - Client başlatıyor
Client → Server: 
"Merhaba Server, bağlanmak istiyorum" 
(SYN paketi gönderir)

// 2. Adım - Server kabul ediyor
Server → Client:
"Merhaba Client, tamam bağlan, ben de bağlanıyorum"
(SYN-ACK paketi gönderir)

// 3. Adım - Client onaylıyor  
Client → Server:
"Teşekkürler, bağlantı hazır!"
(ACK paketi gönderir)

→ Artık veri göndermeye başlayabilirler
Gerçek Hayat Örneği - WhatsApp:
javaWhatsApp mesaj gönderdiğinde:

1. Telefon WhatsApp sunucusuna TCP bağlantısı kurar
   (Üçlü el sıkışma gerçekleşir)

2. "Merhaba nasılsın?" mesajını gönderir
   TCP bunu küçük parçalara böler

3. Her parça sunucuya güvenilir şekilde gönderilir  
   (Kaybolanlar tekrar gönderilir)

4. Server "✓" işareti gönderir (mesaj ulaştı)

5. Karşı taraf okuyunca "✓✓" mavi olur

6. Konuşma bitince bağlantı kapanır
TCP vs UDP - Basit Karşılaştırma:
java               TCP                    UDP
Benzetme:    Telefon görüşmesi      SMS gönderme
Güvenlik:    Çok güvenli           Güvensiz
Hız:         Yavaş                 Hızlı  
Kullanım:    WhatsApp mesaj        Online oyun
             Web sayfası           YouTube video
             Email                 DNS sorgu
             Dosya indirme         Canlı yayın
Özet:

TCP: Güvenilir, yavaş, garanti var
UDP: Hızlı, güvensiz, garanti yok

Spring Boot uygulamanız HTTP kullandığında, altta TCP çalışır. Bu yüzden web sayfanız güvenilir şekilde yüklenir!

# ARP Nedir?

ARP = Address Resolution Protocol
Görevi: IP adresini MAC adresine çevirmek.

Çünkü:

Senin bilgisayarın → “192.168.1.102 adresine veri göndereceğim” diye düşünür.

Ama Ethernet (2. katman) IP adresini tanımaz, sadece MAC adresiyle çalışır.

O zaman:

ARP, IP → MAC çevirisi yapar.

Yani “Bu IP’nin MAC adresi kimde?” diye sorar.

🔹 Hangi Katmanda Çalışır?

OSI Layer 2,5 gibi düşünülür.

Aslında IP adresi (3. katman) ile MAC adresi (2. katman) arasında köprü kurar.

Bu yüzden bazı kaynaklarda Layer 2 (Data Link), bazılarında Layer 3 (Network) der.
Doğrusu: 2 ve 3 arasında çalışan yardımcı bir protokol.

🔹 ARP Nasıl Çalışır?

Bilgisayarın 192.168.1.1 (gateway) ile konuşmak istiyor.

ARP tablosunda bakar: “192.168.1.1’in MAC adresi elimde var mı?”

Yoksa → ARP Request yayınlar (broadcast, FF:FF:FF:FF:FF:FF).

“192.168.1.1 kim? MAC adresini söyler misin?”

Modem cevaplar (ARP Reply): “Benim MAC’im: aa:bb:cc:dd:ee:ff”

Bilgisayar bunu ARP tablosuna kaydeder.

🔹 Hangi Cihazlar Kullanır?

ARP her IP kullanan cihazda vardır:

PC, laptop, telefon

Switch (Layer 3 switchlerde)

Router

Modem

Sunucu

Yani IP üzerinden haberleşen herkesin ihtiyacı var.

# Neden http server deniliyor, bu fiziksel bir server mi?
“HTTP server” lafı ilk duyulduğunda çoğu kişinin kafası karışıyor çünkü hem fiziksel cihaz hem de yazılım anlamına gelebiliyor. 

🔹 1. HTTP Server Ne Demek?

HTTP server = HTTP protokolünü kullanarak istemcilerin (tarayıcı, uygulama) isteklerine cevap veren yazılım.

HTTP (HyperText Transfer Protocol) → Web sayfalarının tarayıcıya aktarılması için kullanılan protokol.

Server → Bu protokolü anlayan ve cevap üreten yazılım.

Yani “HTTP server” dediğimiz şey, bir yazılımdır (örn: Apache, Nginx, Microsoft IIS).

🔹 2. HTTP Server Nerede Çalışır?

HTTP server yazılımı genellikle:

Fiziksel bir sunucuda (örneğin bir veri merkezinde duran güçlü bilgisayar)

veya sanal bir sunucuda (cloud/VPS)
çalışır.

Yani HTTP server kendi başına fiziksel bir cihaz değil, bir programdır. Ama o program bir sunucuda (donanımda) çalıştığı için bazen halk arasında “server” denildiğinde donanım kastedilir.

🔹 3. Örnek

Sen tarayıcıda https://example.com yazıyorsun.

Tarayıcı (client) → HTTP isteği gönderiyor (TCP 80 veya HTTPS ise TCP 443).

Karşı tarafta Nginx veya Apache HTTP Server yazılımı o isteği alıyor.

Server yazılımı sana web sayfasını geri gönderiyor.

Burada:

Donanım: Fiziksel bilgisayar (sunucu)

Yazılım: HTTP server (Apache, Nginx)

Protokol: HTTP

Özet:

HTTP server = yazılım

Ama bu yazılım mutlaka bir sunucu donanımında çalışır.

O yüzden “HTTP server” bazen donanımı da kasteder gibi kullanılır ama teknik olarak protokolü çalıştıran yazılım demektir.

# FTP protokolünü açıklar mısın?
FTP (File Transfer Protocol) bilgisayar ağlarında çok kullanılan temel protokollerden biri.

🔹 1. FTP Nedir?

FTP (File Transfer Protocol) = Dosya transferi için geliştirilmiş, çok eski (1970’lerden beri kullanılan) bir Uygulama Katmanı protokolüdür (OSI Layer 7).

Görevi:

Bir istemci (client) ile bir sunucu (server) arasında dosya yüklemek (upload) ve dosya indirmek (download).

🔹 2. FTP Nasıl Çalışır?

FTP, TCP/IP üzerine kurulu bir protokoldür. Yani:

TCP kullanır (UDP değil) → çünkü güvenilir (veri kaybolmaz) transfer gerekir.

Port 21 → kontrol kanalı (komutlar burada gönderilir: giriş yap, dosya listele vs.)

Port 20 → veri kanalı (dosyaların kendisi buradan akar).

Yani FTP’de iki ayrı bağlantı vardır:

Kontrol Kanalı (21) → “Şu dosyayı indir”, “Şu klasörü listele” gibi komutlar.

Veri Kanalı (20) → İstediğin dosyanın içeriği.

🔹 3. Çalışma Senaryosu

Sen FTP istemcisi açarsın (örn: FileZilla veya terminalden ftp).

Sunucuya bağlanırsın:

ftp://ftp.sunucu.com
kullanıcı: feyyaz
şifre: ****


Sunucu seni kimlik doğrulama (username & password) ile tanır.

Sen komut gönderirsin (21. port üzerinden):

LIST   → klasörleri listele
GET x.txt → x.txt dosyasını indir
PUT y.txt → y.txt dosyasını yükle


Sunucu veri kanalından (20. port) sana dosya akıtır.

🔹 4. FTP Türleri

Klasik FTP → şifreler dahil her şey düz metin (plain text) gönderilir → güvenlik zaafı.

FTPS (FTP Secure) → SSL/TLS ile şifreli.

SFTP (SSH File Transfer Protocol) → FTP ile karıştırılır ama aslında tamamen farklıdır; SSH üzerinden dosya transferidir, port 22 kullanır.

🔹 5. Nerelerde Kullanılır?

Web sitelerine dosya yüklemek (webmaster’lar FTP ile site dosyalarını server’a atar).

Sunucudan büyük veriler indirmek.

Şirket içi dosya paylaşımları.

Ama:
Güvenlik sorunları yüzünden artık çoğu yerde SFTP veya HTTPS tabanlı transfer tercih ediliyor.

Özet:
FTP → Dosya transferi protokolü

OSI Katmanı: 7 (Application)

Port: 21 (kontrol), 20 (veri)

TCP kullanır

Türleri: FTP, FTPS, SFTP


# FTP server dendiğinde ne anlamalıyım?

🔹 1. FTP Server Nedir?

Bir FTP server, üzerinde FTP protokolünü çalıştıran bir yazılımın kurulu olduğu bilgisayardır (sunucu).

Görevi:

İstemcilerden gelen FTP bağlantılarını kabul etmek (port 21 üzerinden).

Kullanıcı kimlik doğrulaması yapmak (kullanıcı adı/şifre).

İsteyenlere dosya indirme (download) ve yükleme (upload) hizmeti vermek.

Yani FTP server, senin dosya deposu gibi düşünebileceğin bir sistemdir.

🔹 2. FTP Server’ın Yapısı

Fiziksel olarak: Bu genelde bir sunucu bilgisayarıdır (datacenter’da duran güçlü bir makine). Ama aslında herhangi bir PC de FTP server olabilir (örn: Windows veya Linux’ta FileZilla Server kurarsan).

Mantıksal olarak: Bir program (daemon/service) sürekli çalışır ve “Port 21’den gelen bağlantı var mı?” diye dinler.


# SMTP zaten protokol, o zaman TCP’yi nasıl kullanıyor?

Evet, SMTP (Simple Mail Transfer Protocol) bir uygulama katmanı protokolüdür (OSI Layer 7).
Ama şunu unutma:
Uygulama katmanındaki protokoller kendi başlarına veri taşıyamazlar.

SMTP: “E-mail göndereceğim, mesaj şu” der.

Ama bu mesajın bilgisayardan karşı tarafa taşınması için alt katmanlara ihtiyaç vardır.

Bu yüzden:

SMTP mesajını Taşıma katmanına verir.

Taşıma katmanında TCP kullanılır (TCP güvenilir iletişim sağlar).

TCP de veriyi IP üzerinden yollar.

IP de veriyi Ethernet / Wi-Fi üzerinden taşır.

Yani SMTP, TCP üzerinden çalışır.
Bu yüzden “SMTP TCP kullanır” deriz.

# Bir protokol başka protokolü kullanır mı?

Kesinlikle evet. İşte OSI katmanları bunun için vardır.

Örnek: Gmail’den mail gönderiyorsun:

SMTP (uygulama katmanı) → “Bu mail Ali’ye gitsin.”

TCP (taşıma katmanı) → “Bu veriyi güvenli, sırayla ve hatasız gönder.”

IP (ağ katmanı) → “Bu veriyi şu IP adresine yönlendir.”

Ethernet/Wi-Fi (fiziksel + veri katmanı) → “Bu veriyi kablo veya havadan gönder.”

Yani üst katman protokolü, alt katman protokolünü kullanır.


# Port numarası, sadece “hangi uygulama/protokol çalışıyor” bilgisini verir.

Örn:

80 → HTTP (TCP kullanır)

443 → HTTPS (TCP kullanır)

25 → SMTP (TCP kullanır)

53 → DNS (hem UDP hem TCP kullanabilir)

67-68 → DHCP (UDP kullanır)

Yani port = kapı numarası
“TCP mi UDP mi” = o kapının arkasında verinin nasıl taşındığı.


# DHCP (Dynamic Host Configuration Protocol)

Görevi: Cihaza IP, Subnet Mask, Gateway, DNS verir.

Örnek: Bilgisayarı açıyorsun → DHCP’den otomatik 192.168.1.105 alıyorsun.

Çalışma katmanı: Uygulama Katmanı (Layer 7), ama UDP port 67/68 üzerinden çalışır.

NAT yapmaz 

Sadece “IP dağıtır”.

🔹 2. NAT (Network Address Translation)

Görevi: Özel IP ↔ Genel IP çevirisi

Örnek: Senin bilgisayarın 192.168.1.105 → modem NAT ile 88.245.xx.xx yapar.

NAT yapan: Modem / Router’dır.

Çalışma katmanı: Layer 3 (Network)

🔹 3. ARP (Address Resolution Protocol)

Görevi: IP → MAC çözmek.

Yani LAN içinde paket gönderebilmek için şart.

Port kullanmaz, TCP/UDP değildir.

Çalışma katmanı: 2 ile 3 arasında köprü

Peki ARP nerede kullanılır?

LAN içinde: Bilgisayarın gateway (192.168.1.1) ile konuşmak ister → önce ARP yapar, “Bu IP hangi MAC’te?” der.

NAT’la ilişkisi: NAT öncesinde LAN tarafında paket fiziksel adrese (MAC) gönderilebilmesi için ARP şarttır.

Yani NAT’tan önce ARP çalışır.

DHCP’yle ilişkisi: DHCP server IP dağıtırken de ARP kullanır → “Bu IP boş mu, çakışma var mı?” diye ARP probe atabilir.

🔹 Özet

DHCP: IP dağıtır.

ARP: IP’nin MAC karşılığını bulur.

NAT: Özel IP’yi genel IP’ye çevirir.

Yani NAT’ı DHCP yapmaz, NAT’ı router/modem yapar.
ARP ise LAN’da iletişim kurabilmek için her zaman devrededir, DHCP veya NAT’tan bağımsızdır ama onlarla birlikte çalışır.

# SMTP (Simple Mail Transfer Protocol) en basit haliyle e-posta gönderme protokolüdür.

Açılımı: Simple Mail Transfer Protocol (Basit Posta Aktarım Protokolü).

Katman: OSI’nin Uygulama Katmanı (Application Layer) protokolüdür.

Görevi: E-posta istemcisinden (Outlook, Thunderbird gibi) veya başka bir e-posta sunucusundan mail gönderimini sağlar.

Çalışma Yapısı:

Bir kullanıcı mail gönderdiğinde SMTP, o maili alır ve hedef mail sunucusuna ulaştırmak için çalışır.

Eğer hedef sunucuya doğrudan erişemiyorsa, aradaki SMTP sunucularına yönlendirerek iletir (relay).

Bağlantı:

Genellikle TCP kullanır (UDP değil).

Varsayılan portları:

25: Sunucular arası mail aktarımı (server-to-server).

587: Mail istemcilerinden gönderim (submission).

465: SSL üzerinden güvenli SMTP (SMTPS).

Özet:

SMTP = Gönderim protokolü.

IMAP/POP3 = Alma protokolleri.

Yani, mail kutuna gelen mailleri görmek için SMTP kullanılmaz, IMAP veya POP3 gerekir.


# IMAP/POP3 = Alma protokolleri nedir?

E-mail dünyasında SMTP sadece gönderim içindir.
Ama mail almak/görmek için başka protokoller gerekir → işte onlar POP3 ve IMAP.

1. POP3 (Post Office Protocol v3)

Açılımı: Postane Protokolü, sürüm 3.

Görevi: E-postaları sunucudan indirir.

Çalışma mantığı:

Outlook, Thunderbird, vs. gibi bir istemci sunucuya bağlanır.

E-mailleri bilgisayara indirir.

Varsayılan ayarlarda indirilen mail sunucudan silinir (yani başka cihazdan göremezsin).

Portları:

110 (standart TCP)

995 (SSL/TLS ile güvenli POP3S)

Avantaj: İnternet olmasa bile indirdiğin maillere erişirsin.

Dezavantaj: Mailler genellikle tek cihaza düşer, senkronizasyon yoktur.

2. IMAP (Internet Message Access Protocol)

Görevi: Mailleri sunucuda tutar, sen cihazdan sadece görüntülersin.

Çalışma mantığı:

Telefon, bilgisayar, tablet → hepsi aynı sunucuya bağlanır.

Mail silersen, klasör eklersen, okundu işaretlersen → bu değişiklik tüm cihazlarda senkronize olur.

Portları:

143 (standart TCP)

993 (SSL/TLS ile güvenli IMAPS)

Avantaj: Çoklu cihaz desteği (mesela Gmail’i hem telefonda hem bilgisayarda aynı anda kullanabilirsin).

Dezavantaj: İnternet yoksa mailleri göremezsin (cache dışında).

Özet

SMTP → Gönderim protokolü

POP3 → Al, indir, genellikle sunucudan sil.

IMAP → Al, senkronize et, sunucuda sakla.

# 🔹 Port Nedir?

Port = Mantıksal kapı / kanal

Bilgisayarında aynı anda bir sürü uygulama interneti kullanıyor olabilir (mesela YouTube, WhatsApp Web, Online oyun).

Hepsi aynı IP adresi üzerinden dış dünyaya çıkar ama hangi paketin hangi programa gideceğini ayırt etmek için port numaraları kullanılır.

Yani IP adresi = Apartman adresi
Port numarası = O apartmandaki daire numarası

🔹 Port Sayısı

Port numaraları 16 bit ile tutulur.

Yani 0’dan 65535’e kadar (toplam 65.536 adet) port vardır.

🔹 Port Türleri

Portlar kullanım alanlarına göre 3 gruba ayrılır:

Well-known ports (0 – 1023)

“Ünlü, bilinen portlar” → Standart protokoller için ayrılmıştır.

Örnekler:

20/21 → FTP

22 → SSH

25 → SMTP

53 → DNS

80 → HTTP

443 → HTTPS

Registered ports (1024 – 49151)

Uygulamalar, servisler için ayrılmıştır.

Örn:

3306 → MySQL

3389 → RDP

8080 → alternatif HTTP

Dynamic / Private / Ephemeral ports (49152 – 65535)

“Geçici portlar” → Sen bir uygulama açtığında işletim sistemi otomatik atar.

Örn: Tarayıcı Google’a bağlanırken 80/443’e gider ama bilgisayarın kendisi rastgele bir yüksek port numarasını (mesela 52341) kullanır.

🔹 Portların Protokollerle İlişkisi

Protokoller (HTTP, SMTP, DNS vs.) TCP ya da UDP üzerinden çalışır.

Yani aslında her portun iki versiyonu vardır:

TCP 80

UDP 80

Toplamda → 65.536 × 2 = 131.072 mantıksal kapı vardır.

Özet:

65.536 port var (0–65535).

İki tür protokol (TCP/UDP) olduğu için her port çift.

Düşük portlar (0–1023) standartlara ayrılmış.

Yüksek portlar uygulamalar ve dinamik bağlantılar için kullanılıyor.

# Aynı Ağdaki Cihazlar Nasıl İletişim Kurar?

1. Başlangıç Durumu - Bilgisayar Düşünüyor
b2b2 isimli bilgisayar (IP adresi 192.168.1.20), ala1 isimli bilgisayara (IP adresi 192.168.1.10) veri göndermek istiyor. Ama bir problem var: b2b2 bilgisayarı ala1'in MAC adresini bilmiyor.
Bilgisayarın mantığı şu: "Ben IP adresini biliyorum ama fiziksel adresi (MAC adresi) bilmiyorum. Veriyi göndermek için önce bu bilgisayarın fiziksel adresini öğrenmem lazım."
b2b2 kendi bellek tablosuna bakıyor ve "192.168.1.10'un MAC adresi nedir?" diye soruyor kendine. Tabloda sadece router'ın MAC adresi var, ala1'in MAC adresi yok.
2. ARP Süreci - Herkese Sesleniyor
b2b2 bilgisayarı şu stratejiyi benimsiyor: "Madem MAC adresini bilmiyorum, o zaman ağdaki herkese sorayım!"
Bu amaçla özel bir mesaj hazırlıyor. Bu mesajın zarfında (Ethernet frame) şu bilgiler var:

Alıcı adresi: FF:FF:FF:FF:FF:FF (Bu özel adres "herkese" demek)
Gönderen adresi: Kendi MAC adresi
Mesaj içeriği: "Hey! 192.168.1.10 IP adresine sahip olan var mı? Varsa MAC adresini söyler misin?"

Bu mesaj ağdaki switch'e ulaşıyor.
3. Switch'in Tepkisi - Herkese Dağıtım
Switch bu "herkese" yazılmış mesajı aldığında şöyle düşünüyor: "Bu mesaj herkese yazılmış, o zaman bağlı olduğum bütün cihazlara iletmeliyim."
Switch aynı zamanda akıllı bir cihaz. Gelen mesajdan şunu öğreniyor: "Ah, b2b2:b2:b2:b2:b2:b2 MAC adresli cihaz 1 numaralı portuma bağlı. Bunu tabloma not edeyim."
Sonra mesajı ala1, e4e4, f5f5 ve router'a gönderiyor.
4. Sadece Bir Cevap - ala1'in Yanıtı
Ağdaki tüm cihazlar bu "Kim 192.168.1.10?" sorusunu alıyor. Ama sadece ala1 bilgisayarı şöyle düşünüyor: "Hey! Bu benim IP adresim! Ben cevap vermeliyim."
ala1 bir cevap mesajı hazırlıyor:

Bu sefer sadece b2b2'ye (broadcast değil, direkt)
"Merhaba b2b2! Ben 192.168.1.10'um ve MAC adresim a1:a1:a1:a1:a1:a1"

Bu cevap switch'e geliyor ve switch de "ala1 cihazı 2 numaralı portumda" diye tabloya not ediyor.
5. Bilgi Güncelleme - Artık Tanışıyorlar
Her iki bilgisayar da artık birbirini tanıyor:

b2b2: "Artık biliyorum, 192.168.1.10'un MAC adresi a1:a1:a1:a1:a1:a1"
ala1: "Artık biliyorum, 192.168.1.20'nin MAC adresi b2b2:b2:b2:b2:b2:b2"

Bu bilgileri kendi adres defterlerine (ARP table) yazıyorlar. Artık bir dahaki sefere sormaya gerek kalmayacak.
6. Gerçek Veri Gönderimi - Ana Mesaj
Artık MAC adresini öğrendiğine göre, b2b2 gerçek mesajını gönderebilir. Paket şöyle hazırlanıyor:
Zarfın üstü (Ethernet Header):

"Kime: a1:a1:a1:a1:a1:a1 adresindeki ala1'e"
"Kimden: b2:b2:b2:b2:b2:b2 adresindeki b2b2'den"
"İçerik türü: IP paketi"

Paketin içindeki adres bilgisi (IP Header):

"192.168.1.20'den 192.168.1.10'a"
"TCP protokolü kullanılıyor"

Uygulama bilgisi (TCP Header):

"5000 numaralı porttan 80 numaralı porta"

Gerçek mesaj:

"Merhaba ala1!"

Hangi Protokoller Neden Kullanılıyor/Kullanılmıyor:
Kullanılan Protokoller ve Nedenleri:
ARP kullanılıyor çünkü: "IP adresini biliyorum ama fiziksel adresi bilmiyorum, öğrenmem lazım."
Ethernet kullanılıyor çünkü: "Yerel ağda fiziksel olarak veri taşımak için gerekli."
IP kullanılıyor çünkü: "Hangi bilgisayardan hangi bilgisayara gideceğini belirtmek için."
TCP kullanılıyor çünkü: "Hangi uygulamadan hangi uygulamaya gideceğini ve güvenilir iletim için."
Kullanılmayan Protokoller ve Nedenleri:
NAT kullanılmıyor çünkü: "İkisi de aynı ağda, dış dünyaya çıkmıyorlar. Router NAT yapmıyor."
DHCP kullanılmıyor çünkü: "IP adresleri zaten var ve sabit. Yeni IP adresi atanmıyor."
DNS kullanılmıyor çünkü: "İsimleri çevirmiyoruz, direkt IP adresi kullanıyoruz."
Switch'in Öğrenme Süreci:
Switch başlangıçta kimsenin nerede olduğunu bilmiyor. Ama her mesaj aldığında şöyle düşünüyor:

"Bu mesaj hangi porttan geldi?"
"Gönderen MAC adresi neydi?"
"O zaman bu MAC adresi bu portta demektir, tabloya yazayım."

Zamanla switch ağdaki herkesin nerede olduğunu öğrenir ve mesajları sadece gerekli porta gönderir, gereksiz yere herkese göndermez.
Bu süreçte router hiç devreye girmez çünkü her iki bilgisayar da aynı ağda (192.168.1.x). Router sadece farklı ağlara gidildiğinde çalışır.

# Subnet Mask: 
IP adresinin hangi kısmının ağ, hangi kısmının ise host olduğunu tanımlamak için kullanılır. Örneğin, 255.255.255.0 subnet maskesi, IP adresinin ilk üç oktetinin ağ adresini, son oktetinin ise host adresini belirlediğini gösterir. Bu durumda, "192.168.1.0" ağ adresi, "0-255" aralığı ise bu ağa bağlı cihazların adreslerini temsil eder.

# Farklı Ağlardaki Cihazlar Nasıl İletişim Kurar?

1. Başlangıç Durumu - Bilgisayar Ağı Analiz Ediyor
b2b2 bilgisayarı (192.168.1.20) bu sefer e4e4 bilgisayarına (192.168.5.10) veri göndermek istiyor.
b2b2 şöyle düşünüyor: "192.168.5.10'a veri göndermek istiyorum. Bakalım bu adres benim ağımda mı?"

Subnet Mask kontrolü yapıyor:
Benim IP'im: 192.168.1.20 (subnet mask: 255.255.255.0)
Hedef IP: 192.168.5.10
Benim network: 192.168.1.0/24
Hedef network: 192.168.5.0/24

"Farklı ağlardayız! Bu durumda gateway (router) kullanmam gerekiyor."

2. Gateway Bilgisini Kontrol Etme
b2b2 kendi ağ ayarlarına bakıyor:

IP: 192.168.1.20
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.1.1 (Router'ın IP'si)

"Tamam, farklı ağa gitmek için 192.168.1.1 adresindeki router'ı kullanacağım. Ama router'ın MAC adresini biliyorum mu?"
ARP tablosunu kontrol ediyor:
IP Address       MAC Address         Interface
192.168.1.1      rr:rr:rr:rr:rr:rr  eth0  (Router MAC var!)
Eğer router'ın MAC adresi yoksa, önce router'a ARP request gönderir.

3. İlk Paket Hazırlığı - Router'a Gönderme
b2b2 paketini şöyle hazırlıyor:
Ethernet Frame (Layer 2):

Dest MAC: rr:rr:rr:rr:rr:rr (Router'ın MAC adresi!)
Src MAC: b2:b2:b2:b2:b2:b2 (Kendi MAC adresi)

IP Packet (Layer 3):

Src IP: 192.168.1.20 (Değişmez!)
Dest IP: 192.168.5.10 (Değişmez!)

TCP Segment (Layer 4):

Src Port: 5000
Dest Port: 80
Data: "Merhaba e4e4!"

"Ben IP paketini 192.168.5.10'a gönderiyorum ama fiziksel olarak router'a teslim ediyorum."

4. Router'ın İlk Ağdaki İşlemleri
Router paketi aldığında şöyle düşünüyor:
"Bana bir paket geldi. Bakalım:"

Dest MAC: Benim MAC adresim (bana geldi)
Dest IP: 192.168.5.10 (bu benim değil, yönlendirmem lazım)

Routing Table kontrolü:
Network          Next Hop        Interface
192.168.1.0/24   Directly Connected   eth0
192.168.5.0/24   Directly Connected   eth1
0.0.0.0/0        ISP Gateway         eth2
"192.168.5.0/24 network'ü eth1 interface'ime bağlı. Paketi oraya yönlendireyim."

5. Router'ın Paket Yeniden Hazırlama Süreci
Router şimdi paketi 192.168.5.x ağına göndermek için yeniden hazırlıyor:
IP paketi aynı kalıyor ama Ethernet frame değişiyor:
Yeni Ethernet Frame:

Src MAC: rr:rr:rr:rr:rr:r5 (Router'ın 192.168.5.x ağındaki interface MAC'i)
Dest MAC: ??? (e4e4'ün MAC adresi gerekiyor!)

Router şöyle düşünüyor: "192.168.5.10'un MAC adresini bilmiyorum. ARP yapmam lazım."

6. Router'dan ARP Request (İkinci Ağda)
Router 192.168.5.x ağına ARP request gönderiyor:
ARP Broadcast (192.168.5.x ağında):

Src MAC: rr:rr:rr:rr:rr:r5 (Router'ın 192.168.5.x interface MAC'i)
Dest MAC: FF:FF:FF:FF:FF:FF (Broadcast)
Message: "Kim 192.168.5.10? MAC adresiniz nedir?"

Switch bu broadcast'i 192.168.5.x ağındaki tüm cihazlara gönderiyor.
7. e4e4'ün ARP Reply'i
e4e4 (192.168.5.10) cevap veriyor:
"Ben 192.168.5.10'um! MAC adresim: e4:e4:e4:e4:e4:e4"
Router bu bilgiyi ARP tablosuna kaydediyor:
IP Address       MAC Address         Interface
192.168.5.10     e4:e4:e4:e4:e4:e4   eth1

8. Son Paket İletimi
Artık router tüm bilgilere sahip. Paketi son şekliyle hazırlıyor:
Final Ethernet Frame (192.168.5.x ağında):

Src MAC: rr:rr:rr:rr:rr:r5 (Router'ın 192.168.5.x MAC'i)
Dest MAC: e4:e4:e4:e4:e4:e4 (e4e4'ün MAC'i)

IP Packet (Hiç değişmedi!):

Src IP: 192.168.1.20 (Hala aynı!)
Dest IP: 192.168.5.10 (Hala aynı!)

TCP Segment:

Data: "Merhaba e4e4!"

e4e4 paketi alıyor ve "192.168.1.20'den bana mesaj gelmiş!" diyor.

Hangi Protokoller Neden Kullanılıyor/Kullanılmıyor:

KULLANILAN PROTOKOLLER:
ARP (İki kez kullanıldı):

İlk: b2b2 → router MAC adresini öğrenmek için (eğer bilmiyorsa)
İkinci: Router → e4e4 MAC adresini öğrenmek için
Neden: "Her ağda fiziksel adresleri bilmek gerekiyor"

IP (Internet Protocol):

Kaynak ve hedef IP hiç değişmedi
Router sadece yönlendirdi
Neden: "Farklı ağlar arası iletişimin temeli"

Routing:

Router routing table kullandı
Hangi ağa nasıl gidileceğini belirledi
Neden: "Farklı ağları birbirine bağlamak için"

Ethernet (İki farklı ağda):

Her ağda farklı MAC adresleri kullanıldı
Frame header'ları değişti ama IP paketi aynı kaldı
Neden: "Her fiziksel ağda yerel adresler gerekiyor"

KULLANILMAYAN PROTOKOLLER:
NAT (Network Address Translation):
Kullanılmadı çünkü: "İki ağ da private (192.168.x.x) ve router sadece yönlendirdi, IP çevirmedi. NAT sadece private → public çevirimde kullanılır."
DHCP:
Kullanılmadı çünkü: "IP adresleri zaten mevcut ve sabit. Yeni IP atanması yok."
DNS:
Kullanılmadı çünkü: "Direkt IP adresi kullandık, isim çevirimi yok."

Router'ın Detaylı Düşünce Süreci:
Paket aldığında:
"Bana gelen bu paket benim için mi?"

Dest MAC benim → Evet, bana geldi
Dest IP benim → Hayır, 192.168.5.10 for someone else

"O zaman ben bu paketi yönlendirmeliyim."
Routing kararı:
"192.168.5.10 hangi ağda?"

Routing table'a bak
192.168.5.0/24 eth1 interface'imde
Oraya yönlendir

MAC adresi problemi:
"eth1'den göndermek için e4e4'ün MAC adresini bilmem lazım"

ARP table'a bak
Yoksa ARP request gönder
Cevap gelince paketi ilet

Switch'lerin Rolü:
192.168.1.x ağındaki switch:

b2b2'den gelen paketi router'a iletti
MAC learning yaptı

192.168.5.x ağındaki switch:

Router'dan gelen ARP broadcast'i herkese iletti
e4e4'ün ARP reply'ini router'a iletti
Son paketi e4e4'e iletti

Özet - Ana Fark:
Aynı ağda: Direkt iletişim (sadece ARP + Ethernet)
Farklı ağda: Router devreye giriyor

IP adresleri değişmiyor
MAC adresleri her ağda değişiyor
Router yönlendirme yapıyor
İki kez ARP gerekiyor (her ağda bir)

En önemli nokta: Router, IP paketini hiç değiştirmedi, sadece hangi ağa göndereceğini belirledi ve uygun MAC adresleriyle sardı.