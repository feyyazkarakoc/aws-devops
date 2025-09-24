
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

# “Computer Network Architecture” dendiğinde, ağların tasarımına ve iletişim şekline göre sınıflandırılması kastedilir.

Genelde iki temel türü vardır:

1. Peer-to-Peer (P2P) Architecture

Tüm bilgisayarlar eşit yetkilere sahiptir.

Her cihaz hem istemci (client) hem de sunucu (server) gibi davranabilir.

Yönetmesi kolaydır ama büyük ağlarda güvenlik ve performans sorunları çıkar.

Örnek:

Evde iki bilgisayarı birbirine bağlayıp dosya paylaşmak.

Torrent ağları (BitTorrent).

Avantajları:

Kurulumu ucuz ve basittir.

Merkezi sunucuya ihtiyaç yoktur.

Dezavantajları:

Güvenlik zayıf.

Çok sayıda kullanıcı olunca yavaşlar.

2. Client-Server Architecture

Ağda bir veya birden fazla sunucu (server) vardır.

Sunucular kaynakları (dosya, yazıcı, internet, veri tabanı) sağlar.

İstemciler (clients) bu kaynaklara erişir.

Örnek:

Bir şirket ağı: Dosya sunucusu, e-posta sunucusu, web sunucusu.

İnternette bir web sitesine bağlanmak (sen = client, site = server).

Avantajları:

Güvenlik ve kontrol daha güçlü.

Büyük ağlarda düzen sağlar.

Dezavantajları:

Sunucu bozulursa hizmet kesilir.

Sunucu kurulumu ve bakımı maliyetli.

3. Hybrid Architecture

P2P ve Client-Server’in birleşimidir.

Küçük ağlarda cihazlar birbirine direkt bağlanabilir (P2P),
ama kritik kaynaklar merkezi bir sunucuda tutulur.

Örnek:

Bir ofiste kullanıcıların kendi aralarında dosya paylaşması (P2P),
ama e-posta ve veritabanı için merkezi sunucuya bağlanmaları.

Özet:

Peer-to-Peer (P2P) → Basit, küçük ağlar.

Client-Server → Büyük, organize ve güvenli ağlar.

Hybrid → İkisini birleştiren yapılar.

# “Types of Communication in the Network” dediğimizde, ağda verinin kaynak ve hedef cihazlar arasında nasıl aktarıldığı anlatılır.

Temel olarak üç tür iletişim vardır:

1. Unicast Communication

Veri bir göndericiden → bir alıcıya gider.

En yaygın kullanılan iletişim türüdür.

IP adresi doğrudan hedef cihazı gösterir.

Örnek:

Senin bilgisayardan Google’a bağlanman.

WhatsApp’ta bir kişiye mesaj atman.

2. Broadcast Communication

Veri bir göndericiden → ağdaki tüm cihazlara gönderilir.

Belirli bir alt ağ (subnet) içindeki herkes veriyi alır.

Örnek:

ARP (Address Resolution Protocol) → “Bu IP kimin?” diye herkese sorar.

DHCP → Modem IP dağıtırken yayın yapar.

3. Multicast Communication

Veri bir göndericiden → belirli bir grup alıcıya gönderilir.

Sadece o gruba üye olan cihazlar veriyi alır.

Örnek:

Canlı maç yayını (aynı yayını izleyenlere aynı anda gönderilir).

Video konferans uygulamaları.

4. (Ek) Anycast Communication

Veri bir göndericiden → en yakın/alakalı alıcıya gönderilir.

Genellikle IPV6 ve DNS sunucuları için kullanılır.

Örnek:

Sen “google.com” yazınca → sana en yakın Google sunucusu cevap verir.

Özet:

Unicast → 1 → 1

Broadcast → 1 → Tüm cihazlar

Multicast → 1 → Belirli grup

Anycast → 1 → En yakın hedef

# 1. 192.168.1.1 herkeste sabit mi?

Değil.

Çoğu ev tipi modem bunu kullanır ama üreticisine göre değişir: 192.168.0.1, 192.168.2.1, 10.0.0.1 gibi.

Neden karışmıyor?

Çünkü bunlar private IP aralıklarıdır (RFC1918’de tanımlı).

Private IP’ler internet üzerinde yönlendirilmez. Yani senin evinde 192.168.1.1 modem olur, benim evimde de olur; ama internette çakışmaz çünkü NAT sayesinde hepsi tek bir public IP üzerinden çıkar.

Karışmama nedeni:

Bu IP sadece senin lokal ağında (LAN) geçerlidir.

Başka bir evdeki 192.168.1.1, senin evindekinden tamamen farklıdır çünkü "private IP range" (özel IP aralığı) internette global olarak yönlendirilmez.

Yani 192.168.1.1 senin evinde modemin, benim evimde de modemim olabilir → çakışmaz çünkü internette görünmezler.

2. Hocanınki neden 192.168.0.1?

Modem üreticisinin fabrika varsayılan ayarı farklı olduğu için.

TP-Link çoğunlukla 192.168.0.1, Zyxel ve Huawei çoğunlukla 192.168.1.1 kullanır.

İkisi de aynı işi yapar, sadece ağ bloğu değişik (192.168.0.x ya da 192.168.1.x).

3. Tarayıcıya 192.168.1.1 yazınca açılan sayfa nedir?

