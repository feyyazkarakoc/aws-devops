
# FHS, Filesystem Hierarchy Standard (Dosya Sistemi Hiyerarşi Standardı) demektir.
Linux sistemlerinde dizinlerin (directories) ve dosyaların nerede bulunması gerektiğini tanımlar. 
Yani Linux dosya sisteminin “iskeletini” oluşturur.

Amaç:

Tüm Linux dağıtımlarında (Ubuntu, CentOS, Debian, Fedora vs.) dosya yollarının standart olması.

Böylece bir uygulama veya kullanıcı her sistemde aynı yerde gerekli dosyaları bulabilir.

FHS’ye göre ana dizinler:

/ (root dizini)
Tüm dosya sisteminin başlangıç noktasıdır.
Her şey / altında organize edilir.

/bin
Temel komutların bulunduğu yer. (örnek: ls, cp, mv, cat)
Sistemin boot olduktan sonra çalışabilmesi için gerekli en temel araçlar.

/sbin
Sistem yönetimi için gerekli komutlar. (örnek: shutdown, reboot, mkfs)
Genellikle sadece root kullanır.

/etc
Sistemin yapılandırma (config) dosyaları.
(örnek: /etc/passwd, /etc/ssh/sshd_config)

/home
Kullanıcıların kişisel dizinleri.
Örn: /home/ec2-user, /home/feyyaz

/root
Root kullanıcısının home dizini.
Normal user’ların /home/username dizinleri olurken, root’un kendi özel alanı vardır.

/var
Değişken (variable) veriler.
(örnek: log dosyaları /var/log, spool dosyaları, cache)

/tmp
Geçici dosyalar. Sistem restart olunca genelde temizlenir.

/usr
Kullanıcı uygulamaları ve ikincil dosyalar.
(örn: /usr/bin, /usr/lib)
Çok önemli bir dizindir, içinde kullanıcıya ait programlar bulunur.

/lib
Temel kütüphaneler.
(örnek: C kütüphanesi, kernel modülleri)

/mnt ve /media
Harici diskler veya CD/DVD gibi taşınabilir medyaların mount edildiği yerler.

/dev
Cihaz dosyaları.
(örnek: /dev/sda → disk, /dev/null → özel aygıt)

Özetle:
FHS = Linux’ta dosya sisteminin rehberi / standart düzeni.
Hangi dosyanın nerede bulunması gerektiğini söyler.

# File permission nedir, user, group ve other'ı anlatur mısın?
Linux’ta file permission (dosya izinleri), bir dosya veya dizine kimlerin hangi tür erişim hakkına 
sahip olduğunu belirleyen güvenlik mekanizmasıdır.

Temel olarak üç tip kullanıcı vardır:

User (Owner / Kullanıcı)

Dosyayı oluşturan kişi (sahibi).

Genelde ls -l çıktısında ilk görünen kullanıcıya aittir.

Örn: feyyaz isimli kullanıcı dosyayı oluşturmuşsa, onun owner hakkı vardır.

Group (Grup)

Dosya sahibinin üyesi olduğu grup.

O gruptaki tüm kullanıcılar, dosya üzerinde grup izinlerine göre erişim sağlar.

Other (Diğerleri / World)

Dosyanın sahibi ve grubu dışında kalan tüm kullanıcılar.

Bu en geniş kullanıcı kitlesidir.

Üç tip izin (permission) vardır:

r (read / okuma) → Dosyanın içeriğini okuma izni.

w (write / yazma) → Dosyayı değiştirme, silme izni.

x (execute / çalıştırma) → Dosyayı çalıştırabilme (program/script ise).

Örnek:

ls -l
-rwxr-xr--


Açıklaması:

- → Bu bir dosya (dizin olsaydı d yazardı).

rwx → User (owner) izinleri: okuma, yazma, çalıştırma.

r-x → Group izinleri: okuma, çalıştırma ama yazma yok.

r-- → Other izinleri: sadece okuma.

Özet tablo:

Kullanıcı Tipi	İzinler
User (owner)	Dosya sahibinin izinleri
Group	Dosya sahibinin grubundaki kullanıcıların izinleri
Other	Geri kalan herkesin izinleri

