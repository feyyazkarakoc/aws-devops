# Repeater – Tekrarlayıcı

OSI Katmanı: Layer 1 (Physical – Fiziksel Katman)

Görevi: Zayıflayan sinyali güçlendirmek ve aynı şekilde tekrar göndermek.

Hiç akıllı değildir, sadece elektrik sinyalini yeniler.

Kullanım: Uzak mesafeli kablolarda (örneğin Ethernet kablosu 100 metreyi geçince sinyal zayıflar).

Repeater = sadece iletim gücünü artırır.

# Hub

OSI Katmanı: Layer 1 (Physical – Fiziksel Katman)

Çok basit bir cihazdır.

Görevi: Gelen veriyi tüm portlara göndermek.

Örn: A bilgisayarı B’ye veri göndermek istiyor. Hub → bu veriyi C, D, E’ye de yollar.

Sonuç: Çarpışma (collision) olur, ağ yavaşlar.

Hub, MAC adresi bilmez, öğrenmez → sadece “tekrarlayıcı + çoklu çıkış” gibidir.

Hub = çok portlu repeater.

Kısaca Özet
Cihaz	OSI Katmanı	                Görevi	                                        Akıllı mı?
NIC	      2 (Data Link)	       Bilgisayarı ağa bağlar, MAC adresi sağlar	          Evet
Repeater  1 (Physical)	       Sinyali güçlendirir, tekrar gönderir	                  Hayır
Hub	      1 (Physical)	       Veriyi tüm portlara dağıtır	                          Hayır

Günümüzde hub ve repeater çok az kullanılır. Onların yerine switch ve router kullanılır, çünkü daha akıllı cihazlardır.


# NIC (Network Interface Card) – Ağ Kartı

Bilgisayarı ağa bağlayan donanımdır.

Her bilgisayarda (Ethernet kartı, Wi-Fi (Wireless kartı) kartı gibi) vardır.

OSI Katmanı: Layer 2 (Data Link – Veri Bağlantı Katmanı)

Görevleri:

Cihaza MAC adresi kazandırır (eşsiz kimlik).

Veriyi bilgisayarın anlayacağı formattan ağın anlayacağı formata çevirir.

Gönderme/alma işlemlerini yönetir.

Yani NIC olmadan bilgisayar ağa bağlanamaz.

# Bridge’in Temel Görevi

İki ağı birbirine bağlar (köprü kurar).

Çalıştığı katman: OSI Layer 2 (Veri Bağlantı Katmanı)

Yani MAC adresleriyle çalışır (IP değil).

Bridge’in Ne İşe Yaradığı

Ağları birleştirme:
İki ayrı LAN’ı (Local Area Network) tek bir ağ gibi çalıştırabilir.

Çarpışma alanlarını azaltma:
Hub gibi cihazlarda bütün bilgisayarlar aynı hattı paylaşır.
Bridge, hangi paketin nereye gitmesi gerektiğini öğrenir → sadece ilgili tarafa yollar.

MAC adres tablosu tutar:

Hangi cihaz hangi porttan ulaşılır, bunu öğrenir.

Gereksiz paket yayılmasını engeller.

Switch’in atasıdır:
Günümüzde bridge yerine switch kullanıyoruz.
Aslında switch = çok portlu bridge diyebilirsin.

Basit Örnek

Diyelim ki iki odada bilgisayarlar var.

Sen bu iki odadaki bilgisayarların tek ağ gibi çalışmasını istiyorsun.

Araya bridge koyarsan → sanki tek ağmış gibi birbirleriyle haberleşirler.

Özet:
Bridge = İki LAN’ı birbirine bağlayan, MAC adresleriyle çalışan, çarpışmaları azaltan cihazdır.
Bugün pek görmesek de switch aslında modern bridge sayılır.

# Switch (Anahtar) Nedir?

OSI Katmanı: Layer 2 (Data Link – Veri Bağlantı Katmanı)

Hub’a çok benzer (çok portludur), ama akıllıdır.

Hub gibi herkese veri yollamaz → sadece hedef bilgisayara yollar.

Nasıl Çalışır?

Switch’e bağlı her cihazın MAC adresini öğrenir (NIC kartından gelen).

Bir tablo oluşturur:

Port 1 → MAC: AA:BB:CC:DD
Port 2 → MAC: EE:FF:GG:HH
Port 3 → MAC: II:JJ:KK:LL


A bilgisayarı B’ye veri göndermek istediğinde:

Switch bakar: “B’nin MAC adresi Port 2’de.”

Veriyi sadece Port 2’ye yollar.

Diğer cihazlar etkilenmez → çarpışma azalır, hız artar.

Switch’in Görevleri

MAC adres tablosu (CAM Table) tutar.

Aynı anda birden fazla bilgisayarın haberleşmesine izin verir.

Collision domain’i bölerek ağ performansını artırır.

Full-duplex iletişimi (aynı anda gönderme ve alma) destekler.

Switch vs Hub
Özellik	                  Hub	                   Switch
Katman	                  Layer 1 (Physical)	   Layer 2 (Data Link)
Veri iletimi	          Herkese (broadcast)	   Sadece hedefe
Çarpışma (Collision)	  Çok olur	               Azalır
Performans	              Düşük	                   Yüksek
Akıllı mı?	              Hayır	                   Evet (MAC tablosu tutar)

Özet:
Switch = Hub’ın akıllı versiyonu.
Bu yüzden günümüzde şirketlerde, evlerde hep switch’li modemler veya router’lar kullanılır.

# Router Nedir?

OSI Katmanı: Layer 3 (Network – Ağ Katmanı)

Görevi: Farklı ağları birbirine bağlamak.

Örn: Senin evindeki LAN (192.168.1.x) → İnternet (WAN). Bunu router/modem yapar.

Nasıl Çalışır?

Bilgisayarın paket gönderir → içinde hedef IP adresi vardır.

Switch sadece “aynı ağ içindeki” cihazları bulabilir.

Ama hedef IP başka ağdaysa (mesela Google: 142.250.74.14), switch bir şey yapamaz.

Router bakar:

“Bu IP benim ağımda değil → o zaman gateway üzerinden başka ağa göndermeliyim.”

Router, routing table (yönlendirme tablosu) kullanarak hangi yoldan gideceğini bulur ve paketi ileri gönderir.

Router’ın Görevleri

Ağlar arası yönlendirme (LAN ↔ WAN, LAN ↔ LAN).

IP adreslerini anlar (MAC değil).

NAT (Network Address Translation) yapar → evdeki 10 cihazı tek Public IP üzerinden internete çıkarır.

DHCP sunucu olabilir (cihazlara otomatik IP dağıtır).

Güvenlik için firewall kuralları çalıştırabilir.

Switch vs Router
Özellik	                 Switch	                                     Router
OSI Katmanı	             2 (Data Link)	                             3 (Network)
Çalıştığı adres	         MAC adresi	                                 IP adresi
Görevi	                 Aynı ağdaki cihazları birbirine bağlar	     Farklı ağları birbirine bağlar
Evdeki kullanım	         Bilgisayar ↔ Bilgisayar	                 Ev LAN ↔ İnternet WAN

Özet:

Switch: Aynı ağda cihazlar arasında veri iletir (MAC ile).

Router: Ağlar arasında veri iletir (IP ile).

Senin modemin aslında bir router → çünkü hem ev ağını (LAN) hem de internet ağını (WAN) bağlıyor.

# NAT (Network Address Translation) Nedir?

Açılımı: Ağ Adres Çevirisi

OSI Katmanı: Layer 3 (Network)

Görevi: Özel (private) IP adreslerini → Genel (public) IP adresine çevirerek internete çıkarmak.

Neden NAT’a İhtiyaç Var?

IPv4 adresleri sınırlı (yaklaşık 4 milyar adet).

Dünyada milyarlarca cihaz var, herkese tek tek public IP verilemez.

Çözüm: Evde/işte cihazlara özel IP veriyoruz (192.168.x.x, 10.x.x.x gibi).

Bu cihazlar internete çıkarken modemdeki tek public IP kullanılıyor.

NAT Nasıl Çalışır?

Senin evinde 3 cihaz var:

Laptop: 192.168.1.101

Telefon: 192.168.1.102

Tablet: 192.168.1.103

Modemin dış IP’si (Public): 78.173.11.70

Sen Google’a gitmek istedin:

Laptop gönderiyor:
192.168.1.101:5050 → 142.250.74.14 (Google)

Router (NAT yapar):

Özel IP’yi alır → Public IP ile değiştirir.

78.173.11.70:30001 olarak internete yollar.

Bir tablo tutar:

192.168.1.101:5050 → 78.173.11.70:30001
192.168.1.102:6060 → 78.173.11.70:30002
192.168.1.103:7070 → 78.173.11.70:30003