Bu modeminin yönetim paneli (router admin interface).

Oradan şunları yapabilirsin:

Wi-Fi SSID ve şifre değiştirme

Bağlı cihazları görme

Port yönlendirme (DevOps’ta sık kullanılır)

Güvenlik ayarları

Bağlı cihazları görebilir misin?
Evet. Yönetim panelinde “Connected Devices / Device List / Bağlı Cihazlar” sekmesi olur.
Buradan şunları görebilirsin:

Cihaz adı (ör. Feyyaz-iPhone)

IP adresi (ör. 192.168.1.105)

MAC adresi (her cihazın benzersiz kimliği)

Hatta bazı modemlerde cihaz engelleme veya erişim süresi sınırlama seçenekleri bile vardır.

Özet:

192.168.1.1 genelde gateway ama sabit değil.

.0.1 veya .1.1 üreticiye göre değişiyor, fark yok.

Tarayıcıdaki sayfa modem paneli, buradan kim ağa bağlı görebilirsin.

# 1. DHCP nedir?

DHCP = Dynamic Host Configuration Protocol

Ağdaki cihazlara otomatik olarak IP adresi dağıtan servistir.

Yani her cihaz bağlandığında tek tek “IP yazmana” gerek kalmaz.

Modemin DHCP’si devredeyse:

Telefona bağlandığında → IP otomatik alır.

Bilgisayarı açtığında → IP otomatik alır.

Örnek: Senin modem diyor ki:
“Benim dağıtacağım IP aralığı 192.168.1.100 → 192.168.1.200 olsun.”
Cihaz bağlandıkça sırayla dağıtır:

192.168.1.100

192.168.1.101

192.168.1.102 …

2. Neden 192.168.1.100–105?

Çünkü DHCP havuzunda şu an 6 cihaz bağlı (veya bağlanmış).

Her bağlanan cihaza modem sırayla IP veriyor.

Senin listende 100–105 arası görünüyorsa → o an 6 farklı cihaz bağlı.

Evinde 2 telefon + 1 laptop + 1 TV + 1 tablet + 1 konsol varsa → tam bu şekilde gözükür.

3. MAC Adresi nedir?

MAC = Media Access Control Address

Cihazın ağ kartının fabrikada verilen benzersiz kimliği.

48 bit uzunluğunda, genelde böyle görünür:

3C:5A:B4:2F:91:A3

Değişmez (ama yazılımla sahte MAC yapılabilir).

IP adresi değişebilir (dinamik verilir), ama MAC sabittir.

Kullanım:

Hangi cihazın kim olduğunu anlamak (ör. telefona ait mi, bilgisayara mı).

Modem üzerinden belirli cihazlara izin/verme-engelleme (ör. komşu bağlanıyorsa banlamak).

Özet:

DHCP: Cihazlara IP’yi otomatik dağıtır.

IP adresi (192.168.1.x): O an cihazın aldığı geçici adres.

MAC adresi: Cihazın değişmeyen fiziksel kimliği.

# Bakır kablo, fiber kablo ve wireless (kablosuz) ağlar, ağlarda fiziksel katmanda (OSI Layer 1) kullanılan iletişim ortamını / taşıyıcıyı ifade eder. 
Yani “veri sinyalinin nasıl iletildiğini” anlatır.

1. Bakır Kablo (Copper Cable)

Ethernet kabloları (UTP, STP, coaxial) genelde bakır tellerden yapılır.

Veriyi elektrik sinyali olarak taşır.

Avantajları:

Ucuz

Kurulumu kolay

Kısa mesafelerde (100 m’ye kadar) yaygın

Dezavantajları:

Uzun mesafede sinyal zayıflar (attenuation)

Elektromanyetik parazitlere (EMI) duyarlı

Fiber kadar hızlı değil

Kullanım: Ev interneti, ofis LAN bağlantıları

2. Fiber Optik Kablo

Veriyi ışık sinyali (lazer/LED) ile taşır.

Cam/plastik liflerden yapılmıştır.

Avantajları:

Çok yüksek hız (Gbps → Tbps seviyeleri)

Çok uzun mesafe (kilometrelerce, zayıflama çok az)

Elektromanyetik parazitlerden etkilenmez

Dezavantajları:

Daha pahalı

Kırılgan, montajı uzmanlık ister

Kullanım: ISS’lerin omurga hatları, FTTH (Fiber to the Home), veri merkezleri

3. Wireless Network (Kablosuz)

Veriyi radyo dalgaları ile taşır. (Wi-Fi, 4G/5G, Bluetooth vb.)

Avantajları:

Kablo gerektirmez → mobil cihazlar için ideal

Esneklik, kolay kurulum

Dezavantajları:

Kapsama alanı sınırlı (duvarlardan etkilenir)

Kablosuz parazit olabilir (mikrodalga, Bluetooth çakışması vs.)

Genelde kabloya göre daha düşük hız / daha yüksek gecikme

Kullanım: Evde Wi-Fi, mobil internet, IoT cihazlar

Kısa Özet:

Bakır → Elektrik sinyali, ucuz ama mesafe/hız sınırlı.

Fiber → Işık sinyali, çok hızlı ve uzun mesafe, pahalı.