# Linux’ta paket (package) nedir?

Bir yazılımı Linux sistemine kurarken sadece tek bir dosya değil, birçok dosya gerekir:

Çalıştırılabilir dosyalar (binary)

Kütüphaneler

Yapılandırma (config) dosyaları

Dokümantasyon (README, man page)

Servis dosyaları (systemd unit, init script vs.)

İşte bunların hepsi bir araya getirilip tek bir dosya halinde dağıtılır. Buna paket denir.
Örneğin:

Ubuntu/Debian’da paketler .deb uzantılıdır.

RedHat/CentOS/Amazon Linux’ta .rpm uzantılıdır.

Package Management (Paket Yönetimi) nedir?

Bir yazılımın yüklenmesi, güncellenmesi, kaldırılması sürecini kolaylaştıran sistemdir.
Paket yöneticisi (package manager):

Bağımlılıkları (dependencies) çözer → yani bir paketin ihtiyaç duyduğu diğer paketleri otomatik indirir.

Merkezi depolardan (repository) yazılımları çeker.

Versiyon kontrolü yapar.

Örneğin:

Debian/Ubuntu → APT (Advanced Package Tool) → apt install, apt update, apt remove

RHEL/CentOS → YUM veya yeni nesil DNF → yum install, dnf update

SUSE → zypper

Arch Linux → pacman

Basit örnek:

Diyelim ki curl kurmak istiyoruz:

Ubuntu/Debian:

sudo apt update
sudo apt install curl


Amazon Linux / CentOS:

sudo yum install curl


Arch Linux:

sudo pacman -S curl


Burada aslında curl paketini indirip içindeki binary, config ve diğer dosyaları sistemin doğru klasörlerine yerleştiriyor.

Özet:

Paket: Yazılım + gerekli dosyaların arşivlenmiş hali (.deb, .rpm vs.)

Paket yönetimi: Bunları kolayca indirip kurma, güncelleme, kaldırma işi.

# Senin backend developer bakış açın ile Linux dünyasındaki Paket Yönetim Sistemi (PMS) bakış açısını birleştirelim:

Senin dediğin durum (örnek: Spring Boot JAR)

Sen uygulamayı build ediyorsun → mesela mvn package → app.jar çıkıyor.

Bunun içine Maven/Gradle sayesinde tüm bağımlılıklar (dependencies) gömülüyor (fat jar / uber jar).

Sonra EC2’ye gönderiyorsun (scp veya git pull) ve java -jar app.jar diyerek çalıştırıyorsun.

Burada PMS’ye gerek yok, çünkü bağımlılıklarını zaten jar’a koymuşsun.

Peki PMS (Package Management System) nerede devreye giriyor?

PMS (örneğin apt, yum, dnf) uygulamanın kendisini değil, sistemin temel bileşenlerini yönetir.

Java Runtime (java, openjdk-17, maven)

Nginx, Apache, MySQL, PostgreSQL gibi servisler

Sistem araçları (curl, git, unzip)

Kütüphaneler (glibc, openssl, libxml2)

Yani: senin app.jar çalışsın diye önce EC2’de Java kurulu olmalı.
O Java’yı → sen yum install java-17-amazon-corretto ile kuruyorsun → işte orada PMS devreye giriyor.

AWS tarafı nerede?

AWS, PMS çalıştırmaz.
PMS her zaman EC2’nin içinde, Linux işletim sisteminin bir parçasıdır.

Sen EC2 açtığında (mesela Amazon Linux 2023) içinde dnf vardır.

AWS sadece repository’leri (paket depolarını) Amazon’un serverlarına yönlendirir. (mesela amazon-linux-extras)

PMS neyi install / upgrade / configure eder?

install → yeni paket kurar (ör. dnf install git)

upgrade → mevcut paketleri daha yeni versiyonuna günceller

configure → çoğu zaman otomatik yapılandırma dosyası (/etc altına) koyar ve gerekli servisleri (systemctl enable nginx) başlatır

Kısaca:

Senin app.jar bağımlılıklarını zaten yanında getiriyor. (Maven/Gradle → JAR içine gömüyor)

