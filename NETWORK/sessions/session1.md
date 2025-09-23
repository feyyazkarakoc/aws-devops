
# Cisco, dünyanın en büyük ağ (network) donanım ve yazılım üreticilerinden biridir.
Merkezi ABD, Kaliforniya’dadır ve 1984 yılında kurulmuştur.

Cisco özellikle:

Router (yönlendirici)

Switch (anahtar)

Firewall (güvenlik duvarı)

Kablosuz erişim cihazları

VoIP (internet üzerinden ses iletişimi) çözümleri

Siber güvenlik yazılımları

Bulut tabanlı ağ çözümleri

gibi ürünleriyle tanınır.

Ayrıca Cisco’nun çok bilinen bir tarafı da eğitim ve sertifikasyon programlarıdır (Cisco Networking Academy, CCNA, CCNP, CCIE). Bu sertifikalar dünya genelinde ağ uzmanlarının yetkinliğini kanıtlayan önemli belgelerdir.

Yani Cisco hem donanım/yazılım üreten teknoloji şirketi, hem de IT profesyonelleri için eğitim ve sertifika sağlayıcısıdır.

# ISP, İngilizce Internet Service Provider (İnternet Servis Sağlayıcı) kelimesinin kısaltmasıdır. 
Türkçe’de İnternet Servis Sağlayıcısı denir.

ISP, kullanıcılara internet erişimi sağlayan şirkettir.
Türkiye’deki örnekler: Türk Telekom, TurkNet, Superonline, Vodafone, Kablonet vb.

Bir ISP’nin sunduğu hizmetler:

İnternet bağlantısı (ADSL, VDSL, fiber, mobil internet vb.)

IP adresi tahsisi

DNS hizmeti

Barındırma (hosting) ve e-posta hizmeti

Güvenlik ve firewall çözümleri

Özetle: İnternete bağlanabilmemiz için servis sunan kurumlara ISP denir.

# Modem kelimesi:
“Modem” = Modulator – Demodulator’un kısaltmasıdır.

Modülasyon: Bilgisayardan çıkan sayısal (dijital) veriyi, telefon hattı/kablo üzerinden taşınabilmesi için analog sinyale çevirir.

Demodülasyon: İnternetten gelen analog sinyali tekrar sayısal veriye çevirir.

Modemin görevleri:

İnternete bağlanmak – ISS (internet servis sağlayıcısı) ile bağlantıyı kurar.

Sinyal çevirme – Dijital veriyi analog sinyale, analog sinyali dijitale çevirir.

IP adresi alma ve dağıtma – ISS’den aldığı IP adresini bilgisayara/cihazlara verir.

Veri iletimini sağlamak – Bilgisayar, telefon, tablet gibi cihazların internete erişmesini sağlar.

(Eğer modem aynı zamanda router özelliği içeriyorsa) Yerel ağ (LAN) yönetimi yapar, cihazlara DHCP ile IP dağıtır, bazen Wi-Fi yayını da yapar.

Günümüzde çoğu cihaz aslında “Modem + Router (Yönlendirici)” birleşimi olduğu için sadece internet bağlantısı kurmakla kalmaz, aynı zamanda:

Kablosuz ağ (Wi-Fi) sağlar.

Güvenlik (NAT, firewall) sağlar.

Evdeki cihazlar arasında veri paylaşımına aracılık eder.

# Analog sinyal sayısal (dijital) veriyi anlatır mısın?


1. Analog sinyal nedir?

Sürekli (kesintisiz) bir dalga şeklindedir.

Elektrik voltajı, ses dalgası, radyo sinyali gibi doğal dünyadaki şeyler analogtur.

Örneğin: Mikrofonla konuştuğunda çıkan ses dalgaları analog sinyaldir.

Özellikleri:

Sonsuz sayıda değer alabilir (örneğin 1.2V, 1.25V, 1.2503V ...).

Dalgalarla (sinüs, kare, üçgen vb.) temsil edilir.

Gürültüden (noise) kolay etkilenir.

2. Sayısal (dijital) veri nedir?

Bilgisayarların anlayabildiği biçimdir: 0 ve 1 (binary).