Wireless → Radyo dalgaları, kablosuz özgürlük, ama parazite ve güvenliğe dikkat.


# Kıtalar Arası İletişimde Hangi Ortam Kullanılır?
1. Fiber Optik Kablolar (Denizaltı Kabloları)

Dünyadaki kıtalar arası internet trafiğinin %95’inden fazlası deniz altındaki fiber optik kablolar üzerinden taşınır.

Bu kablolar okyanusların dibine döşenir.

Neden fiber?

Çok yüksek kapasite (Tbps seviyelerinde)

Çok uzun mesafe (binlerce km)

Elektromanyetik parazite dayanıklı

Örnek: SEA-ME-WE 5 (South East Asia – Middle East – Western Europe) kablosu Türkiye’den de geçiyor.

2. Uydu Haberleşmesi

Yedek ve özel kullanım için vardır ama toplam internet trafiğinin %5’inden azını taşır.

Dezavantajı:

Gecikme çok yüksek (özellikle jeostatik uydularda ~600 ms).

Kullanım alanı:

Uzak bölgeler (kutup, dağ, deniz)

Askeri veya acil durum haberleşmesi

Starlink gibi alçak yörünge (LEO) uyduları yeni nesil çözüm.

3. Bakır Kablo?

Kıtalar arası asla kullanılmaz. Çünkü kısa mesafe için uygun, binlerce km’ye dayanmaz.

4. Wireless (Mikrodalga / Radyo Link)?

Kıtalar arası kullanılmaz.

Sadece kısa mesafelerde (örneğin iki bina arasında) tercih edilir.

Özet:

Kıtalar arası iletişimde ana taşıyıcı fiber optik kablolardır.

Uydu ise sadece destekleyici/alternatif bir rol oynar. 

# IP Address (IP Adresi), IPv4 ve IPv6 formatı ne demek? IP nasil alınır? MAC adresi ile ilişkili mi?

1. IP Adresi Nedir?

IP (Internet Protocol) adresi, bir cihazın ağ üzerindeki kimliğidir.

Aynı senin ev adresin gibi düşün: Paket (data) hangi eve (cihaza) gideceğini IP adresiyle bulur.

Her cihazın ağda benzersiz bir IP’si olmalı.

2. IP Nasıl Alınır?

2 yöntem var:

Dinamik IP (DHCP üzerinden)

En yaygın yöntem.

Modemin üzerinde çalışan DHCP sunucu otomatik IP dağıtır.

Örn: Telefonunu Wi-Fi’ye bağladığında, modem sana otomatik bir IP verir (192.168.1.105 gibi).

Statik IP

Manuel olarak elle ayarlanır.

Örn: Server’a her zaman aynı IP’den erişilmesi gerekiyorsa.

3. IP ile MAC Adresi İlişkisi

MAC adresi = Cihazın fiziksel kimliği (donanım kartının fabrikadan gelen numarası).

IP adresi = Ağdaki geçici/lojik kimliği.

İlişki:

IP → MAC eşleştirmesini ağda ARP (Address Resolution Protocol) yapar.

Yani sen 192.168.1.105’e paket göndermek istediğinde, önce “Bu IP hangi MAC’e ait?” diye sorulur.

Önemli fark:

MAC = Sabit (donanım kimliği, değişmez → ama spoof yapılabilir)

IP = Dinamik/Değişken (DHCP’den yeni IP alabilir)

4. IPv4 ve IPv6 Farkı
IPv4:

32 bit adres → xxx.xxx.xxx.xxx formatında

Örn: 192.168.1.105

Yaklaşık 4.3 milyar adres → artık yetersiz hale geldi

IPv6:

128 bit adres → daha uzun ve karmaşık

Örn: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

Neredeyse sınırsız adres kapasitesi (2^128)

Daha güvenli, daha hızlı yönlendirme için tasarlandı

Yeni cihazlarda IPv6 desteği zorunlu

Özet:

IP = Ağdaki adres, cihazı tanımlar.

DHCP’den otomatik alınır ya da elle verilir.

IP → MAC eşleştirilerek çalışır.

IPv4 (32 bit, 4 milyar adres) artık dar geldiği için → IPv6 (128 bit, devasa kapasite) kullanılmaya başlandı.

# 1. IP adresi neden karışmıyor?

192.168.x.x gibi adresler aslında özel (private) IP adresleridir.

Bu adresler ev veya işyeri içindeki yerel ağda (LAN) kullanılır.

Yani senin evindeki 192.168.1.105 ile benim evimdeki 192.168.1.105 aynı anda olabilir, çünkü bu adresler internette görünmez.

Dış dünyaya çıkarken (ör. Google’a bağlanırken) modem, NAT (Network Address Translation) denilen mekanizma ile senin cihazının iç IP’sini kendi dış IP’sine çevirir.

İnternette görünen adres aslında modemine ISS (Turkcell, Türk Telekom, Superonline vb.) tarafından verilen public (genel) IP adresidir.

Yani internette sen sadece tek bir IP (modeminin dış IP’si) ile görünürsün.

2. MAC adresi ile ilişkisi

MAC adresi, cihazının ağ kartına üretici tarafından verilen donanımsal ve değişmez bir kimliktir (ör: D4:5E:7A:12:34:56).

Modem (DHCP servisi) cihazları ayırt etmek için MAC adresini tanır ve ona uygun bir IP verir.