Google cevap gönderir:
78.173.11.70:30001 → Router bakar tablodan → 192.168.1.101’e geri yollar.

NAT Türleri

SNAT (Source NAT): En yaygın, çıkış adresini değiştirir.

DNAT (Destination NAT): Giriş trafiğini içerdeki bir cihaza yönlendirir (örneğin port forwarding ile evdeki kamerana uzaktan bağlanma).

PAT (Port Address Translation): Bir public IP’yi port numaralarıyla çok cihaza paylaştırır (senin evinde olan).

Özet

NAT olmasa evdeki cihazların internete çıkması için her birine ayrı Public IP gerekirdi.

NAT sayesinde → 1 Public IP yeterli.

Ama NAT aynı zamanda güvenlik de sağlar → dışarıdan senin cihazların görünmez, sadece modem görünür.

# Modem Nedir?

Modem kelimesi: MOdulator + DEModulator’dan gelir.

İlk modemler, telefon hattı (analog) üzerinden internet bağlantısı sağlıyordu.

Bilgisayarların verisi sayısaldır (dijital), ama telefon hatları analog çalışıyordu.
Modem, bilgisayarın dijital verisini analog sinyale çevirir (modülasyon), gelen analog sinyali de tekrar dijitale çevirirdi (demodülasyon).

Yani modem = iki farklı dünya arasında çevirmen.

Günümüzde Modemler

Artık çoğu internet hattı dijital çalışıyor (ADSL, VDSL, Fiber, 4G/5G).
Bu yüzden “modem” dediğimiz cihazlar aslında sadece modem değil, birleşik cihazlar:

Modem (hattı internete çevirir)

Router (Yönlendirici) (ağlar arasında yönlendirme yapar, NAT yapar)

Switch (evdeki cihazları birbirine bağlar)

Wi-Fi Access Point (kablosuz bağlantı sağlar)

Yani senin evindeki modem aslında 4 cihazın birleşimi.

Modem Çeşitleri
1. Dial-up Modem (Eski – Analog Telefon Hattı)

56 kbps hız (çok yavaştı).

Telefon hattını meşgul ederdi.

Artık kullanılmıyor.

2. ADSL/VDSL Modem

Bakır telefon hattı üzerinden çalışır.

ADSL: Asymmetric → indirme hızı yüksek, yükleme düşük.

VDSL: Daha yeni, daha hızlı.

3. Kablo Modem

TV kablosu (koaksiyel kablo) üzerinden internet sağlar.

Özellikle bazı ülkelerde yaygın (Türkiye’de çok değil).

4. Fiber Modem / ONT (Optical Network Terminal)

Fiber optik kabloyu kullanır.

Işık sinyalini alıp dijitale çevirir.

Çok yüksek hızlar (100 Mbps – Gbps seviyeleri).

5. Mobil Modem (4G/5G Modem / Hotspot)

SIM kart takılan modemlerdir.

Cep telefonları da aslında küçük birer modemdir (hotspot açınca).

6. DSL Modem + Router Kombine Cihaz

Bugün evlerde en çok gördüğün.

Hem internete bağlanıyor, hem de ev içi ağı kuruyor.

Özet

Modem’in görevi: internet hattını bilgisayara/ağa çevirmek.

Günümüzdeki modemler aslında: Modem + Router + Switch + Wi-Fi birleşimidir.

Çeşitleri: Dial-up, ADSL/VDSL, Kablo, Fiber, Mobil (4G/5G).

# Firewall (Güvenlik Duvarı) Nedir?

Tanım: İnternetten gelen ve internete giden veri paketlerini denetleyen bir güvenlik sistemidir.

Görevi: Zararlı, istenmeyen ya da yetkisiz erişimleri engeller; sadece izin verilen trafiğe yol verir.

Mantık: Sanki evinin kapısındaki güvenlik görevlisi gibi. Gelen kişiye bakar:

“Bu izinli, geçebilir.”

“Bu yasaklı, içeri giremez.”

Firewall Türleri

Donanımsal (Hardware Firewall):

Genelde büyük şirketlerde veya kurumlarda özel cihazlar şeklinde olur.

Tüm ağın girişinde çalışır.

Yazılımsal (Software Firewall):

Windows Defender Firewall, Linux iptables, antivirüslerin içindeki güvenlik duvarları.

Tek bir bilgisayarı korur.

Modem/Router Firewall’u:

Günümüzde çoğu modem ve router’ın içinde basit bir firewall bulunur.

NAT (Network Address Translation) + paket filtreleme mantığıyla çalışır.

Örneğin: “Şu portu dışarıya açma”, “Şu IP’den gelen trafiği engelle” gibi ayarlar yapılabilir.

Modemlerde Firewall Nasıl Çalışır?

Modem arayüzüne girdiğinde (genelde 192.168.1.1) “Security” veya “Firewall” sekmesi olur.

Buradan:

Port yönlendirme (Port Forwarding) yapabilirsin.

IP filtreleme ayarlayabilirsin.

Bazı modemlerde DoS Attack Protection (hizmet engelleme saldırısına karşı koruma) vardır.

Kısaca: Evet, modemlerin içinde firewall vardır.
Ama bu genelde temel güvenlik sağlar. Daha gelişmiş koruma istiyorsan:

Ekstra yazılımsal firewall kullanılır (örneğin bilgisayarda Windows/Linux güvenlik duvarı).

Kurumsal yerlerde donanım firewall cihazları kullanılır (Fortigate, Cisco ASA, Palo Alto vb.).

# Evdeki modeme dsl kablosu geliyor. Bu durumda internet ne ile gelmiş oluyor?

1️⃣ DSL kablosu nedir?

Evindeki telefon hattı kablosu (bakır tel) aslında.

Yani duvardaki telefon prizinden çıkan kablo, DSL (Digital Subscriber Line) teknolojisiyle hem ses (telefon görüşmesi) hem de internet verisini taşıyor.

Senin “DSL kablosu” dediğin aslında telefon hattı kablosu.

2️⃣ İnternet nasıl geliyor?

Servis sağlayıcı (Türk Telekom, Superonline, vb.) santralde DSLAM denen cihazlarla senin hattını internete bağlıyor.

İnternet sinyali bakır kablo üzerinden elektriksel sinyal olarak evine kadar geliyor.

Yani evine fiber değilse, bakır telefon kablosuyla (DSL sinyali) internet geliyor.

3️⃣ Modem burada ne yapıyor?

DSL hattından gelen elektriksel sinyali alıyor.

İçindeki DSL modem bunu çözümleyip dijital internet verisine (IP paketlerine) çeviriyor.

Sonra bu veriyi ethernet kablosu veya Wi-Fi ile bilgisayar/telefonuna dağıtıyor.

4️⃣ Özet:

Evindeki modeme gelen DSL kablosu aslında telefon hattı (bakır tel).
Yani internet bakır kablo üzerinden elektrik sinyalleri şeklinde geliyor.
Senin modem bu sinyali “internet dili” olan IP paketlerine çevirip cihazlarına dağıtıyor.

# O halde fiber kablo değil, peki sokağa evin önüne kadar fiber kablo kullanılmış olabilir mi?
Evine fiber gelmiş mi yoksa bakır mı bunu modem arayüzünden veya kablodan nasıl anlarsın.

1️⃣ Modem Arayüzünden Kontrol

Tarayıcıya modem IP’sini yaz (genelde 192.168.1.1).

Kullanıcı adı ve şifre ile giriş yap.

Menüden genellikle DSL, WAN veya Internet Status sekmesini bul.

Orada göreceğin bilgiler:

Line Type / Connection Type

VDSL → Fiber sokağa kadar, evine bakır (VDSL2)

ADSL → Tamamen bakır

GPON / FTTH → Eve kadar fiber

Downstream / Upstream hızları

Yüksek hız (100 Mbps ve üzeri) → büyük ihtimal fiber sokağa kadar.

SNR, Attenuation (zayıflama) değerleri

Çok düşük değilse ve hız yüksek → fiber sokağa kadar.

2️⃣ Kablo Görünümüne Göre

Evdeki prizden çıkan kablo ince bakır tel (telefon kablosu) ise:

Büyük ihtimalle VDSL2 (fiber sokağa kadar, ev bakır)

Eğer evine gelen kablo kalın sarı/yeşil fiber kablo ve üzerinde ONT cihazı varsa:

Fiber eve kadar (FTTH)

