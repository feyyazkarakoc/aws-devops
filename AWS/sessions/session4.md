# İmaj nedir, ami nedir, bileşenleri nelerdir, neden kullanıllır, nerde kullanılır, amazon 2'de ami nasıldı?
1️⃣ “İmaj (Image)” nedir?

Genel anlamda imaj, bir sistemin birebir kopyasıdır —
içinde işletim sistemi, konfigürasyonlar, uygulamalar, ayarlar ve veriler bulunur.

Kısaca:

“Bir bilgisayarı veya sunucuyu olduğu gibi klonlayıp başka yerde aynısını oluşturmanı sağlar.”

Bilgisayarlarda (örneğin Windows ISO, Linux ISO) imaj dosyası = işletim sistemi kurulum dosyasıdır.
AWS’de ise bu konsept, EC2 sunucularını çoğaltmak için kullanılır.

2️⃣ AMI nedir? (Amazon Machine Image)

AMI (Amazon Machine Image) =
AWS üzerinde bir sanallaştırılmış makine şablonu (image)’dir.

Yani:

“EC2 instance’larının (sanal sunucuların) oluşturulduğu temel kalıptır.”

🔹 AMI’nin içinde neler var?

Bir AMI şu 3 temel bileşenden oluşur:

Bileşen	Açıklama
1️⃣ Root Volume (Root Device Template)	İşletim sistemi, uygulamalar, konfigürasyonlar, yani diskin asıl içeriği. (örneğin Linux, Apache, Java yüklü olabilir)
2️⃣ Launch Permissions	Bu AMI’yi kimlerin kullanabileceğini belirler. (örneğin sadece sana açık olabilir veya public olabilir)
3️⃣ Block Device Mapping	EC2 instance’ına bağlanacak ek disklerin (EBS volume’ların) nasıl monte edileceğini gösterir.


🔹 AMI türleri:

Public AMIs:
AWS veya topluluk tarafından herkese açık sunulan imajlar
(örnek: Amazon Linux 2, Ubuntu, Windows Server).

Private AMIs:
Senin oluşturduğun ve sadece hesabına özel olan imajlar.
Örneğin “benim yapılandırılmış web sunucumun imajı”.

Marketplace AMIs:
Ücretli veya ücretsiz olarak satılan, 3. parti firmaların hazırladığı imajlar
(örnek: WordPress, Jenkins, Red Hat, Bitnami paketleri).

3️⃣ AMI ne işe yarar?

Bir AMI sayesinde:

Her defasında sunucuyu sıfırdan kurmak yerine,
önceden hazırlanmış bir imajdan saniyeler içinde aynı ortamı oluşturabilirsin.

Otomasyon (CI/CD), ölçeklenebilirlik (Auto Scaling), yedekleme gibi işlemler çok hızlanır.

Kısaca:

AMI = “Bir EC2 makinesini çoğaltmak için kullanılan şablon.”

4️⃣ AMI nasıl oluşturulur?

Sen bir EC2 instance’ı kurarsın, içinde:

Güncellemeleri yaparsın,

Uygulama kurarsın (örneğin NGINX, Java, Node.js),

Sonra “Create Image (AMI)” dersen → AWS bu makinenin tam bir snapshot’unu alır.

Sonra bu AMI’den yeni EC2’ler oluşturursan,
yeni makineler aynı konfigürasyona sahip olur (adeta “klon” gibi).

5️⃣ Amazon Linux 2 AMI’si nasıl bir şeydi?

Amazon Linux 2, AWS’in kendi geliştirdiği bir **Linux dağıtımı (distro)**dur.
Bu nedenle onun AMI’si, AWS optimizasyonlu bir Linux imajıdır.

🔹 Özellikleri:

Temelinde RHEL / CentOS tabanlıdır.

Paket yöneticisi: yum (bazı yeni versiyonlarda dnf de destekler)

AWS için optimize edilmiştir:

EC2’de hızlı boot olur

AWS CLI, CloudInit, EC2 metadata servisi gibi araçlar yüklü gelir

Hafif, güvenli ve performanslıdır.

🔹 Amazon Linux 2 AMI örneği:

AWS Management Console’da “Launch Instance” dediğinde
şöyle görürsün:

AMI Name: Amazon Linux 2 AMI (HVM), SSD Volume Type
AMI ID: ami-0abcdef1234567890
Architecture: x86_64
Root Device Type: EBS
Virtualization Type: HVM


Bu senin EC2 instance’ının tabanını oluşturur.
Yani “sunucunun işletim sistemi diski” buradan gelir.

6️⃣ AMI – Snapshot ilişkisi

Bunu bilmek çok önemli:

Kavram	Anlamı
Snapshot	EBS diskinin yedeğidir.
AMI	EC2’nin sistem imajıdır (snapshot + metadata).

Yani:

AMI aslında bir veya daha fazla snapshot’tan oluşur.

AWS, AMI’yi oluştururken diskin snapshot’unu otomatik alır.

7️⃣ Nerelerde kullanılır?
Kullanım Alanı	Açıklama
Otomatik ölçeklendirme (Auto Scaling)	Yeni EC2’ler aynı imajdan çoğalır
Yedekleme / kurtarma	Sistemi aynı haliyle geri yükleme
Ortam çoğaltma	Test, staging, prod gibi ortamları birebir oluşturma
CI/CD pipeline	Build sonrası custom AMI üretip deployment’a geçiş