Yani senin laptopun her bağlandığında modem onun MAC adresini görüp “tamam bu cihaz, ben buna 192.168.1.105 vereyim” diyebilir.

3. IPv4 ve IPv6 farkı

IPv4: 32-bit adres → 4 sayıdan oluşur (0–255 arası). Örnek: 192.168.1.105

Toplam ~4 milyar adres vardır (yetersiz kalmaya başladı).

IPv6: 128-bit adres → çok daha uzun. Örnek: fe80::5e63:bfff:fefe:f828

Milyarlarca kat daha fazla cihaz adreslenebilir.

Yavaş yavaş dünyada yaygınlaşıyor ama hâlâ çoğunluk IPv4 kullanıyor.

Özet:

Evde gördüğün 192.168.1.x adresleri sadece iç ağda geçerli.

Dışarıya çıkınca modem senin adına tek bir public IP ile internete bağlanıyor.

O yüzden karışma olmuyor.

# 1. Senin bilgisayarının IP adresleri

LAN (Local Area Network / yerel ağ)

Modemden DHCP ile aldığın private IP (ör. 192.168.1.105).

Bu IP sadece evde, modeminin içinde geçerli.

WAN (Wide Area Network / geniş ağ - internet)

İnternete çıkarken modem, senin private IP’ni kendi public IP’sine çevirir (NAT sayesinde).

İnternette herkes senin public IP’ni görür (ör. 88.245.137.42).

Yani senin bilgisayarında private IP var, ama dış dünyada siteler senin modeminin public IP’sini görüyor.

2. Aynı anda kaç IP adresin var?

Genelde:

En az 2 tane:

Private IP (LAN) → 192.168.1.xxx

Public IP (WAN) → ISS’den alınan → x.x.x.x

Ama ek olarak:

IPv6 açıksa, bir de IPv6 adresin olur (ör: fe80::5e63:bfff:fefe:f828).

VPN kullanıyorsan, VPN’in sana verdiği ek bir IP daha olur.

3. Kendi IP adreslerini nasıl görebilirsin?

Windows’ta:

Komut satırını aç → ipconfig yaz → Private IP adresini (192.168.1.xxx) görürsün.

Public IP’ni görmek için:

Tarayıcıdan whatismyip.com
 veya Google’a “what is my IP” yaz → dış IP’ni görürsün.

Özet:

Sen bilgisayarında private IP kullanıyorsun.

İnternette gezerken modem onu tek bir public IP’ye çeviriyor.

Yani senin gözünden bakarsak LAN’da bir IP, WAN’da bir IP var.

Sen internete çıktığında, senin bilgisayarının IP’si değil modeminin (daha doğrusu ISS’nin sana verdiği public IP) görünüyor.

Basit akış:

Senin bilgisayarın → private IP (ör. 192.168.1.105)

Modemin bu private IP’yi alıp → kendi public IP’sine çeviriyor (NAT işlemi).

İnternette gezdiğin siteler → public IP’ni görüyor (ör. 88.245.xx.xx).

Önemli Nokta

Aynı evde 5 cihaz (telefon, laptop, TV vs.) olsa bile, hepsi dışarıya aynı public IP ile çıkar.

Siteler, hepsini tek kişiymiş gibi görür.

Ama modem içinde (LAN tarafında) her cihazın farklı private IP’si vardır (192.168.1.101, 192.168.1.102, ...).

Yani özetle:
İnternette gezerken sen “modeminin IP’siyle” geziyorsun.

# NAT (Network Address Translation)

NAT = Ağ Adres Çevirisi demek.

Evde kullandığın IP’ler (192.168.x.x gibi) → private IP’lerdir. Bunlar internette geçerli değildir.

Modem, senin private IP’ni tek bir public IP’ye çevirir ve internete gönderir.

Bu sayede evde 10 cihaz olsa bile, hepsi tek public IP üzerinden internete çıkar.

Örnek:

Bilgisayarın: 192.168.1.101

Telefonun: 192.168.1.102

Modemin dış IP’si (public): 88.245.22.19

Sen Google’a girince modem şunu yapar:
192.168.1.101 → 88.245.22.19:port12345
192.168.1.102 → 88.245.22.19:port23456

Yani sadece IP değil, port numaralarıyla da ayırır. Böylece siteler seni tek IP olarak görür ama modem içeride kimin hangi cihaz olduğunu bilir.

ISS (İnternet Servis Sağlayıcı)

ISS (ISP - Internet Service Provider) = Sana interneti sağlayan firma.
Türkiye’de örnekler: Türk Telekom, TurkNet, Superonline, Vodafone Net …

ISS, modemine bir public IP adresi verir.

Senin internette gördüğün dış IP aslında ISS’nin sana geçici olarak verdiği adrestir.

ISS ayrıca sana DNS, bant genişliği, hız limitleri gibi hizmetleri de sunar.

Özet:

NAT: Modemin evdeki cihazların private IP’lerini public IP’ye çeviren sistem.

ISS: İnternete çıkmanı sağlayan servis sağlayıcı firma.

# Senin WhatIsMyIP çıktının anlamı:
IPv4: 78.173.11.70

Bu, dış dünyaya görünen asıl IP adresin.

TTNET (Türk Telekom) sana bunu vermiş.