WAN Bağlantı Satırları
Name	Type	Status	Açıklama
dsl_iptv	Dynamic IP	Disconnected	IPTV hizmeti için VDSL hattından ayrı bir dinamik IP bekleniyor, şu anda bağlı değil.
ewan_iptv	Dynamic IP ETH	Disconnected	Ethernet üzerinden IPTV hizmeti, bağlı değil.
dsl_internet	PPPoE	Connected	Senin internet hattın buradan geliyor. PPPoE protokolü ile ISS’ye bağlanıyor. Bu satır aktif ve internete bağlı.
ewan_internet	PPPoE ETH	Disconnected	Ethernet üzerinden başka bir PPPoE bağlantısı, şu anda yok.

Ne Anlamalıyız?

Senin internete çıkış hattın: dsl_internet → yani VDSL2 ve PPPoE üzerinden.

Evine gelen internet bakır VDSL hattı üzerinden geliyor, fiber sokağa kadar.

Diğer satırlar genellikle yedek veya ekstra servisler (IPTV, ikinci internet hattı) için.

Özetle:

Hattın VDSL → Fiber sokağa kadar, evine bakır.

İnternet aktif bağlantı → dsl_internet PPPoE.

Modemin WAN portundan başka bir ethernet hattı yok → o yüzden ewan_internet disconnected.

# encapsulation / decapsulation kavramlarını adım adım anlatayım. Bu, ağdaki verinin nasıl taşındığını anlamak için çok önemli.

1️⃣ OSI Modeli Hatırlatma

OSI modeli 7 katmanlı bir iletişim modelidir:

Physical (Fiziksel) → Kablolar, sinyaller

Data Link (Veri Bağlantı) → MAC adresleri, çerçeveler (frame)

Network (Ağ) → IP adresleri, paketler (packet)

Transport (Taşıma) → TCP/UDP, segment

Session (Oturum) → Bağlantı kontrolü

Presentation (Sunum) → Şifreleme, veri formatı

Application (Uygulama) → Tarayıcı, e-posta, FTP

2️⃣ Encapsulation (Kapsülleme)

Encapsulation = veriyi bir katmandan diğerine gönderirken, üst katman verisini alt katman protokol başlığıyla sarmak.

Mantık: Üst katman verisi → alt katmanda  segment, paket, frame, bit gibi formatlara dönüşür.

Örnek

Uygulama katmanı → “Hello” mesajı oluşturur

Transport katmanı → TCP başlığı ekler → segment oluşur

Network katmanı → IP başlığı ekler → packet (paket) oluşur

Data Link katmanı → MAC başlığı ekler → frame (çerçeve) oluşur

Physical katman → bitler üzerinden iletilir

Yani veri katman katman sarılır, paket sonunda kablo/air üzerinden gider.

3️⃣ Decapsulation (Kapsül Açma)

Decapsulation = alıcı tarafta gelen veriyi katman katman çözmek.

Mantık: Her katman kendi başlığını okur ve veri kısmını üst katmana verir.

Örnek

Physical katmanı → bitleri alır → Data Link’e verir

Data Link → MAC başlığını çıkarır → Network’e paket verir

Network → IP başlığını çıkarır → Transport’a segment verir

Transport → TCP başlığını çıkarır → Uygulamaya mesaj ulaşır

4️⃣ Özet Mantık
İşlem	Görev
Encapsulation	Veriyi “alt katman başlığı ile sarmak”
Decapsulation	Gelen veriyi “katman katman çözmek”

Gönderici → encapsulation

Alıcı → decapsulation

Örnek günlük hayat benzetmesi:

Bir mektubu zarfla göndermek gibi:

Mektup = Application Data

Zarf = Transport/Network/Data Link başlığı

Karşı taraf zarfı açar → mektubu okur → bu decapsulation

# segment nedir?

1️⃣ Segment Tanımı

Segment, OSI modelinde Transport katmanında (Layer 4) oluşturulan veri birimidir.

Yani uygulama verisinin TCP veya UDP başlığı eklenmiş hali.

Görevi: Veriyi parçalara bölmek ve güvenli iletim sağlamak.

2️⃣ Hangi Katmanda Oluşur?

Transport Layer (Taşıma Katmanı)

TCP kullanılıyorsa: segment

UDP kullanılıyorsa: datagram (ama mantık aynı → veri + taşıma başlığı)

3️⃣ Segment İçeriği
Parça	Açıklama
TCP/UDP başlığı	Kaynak port, hedef port, sıra numarası, kontrol bilgisi
Data (veri)	Uygulama katmanından gelen mesaj

Örnek:
Tarayıcı HTTP isteği gönderiyor → HTTP mesajı = veri
TCP segmenti oluşturur → TCP başlığı eklenir → segment oluşur
Sonra Network katmanına paket olarak iletilir