Her şey en küçük parçaya indirgenir → ya var (1) ya yok (0).

Örneğin: Bir fotoğraf, ses kaydı veya video → bilgisayarda milyonlarca 0-1 dizisi olarak saklanır.

Özellikleri:

Kesikli (discrete) değerlerden oluşur.

Daha az gürültüye duyarlıdır.

Bilgisayar, telefon, internet gibi dijital sistemlerde kullanılır.

3. Analog → Dijital dönüşüm

Buna ADC (Analog to Digital Converter) denir.
Örneğin:

Mikrofon → sesi (analog) alır.

Ses kartı → onu sayısal 0-1 dizisine çevirir.

Bilgisayar → artık sesi sayılarla işleyebilir.

4. Dijital → Analog dönüşüm

Buna DAC (Digital to Analog Converter) denir.
Örneğin:

Bilgisayardan bir şarkı açtığında → veriler 0 ve 1’dir.

Ses kartı → bu dijitali tekrar analog dalgaya çevirir.

Hoparlör → kulağımıza doğal ses dalgası (analog) olarak ulaşır.

Kısaca:

Analog: Doğadaki sürekli sinyaller (ses, ışık, radyo dalgası).

Dijital: 0 ve 1 ile temsil edilen bilgisayar dili.

Modem: Bu iki dünya arasında çevirmenlik yapar.

# Bilgisayar ağlarında protokol, aslında iletişim kuralları demektir.

Basit tanım

Protokol = İki cihazın birbiriyle nasıl konuşacağını belirleyen standart kurallar bütünü.

İnsanların anlaşması için dil kuralları (gramer) neyse, bilgisayarların anlaşması için de protokoller odur.

Örneklerle

HTTP / HTTPS → Web sitelerinin tarayıcı ile konuşma protokolü.

FTP → Dosya transferi protokolü.

SMTP, POP3, IMAP → E-posta protokolleri.

TCP / IP → İnternetin temel iletişim protokolü.

DNS → Alan adlarını IP adresine çeviren protokol.

Özellikleri

Veri nasıl gönderilecek?

Hangi sırayla iletilecek?

Hata olursa nasıl düzeltilecek?

Kimlik doğrulama (güvenlik) nasıl sağlanacak?

Bütün bunları protokoller tanımlar.

Kısaca:
Protokol, bilgisayarların veya cihazların ağ üzerinde anlaşabilmesi için ortak dil / kurallar bütünüdür.

# Ağ Topolojisi Nedir?

Topoloji, bilgisayarların ve diğer cihazların (switch, router, modem vb.) ağ üzerinde nasıl bağlandığını ve birbirleriyle nasıl iletişim kurduğunu gösteren yapıdır.

Yani ağın fiziksel veya mantıksal haritasıdır.

Temel Ağ Topolojileri

Bus (Veriyolu) Topoloji

Tüm cihazlar tek bir kabloya bağlanır.

Kablo koparsa tüm ağ çöker.

Günümüzde pek kullanılmaz.

Star (Yıldız) Topoloji

Tüm cihazlar merkezi bir cihaza (switch/hub) bağlanır.

En yaygın kullanılan topolojidir.

Bir cihaz arızalansa ağ çalışmaya devam eder, ama merkez bozulursa tüm ağ gider.

Ring (Halka) Topoloji

Cihazlar halka şeklinde birbirine bağlanır.

Veri tek yönde veya çift yönde dolaşır.

Bir cihazda sorun olursa ağ aksayabilir.

Mesh (Örgü) Topoloji

Her cihaz diğer cihazlarla direkt bağlantılıdır.

Çok güvenilir ama maliyeti yüksektir.

Özellikle büyük ve kritik sistemlerde kullanılır.

Tree (Ağaç) Topoloji

Yıldız topolojilerin hiyerarşik olarak birleşmesi gibidir.

Büyük ağlarda kullanılır.

Hybrid (Melez) Topoloji

Birden fazla topolojinin karışımıdır.

Günümüzde çoğu ağ hibrit yapıdadır.

Özet

Topoloji = ağın bağlanma şekli.