İnternette girdiğin siteler seni bu adres üzerinden tanıyor.

IPv6: 2a00:1d34:f4ce:1801:fd35:9fe9:8f4c:7935

IPv6 adresin de aktif görünüyor.

IPv4 adresleri dünya genelinde yetersiz kalmaya başladı. IPv6 bu sorunu çözmek için geliştirildi.

IPv6 çok daha uzun, çok daha fazla cihazın adreslenmesini sağlıyor.

Hostname:

IPv6 adresinle eşleşen alan adı gibi düşünebilirsin.

Burada özel bir hostname atanmamış, direkt IP görünüyor.

ASN: 47331

ASN (Autonomous System Number) → internet servis sağlayıcılarının ve büyük ağların kimlik numarasıdır.

Seninki 47331 – TTNET A.Ş.

Yani bu IP’nin hangi şirkete ait olduğunu gösteriyor.

ISP: TTNET A.S.

İnternete çıkmanı sağlayan ISS (İnternet Servis Sağlayıcı) → Türk Telekom.

Country/Region/City:

Türkiye / İstanbul görünüyor.

Bu, senin bulunduğun yerin yaklaşık konumunu gösteriyor.

Ama genelde %100 doğru olmaz, çünkü IP adresleri bölgesel bloklar halinde verilir.

Yani sen aslında İstanbul dışında da olabilirsin ama IP’nin kaydı İstanbul bölgesinde gözüküyor.

Latitude / Longitude:

IP adresinin kayıtlı olduğu merkezin yaklaşık koordinatları.

GPS değil! Yani telefonunun gerçek konumunu değil, IP’nin kayıtlı olduğu noktayı verir.

Bundan ne anlamalısın?

Dış IP adresin (78.173.11.70) → internette seni temsil eden adres.

ISP’in TTNET → yani IP’yi sana sağlayan kurum Türk Telekom.

Konum bilgisi → çok kesin değil, sadece “hangi şehir/bölge” seviyesinde.

IPv6 → senin hattında aktif, yani cihazların isterse IPv6 üzerinden de internete çıkabilir.

Yani özetle:
Sen internete çıktığında, web siteleri seni “TTNET’in İstanbul’daki 78.173.11.70 IP’si” olarak görüyor.
Ama evdeki private IP’lerin (192.168.x.x) görünmüyor.

# Gateway (Ağ Geçidi) çoğu ev ortamında modem veya modem+router cihazıdır.
Ama aslında kavram biraz daha geniştir.

Gateway (Ağ Geçidi) nedir?

Bir ağdan başka bir ağa çıkışı sağlayan cihaztır.

Senin bilgisayarın yerel ağda (LAN, 192.168.x.x) çalışır.

İnternete çıkabilmesi için bu LAN’dan WAN’a (geniş ağa) geçmesi gerekir.

İşte gateway burada devreye girer → genelde modem/router’dır.

Evde senin durumun

Bilgisayarının IP’si: 192.168.1.105 gibi.

Gateway: 192.168.1.1

Yani sen bilgisayarında internete çıkarken:
“Bilmiyorsam, tüm trafiği 192.168.1.1’e (modeme) gönder” dersin.

Modem ise → ISS’ye gönderir → internet.

Gateway her zaman modem midir?

Evlerde: Evet, modem/router cihazı gateway görevi görür.

Şirketlerde: Gateway genellikle router veya firewall olur (modemden ayrı).

Büyük ağlarda: Gateway, farklı ağları birbirine bağlayan router cihazları olabilir.

Özet:

Gateway = Senin bilgisayarın için “internetin kapısı”.

Evde bu genellikle modem (hem modem hem router).

Şirkette/gelişmiş ağlarda → ayrı router veya firewall olabilir.

# Bilgisayar internete nasıl çıkıyor?

Senin bilgisayarın diyelim ki şu IP’ye bağlanmak istiyor:
142.250.74.14 (Google’ın bir IP’si).

Bilgisayar şöyle düşünüyor:

“Benim kendi ağım 192.168.1.x ile başlıyor.”

“Ama bu IP (142.250.74.14) benim ağımda değil.”

“O zaman bunu ağ geçidine (gateway) göndermem lazım.”

Yani bilmediği tüm adresleri gateway’e yollar.

Gateway ne yapıyor?

Senin gateway’in (ör: 192.168.1.1 modem/router):

Senin isteğini alıyor.

“Bu cihaz 192.168.1.105 Google’a gitmek istiyor” diyor.

Kendi public IP’siyle (ör: 78.173.11.70) isteği ISS’ye iletiyor.

ISS de bunu internete yönlendiriyor.

Basit benzetme

Sen = Bilgisayar (sadece ev adresini biliyorsun).

Gateway = Postane (bilmiyorsan, tüm mektupları oraya veriyorsun).

ISS = PTT sistemi / dağıtıcı (mektubu tüm ülkeye, sonra dünyaya gönderiyor).

İnternet = Dünya (hangi eve/makineye ulaşacağını ISS biliyor).

Özet:

Gateway = bilgisayarının internet kapısıdır.

Bilgisayar “benim yerel ağımın dışında bir adres” görünce → gateway’e yollar.

Modem/gateway ise ISS üzerinden internete çıkarır.