4️⃣ Mantık

Segment, ağdaki iletim için veriyi küçük ve yönetilebilir parçalara ayırır.

TCP’de segmentler sıralı ve hatasız iletim sağlar (ACK, sequence number ile).

UDP’de segment (datagram) daha basit → sırasız ve güvenli değil.

Özet:

Segment = Transport layer veri birimi

İçinde: Transport başlığı + Uygulama verisi

Gönderici → segment oluşturur

Alıcı → segmenti açar → veri uygulamaya ulaşır

# NOS (Network Operating System)

Açılımı: Network Operating System (Ağ İşletim Sistemi).

Tanım: Bir bilgisayarın veya sunucunun ağ kaynaklarını (dosya paylaşımı, yazıcı, kullanıcı hesapları, güvenlik, erişim izinleri) yönetmesini sağlayan işletim sistemidir.

Örnekler:

Eski: Novell NetWare, Windows NT Server

Günümüz: Windows Server, Linux tabanlı dağıtımlar

Görevi:

Ağdaki kullanıcıları tanır (login işlemleri)

Dosya/yazıcı paylaşımı yapar

Güvenlik politikalarını uygular

Ağ yönetimi ve hata takibini yapar

Yani NOS = “Ağ için özel işletim sistemi.”

# Workstation

Tanım: Genelde yüksek performanslı bilgisayar anlamına gelir.

Normal PC’lerden farkı:

Daha güçlü işlemci, RAM, ekran kartı

Bilimsel hesaplama, mühendislik, grafik tasarım gibi işler için tasarlanır

Ağ bağlamında:

“Ağda çalışan kullanıcı bilgisayarı” anlamında da kullanılır.

Örnek:

Bir şirkette herkesin masasındaki bilgisayar workstation sayılır.

Mühendislikte kullanılan güçlü bilgisayarlar da workstation’dır.

Workstation = ya güçlü bireysel bilgisayar ya da ağdaki istemci bilgisayar.

# Multimode Fiber

Tanım: Veri iletiminde kullanılan fiber optik kablo türüdür.

“Multimode” = birden fazla ışık yolu (mode) ile veri taşır.

Özellikleri:

Daha kısa mesafe (genelde 2 km’ye kadar)

Daha ucuz ekipman (lazer yerine LED ışık kaynağı kullanılır)

Geniş bant desteği (10 Gbps, 40 Gbps hızlara çıkabilir kısa mesafede)

Kullanım Alanı:

Kampüs ağları

Binalar arası bağlantı

Veri merkezlerinde kısa mesafe fiber bağlantı

Multimode fiber = ucuz, kısa mesafe, çok ışık yolu → daha fazla sinyal kayması (distorsiyon).

# Packet-Switching

Tanım: Verilerin küçük paketlere bölünerek ağ üzerinden gönderilmesi yöntemidir.

Her paket: veri + kaynak adresi + hedef adresi + kontrol bilgisi içerir.

Özellikleri:

Aynı anda birçok kullanıcı veri gönderebilir (kaynaklar paylaşılır).

Paketler farklı yollardan gidip hedefte birleşebilir.

Günümüz internetinin temelini oluşturur.

Avantajları:

Daha verimli bant genişliği kullanımı

Hata olursa sadece kayıp paket yeniden gönderilir

Örnek:

Sen WhatsApp’tan fotoğraf gönderdiğinde → tek parça gitmez → paketlere bölünür → internet üzerinden farklı rotalardan geçip karşı tarafta birleştirilir.

Packet-switching = “veri parçalanır → paket olur → ağda yol bulur.”

# Proxy Server

Tanım: Kullanıcı ile internet arasına giren aracı sunucu.

Görevleri:

Anonimlik/Gizlilik → Kullanıcı gerçek IP’sini gizler.

Cache (önbellek) → Sık ziyaret edilen siteleri saklar, hızlandırır.

Filtreleme → Yasaklı siteleri engeller (okullar, şirketler).

Güvenlik → Trafiği kontrol ederek kötü amaçlı içerikleri engeller.

Çalışma Şekli:

Sen bir siteye istek atarsın → önce proxy server’a gider → proxy siteye ulaşır → cevabı sana döner.

Örnek:

Bir okulda öğrenciler internete çıkarken önce proxy’den geçer, okul hangi sitelere girileceğini kontrol eder.

Proxy = arada duran trafik kontrolcüsü + hızlandırıcı + gizleyici.