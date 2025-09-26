
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

İstersen sana Ethernet frame’in iç yapısını (başlık, adresler, veri, hata kontrol kısmı) görsel gibi şematik anlatabilirim. Onu da ister misin?

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
java// Tipik ofis ağı
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
java// Büyük dosya gönderiyorsun
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
javaGönderen: "1000 byte gönderiyorum!"
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
java// TCP Bağlantı kurma
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

# TCP kullanan ve kullanmayan portlar?

Port numarası, sadece “hangi uygulama/protokol çalışıyor” bilgisini verir.

Örn:

80 → HTTP (TCP kullanır)

443 → HTTPS (TCP kullanır)

25 → SMTP (TCP kullanır)

53 → DNS (hem UDP hem TCP kullanabilir)

67-68 → DHCP (UDP kullanır)

Yani port = kapı numarası
“TCP mi UDP mi” = o kapının arkasında verinin nasıl taşındığı.

# Portlar da mı protokol kullanır?

Port protokol değildir, sadece numaradır.

Ama o portun hangi protokole bağlı olduğunu IANA belirlemiştir.

25 → SMTP

3306 → MySQL

22 → SSH

O protokol de TCP mi, UDP mi kullanacağına karar verir.

Kısa özet:

SMTP bir uygulama protokolüdür → ama taşıma için TCP’ye ihtiyaç duyar.

TCP = güvenilir taşıma protokolü

UDP = hızlı ama güvenilmez taşıma protokolü

Port = kapı numarası, hangi protokolün çalıştığını söyler.

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

# 🔹 1. DHCP (Dynamic Host Configuration Protocol)

Görevi: Cihaza IP, Subnet Mask, Gateway, DNS verir.

Örnek: Bilgisayarı açıyorsun → DHCP’den otomatik 192.168.1.105 alıyorsun.

Çalışma katmanı: Uygulama Katmanı (Layer 7), ama UDP port 67/68 üzerinden çalışır.

NAT yapmaz ❌

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

🔗 Peki ARP nerede kullanılır?

LAN içinde: Bilgisayarın gateway (192.168.1.1) ile konuşmak ister → önce ARP yapar, “Bu IP hangi MAC’te?” der.

NAT’la ilişkisi: NAT öncesinde LAN tarafında paket fiziksel adrese (MAC) gönderilebilmesi için ARP şarttır.

Yani NAT’tan önce ARP çalışır.

DHCP’yle ilişkisi: DHCP server IP dağıtırken de ARP kullanır → “Bu IP boş mu, çakışma var mı?” diye ARP probe atabilir.

🔹 Özet

DHCP: IP dağıtır.

ARP: IP’nin MAC karşılığını bulur.

NAT: Özel IP’yi genel IP’ye çevirir.

📌 Yani NAT’ı DHCP yapmaz, NAT’ı router/modem yapar.
📌 ARP ise LAN’da iletişim kurabilmek için her zaman devrededir, DHCP veya NAT’tan bağımsızdır ama onlarla birlikte çalışır.