Ama o JAR’ın çalışacağı ortam (Java, DB, web server, sistem kütüphaneleri) → PMS tarafından yönetiliyor.

Yani PMS = Server ortamını hazırlayan sistem
Senin JAR = Uygulaman

# Linux’ta paket yönetimi çeşitleri, kullanılan dağıtıma (distribution) ve tarihsel olarak geliştirilen yöntemlere göre oluşmuştur.
Yani her Linux dağıtımı kendi paketleme ekosistemine sahiptir.

1. İkili Paket Yöneticileri (Binary Package Managers)

Kaynak koddan derlemekle uğraştırmaz, hazır derlenmiş paketleri yükler.

Debian tabanlı (Ubuntu, Linux Mint vb.)

dpkg → en temel araçtır (paketi kurar ama bağımlılık çözmez).

APT (Advanced Package Tool) → bağımlılık çözme, güncelleme, repository yönetimi yapar.

Red Hat tabanlı (Fedora, CentOS, RHEL, Rocky Linux vb.)

RPM (RedHat Package Manager) → temel paket aracı.

YUM / DNF → RPM üzerine kurulmuş, bağımlılık çözümü ve repo yönetimi sağlar.

Arch Linux tabanlı (Manjaro vb.)

pacman → Arch’ın kendi güçlü paket yöneticisi.

Bu grupta her dağıtım kendi formatını (.deb, .rpm, vb.) geliştirmiştir.
Seçim sebebi: dağıtımın felsefesi, hedef kitlesi ve tarihsel gelişim.

2. Kaynak Kod Tabanlı Paket Yöneticileri

Paket, hazır derlenmiş değil, kaynak kod olarak gelir ve kullanıcı sisteminde derlenir.

Gentoo → Portage (FreeBSD’nin ports sisteminden esinlenmiş).

BSD’lerde (FreeBSD, OpenBSD) → ports collection mantığı.

Bu yöntem sistem üzerinde tam optimizasyon sağlar (kendi CPU’ya göre derleme, özel ayarlar).
Ama kurulum uzun sürer.

3. Evrensel / Dağıtım Bağımsız Paket Sistemleri

Her dağıtımda aynı paketi çalıştırabilmek için geliştirildi.

AppImage → Tek dosya halinde çalışır, kurulum gerekmez.

Snap (Ubuntu/Canonical) → sandbox içinde paket çalıştırma.

Flatpak (Red Hat destekli) → benzer şekilde sandbox tabanlı.

Buradaki amaç: “her dağıtımda çalışacak, bağımlılık derdi olmayan, evrensel paketleme”.

4. Konfigürasyon ve Otomasyon Bazlı Yönetim

Daha üst seviye araçlar, paket yönetimini otomasyonla birleştirir.

Ansible, Puppet, Chef, SaltStack → paketlerin belirli versiyonlarını otomatik kurma ve güncelleme.
Bunlar sistem yöneticileri için yüzlerce makineyi aynı anda yönetmek amacıyla ortaya çıkmıştır.

Özet:

.deb / .rpm tabanlı → dağıtım felsefesi ve tarihsel ayrışma nedeniyle.

pacman / portage gibi özel sistemler → dağıtımın özgün yaklaşımı nedeniyle.

Snap / Flatpak / AppImage → dağıtımlar arası ortak bir çözüm sunmak için.

Otomasyon sistemleri → çoklu sunucu ve kurumsal yönetim için.

# Distribution (Dağıtım / Distro) nedir?

Linux aslında tek başına tam bir işletim sistemi değildir; sadece çekirdektir (Linux kernel).

Bunun üzerine paket yöneticileri, kütüphaneler, grafik arayüz (GNOME, KDE gibi), sistem araçları, sürücüler ve uygulamalar eklenince kullanılabilir bir işletim sistemi haline gelir.

Bu bütünleşmiş sistemlere Linux dağıtımı (distribution, distro) denir.

Örneğin:

Ubuntu → Debian tabanlı bir dağıtımdır.

Debian → Kendi başına büyük bir dağıtımdır.