# Bilgisayar her yeni ağ isteği gönderdiğinde şunu yapar:

🔹 Nasıl çalışıyor?

Hedef IP’yi kontrol eder:

Hedef IP (örn. 142.250.74.14) LAN (192.168.1.x) içinde mi değil mi diye bakar.

Routing tablosuna bakar:

Bilgisayarın içinde küçük bir tablo vardır → hangi IP aralığı LAN içinde, hangi IP dışarıda (internet) diye listelenir.

Örnek: 192.168.1.0/24 → LAN, diğerleri → gateway’e gitmeli.

LAN içinde değilse → Gateway’e gönderir:

LAN IP değil → bilgisayar “bu paketi ağ geçidine ver” der.

Gateway (modem/router) ise NAT ile paketleri internete yollar.

Özet

Her istek için kontrol edilir, ama çok hızlıdır → sen fark etmezsin.

Bilgisayar her paketi tek tek kontrol etmez, sadece hedef IP’ye bakar ve routing tablosu ile karar verir.

Bu sayede LAN içi ile internet trafiği doğru şekilde ayrılır.

# WWW (World Wide Web) nedir?

WWW, internet üzerinde çalışan bir servistir.

İnternet = altyapı (kablolar, IP, routerlar).

WWW = bu altyapının üstünde çalışan bir uygulama sistemi (web siteleri).

Yani internet varsa ama WWW olmayabilir.
Mesela e-posta (SMTP), dosya transferi (FTP) de internet üzerinde çalışır ama WWW değildir.

WWW’nin farkı:

Web sitelerini tarayıcı (browser) üzerinden görmemizi sağlar.

HTTP/HTTPS protokolü ile çalışır.

İçerikler → HTML sayfaları, resimler, videolar, linkler.

WWW ne zaman ve kim tarafından bulundu?

1989: Tim Berners-Lee (İsviçre, CERN’de bilim insanı) tarafından önerildi.

1990: İlk web tarayıcısı (WorldWideWeb adında) yazıldı.

1991: WWW sistemi kamuya açıldı. İlk web sitesi http://info.cern.ch/ oldu.

Yani WWW’nin doğduğu yer: CERN (Avrupa Nükleer Araştırma Merkezi, İsviçre)

İlk kullanım amacı

CERN’deki bilim insanlarının araştırma verilerini ve dokümanlarını birbirleriyle paylaşabilmesi.

Yani aslında akademik bilgi paylaşımı için tasarlandı.

Sonra hızla büyüyerek dünyadaki tüm web sitelerinin temelini oluşturdu.

Özetle

WWW (World Wide Web) = internet üzerindeki web sayfaları ağı.

İlk yer: CERN, İsviçre.

İlk tarih: 1989–1991.

Kurucu: Tim Berners-Lee.

İlk site: http://info.cern.ch

# 1. WWW nerede kullanılır?

URL’lerde (adres çubuğunda) görürsün → https://www.google.com gibi.

Aslında www = sadece bir subdomain (alt alan adı).

Yani teknik olarak google.com ile www.google.com farklı adreslerdir, ama çoğu site bunları aynı yere yönlendirir.

2. Site isimlerinde şart mı?

Hayır, şart değil.

Bir site www kullanmadan da çalışır → örnek: https://twitter.com

Hatta günümüzde çoğu site kısa olsun diye www’siz kullanıyor.

3. Kullanmasak ne olur?

Hiçbir şey olmaz 

Sitenin sahibi isterse www kullanır, isterse kullanmaz.

DNS ayarlarına bağlıdır. Yani yönlendirmeyi yapan site sahibidir.

4. Kullanmayıp sadece alan adını kullanan var mı?

Evet, çok fazla!

Örn: facebook.com, youtube.com, twitter.com → çoğu modern site artık www kullanmıyor.

Bazıları ise geleneksel olarak hala www ile çalışıyor (örn: www.wikipedia.org).

5. WWW’yi kim yönetiyor?

WWW tek bir firma tarafından yönetilmez.

Temellerini kuran kişi → Tim Berners-Lee.

Şu anda W3C (World Wide Web Consortium) denen bir organizasyon tarafından standartları belirleniyor (HTML, CSS, Web protokolleri vs.).

Ama her sitenin kendi www subdomain’i site sahibinin kontrolündedir.

6. WWW bir firmanın mı?

Hayır 

WWW = internet üzerindeki web sayfaları ağı → açık standarttır.

Ne Google’a, ne Microsoft’a, ne başka bir şirkete aittir.

Tüm dünya kullanır, geliştirmeler de W3C gibi bağımsız kuruluşlar tarafından yapılır.

Özet:

www sadece subdomain, şart değil.

Eskiden alışkanlık olduğu için yaygındı, şimdi çoğu site kısaltıyor.

WWW servisi → bir firmanın değil, tüm dünyanın ortak kullandığı sistem.

# OSI Modeli konusu ağları anlamak için çok temel. Adım adım açıklayayım:

1. OSI Modeli Nedir?

OSI = Open Systems Interconnection

Açık Sistemler Bağlantısı demek.

Amaç: Farklı üreticilerin cihazlarının ve yazılımların birbiriyle iletişim kurmasını sağlamak.

Ağ iletişimini 7 katmana ayırır → her katmanın ayrı bir görevi vardır.

