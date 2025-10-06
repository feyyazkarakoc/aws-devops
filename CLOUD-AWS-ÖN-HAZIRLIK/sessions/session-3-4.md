

# SSH Nedir?
SSH = Secure Shell
Uzak bir sunucuya (örneğin EC2 instance’a) şifreli, güvenli bir terminal bağlantısı kurmak için kullanılan protokoldür.
Yani:
Başka bir bilgisayarda (sunucuda) çalışıyorsun ama sanki kendi bilgisayarınmış gibi komutlar yazabiliyorsun.
SSH Ne İşe Yarar?
Amaç	Açıklama
Uzak sunucuya bağlanmak	Örn: EC2 instance’a erişmek
Kod çalıştırmak / deploy yapmak	Örn: Spring Boot uygulamanı başlatmak
Paket kurmak / log bakmak	Örn: Java, Docker kurmak
Log dosyalarını incelemek	Uygulama hatalarını kontrol etmek

SSH Bağlantısı Nasıl Çalışır?
SSH ile bağlanmak için genelde şu bilgilere ihtiyacın olur:
Uzak sunucunun IP adresi
Bir SSH anahtarı (genellikle .pem uzantılı özel anahtar dosyası)
Giriş yapılacak kullanıcı adı (örneğin: ec2-user, ubuntu, root)
Komut Örneği:
ssh -i anahtar-dosyasi.pem ec2-user@13.57.123.45
Bu komutla sen kendi bilgisayarından → EC2 instance’ına terminalden bağlanırsın.

SSH Güvenli midir?
Evet çünkü:
Şifre yerine genelde özel anahtar (private key) kullanılır
Tüm iletişim şifrelenmiştir
AWS EC2 instance’larına varsayılan olarak sadece SSH portu (22) açıktır

Gerçek Hayat Senaryosu
Diyelim Spring Boot uygulamanı EC2’ye deploy ettin:
ssh ile EC2’ye bağlanırsın
java -jar okul-yonetim.jar komutuyla çalıştırırsın
Uygulama logs vs. terminalde görünür
Gerekirse nano veya vim gibi editörlerle konfigürasyon dosyalarını düzenlersin

Özet
Konu	Açıklama
SSH	Uzak sunucuya güvenli bağlantı kurma protokolü
Kullanım alanı	EC2, VPS, sunucu yönetimi, deploy
Ne gerekiyor?	IP adresi, SSH key, kullanıcı adı
Kullanımı	ssh -i key.pem user@ip şeklinde komut

# Key Pair Nedir?
Key Pair = Anahtar Çifti demektir.
Uzak bir sunucuya (örneğin EC2) şifre yerine güvenli bir şekilde bağlanmanı sağlayan iki parçalı bir dijital kimliktir.

İki Parçası Vardır:
Private Key (gizli)	Senin bilgisayarında (.pem dosyası)	SSH bağlantısı yaparken kullanılır
Public Key (açık)	Sunucuda (örneğin EC2 üzerinde)	Kimliğini doğrulamak için gereken açık anahtar
Bu ikili birlikte çalışır:
Sen SSH ile sunucuya bağlanırken, sunucu public key’i ile kontrol eder → senin private key’in uyuyorsa bağlantıya izin verir.

Neden Kullanılır?
Şifre kullanmadan, daha güvenli bir şekilde oturum açmak için.
Çünkü:
Şifre tahmin edilebilir → ama key pair çok daha güçlü
Private key sadece sende olur
AWS gibi platformlar güvenliği bu şekilde sağlar

EC2 Oluştururken Key Pair Ne Demek?
EC2 başlatırken şunu görürsün:
"Select an existing key pair or create a new one"
Bu şu anlama gelir:
EC2’ye SSH ile bağlanmak için ya:
Daha önce oluşturduğun bir key pair’i seç
Ya da “Create new key pair” diyerek .pem uzantılı özel anahtar indir (sadece bir kere verilir)

Dikkat!
.pem dosyası kaybolursa	EC2’ye SSH ile bağlanamazsın (erişim yok olur)
.pem dosyası paylaşılmaz	Çünkü gizlidir, sadece senin bilgisayarında olmalı
Yeni key oluşturmak gerekirse	EC2'yi stop edip yeni bir key ile AMI’den yeni instance üretmen gerekebilir

Örnek Kullanım:
ssh -i "feyyaz-key.pem" ec2-user@13.59.12.34
Bu komut:
feyyaz-key.pem → senin özel anahtarın (private key)
ec2-user → AWS Amazon Linux kullanıcısı
13.59.12.34 → EC2 IP adresi