Fedora → Red Hat tabanlıdır.

Arch Linux → Minimalist, kullanıcıya bırakılan bir dağıtımdır.

Yani distro, Linux çekirdeğini + ek yazılımları + paket yöneticisini bir araya getirip sana hazır bir işletim sistemi sunan versiyonudur.

Paket yönetimi çeşitleri ve dağıtımla ilişkisi

Her dağıtımın kendine has bir paket yönetim sistemi vardır:

Debian/Ubuntu tabanlılar → APT (Advanced Package Tool)

Paket uzantıları: .deb

Komutlar: apt-get install, apt update

Red Hat/CentOS/Fedora → YUM / DNF

Paket uzantıları: .rpm

Komutlar: dnf install, yum update

Arch Linux → pacman

Paket uzantıları: .pkg.tar.zst

Komutlar: pacman -S, pacman -Sy

OpenSUSE → zypper

Paket uzantıları: .rpm

Komutlar: zypper install

Özet:

Distribution (distro, dağıtım) → Linux çekirdeği + ek yazılımlar + paket yöneticisi ile oluşturulmuş tam işletim sistemi.

Paket yöneticisi → Dağıtıma göre değişir, program kurma/kaldırma/ güncelleme işini yapar.

#  pms'lerde format ve tools  nedir?

1. Format nedir?

Her Linux dağıtımı (distro), paketlerini belirli bir formatta paketler:

Debian/Ubuntu → .deb dosyası

CentOS/Fedora/RHEL → .rpm dosyası

FreeBSD → .txz veya Ports sistemi

Bu format, paket dosyasının uzantısıdır. İçinde yazılımın kendisi + metadata (sürüm bilgisi, bağımlılıklar vs.) vardır.
Windows’taki .exe veya .msi, Android’deki .apk gibi düşünebilirsin.

2. Tools nedir?

Paketleri yönetmek için kullanılan komut satırı araçlarıdır (Package Manager Tools).
Bunlar paketleri:

indirir,

kurar,

günceller,

bağımlılıkları çözer,

kaldırır.

Örneğin:

Debian/Ubuntu → apt, apt-get, dpkg

CentOS → yum

Fedora → dnf

FreeBSD → pkg, make

Özetle:

Format → Paketlerin dosya türü (deb, rpm, txz vs.).

Tools → O paketleri yönetmek için kullanılan araçlar (apt, yum, dnf, dpkg vs.).

# Linux distro’larının formatı (paket dosya uzantısı) ve tools (paket yöneticisi araçları) vardır:

1. Debian

Format: .deb (Debian package format)

Tools:

apt → modern, kolay kullanım aracı

apt-get → eski ama hâlâ kullanılan araç

apt-cache → paket arama ve önbellek yönetimi

dpkg → en düşük seviyede, tek .deb dosyasını kurup kaldırır

2. Ubuntu (Debian tabanlı)

Format: .deb

Tools: Debian ile aynı (çünkü Debian üzerine kurulu):

apt, apt-get, apt-cache, dpkg

3. CentOS (Red Hat tabanlı)

Format: .rpm (Red Hat Package Manager format)

Tools:

yum → paket yöneticisi (eski ama uzun süre kullanıldı)

4. Fedora (Red Hat tabanlı, CentOS’un abisi gibi düşünebilirsin)

Format: .rpm

Tools:

dnf → yum’un modern ve daha hızlı versiyonu

5. FreeBSD (Linux değil, ama Unix türevi)

Format: Ports, .txz (sıkıştırılmış paket formatı)

Tools:

make (kaynak koddan derleme)

pkg (ikili paket yönetimi)

Özet:

Format → hangi uzantıda paket dosyaları geldiğini gösterir (.deb, .rpm, .txz gibi).

Tools → o formatı kullanarak paketleri indirip kurmaya, güncellemeye yarayan araçlardır (apt, yum, dnf, pkg gibi).

# Görselde Linux dağıtımları ve paket yönetim sistemleri arasındaki ilişkiyi açıklayan bir diyagram var. 
Temel Kavramlar:

Linux Dağıtımları (Distrolar):