Fiziksel topoloji → Kabloların ve cihazların fiziksel bağlantısı.

Mantıksal topoloji → Verinin ağ içinde izlediği yol.

# Mantıksal ağ topolojisi, ağ üzerindeki cihazların fiziksel olarak nasıl bağlandığından bağımsız olarak, verinin hangi yolu izleyerek iletildiğini gösterir.

Yani “veri akışı”nı gösteren ağ haritasıdır.

Fiziksel vs Mantıksal Topoloji

Fiziksel topoloji: Kablolar, switchler, routerlar nasıl bağlanmış → ağın donanım haritası.

Mantıksal topoloji: Veri ağda nasıl dolaşıyor → ağın iletişim haritası.

Örneğin:

Bir şirket ağı yıldız topolojisi ile kurulmuş olabilir (fiziksel).

Ama veriler halkada (ring) dolaşacak şekilde yönlendirilmiş olabilir (mantıksal).

Günlük hayattan benzetme

Fiziksel topoloji: Şehrin yolları, köprüleri.

Mantıksal topoloji: Arabaların o yolları kullanırken izlediği güzergâh (trafik akışı).

Örnekler

Ethernet ağları → Fizikselde genelde yıldız topoloji vardır, ama mantıksal olarak bus gibi davranır (tüm cihazlar aynı kabloyu paylaşıyor gibi).

Token Ring → Fizikselde yıldız topoloji olabilir, ama mantıksal olarak halka şeklinde veri dolaşır.

Kısaca:
Mantıksal ağ, cihazların veriyi birbirine hangi sırayla, hangi yolla ve hangi kurallarla ilettiğini tanımlar.

# Ağ topolojisi sadece “internetsiz ortam” değildir.

Ağ topolojisi dediğimizde, temel olarak cihazların birbirine bağlanma şeklini kastediyoruz.

Bu yerel ağ (LAN) olabilir → örneğin bir ofiste bilgisayarlar, yazıcılar, switchler.

Ya da daha geniş ölçekte WAN / internet olabilir → farklı şehirlerdeki ofisler, şubeler arası bağlantı.

Yani topoloji hem internetsiz ortamda (kapalı ağ) hem de internete bağlı ortamlarda vardır.

Firmalarda nasıl kullanılır?

Evet, internet olsa bile firmalar kendi iç ağ topolojilerini kurar:

Çünkü şirket içindeki bilgisayarların birbirine dosya göndermesi, yazıcı paylaşımı, sunucu erişimi için LAN topolojisi gerekir.

Örneğin bir şirkette:

Tüm bilgisayarlar yıldız topolojisi ile switch’e bağlanır.

Switch → router’a bağlanır.

Router → internet sağlayıcıya (ISP) bağlanır.

Bu durumda firma ağı hem kendi içinde topolojiye sahiptir, hem de internet üzerinden dış dünyaya bağlanır.

Özet

Topoloji: Cihazların nasıl bağlandığı → internete bağlı olup olmaması fark etmez.

Firmalar: İnterneti kullanıyor olsalar da içeride kendi ağ topolojilerini kurmak zorundadır.

İnternetsiz ortamda → sadece lokal iletişim vardır.

İnternet olduğunda → hem lokal topoloji, hem de WAN / internet topolojisi birlikte çalışır.

# Bant Genişliği Nedir?

Bant genişliği (bandwidth), bir ağ bağlantısının veya iletişim kanalının birim zamanda taşıyabileceği maksimum veri miktarıdır.

Yani aslında “internet yolunun genişliği” gibi düşünebilirsin.
Ne kadar genişse, o kadar çok veri aynı anda geçebilir.

Ölçü Birimi

bit/s (bps → bit per second) kullanılır.

Günlük hayatta Mbps (megabit/s) veya Gbps (gigabit/s) görürüz.

Örneğin: 100 Mbps internet = saniyede 100 milyon bit veri taşıma kapasitesi.

Benzetme (trafik yolu)

Bant genişliği = otoban şerit sayısı

Veri paketleri = arabalar

Daha çok şerit → aynı anda daha çok araba geçebilir.

