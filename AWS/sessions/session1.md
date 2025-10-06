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

# AWS, farklı kullanım senaryoları için EC2 instance tiplerini ailere (families) ayırıyor:

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

Clock speed (GHz): Çekirdeğin saniyede kaç işlem yaptığı. Daha yüksek → daha hızlı işlem.                        nnh

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

# memory ile storage farkı nedir?

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

# Accelerated Computing Nedir?

Normal CPU’nun tek başına yeterli olmadığı, yüksek işlem gücü isteyen işlerde kullanılan EC2 instance tipidir.

Bu tip instance’lar, özel donanım hızlandırıcılar (GPU, FPGA, özel çipler) içerir.

Amaç: CPU’yu destekleyerek çok daha yüksek hızda hesaplama yapmak.

🔹 Hangi Donanımlar Kullanılır?

GPU (Graphics Processing Unit)

Yüksek paralel işlem gücü sağlar.

Özellikle:

Yapay Zeka (AI) ve Makine Öğrenimi (ML)

Derin öğrenme (Deep Learning)

3D rendering, video işleme

FPGA (Field Programmable Gate Array)

Donanımın programlanabilir versiyonu.

Özel algoritmaları donanım seviyesinde hızlandırır.

Özellikle:

Kriptografi

Finansal hesaplamalar

Gerçek zamanlı veri işleme

AWS Inferentia & Trainium (özel çipler)

AWS’nin AI/ML için geliştirdiği özel işlemciler.

Inferentia → inference (tahmin) için

Trainium → model eğitimi için

🔹 AWS Accelerated Computing Instance Aileleri

P family → GPU yoğun (AI/ML training, HPC)

G family → Graphics yoğun (gaming, 3D rendering, streaming)

F family → FPGA tabanlı (özel hızlandırıcı algoritmalar)

Inf/Trn family → AWS’nin AI çipleri (ML inference/training)

🔹 Ne Zaman Kullanılır?

AI/ML model eğitimi ve tahmini (TensorFlow, PyTorch, HuggingFace modelleri)

HPC (High Performance Computing) → bilimsel hesaplamalar

3D grafik işleme (CAD, animasyon, oyun)

Video encoding/decoding (canlı yayın, rendering)

Finansal analiz, risk modelleme (yüksek işlem gücü gerektiren algoritmalar)

🔹 Özet

Accelerated Computing = CPU + GPU/FPGA/özel çip kombinasyonu

Avantaj: Paralel ve yoğun hesaplama işlerini CPU’dan çok daha hızlı yapar.

Kullanım alanı: AI, ML, Deep Learning, HPC, 3D rendering, video işleme

# Ama zaten comput işlemci yoğun değil miydi neden accelarete ihtiyaç duyulmuş?

🔹 CPU (Compute Optimized)

CPU çok genel amaçlı bir işlemcidir.

Tekrarlayan, sıradan, farklı türden işlemleri yapmada iyidir (ör. web server, API, veri tabanı işlemleri).

Ancak bazı işler vardır ki çok büyük veri üzerinde aynı tür hesaplamanın milyonlarca kez yapılmasını gerektirir.

Örnekler:

Makine Öğrenmesi / Yapay Zekâ eğitimi (milyonlarca matris çarpımı)

Video işleme / render (piksel piksel aynı hesaplama)

Bilimsel simülasyonlar (iklim, molekül modelleme)

Kripto / hash işlemleri

Bu tür işlerde CPU göreceli olarak yavaştır çünkü çekirdek sayısı sınırlı ve her çekirdek çok genel iş yapmak için tasarlanmıştır.

🔹 GPU (Accelerated Computing)

GPU’lar (Graphics Processing Unit), CPU’ya kıyasla binlerce küçük çekirdeğe sahiptir.

Aynı işlemi paralel olarak çok hızlı yapabilir.

Örneğin bir GPU, 5000 matris çarpımını aynı anda yapabilirken CPU bunları sırayla işler.

Yani:

CPU → "çok iş yapabilen ama aynı anda az kişiye hizmet veren ofis çalışanı"

GPU → "aynı anda binlerce küçük işçi çalıştırabilen fabrika"

🔹 Neden “Accelerated Computing” Kategorisi Açılmış?

Çünkü:

Her iş GPU’ya uygun değildir. Web server, API, veritabanı → CPU yeterli.

Ama AI, Machine Learning, Big Data Analytics gibi işler → GPU veya FPGA (donanım hızlandırıcı) şarttır.

AWS ve diğer bulut sağlayıcılar bu yüzden “Accelerated Computing” diye ayrı bir kategori açtı. Çünkü buradaki donanım (GPU, FPGA, TPU) CPU’dan çok farklı ve özel kullanım senaryoları var.

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

# /var/www/html genelde web sunucusunun (Apache, Nginx vs.) default document root dizinidir.

Linux’ta web servisleri (Apache, Nginx) dosyaları “document root” denilen bir dizinden yayınlar.

Çoğu dağıtımda bu dizin:

/var/www/html

olarak ayarlanmıştır.

Buraya koyduğun dosyalar HTTP üzerinden erişilebilir olur.
Örn.:

/var/www/html/index.html dosyası varsa ve sunucunun IP’si 54.90.151.48 ise:
http://54.90.151.48/index.html

şeklinde tarayıcıdan görebilirsin.

Apache veya Nginx konfigürasyon dosyasında bu yol değiştirilebilir.

Apache: /etc/httpd/conf/httpd.conf (CentOS/RedHat) veya /etc/apache2/sites-available/000-default.conf (Ubuntu/Debian)

Nginx: /etc/nginx/sites-available/default

Örnek Senaryo

Sunucunda Apache kuruluysa:

sudo yum install httpd -y   # CentOS/RedHat
sudo systemctl start httpd
sudo systemctl enable httpd


