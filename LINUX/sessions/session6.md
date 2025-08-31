
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