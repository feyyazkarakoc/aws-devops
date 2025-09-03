
# /etc/passwd dosyası

Linux sisteminde kullanıcı hesaplarının bilgilerini tutar.

Her satır bir kullanıcıya aittir.

Şifreler burada yok (eski Unix’lerde vardı, ama güvenlik nedeniyle /etc/shadow dosyasına taşındı).

Her satır şu formatta:

kullanıcı_adı : parola : UID : GID : açıklama : home_dizini : shell

Sütunlar (örnek: ec2-user:x:1000:1000:EC2 Default User:/home/ec2-user:/bin/bash)

Kullanıcı adı

ec2-user


Sisteme giriş yaparken kullandığın hesap adı.

Parola alanı

x


Eskiden burada hashli şifre olurdu. Şimdi güvenlik için /etc/shadow dosyasına taşındı. Burada x yazıyorsa "şifre shadow dosyasında" demek.
Eğer * veya ! olursa o kullanıcı login olamaz.

UID (User ID)

1000


Kullanıcının sayısal kimliği.

0 = root

1–999 = sistem kullanıcıları (daemon, service account)

1000+ = normal kullanıcılar (mesela ec2-user)

GID (Group ID)

1000


Kullanıcının primary group kimliği (/etc/group dosyasında detay var).

GECOS (Açıklama alanı)

EC2 Default User


Kullanıcı hakkında açıklama. Opsiyonel, genellikle boş bırakılır.

Home dizini

/home/ec2-user


Kullanıcının giriş yaptığında bulunduğu başlangıç dizini.
root için genelde /root.

Shell (login shell)

/bin/bash


Kullanıcı giriş yaptığında açılacak komut yorumlayıcısı (bash, sh, zsh vs).
Eğer /sbin/nologin veya /bin/false yazıyorsa → o kullanıcıyla giriş yapılamaz, sadece servis için vardır.

/etc nedir?

/etc dizini, Linux’te sistem yapılandırma dosyalarının merkezidir.

Kullanıcı parolaları (/etc/passwd, /etc/shadow), servis ayarları (/etc/ssh/sshd_config), ağ ayarları vs. burada tutulur.

Yani sistemin “ayar klasörü”dür.


Özet:

/etc/passwd = kullanıcı kayıtları.

7 sütun var → kullanıcı_adı : parola_göstergesi : UID : GID : açıklama : home_dizini : shell.

/etc = tüm sistem ayarlarının bulunduğu dizin.

# usermod komutu Linux’ta bir kullanıcı hesabının özelliklerini değiştirmek için kullanılır. Yapabildiği şeyler parametreye göre değişir:

usermod -c "Açıklama" 👉 sadece description (GECOS field) değişir.

usermod -d /yeni/home/dir 👉 home directory değiştirilir.

usermod -s /bin/bash 👉 login shell değiştirilir.

usermod -l yeniad eskiad 👉 kullanıcı adı değiştirilir.

usermod -g grup 👉 primary group değiştirilir.

usermod -G grup1,grup2 👉 ek gruplar değiştirilir.

usermod -u 2001 👉 UID değiştirilir.

Yani tek başına sadece description değiştirmez, hangi parametreyi verdiğine bağlıdır.

# Sorun şu: linux1 kullanıcısının sudo yetkisi yok ve şifresi tanımlanmamış.
Ne oldu:

sudo useradd linux1 - Kullanıcı oluşturuldu ama:

Şifre atanmadı
Sudo yetkisi verilmedi


sudo su - linux1 - linux1'e geçiş yaptınız
sudo su - ec2-user - linux1 olarak sudo kullanmaya çalıştınız ama:

linux1'in sudo yetkisi yok
linux1'in şifresi yok



Çözüm:
ec2-user'a geri dönün:
exit                    # linux1'den çık
veya Ctrl+D
Şifre atayın:
sudo passwd linux1      # ec2-user olarak
sudo passwd linux2
sudo passwd linux3


# sudo usermod -G aws ec2-user    

DİKKAT! Bu komut tehlikeli!

sudo usermod -G aws ec2-user
ec2-user'ın tüm üyelikleri değişir (diğer gruplardan çıkar, sadece aws'de kalır)
ec2-user'ı adm, wheel, systemd-journal, linux gruplarından çıkarır
ec2-user'ı sadece aws grubuna üye yapar

Fark:

sudo usermod -a -G aws ec2-user    # GÜVENLI - aws grubunu EKLER
sudo usermod -G aws ec2-user       # TEHLİKELİ - SADECE aws grubuna üye yapar