2. OSI’nin 7 Katmanı (Layer)
Katman	İngilizce	Görev / Ne Yapar?
7	Application	Uygulama katmanı → tarayıcı, e-posta, web servisleri gibi kullanıcıya yakın katman
6	Presentation	Sunum katmanı → veriyi dönüştürür, şifreler, sıkıştırır (örn. .jpg, .mp3)
5	Session	Oturum katmanı → cihazlar arası bağlantıyı açar, kapatır, yönetir
4	Transport	Taşıma katmanı → veri paketlerini böler ve sıralar (TCP, UDP)
3	Network	Ağ katmanı → IP adresleme, paketlerin yönlendirilmesi (routerlar)
2	Data Link	Veri Bağlantı katmanı → MAC adresleri, LAN içi paket iletimi (switchler)
1	Physical	Fiziksel katman → kablolar, fiber, sinyaller, elektrik/optik dalgaları

3. Katmanlar arasındaki mantık

En alttan (Layer 1) en üste (Layer 7) doğru → veri gidip gelirken hangi işleme uğruyor belirlenir.

Örnek: Web sayfası açtığında

Layer 7: Tarayıcı → “google.com sayfasını istiyorum”

Layer 4: TCP → veriyi paketlere böler

Layer 3: IP → paketlerin internette hangi yoldan gideceğini belirler

Layer 2: MAC → LAN’da hangi cihaza gidecek

Layer 1: Fiziksel → elektrik sinyali/fiber ışık ile modem/router üzerinden gider

4. Özet

OSI = ağ iletişimini 7 katmana bölen standart

Her katman kendi işi ile ilgilenir

Layer 1 = Physical → kablo, sinyal, fiber

Layer 7 = Application → tarayıcı, e-posta, web servisleri

# OSI (Open Systems Interconnection) modeli, bilgisayar ağlarında iletişimin nasıl gerçekleştiğini açıklayan 7 katmanlı bir referans modelidir. 
ISO (International Organization for Standardization) tarafından geliştirilmiştir.
OSI Modelinin 7 Katmanı:
1. Fiziksel Katman (Physical Layer)

En alt katman
Elektriksel, mekanik ve fiziksel özellikleri tanımlar
Kablolar, hub'lar, repeater'lar bu katmanda çalışır
Bit'leri elektriksel sinyallere çevirir

2. Veri Bağlantısı Katmanı (Data Link Layer)

Fiziksel katman üzerinde güvenilir iletişim sağlar
Frame'leri oluşturur ve hata kontrolü yapar
Switch'ler ve köprüler bu katmanda çalışır
MAC adresleri bu katmanda kullanılır

3. Ağ Katmanı (Network Layer)

Paketlerin yönlendirilmesini (routing) sağlar
IP adresleri bu katmanda kullanılır
Router'lar bu katmanda çalışır
En iyi yolu bulma işlevi

4. Taşıma Katmanı (Transport Layer)

Uçtan uca güvenilir veri iletimi sağlar
TCP ve UDP protokolleri bu katmanda çalışır
Segmentasyon ve akış kontrolü yapar
Port numaraları bu katmanda kullanılır

5. Oturum Katmanı (Session Layer)

Uygulamalar arasında oturum yönetimi
Bağlantı kurma, sürdürme ve sonlandırma
Senkronizasyon noktaları oluşturur

6. Sunum Katmanı (Presentation Layer)

Veri formatı dönüştürmeleri
Şifreleme ve sıkıştırma işlemleri
Karakter kodu çevrimleri (ASCII, Unicode)

7. Uygulama Katmanı (Application Layer)

En üst katman
Kullanıcıya ağ hizmetleri sunar
HTTP, FTP, SMTP, DNS gibi protokoller bu katmanda çalışır

OSI Modelinin Amacı:

Farklı üreticilerin cihazları arasında standart oluşturmak
Ağ problemlerini katman bazında çözmeyi kolaylaştırmak
Ağ mimarisini anlaşılır hale getirmek
Her katmanın kendi sorumluluğunu net olarak tanımlamak

OSI modeli teorik bir referans modelidir. Pratikte daha çok TCP/IP modeli kullanılır, ancak OSI modeli ağ kavramlarını öğrenmek ve problemleri anlamak için çok değerlidir.

# Port Nedir?

Port, bir cihazdaki “iletişim kapısı” gibi düşünebilirsin.

IP = cihazın adresi (modem/public IP)

Port = o cihazdaki hangi servise veya uygulamaya mesaj gönderileceğini belirten numara

Örnek:

IP: 88.245.22.19 → bilgisayar/modem/internet cihazı

Port: 80 → web servisi (HTTP)

Port: 443 → HTTPS (güvenli web)

Port: 3306 → MySQL veritabanı

Port: 8080 → Spring Boot uygulaması

Nasıl çalışıyor?

Ev ağında:

Bilgisayar 1: 192.168.1.101 → internete bir HTTP isteği gönderiyor → NAT ve modem sayesinde public IP üzerinden çıkıyor.

Modem kaydeder: 192.168.1.101 → 88.245.22.19:port12345

Bilgisayar 2: 192.168.1.102 → 88.245.22.19:port23456

Yani modem, aynı public IP’yi kullanan birden fazla cihazı “port numarası” ile ayırt ediyor.
Bu sayede siteler veya servisler hangi cihazın hangi isteği yaptığını bilir.