Ama dikkat: Otobanda şerit çok olsa da trafik sıkışırsa (gecikme, ping) hız düşebilir.

Bant Genişliği ve Hız Farkı

İnsanlar bazen bant genişliği ile internet hızını karıştırır.

Bant genişliği: En fazla ne kadar kapasiten var.

Hız (throughput): Gerçekte elde ettiğin hız (trafik, yoğunluk, gecikme etkiler).

Örneğin:

100 Mbps internet paketine sahipsin (bant genişliği).

Ama yoğun saatlerde 70 Mbps ölçüyorsun (gerçek hız).

Kısaca:
Bant genişliği, bir ağ bağlantısının veri taşıma kapasitesidir.

# Ağ çeşitleri (network types):

1. LAN (Local Area Network – Yerel Alan Ağı)

Küçük alanlarda kurulan ağdır (ev, ofis, okul).

Genellikle tek bina veya yakın odalar.

Hızlı, maliyeti düşük.

Örn: Evde modem ile bağlanan bilgisayarlar, yazıcılar.

2. WAN (Wide Area Network – Geniş Alan Ağı)

Şehirler, ülkeler hatta kıtalar arası geniş alanları kapsar.

Birçok LAN’ın birleşmesiyle oluşur.

İnternet aslında en büyük WAN’dır.

3. MAN (Metropolitan Area Network – Şehir Ağı)

Bir şehir veya kampüs ölçeğinde ağ.

LAN’dan büyük, WAN’dan küçük.

Örn: Bir belediyenin tüm binalarını birbirine bağlaması.

4. PAN (Personal Area Network – Kişisel Alan Ağı)

Çok kısa mesafeli ağdır.

Örn: Telefon ↔ Bluetooth kulaklık, Akıllı saat ↔ Telefon.

5. WLAN (Wireless LAN – Kablosuz Yerel Ağ)

LAN’ın kablosuz versiyonu.

Örn: Wi-Fi ile evdeki bilgisayar ve telefonların bağlanması.

6. SAN (Storage Area Network – Depolama Alan Ağı)

Büyük kurumlarda veritabanı ve depolama sistemleri için özel ağ.

Veri merkezlerinde sık kullanılır.

7. VPN (Virtual Private Network – Sanal Özel Ağ)

İnterneti kullanarak özel ve güvenli bir tünel oluşturan ağ.

Şirketler uzak çalışanlarını güvenli bağlamak için kullanır.

Özet:

LAN → Ev / Ofis

MAN → Şehir

WAN → Ülke / Dünya (İnternet)

PAN → Kişisel küçük alan

WLAN, SAN, VPN → Özel türler

# Çünkü çoğu kişi hız ile bant genişliğini aynı şey sanıyor ama aslında farklı kavramlar.

1. Bant Genişliği (Bandwidth)

Bir bağlantının teorik kapasitesidir.

Yani bir anda maksimum ne kadar veri taşınabileceğini gösterir.

Ölçü birimi: bit/s (bps) → genelde Mbps veya Gbps.

Örn: 100 Mbps internet paketin var → bu senin “otoban şerit sayın”.

2. Hız (Throughput / Speed)

Gerçekte elde ettiğin veri aktarım miktarıdır.

Bant genişliğinden düşük olabilir (trafik yoğunluğu, gecikme, paket kaybı yüzünden).

Ölçü birimi de aynı → Mbps / Gbps.

Örn: 100 Mbps paket alıyorsun ama testte 70 Mbps görüyorsun → bu senin “gerçek hızın”.

Benzetme (Otoban örneği 🚗)

Bant genişliği = Otobandaki şerit sayısı

Hız = Arabaların gerçekten gidebildiği km/saat

8 şeritli otoban (yüksek bant genişliği) olabilir,
ama trafik sıkışıksa arabalar yavaş gider (düşük hız).

Özet

Bant genişliği: Potansiyel kapasite (teorik üst sınır).

Hız: Gerçekte aldığın performans.

Bant genişliği yüksek → Daha çok veri aynı anda taşınabilir.

Hız yüksek → Veriler daha hızlı ulaşır.