Sonra /var/www/html/ içine basit bir dosya oluştur:

echo "Merhaba Linux Web Sunucusu!" | sudo tee /var/www/html/index.html


Tarayıcıdan:

http://<public-ip>/


adresine gittiğinde bu yazıyı görürsün.

Best Practice

/var/www/html sadece test veya basit siteler için uygundur.

Profesyonel projelerde genelde:

Her site için ayrı dizin açılır (/var/www/site1, /var/www/site2)

Her site için ayrı virtual host (Apache) veya server block (Nginx) tanımlanır.

Dosyaları root değil, özel bir kullanıcı (örn. www-data) yönetmeli, güvenlik için.

# AWS’de stateless kavramı sık sık geçiyor ama birkaç farklı bağlamda kullanılıyor. Hemen detaylı anlatayım:

🔹 1. AWS’de “Stateless” Kavramı

Stateless, en basit haliyle oturum bilgisinin (state) bir sunucu üzerinde tutulmaması demektir.

Bir istek (request) geldiğinde, o isteğin cevaplanması için önceki isteklerle ilgili bilgiye ihtiyaç duyulmaz.

Yani her istek bağımsızdır.

Stateful sistemlerde ise önceki isteklerden gelen bilgiler tutulur (örneğin bir web oturumu, alışveriş sepeti).

AWS’de stateless örnekleri:

Security Groups: Inbound (gelen) ve Outbound (giden) kurallarını ayrı yazmazsın. Bir yönde izin verdiğinde cevap trafiği otomatik izinlidir → yani “stateful” çalışır.

Network ACL (NACL): Hem inbound hem outbound için ayrı kurallar yazarsın. Trafiğin dönüşüne otomatik izin verilmez. Yani tamamen bağımsızdır → bu yüzden stateless çalışır.

Kısacası: SG → stateful, NACL → stateless

🔹 2. Inbound / Outbound ile Stateless İlişkisi

Security Group (SG)

Örneğin inbound’da port 80 (HTTP) açarsan, dışarıya doğru outbound kuralı yazmana gerek yoktur. Çünkü SG stateful’dur → dönüş trafiğine otomatik izin verilir.

NACL (Network ACL)

Örneğin inbound’da port 80 açtığında, outbound’da da ephemeral port (1024–65535) aralığını açman gerekir. Çünkü NACL stateless’tir → gelen ve giden trafik bağımsızdır.

🔹 3. Uygulama Tarafında Stateless

AWS’de sadece network değil, uygulama mimarisi tarafında da stateless önemlidir.

Örneğin Elastic Load Balancing (ELB) kullanıyorsan, backend instance’ların stateless olması tavsiye edilir. Çünkü bir request farklı instance’a yönlendirilebilir. Eğer session bilgisini instance içinde tutarsan, diğer instance’lar o bilgiden habersiz olur.

Çözüm: Session bilgisini DynamoDB, ElastiCache (Redis), S3 gibi merkezi bir depoda tutarsın → application stateless olur.

Özet:

AWS’de Network ACL = Stateless, Security Group = Stateful

Inbound / outbound bağımsızlığı NACL’de vardır çünkü stateless’tir.

SG’de inbound izni verildiğinde outbound dönüşe otomatik izin çıkar çünkü stateful’dur.

Uygulama mimarisinde de “stateless” çok önemlidir → özellikle load balancing, auto scaling gibi yapılarda session bilgisini merkezi depoya taşımak gerekir.

# Bu komut AWS EC2 üzerindeki bir web sunucusuna HTTP isteği (request) göndermek için kullanılır.
curl http://ec2-3-15-183-78.us-east-2.compute.amazonaws.com

1️⃣ curl nedir?

curl (“client URL”) bir komut satırı aracıdır.
Bir URL’ye (örneğin bir web sitesi veya API adresi) istek (request) gönderip cevabı terminalde gösterir.

2️⃣ Bu örnekte ne oluyor?
curl http://ec2-3-15-183-78.us-east-2.compute.amazonaws.com

Bu komut:

AWS’de us-east-2 (Ohio) bölgesinde çalışan

IP adresi: 3.15.183.78 olan

EC2 instance’a, HTTP (port 80) üzerinden istek yollar.
Yani web tarayıcısında şu adrese gitmekle aynı şeydir:

http://ec2-3-15-183-78.us-east-2.compute.amazonaws.com

3️⃣ Dönüşte ne olur?

Eğer bu EC2 üzerinde bir web server (örneğin Apache, Nginx, Tomcat) çalışıyorsa, sana HTML cevabı döner.

Eğer hiçbir web servisi yoksa, genellikle hata alırsın:

curl: (7) Failed to connect to ... port 80: Connection refused

veya

curl: (28) Connection timed out

4️⃣ curl Ne İçin Kullanılır?

AWS’de EC2, Load Balancer, API Gateway, S3 URL gibi servisleri test etmek için.

Uygulamanın dışarıdan erişilebilir olup olmadığını görmek için.

Web servislerinin (REST API’lerin) yanıtlarını test etmek için.

🔹 Örnekler:
EC2 web server’ı test et
curl http://ec2-3-15-183-78.us-east-2.compute.amazonaws.com

HTTPS portunu test et
curl https://example.com

Yalnızca HTTP başlıklarını gör
curl -I http://ec2-3-15-183-78.us-east-2.compute.amazonaws.com

JSON API’ye GET isteği gönder
curl https://api.example.com/users


Özetle:
curl http://ec2-3-15-183-78.us-east-2.compute.amazonaws.com komutu,
EC2’de çalışan web sunucusuna HTTP isteği atar ve cevabı terminalde gösterir.
Bu sayede EC2’nün doğru çalışıp çalışmadığını test edebilirsin.