Portta yayın yapmak ne demek?

Bir uygulama veya servis, belirli bir port üzerinden gelen bağlantıları dinler.

Örnek Spring Boot:

http://localhost:8080 → uygulama 8080 portunu dinliyor.

localhost:3306 → MySQL veritabanı 3306 portunu dinliyor.

Modem tarafında da port var, ama genelde sadece NAT ve yönlendirme için kullanılır:

Örn. “Dışarıdan 8080 portuna gelen istek → LAN’daki 192.168.1.101:8080’e gönder”

Özet

IP = cihaz, port = o cihazdaki kapı

Port sayesinde bir cihazda birden fazla servis çalışabilir (web, db, oyun sunucusu, vs.)

Modem NAT ile public IP + port üzerinden LAN cihazlarını ayırt eder

Spring Boot / DB portu örneği = uygulama veya servis hangi “kapıdan” dinleyeceğini belirler

# Nasıl çalışıyor?

Hedef IP’yi kontrol eder:

Hedef IP (örn. 142.250.74.14) LAN (192.168.1.x) içinde mi değil mi diye bakar.

Routing tablosuna bakar:

Bilgisayarın içinde küçük bir tablo vardır → hangi IP aralığı LAN içinde, hangi IP dışarıda (internet) diye listelenir.

Örnek: 192.168.1.0/24 → LAN, diğerleri → gateway’e gitmeli.

LAN içinde değilse → Gateway’e gönderir:

LAN IP değil → bilgisayar “bu paketi ağ geçidine ver” der.

Gateway (modem/router) ise NAT ile paketleri internete yollar.

Özet

Her istek için kontrol edilir, ama çok hızlıdır → sen fark etmezsin.

Bilgisayar her paketi tek tek kontrol etmez, sadece hedef IP’ye bakar ve routing tablosu ile karar verir.

Bu sayede LAN içi ile internet trafiği doğru şekilde ayrılır.

# Port Nedir?
Port, bir IP adresinde çalışan farklı servisleri/uygulamaları ayırt etmek için kullanılan 16 bit'lik sayılardır (0-65535 arası).
Modemde Port Kullanımı (NAT - Network Address Translation):
Modemin yaptığı işlem:
İç Ağ (LAN)          →    Dış Ağ (WAN)
192.168.1.101:3456   →    88.245.22.19:12345
192.168.1.102:8080   →    88.245.22.19:23456
192.168.1.103:443    →    88.245.22.19:34567
Modem bu mapping'i nasıl yapar:

Bir cihaz dışarıya istek gönderdiğinde
Modem bu isteği kendi public IP'si + rastgele port ile dışarıya iletir
Cevap geldiğinde, hangi iç cihaza göndereceğini port numarasından anlar

Spring Boot'taki Port Kavramı:
Spring Boot projenizde gördüğünüz durum:
java# application.properties
server.port=8080              # Spring Boot uygulaması
spring.datasource.url=jdbc:mysql://localhost:3306/mydb  # MySQL
Burada:

8080 portu: Spring Boot web uygulamanız çalışıyor
3306 portu: MySQL veritabanı çalışıyor
Aynı makine (localhost) üzerinde farklı servisler

Port Kavramının Genel Mantığı:
Bir bilgisayarda aynı anda birçok uygulama çalışabilir:
IP: 192.168.1.100
├── Port 80   → Apache Web Server
├── Port 22   → SSH Server  
├── Port 3306 → MySQL Database
├── Port 8080 → Spring Boot App
└── Port 5432 → PostgreSQL
Analoji:
IP Adresi = Apartman adresi
Port = Daire numarası
192.168.1.100:8080 = "192.168.1.100 adresindeki 8080 numaralı servise git"
Yaygın Port Numaraları:
java// Well-known ports (0-1023)
80   → HTTP
443  → HTTPS  
22   → SSH
21   → FTP
25   → SMTP (Email)
3306 → MySQL
5432 → PostgreSQL

// Spring Boot default
8080 → Spring Boot web app
8443 → Spring Boot HTTPS
Özet:

Modemde port: Farklı iç cihazları ayırt etmek için NAT mapping
Uygulama geliştirmede port: Aynı makinede farklı servisleri ayırt etmek için
Temel mantık: Aynı IP'de birden fazla servisi çalıştırabilmek

Evet, hem modem hem de bilgisayarınız port kavramını kullanır, sadece farklı amaçlarla!

# Modem Gerçekte Şunu Yapar:
İÇ AĞDAN GELEN İSTEK:
192.168.1.101:3456 → google.com:80

MODEM BUNU KAYDEDER:
İç: 192.168.1.101:3456  ↔  Dış: 88.245.22.19:3456
Modem kaydettiği bilgiler:

Hangi iç IP'den geldi (192.168.1.101)
Hangi iç port'tan geldi (3456)
Hangi dış port kullandı (3456 - genelde aynı)
Hedef adres (google.com:80)

Cevap Geldiğinde:
GOOGLE'DAN CEVAP:
google.com:80 → 88.245.22.19:3456

MODEM NAT TABLOSUNA BAKAR:
"88.245.22.19:3456'ya gelen bu cevabı 
 192.168.1.101:3456'ya yönlendir