Linux, farklı dağıtımlar (distro) olarak kullanılır. Her dağıtım, kendine özgü özellikler ve paket yönetim araçları sunar. Görselde şu dağıtımlar yer alıyor:

Debian ve Ubuntu: Debian ailesine aittir.
CentOS ve Fedora: Fedora ailesine aittir.
Amazon Linux: Bağımsız bir ticari dağıtım.
FreeBSD: Linux değil, BSD tabanlı bir işletim sistemi (farklı bir aile).




Paket Formatları:

Yazılımlar, dağıtımlarda paketler halinde gelir. Her dağıtım farklı bir paket formatı kullanır:

.deb: Debian ve Ubuntu için kullanılır.
.rpm: CentOS, Fedora ve Amazon Linux için kullanılır.
Ports, .txz: FreeBSD için kullanılır (farklı bir sistem).




Paket Yönetim Araçları:

Bu araçlar, paketlerin yüklenmesini, güncellenmesini ve yönetilmesini sağlar. Her dağıtım, kendi araç setine sahiptir:

Debian/Ubuntu: apt, apt-cache, apt-get, dpkg (örneğin, apt install ile bir yazılım yükleyebilirsin).
CentOS/Fedora/Amazon Linux: yum veya dnf (örneğin, yum install veya dnf install).
FreeBSD: make, pkg.





İlişkiler:

Aileler ve Sistemler:

Debian ve Ubuntu, Debian ailesine aittir ve aynı .deb formatını kullanır. Bu aile, apt tabanlı araçlarla yönetilir.
CentOS ve Fedora, Fedora ailesine aittir ve .rpm formatını kullanır. Bu ailede yum (CentOS) veya dnf (Fedora) kullanılır.
Amazon Linux da .rpm kullanır ama bağımsız bir sistemdir.
FreeBSD, Linux’tan farklı bir kökene sahip olduğundan ayrı bir yol izler (Ports ve pkg).


Diyagramdaki Akış:

Üstteki kutular (Ubuntu, Amazon Linux, vb.) ana dağıtımları gösterir.
Bunlar, orta seviyedeki paket yönetim araçlarına (örneğin, apt-get, zypper, yum) bağlanır.
Alt seviyede ise paket formatları (.deb, .rpm, vb.) ve ilgili komutlar (örneğin, dpkg, rpm) yer alır.
Her şey en altta "Linux System" veya FreeBSD ile birleşir, çünkü bunlar temel işletim sistemleridir.



Özet:

Her Linux dağıtımı, kendine özgü bir paket formatı ve yönetim aracı kullanır.
Debian/Ubuntu .deb ve apt ile, CentOS/Fedora .rpm ve yum/dnf ile çalışır.
FreeBSD ise farklı bir yaklaşımla (Ports ve pkg) iş görür.
AWS kursunda Amazon Linux ile çalışacaksan, .rpm ve yum/dnf komutlarını öğrenmek iyi bir başlangıç olur.


# 1. | ne demek?

| (pipe / boru) bir komutun çıktısını başka bir komutun girdisi yapar.

Yani:

yum list installed | grep ^http


burada:

yum list installed → tüm kurulu paketleri listeler.

grep ^http → gelen listede adı http ile başlayanları süzer.

Aynı şey apt tarafında da geçerli:

dpkg -l | grep ^ii | grep ^http


dpkg -l → tüm paketleri listeler.

grep ^ii → sadece kurulu olanları (başında ii yazanlar) seçer.

grep ^http → onların içinden http ile başlayanları alır.

2. Neden dpkg kullandık, apt değil?

apt genelde yükleme, kaldırma, güncelleme işlemleri için kullanılır.

Paketleri listeleme işinde ise en doğru ve detaylı aracı dpkg’dir.

Örnek:

apt list --installed komutu da var ama çıktısı daha uzun ve farklı formatta.

dpkg -l ise standart ve kolay filtrelenebilir çıktısı olduğu için daha çok tercih edilir.

Özet:

| → bir komutun çıktısını diğerine gönderir.

dpkg -l → apt tabanlı sistemlerde paketleri listelemek için kullanılır (apt daha çok paket yönetimi için).