Özetle:
Key Pair	SSH bağlantısı için gerekli dijital kimlik çifti
Private Key	Sadece sende olan gizli dosya (.pem)
Public Key	AWS EC2 üzerinde duran açık anahtar
Kullanım amacı	Şifresiz ama güvenli bağlantı kurmak

# Bölgesel Farklılıklar:
US East (N. Virginia) - us-east-1:
En eski ve en kapsamlı bölge
Tüm instance type'ları (t2, t3, t4g)
Tüm kaynaklarınız burada
Key pair'lar burada kayıtlı

Europe (Stockholm) - eu-north-1:
Nispeten yeni bölge (2018)
Sadece yeni nesil instance'lar (t3, t4g)
Kaynaklarınız yok (farklı bölge)
Key pair'lar ayrı tutulur

AWS Bölge Mantığı:
Kaynak Bağımsızlığı:
Key pair'lar bölgeye özel
Instance'lar bölgeye özel
Security group'lar bölgeye özel
AMI'ler bölgeye özel

# En temel virtualization çeşitleri:

Software Virtualization

Server Virtualization

Storage Virtualization

Operating System Virtualization (OS V.)


1. Software Virtualization

Yazılımların, işletim sisteminden bağımsız çalışabilmesini sağlayan sanallaştırmadır.

Yani bir uygulamayı sanki o işletim sistemine kurulmuş gibi çalıştırırsın ama aslında izole bir ortamda çalışır.

Uygulama, kullandığı dosyaları ve ayarları işletim sisteminden ayrı görür.

Örnekler:

Wine (Linux’te Windows programlarını çalıştırmak için)

VMware ThinApp veya Microsoft App-V

Eğitim/deneme amaçlı programları ana bilgisayarına zarar vermeden çalıştırabilirsin.

Ne işimize yarar?

Eski programları yeni sistemlerde çalıştırmak

Güvenlik: Ana işletim sistemini bozmaz

Tek seferde yüzlerce kullanıcıya uygulama dağıtımı

2. Server Virtualization

Fiziksel bir sunucuyu sanal sunuculara bölmektir.

Burada Hypervisor adı verilen bir yazılım kullanılır (VMware ESXi, KVM, Hyper-V gibi).

Tek fiziksel makinede onlarca sanal makine (VM) çalıştırabilirsin.

Her VM bağımsızdır, kendi işletim sistemini (Windows/Linux) kurabilirsin.

Örnekler:

VMware vSphere, Microsoft Hyper-V, Oracle VM, AWS EC2

Ne işimize yarar?

Donanım verimliliği: Tek bir güçlü sunucu, 10 farklı küçük sunucu gibi kullanılabilir

Test ortamları oluşturmak kolay

Yedekleme ve failover (çökünce başka sunucuya geçiş) kolaydır

3. Storage Virtualization

Birden fazla fiziksel depolama aygıtını tek bir depolama havuzu (pool) gibi gösterir.

Kullanıcıya tek bir büyük disk gibi görünür, ama aslında arka planda onlarca farklı disk olabilir.

Diskler farklı yerlerde olsa bile (RAID, SAN, NAS) hepsi tek yerden yönetilir.

Örnekler:

RAID sistemleri (birden fazla disk, tek sürücü gibi)

SAN (Storage Area Network)

AWS EBS (Elastic Block Store)

Ne işimize yarar?

Depolamayı büyütmek/küçültmek kolay

Veriler daha güvenli ve hızlı erişilebilir

Donanımın nerede olduğunu bilmeden tek bir sistemden yönetebilirsin

4. Operating System Virtualization (OS Virtualization)

Aynı işletim sistemi çekirdeği üzerinde birden fazla izole ortam çalıştırmaktır.

Burada VM’deki gibi her seferinde yeni işletim sistemi kurulmaz.

Daha hafif, daha hızlıdır.

Container teknolojisi bu mantıkla çalışır.

Örnekler:

Docker, Kubernetes, LXC (Linux Containers)

Ne işimize yarar?

Mikroservis mimarisi için idealdir

Çok hızlı başlar (VM’den saniyelerce daha hızlı)

Daha az kaynak tüketir

“Aynı bilgisayarda farklı uygulamaları izole etmek” için kullanılır

ÖZET (basitleştirilmiş):

Software Virtualization → Tek tek uygulamaları izole çalıştırma.

Server Virtualization → Tek sunucuyu onlarca sanal sunucuya bölme.

Storage Virtualization → Birden fazla fiziksel diski tek bir sanal disk gibi kullanma.

OS Virtualization → Aynı işletim sistemi üzerinde container tabanlı izolasyon.