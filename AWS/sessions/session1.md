# Host, Hypervisor, Guest
1️⃣ Host (veya Host Server) 

Fiziksel makine / sunucu anlamına gelir.

İçinde işletim sistemi, CPU, RAM, disk vs. gibi donanımlar vardır.

Örneğin: Bir veri merkezinde duran gerçek sunucu kasası → bu host server.

Sanallaştırma (virtualization) yapılırken bu fiziksel kaynaklar parçalanıp farklı sanal makineler (VM) arasında paylaştırılır.

Kısaca: "Ev sahibi". Misafirlere (guest VM’lere) ortam sağlayan ana makine.

2️⃣ Hypervisor

Host’un kaynaklarını bölüştürüp sanal makineleri çalıştıran yazılım katmanıdır.

Hypervisor olmadan host üzerinde birden çok VM çalıştıramazsın.

Türleri:

Type 1 (Bare-metal): Direkt fiziksel donanım üzerinde çalışır. (VMware ESXi, Microsoft Hyper-V, Xen, KVM)

Type 2 (Hosted): Normal işletim sistemi üstünde çalışır. (Oracle VirtualBox, VMware Workstation)

Örnek: Senin bilgisayarına VirtualBox kurup içine Ubuntu VM açman → VirtualBox burada hypervisor.

3️⃣ Guest (veya Guest VM)

Hypervisor tarafından oluşturulan sanal makinelerdir.

Her biri ayrı bir işletim sistemi çalıştırır (Linux, Windows vb.).

Host’un donanım kaynaklarını hypervisor aracılığıyla kullanır.

AWS EC2 instance’larını düşünebilirsin → onlar aslında guest VM’lerdir.

Kısaca: "Misafir". Host’un kaynaklarını kiralayıp çalışan sanal sistem.

AWS’de bağlantı:

AWS veri merkezindeki fiziksel host server → donanım.

Bu donanımın üstünde çalışan hypervisor → sanallaştırma katmanı (AWS kendi Xen/KVM tabanlı hypervisor kullanıyor).

Senin oluşturduğun EC2 instance → guest VM.

# On-Demand Özellikleri

“You pay for compute capacity by the hour or the second”

Yani kullandığın kadar ödersin.

Örneğin EC2 instance’ı 2 saat çalıştırırsan → sadece 2 saatlik ücret ödersin.

Uzun vadeli bir taahhüt gerekmez.

“No commitments” (Taahhüt yok)

1 yıl / 3 yıl sözleşme yapmak zorunda değilsin.

Kullan, kapat → fatura sadece kullandığın kadar.

“No upfront payments” (Peşin ödeme yok)

Başlangıçta toplu bir ödeme yapmazsın.

Sadece kullanıldığı anda ücretlendirme yapılır.

“You can increase or decrease your compute capacity” (İhtiyaca göre artır/azalt)

Aniden daha fazla kapasiteye ihtiyacın olursa hemen yeni instance açabilirsin.

Trafik düştüğünde instance kapatıp maliyeti azaltabilirsin.

“Pre-estimated”

Maliyeti öngörmesi kolaydır çünkü sadece kullandığın süreyi ödersin.

Sürpriz maliyetler genelde olmaz (ama çok uzun süre çalıştırırsan Reserved daha ucuz olur).

On-Demand Kullanım Senaryoları

Düşük maliyet ve esneklik isteyen kullanıcılar

“Ben uzun vadeli sözleşme istemiyorum, sadece gerektiğinde çalıştırayım” diyorsan.

Kısa vadeli, dalgalı veya öngörülemez iş yükleri

Örneğin:

Yeni bir uygulama test ediyorsun.

Bir proje için birkaç hafta süreyle sunucu lazım.

Trafiğin aniden artabilir (kampanya, sezonluk yoğunluk).

Kesintiye uğramaması gereken uygulamalar

Spot Instances ucuzdur ama kesilebilir.

On-Demand ise kesilmez, istediğin kadar çalışır.

Kısaca:

Kısa süreli, belirsiz veya test amaçlı işler → On-Demand

Uzun süreli, sürekli çalışacak işler → Reserved / Savings Plans daha mantıklı olur.