# Snapshot “AMI” konusunun teknik temeli — yedekleme, klonlama, hatta felaket kurtarma (disaster recovery) süreçlerinin merkezinde yer alıyor.

1️⃣ Snapshot nedir?

AWS Snapshot, bir EBS (Elastic Block Store) disk’inin tam yedeğidir (backup).

Snapshot = EBS diskinin belirli bir andaki durumunun (state) fotoğrafı

Yani senin EC2 instance’ındaki disk (örneğin /dev/xvda) o anda hangi dosyalara sahipse, snapshot bunu kaydeder.

2️⃣ Snapshot neden kullanılır?

Bir EBS volume (örneğin EC2’nün root diski veya data diski):

Bozulabilir 

Yanlışlıkla silinebilir 

Yeni bir bölgeye (region) taşınmak istenebilir 

Bu durumlarda snapshot sayesinde:

Veriyi geri yükleyebilirsin (restore),

Aynı diskten yeni bir volume oluşturabilirsin,

Farklı bir bölgeye (region’a) kopyalayabilirsin.

Kısaca: Snapshot = “EBS için yedekleme + çoğaltma mekanizması”.

3️⃣ Snapshot nasıl çalışır?

AWS snapshot’lar incremental (artımlı) olarak çalışır:

Durum	Açıklama
İlk snapshot	Tüm diskin tam yedeği alınır (full backup).
Sonraki snapshot’lar	Sadece değişen bloklar kaydedilir. (delta backup)

Bu sayede:

Depolama maliyeti azalır,

Snapshot alma süresi kısalır,

AWS arka planda sürüm kontrolü gibi bir yapı oluşturur.

4️⃣ Snapshot nasıl alınır?
A. AWS Console’dan:

EC2 → “Elastic Block Store” → “Volumes”

İlgili volume’u seç

Actions → “Create snapshot”

İsim, açıklama gir

AWS snapshot ID üretir (örneğin: snap-0ab1234cd5678ef90)

B. CLI ile:
aws ec2 create-snapshot --volume-id vol-0abc123def456 --description "Backup of web server volume"

5️⃣ Snapshot’tan volume oluşturma

Snapshot sadece bir yedek değildir;
istersen ondan yeni bir EBS volume oluşturabilirsin

aws ec2 create-volume \
  --snapshot-id snap-0ab1234cd5678ef90 \
  --availability-zone us-east-1a


Bu yeni volume:

Eski diskin birebir kopyası olur,

Yeni bir EC2’ye bağlanabilir (Attach Volume).

6️⃣ Snapshot ve AMI ilişkisi
Kavram	Tanım	İlişki
EBS Snapshot	Diskin yedeği	AMI’nin temel bileşeni
AMI	EC2 makinesinin işletim sistemi + snapshot + izin bilgileri	AMI içinde 1 veya daha fazla snapshot bulunur

Yani AMI oluşturduğunda, AWS otomatik olarak EC2’nin diskinin snapshot’unu da alır.
O snapshot’lar AMI’nin parçası olur.

7️⃣ Snapshot’ın özellikleri
Özellik	Açıklama
S3 tabanlı depolama	Snapshot’lar EBS’te değil, S3’te saklanır (görünmez ama S3 altyapısı kullanılır)
Region bağımlı	Snapshot’lar alındığı region’a bağlıdır (isteğe bağlı cross-region copy yapılabilir)
Paylaşılabilir	Snapshot private, public veya belirli hesaplarla paylaşılabilir
Şifrelenebilir	Snapshot’lar AES-256 ile şifrelenebilir
Otomatik alınabilir	Data Lifecycle Manager (DLM) veya Backup service ile planlı otomatik snapshot alınabilir

8️⃣ Örnek senaryolar
Senaryo	Snapshot Kullanımı
Günlük yedekleme	Her gece EBS snapshot alınır
Migration (taşıma)	Snapshot başka region’a kopyalanır, orada volume oluşturulur
Disaster Recovery (felaket kurtarma)	Snapshot’tan yeni EC2 başlatılır
AMI oluşturma	EC2 imajı alınırken AWS snapshot oluşturur
Veri kurtarma	Eski snapshot’tan volume oluşturulup dosyalar alınır

9️⃣ Özet tablo
Kavram	Anlamı	Kullanım amacı
Volume	EC2’nin bağlı olduğu sanal disk	Aktif veri depolama
Snapshot	Volume’un yedeği	Yedekleme / restore / çoğaltma
AMI	EC2’nin tam sistem imajı	Yeni EC2 oluşturma, klonlama
AMI ↔ Snapshot	AMI içinde snapshot’lar bulunur	Snapshot = AMI’nin temeli

1️0️⃣ Gerçek hayattan örnek

Diyelim ki bir EC2 web sunucun var: /var/www/html altında bir web sitesi çalışıyor.

Sen her gün Create Snapshot yapıyorsun → günlük yedek.

Bir gün site bozuldu → yeni bir volume oluştur, snapshot’tan yükle → siteyi geri getir.

Hatta başka bir region’da aynı snapshot’tan yeni EC2 oluştur → yedek sistem çalışsın.