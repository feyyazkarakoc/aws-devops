
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