Esneklik ve risksiz çalışma istiyorsan → yine On-Demand seçilir.

# Reserved Instance (RI) Nedir?

Uzun vadeli kiralama mantığıdır.

Bir EC2 instance’ını 1 yıl veya 3 yıl taahhütle rezerve edersin.

Bunun karşılığında %40 – %72’ye varan indirim kazanırsın.

Yani On-Demand’a göre çok daha ucuzdur.

🔹 Özellikleri

Uzun süreli kullanım için tasarlanmıştır

1 yıl veya 3 yıl boyunca kapasiteyi garanti etmiş olursun.

Daha ucuz maliyet

On-Demand’e göre ciddi indirim sağlar.

Ödeme seçenekleri:

All Upfront → Peşin ödersin, en ucuz fiyat.

Partial Upfront → Bir kısmı peşin, kalanı aylık.

No Upfront → Hiç peşin ödeme yok, ama aylık taksit.

Kapasite rezervasyonu sağlar (özellikle yoğun bölgelerde avantajlıdır).

Instance Type ve Region’a bağlıdır

Örn: m5.large için eu-central-1 (Frankfurt) bölgesinde rezervasyon yaptıysan, başka bölgede geçerli olmaz.

Ama “Convertible RI” seçersen → benzer instance türlerine dönüştürebilirsin.

🔹 Ne Zaman Kullanılır?

Sürekli çalışan uygulamalar için

Örn: Şirketin web sitesi her zaman çalışıyor → 7/24 aktif → Reserved daha ucuz.

Tahmin edilebilir iş yükleri için

Örn: Her ay düzenli çalışan bir veritabanı, ERP sistemi, kurumsal uygulama.

Uzun vadeli projelerde

En az 1 yıl boyunca bu sunucuyu kullanacağından eminsen.

# Scheduled Reserved Instance (Scheduled RI) Nedir?

Normal Reserved Instance (RI) gibi indirimli fiyat sunar,
ama farkı şudur:
Belirli zaman aralıklarında (örneğin haftanın belirli günleri, günün belirli saatleri) kullanılacak şekilde planlanır.

Yani instance 7/24 çalışmaz, sadece senin önceden belirlediğin zaman dilimlerinde aktif olur.

🔹 Özellikleri

Belirli zaman aralıkları için kapasite rezerve edilir:

Örn: Pazartesi–Cuma günleri, saat 09:00–18:00 arası.

Bu saatler dışında instance çalışmaz ve ücret ödemezsin.

Daha düşük maliyet sağlar çünkü 7/24 ödeme yapmazsın, sadece planlı süre için ödeme yaparsın.

Kapasite garantisi verir

O belirlenen saatlerde sana instance kesinlikle ayrılmış olur.

Genelde 1 yıllık taahhütle alınır.

🔹 Ne Zaman Kullanılır?

Düzenli ama kesintili iş yüklerinde:

Ofis saatlerinde çalışan uygulamalar.

Hafta içi mesai saatlerinde kullanılan sistemler.

Belirli zamanlarda çalışan batch job’lar veya raporlama uygulamaları.

Maliyet optimizasyonu gereken senaryolarda:

7/24 çalışan RI almak gereksiz pahalıysa → Scheduled RI daha uygun olur.

🔹 Örnek Senaryolar

Bir şirketin mesai saatlerinde kullanılan muhasebe yazılımı → sadece 09:00–18:00 arası lazım.

Sınav veya etkinlik uygulaması → sadece hafta sonu veya belli günlerde çalışıyor.

Batch processing / raporlama sistemi → her gece 3 saatlik işlem yapıyor.

# Spot Instance Nedir?

AWS Spot Instance'ları, Amazon'un kullanılmayan EC2 kapasitesini büyük indirimlerle (normal fiyatın %50-90'ına kadar) sunan bir hizmetidir.
Spot Instance Nasıl Çalışır?
Spot Instance'lar açık artırma modeline benzer bir sistemle çalışır:

AWS'nin boşta kalan kapasitesini kullanırsınız
Normal EC2 fiyatlarına göre çok daha ucuza erişirsiniz
AWS kapasiteye ihtiyaç duyduğunda, 2 dakika önceden uyararak instance'ınızı sonlandırabilir

Ne Zaman Tercih Edilmeli?
İdeal Kullanım Senaryoları:

Batch işlemler ve veri analizi - Kesintiye toleranslı, yeniden başlatılabilen işler
Big Data ve makine öğrenimi - Eğitim süreçleri, büyük veri işleme
CI/CD pipeline'ları - Test ve build süreçleri
Rendering ve medya işleme - Video encoding, 3D rendering
Web crawling ve scraping
Stateless uygulamalar - Containerized mikroservisler

Tercih Edilmemeli:

Kritik production veritabanları
Kesintiye toleransı olmayan uygulamalar
Uzun süren, checkpoint alınamayan işler
Yüksek kullanılabilirlik gerektiren sistemler

Best Practice'ler:

Checkpoint mekanizması kullanın - İş ilerlemenizi kaydedin
Spot Fleet veya Auto Scaling ile birden fazla instance tipini hedefleyin
Interruption handling kodlayın - 2 dakikalık uyarıyı yakalayın
Flexible instance tipleri seçin - Farklı instance ailelerini karıştırın
Spot + On-Demand karışımı kullanın - Hibrit yaklaşım daha güvenli

Örneğin, bir makine öğrenimi modelini eğitiyorsanız ve düzenli checkpoint alıyorsanız, Spot Instance mükemmel bir seçenektir. 
Ancak production'da 7/24 çalışması gereken bir API sunucusu için uygun değildir.

# Dedicated Instance Nedir?

AWS’de çalıştırdığın EC2 instance’ın, yalnızca senin hesabına ayrılmış fiziksel sunucular üzerinde çalışmasıdır.

Normalde On-Demand / Spot / RI instance’lar başka müşterilerin sanal makineleriyle aynı fiziksel host üzerinde olabilir.

Ama Dedicated Instance seçersen → o fiziksel sunucuda sadece senin account’unun instance’ları olur.

🔹 Özellikleri

Aynı fiziksel donanımda başka müşteri yoktur

Güvenlik / uyumluluk (compliance) isteyen kurumlar için önemlidir.

Yine de AWS’nin yönettiği bir altyapıdadır

Yani fiziksel sunucu sana özel ayrılır ama sahiplik senin değil, AWS’nin.

Fiyatlandırma

Normal EC2’den daha pahalıdır (çünkü fiziksel host’u başkalarıyla paylaşmazsın).

Uyumluluk (compliance) avantajı

Bazı sektörlerde (finans, sağlık, devlet kurumları) → “multi-tenant” (çok kiracılı) sistemler kabul edilmez.

Dedicated Instance bu durumda çözüm olur.

🔹 Ne Zaman Kullanılır?

Regülasyon / güvenlik zorunluluğu varsa:

Örn: Finans kurumları, sağlık sektörü, kamu projeleri.

“Benim verim başka müşterilerle aynı donanımda olamaz” şartı varsa.

Donanım düzeyinde ayrışma istendiğinde:

CPU cache, memory isolation gibi en alt seviyede güvenlik gerekirse.

Lisanslama gereklilikleri varsa:

Bazı lisanslı yazılımlar fiziksel ayrışma ister.

🔹 Dedicated Instance vs Dedicated Host

Dedicated Instance

Sadece senin hesabındaki instance’lar aynı fiziksel sunucuda olur.

Ama fiziksel host’un tam kontrolünü vermez.

Dedicated Host

Sana özel fiziksel sunucu verilir.

Donanımı tamamen kontrol edersin (sabit donanım kimliği, CPU soketleri, çekirdekler vs.).

Lisans yönetiminde (Windows Server, Oracle DB gibi) avantaj sağlar.

Özet:

Dedicated Instance = Fiziksel host sadece senin AWS hesabına ayrılır (başka müşteri yok).

Kullanım: Regülasyon, güvenlik, uyumluluk, özel lisanslama durumları.

Dedicated Host = Daha da ileri seviye kontrol, tüm host’u sana verir.

# Savings Plans Nedir?

AWS’nin uzun vadeli taahhüt karşılığında indirim sunduğu bir fiyatlandırma modelidir.

Sen 1 yıl veya 3 yıl boyunca belli bir compute kullanımına ($/saat) taahhüt verirsin.

Karşılığında %66’ya varan indirim alırsın.

On-Demand gibi esnektir ama RI gibi indirimlidir.

Yani: “Benim ortalama 10$/saat compute tüketimim olacak” diye söz veriyorsun → AWS sana ucuz fiyattan compute hizmeti veriyor.

🔹 Türleri

AWS 2 çeşit Savings Plans sunar:

Compute Savings Plans

En esnek olanıdır.

Taahhüt ettiğin miktarı herhangi bir instance türünde, bölgede, OS’de kullanabilirsin.

Hatta AWS Fargate ve AWS Lambda ile de geçerlidir.

Örn: Bugün m5.large Frankfurt’ta kullanıyorsun, yarın c6g.xlarge Londra’da kullanabilirsin → yine indirim uygulanır.

EC2 Instance Savings Plans

Daha az esnektir ama daha fazla indirim sağlar.

Sadece seçtiğin instance family ve region için geçerlidir (örn: m5 family, eu-central-1).

Instance boyutunu değiştirebilirsin (m5.large → m5.xlarge), ama başka family’ye (c5, t3 vs.) geçemezsin.

🔹 Ödeme Seçenekleri

All Upfront → tamamını peşin ödersin, en ucuz fiyat.

Partial Upfront → bir kısmı peşin, kalanı aylık.

No Upfront → hiç peşin yok, aylık ödersin (en esnek ama biraz daha pahalı).

🔹 Ne Zaman Tercih Edilir?

Uzun vadeli iş yüklerin varsa:

Sürekli çalışan production sistemleri (web app, veritabanı, ERP).

Maliyet optimizasyonu istiyorsan ama RI kadar katı kısıtlamalarla uğraşmak istemiyorsan.

Değişken instance tipleri veya hizmetleri kullanıyorsan (özellikle Compute Savings Plan burada ideal).

🔹 RI ile Farkı
Özellik	Reserved Instance	Savings Plans
Taahhüt	Belirli instance tipi + bölge	Belirli $ kullanım/saat
Esneklik	Düşük (özellikle SRI)	Yüksek (özellikle Compute SP)
Hizmet	Sadece EC2	EC2 + Fargate + Lambda
İndirim	%40–72	%30–66
Yönetim	Daha karmaşık	Daha basit

Özet:

Savings Plans, RI’nin daha esnek alternatifi.

Eğer sürekli compute ihtiyacın varsa (7/24 çalışan uygulamalar) ve esneklik istiyorsan → Compute Savings Plan seç.

Eğer sabit bir instance family + region’da kalacaksan → EC2 Instance Savings Plan daha ucuzdur.

# AWS, farklı kullanım senaryoları için EC2 instance tiplerini ailere (families) ayırıyor. Bunlardan en temel olanı General Purpose.

# General Purpose Instances Nedir?

Adından da belli: Genel amaçlı iş yükleri için tasarlanmış, dengeli bir instance tipidir.

CPU, RAM ve Network kaynakları dengelidir → ne çok CPU yoğun, ne de çok bellek yoğun.

En çok kullanılan instance ailesidir çünkü çoğu uygulama bu dengeyi ister.

🔹 Örnek Aileler

T serisi (örn: t3, t4g)

Burstable (patlamalı) performans sağlar → düşük sürekli yük, ama ara sıra CPU artışı.

Örn: Blog sitesi, küçük web app.

M serisi (örn: m5, m6g)

Daha istikrarlı ve güçlü → CPU & RAM dengesi.

Örn: Orta ölçekli uygulamalar, backend servisleri, küçük veritabanları.

A serisi (a1)

ARM tabanlı, düşük maliyetli genel amaçlı instance.

🔹 Ne Zaman Kullanılır?

Web sunucuları (web app, backend API)

Küçük/orta ölçekli veritabanları (MySQL, PostgreSQL)

Geliştirme ve test ortamları

Cache server (Redis, Memcached)

Küçük/orta ölçekli container uygulamaları

🔹 Avantajları

Esnek ve çok yönlüdür → neredeyse her işe uygundur.

Fiyat/performans dengesi en iyi gruptur.

Yeni başlayanlar için AWS genelde General Purpose tavsiye eder.

🔹 Özet

General Purpose = Dengeli CPU + RAM + Network → Her işe biraz uygun.

Özel bir işlemci yoğunluğu (Compute), bellek yoğunluğu (Memory), depolama yoğunluğu (Storage) ya da GPU ihtiyacın yoksa → General Purpose seçilir.

# Compute Optimized Instances Nedir?

CPU ağırlıklı iş yükleri için tasarlanmış EC2 instance ailesidir.

Hesaplama (compute) kapasitesi yüksek, RAM biraz daha sınırlıdır.

CPU-intensive uygulamalar için idealdir.

🔹 Örnek Aileler

C serisi (örn: c5, c6g)

Yüksek performanslı işlemci (vCPU) sunar.

Genellikle Intel Xeon veya Graviton (ARM) tabanlı CPU’lar kullanılır.

🔹 Ne Zaman Kullanılır?

CPU yoğun işlemler

Video işleme, transcoding

Bilimsel hesaplamalar, simülasyonlar

Yüksek performanslı web sunucuları (high traffic)

Makine öğrenmesi eğitim aşaması (inference için değil)

Batch processing ve veri analizleri

Büyük veri setlerinde yoğun hesaplama gereken işlemler

🔹 Avantajları

CPU/RAM oranı yüksektir → hesaplama gücü yüksek.

Performans optimizasyonu yapılmış → işlem süreleri kısalır.

On-Demand, Reserved veya Spot ile kullanılabilir.

🔹 Dezavantajları

RAM/Depolama dengesi General Purpose kadar iyi değildir → bellek yoğun uygulamalar için ideal değildir.

Fiyat/performans RAM gerektiren işlerde daha düşük olabilir.

🔹 Özet

Compute Optimized = CPU-intensive uygulamalar için

Eğer iş yükün çok işlemci, az RAM istiyorsa → C serisi seç.

RAM veya bellek yoğunluğu önemliyse → Memory Optimized veya General Purpose düşün.

# Memory Optimized Instances Nedir?

Bellek (RAM) ağırlıklı iş yükleri için tasarlanmış EC2 instance ailesidir.

Çok yüksek RAM kapasitesi sunar, CPU/RAM dengesi Compute Optimized kadar yüksek değildir.

Büyük veri ve bellek yoğun uygulamalarda tercih edilir.

🔹 Örnek Aileler

R serisi (r5, r6g) → Genel amaçlı bellek yoğun uygulamalar

X serisi (x1, x2gd) → Çok büyük RAM gerektiren uygulamalar (in-memory database)

U serisi (u-6tb1.metal) → Çok büyük RAM (multi-terabyte) uygulamalar

🔹 Ne Zaman Kullanılır?

Bellek yoğun uygulamalar:

In-memory veritabanları (Redis, Memcached, SAP HANA)

Büyük veri analizleri (Spark, Hadoop)

Bellek tabanlı caching sistemleri

Yüksek performanslı web uygulamaları (çok RAM gerektiren backend)

CPU yoğunluğu ikinci plandaysa → RAM önceliklidir

🔹 Avantajları

Yüksek RAM → büyük veri setlerini bellekte tutabilirsin

Performans optimizasyonu → RAM sıkıntısı çekmeden uygulamalar çalışır

🔹 Dezavantajları

CPU/RAM dengesi Compute Optimized kadar iyi değildir

Fiyat/performans CPU odaklı işler için uygun değildir

🔹 Özet

Memory Optimized = RAM-intensive, bellek kritik uygulamalar

Örnek:

In-memory veritabanı (Redis, Memcached)

Büyük veri analizi

Bellek tabanlı caching sistemleri

# Storage Optimized Instances Nedir?

Depolama ağırlıklı (I/O intensive) iş yükleri için tasarlanmış EC2 instance ailesidir.

Yüksek disk I/O performansı sağlar (okuma/yazma işlemleri çok hızlı).

Genellikle büyük veri tabanları, veri analizi ve log işleme gibi disk yoğun uygulamalarda kullanılır.

🔹 Örnek Aileler

I serisi (i3, i4i) → NVMe SSD tabanlı yüksek IOPS disk performansı

D serisi (d2, d3) → büyük veri depolama (HDD ağırlıklı)

H serisi (h1) → yüksek depolama kapasitesi ve orta I/O

🔹 Ne Zaman Kullanılır?

Disk ağırlıklı iş yükleri için:

Büyük veritabanları (NoSQL veya SQL)

Data warehousing (Redshift, Big Data)

Log analizi ve streaming veri

Hadoop, Spark gibi dağıtık veri işleme

Yoğun okuma/yazma (read/write) gerektiren uygulamalar

🔹 Avantajları

Yüksek IOPS → disk performansı kritik iş yükleri için ideal

Büyük veri depolama → TB’larca veri ile çalışan uygulamalarda avantajlı

SSD ve NVMe seçenekleri → yüksek hızlı disk erişimi

🔹 Dezavantajları

RAM/CPU dengesi General Purpose veya Compute Optimized kadar iyi değildir

Fiyat biraz daha yüksek olabilir

🔹 Özet

Storage Optimized = Disk yoğun, I/O kritik uygulamalar

CPU/RAM değil, disk performansı öncelikliyse → Storage Optimized seçilir

Örnek:

Finansal işlem logları

E-ticaret site veritabanları

Hadoop cluster node’ları

# İşlemci, bellek, ram, I/O  detaylı anlatır mısın?

1️⃣ İşlemci (CPU – Central Processing Unit)

Bilgisayarın veya sunucunun “beyni”.

Programların ve hesaplamaların yürütüldüğü birim.

Özellikleri:

Cores (çekirdek sayısı): Paralel işlem yapabilme kapasitesi. Örn: 4 core → 4 işlem aynı anda çalışabilir.

Clock speed (GHz): Çekirdeğin saniyede kaç işlem yaptığı. Daha yüksek → daha hızlı işlem.

Threads (iş parçacığı): Modern CPU’lar her çekirdeği birden fazla thread ile çalıştırabilir (Hyper-Threading).

AWS örneği:

m5.large → 2 vCPU (virtual CPU)

c6g.xlarge → 4 vCPU → CPU-intensive işler için daha uygun

Özet: CPU → hesaplama gücü. Çok işlem yapacak uygulamalar için kritik.

2️⃣ Bellek (RAM – Random Access Memory)

CPU’nun geçici veri saklama alanı.

Programlar ve veri burada çalışır; diskten çok daha hızlıdır.

Özellikleri:

Kapasite (GB): Ne kadar veri aynı anda bellekte tutulabilir.

Hız (MHz): CPU ile veri alışveriş hızı.

Bellek dolarsa: CPU verileri diskten almak zorunda kalır → çok yavaşlar.

AWS örneği:

Memory Optimized instance → yüksek RAM (32GB, 64GB, hatta TB seviyeleri)

Özet: RAM → veri ve uygulamaların hızlı erişilen geçici deposu.

3️⃣ Depolama (Storage)

Kalıcı veri saklama birimidir.

Disk türleri:

HDD (Hard Disk Drive): Yavaş ama ucuz ve büyük kapasiteli

SSD (Solid State Drive): Hızlı, ama maliyeti daha yüksek

NVMe SSD: SSD’den daha hızlı, yüksek IOPS

AWS örneği:

i3 / i4i → NVMe tabanlı Storage Optimized

d2 → HDD tabanlı büyük depolama

Özet: Storage → verilerin kalıcı olarak saklandığı yer. Disk I/O kritik olduğunda Storage Optimized instance kullanılır.

4️⃣ I/O (Input / Output)

CPU veya RAM ile dış dünya arasındaki veri transferi hızıdır.

Disk veya network üzerinden veri alma/gönderme hızıyla ilgilidir.

Disk I/O: Diskten okuma/yazma hızı → Storage Optimized instance için kritik

Network I/O: Sunucu ile internet / diğer sunucular arasındaki veri transferi

Örnek:

Büyük veritabanı → yüksek disk I/O

Video streaming → yüksek network I/O

Özet: I/O → CPU ve RAM’in veri ile etkileşim hızını belirler.

# memory ile storage farkı nedir:

1️⃣ Memory Optimized Instances

Öncelik RAM (bellek)

CPU ve disk kapasitesi orta düzeydedir.

Amaç: Uygulamanın tüm veri setini veya büyük kısmını bellekte tutabilmek.

Kullanım örnekleri:

In-memory veritabanları (Redis, Memcached, SAP HANA)

Büyük veri analizi (Spark, Hadoop, bellek tabanlı processing)

Bellek yoğun backend uygulamaları

Öz: Bellek kritik, disk I/O ikincil öncelik.

2️⃣ Storage Optimized Instances

Öncelik disk ve I/O performansı

RAM ve CPU dengesi orta veya düşük olabilir.

Amaç: Yoğun okuma/yazma işlemlerini hızlı yapmak.

Kullanım örnekleri:

Büyük veri tabanları (NoSQL, SQL)

Log analizi ve streaming veri

Hadoop/Spark cluster node’ları

Data warehousing

Öz: Disk I/O kritik, RAM ikinci planda.

# Web Server Nedir?

Web server (web sunucusu), istemcilerden (genellikle tarayıcılardan) gelen HTTP/HTTPS isteklerini karşılayan ve yanıt olarak web sayfası, dosya veya veri döndüren bir yazılım (ve bazen donanım).

Yani kullanıcı adres çubuğuna www.site.com yazınca, web server:

Bu isteği alır

İlgili içerik (HTML, CSS, JS, resim, video, API cevabı vb.) bulur

İstemciye geri gönderir

Kısaca: “Tarayıcıdan gelen isteği işler, uygun yanıtı döner.”

🔹 Web Server Çeşitleri
1. Statik Web Server

Sadece sabit dosyaları (HTML, CSS, JS, resim) sunar.

Dinamik işlem yapmaz.

Çok hızlıdır.

Örn: Nginx, Apache (statik modda)

Kullanım: Basit web siteleri, dokümantasyon sayfaları.

2. Dinamik Web Server

Sunucu tarafında kod çalıştırır (Java, PHP, Python, Node.js vb.).

Kullanıcı isteğine göre dinamik içerik üretir (örneğin: haber siteleri, e-ticaret, sosyal medya).

Çalışma şekli:

Kullanıcı istek yapar

Web server, uygulama sunucusuna yönlendirir (Tomcat, Spring Boot, Django, Express.js)

Veritabanından veri alır, işler

Sonucu tarayıcıya gönderir

Kullanım: Facebook, Amazon, bankacılık siteleri gibi dinamik içerikli sistemler.

3. Donanım Web Server

Fiziksel bir makinedir (sunucu).

İçinde web server yazılımı çalışır.

Veri merkezlerinde bulunur.

Kullanım: Büyük ölçekli şirketlerin kendi sunucu sistemleri.

4. Yazılım Web Server

Bir bilgisayara/sunucuya yüklenmiş yazılımdır.

En popülerleri:

Apache HTTP Server

Nginx

IIS (Microsoft Internet Information Services)

LiteSpeed

🔹 Ne İçin Kullanılır?

Web sitelerini yayınlamak (HTML, CSS, JS servis etmek)

API servislerini sunmak (örneğin: bir mobil uygulamanın backend’i)

Dinamik web uygulamaları çalıştırmak (e-ticaret, sosyal medya, blog)

Dosya dağıtımı yapmak (resim, video, doküman paylaşımı)

Yük dengeleme (Load Balancer ile gelen trafiği dağıtmak)

Güvenlik (SSL/TLS ile HTTPS sağlamak)

🔹 Özet

Web Server = İstekleri karşılayan yazılım/sunucu

Statik Web Server → sabit dosyalar

Dinamik Web Server → veritabanı + backend ile çalışan siteler

Yazılım örnekleri: Apache, Nginx, IIS

Kullanım alanları: web siteleri, API servisleri, dosya paylaşımı
