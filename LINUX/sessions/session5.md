
# Shell Variables (Kabuk Değişkenleri)

Bir shell oturumu (ör. bash, zsh) içinde tanımladığın değişkenlerdir.

Sadece o shell’de (ve onun alt shell’lerinde) geçerlidir.

Başka bir programa veya başka bir shell’e aktarılmaz.

Örn:

NAME="Feyyaz"
echo $NAME   # Feyyaz


Burada NAME sadece mevcut terminal oturumunda bilinir.

# Environmental Variables (Çevresel Değişkenler)

Sistemde çalışan programların veya processlerin görebileceği değişkenlerdir.

Shell variables’tan farkı: export edilerek ortama aktarılır.

Örn:

NAME="Feyyaz"        # Shell variable
export NAME          # Artık environment variable oldu
bash                 # Yeni bir alt shell aç
echo $NAME           # Feyyaz (çünkü export edildi)


Örnek yaygın environment değişkenleri:

PATH → komutların nereden çalıştırılacağını belirler.

HOME → kullanıcının ana dizini.

USER → kullanıcı adı.


Her environment variable aynı zamanda bir shell variable’dır, ama her shell variable environment variable değildir.

Yani:

VAR=value → sadece shell’de.

export VAR=value → shell + tüm alt processlerde.

Listelemek için

Shell değişkenlerini görmek:

set


Environment değişkenlerini görmek:

printenv


veya

env

Özet:

Shell variable = sadece o shell için geçerli.

Environment variable = export edilirse shell dışındaki processlere de aktarılır.

# common enviroment varriables nedir?
Linux ve genel olarak işletim sistemlerinde environment variables (çevre değişkenleri), oturumlar ve işlemler (process) 
arasında kullanılan ön tanımlı ya da kullanıcı tarafından tanımlanmış değişkenlerdir. Bunlar genellikle sistemin nasıl 
davranacağını, programların nereden kütüphane arayacağını, hangi dil/yerel ayar kullanılacağını belirler.

Common (yaygın) environment variables:

Aşağıdakiler Linux/Unix tabanlı sistemlerde en sık görülen çevre değişkenleridir:

Kullanıcı & Sistem ile ilgili:

USER → Mevcut kullanıcı adı

HOME → Kullanıcının ev dizini (/home/username)

SHELL → Kullanıcının varsayılan shell’i (ör: /bin/bash)

PWD → Mevcut çalışma dizini (Print Working Directory)

OLDPWD → Bir önceki çalışma dizini

Komut yolları:

PATH → Çalıştırılabilir dosyaların aranacağı dizin listesi (örn: /usr/bin:/bin:/usr/local/bin)

LD_LIBRARY_PATH → Paylaşımlı kütüphanelerin aranacağı dizinler

MANPATH → man sayfalarının aranacağı dizinler

Sistem & Dil/Locale:

LANG → Varsayılan dil/yerel ayar (örn: en_US.UTF-8, tr_TR.UTF-8)

LC_ALL, LC_CTYPE, LC_TIME → Locale ile ilgili detaylı ayarlar

TZ → Zaman dilimi (örn: Europe/Istanbul)

HOSTNAME → Makinenin adı

Programlarla ilgili:

EDITOR → Varsayılan metin editörü (örn: vim, nano)

VISUAL → Terminal tabanlı editör yerine görsel editör tercihi

PAGER → Uzun çıktılar için kullanılan program (örn: less)

MAIL → Kullanıcının mail kutusu yolu

Geliştirme / Debug:

JAVA_HOME → Java kurulum dizini

PYTHONPATH → Python modüllerinin aranacağı dizinler

CFLAGS, LDFLAGS → Derleyiciye verilecek parametreler

Özet:

Common environment variables = tüm sistemlerde yaygın olarak bulunan, kullanıcı oturumunu ve programların
çalışma şeklini belirleyen değişkenlerdir.

Bunların bir kısmı login sırasında shell tarafından set edilir, bir kısmı system-wide (/etc/environment, /etc/profile)
dosyalarında tanımlıdır.

# Bir dosyanın Linux’ta executable (çalıştırılabilir) olması için üç temel şart vardır:

1. Dosyanın izinlerinde (permissions) çalıştırma izni (x) olması gerekir

Bir dosya çalıştırılabilir hale gelmesi için owner (kullanıcı), group (grup) veya others (diğerleri) için x izni verilmelidir.

Örneğin:

ls -l script.sh
-rw-r--r-- 1 feyyaz feyyaz 1234 Aug 26 10:00 script.sh


Burada rw- var ama x yok → çalıştırılamaz.

Çalıştırılabilir yapmak için:

chmod +x script.sh


Şimdi:

ls -l script.sh
-rwxr-xr-x 1 feyyaz feyyaz 1234 Aug 26 10:00 script.sh

2. Dosyanın içeriği çalıştırılabilir bir şey olmalı

Eğer binary dosya ise zaten makine kodudur, direkt çalışır.

Eğer script ise (ör. .sh), en başta shebang (#!) satırı olmalıdır. Bu, hangi yorumlayıcı ile çalıştırılacağını belirtir.
Örnek:

#!/bin/bash
echo "Hello World"

3. Dosyanın çalıştırılması için doğru şekilde çağrılması gerekir

Eğer bulunduğunuz klasördeyse:

./script.sh


(./ koymak gerekir çünkü $PATH içinde genelde . yani bulunduğun dizin yoktur.)

Eğer sistemin bir yerinde çalışmasını istiyorsan, dosyayı PATH değişkeninde olan dizinlere (ör. /usr/local/bin) taşıyabilirsin.

sudo mv script.sh /usr/local/bin/myscript
myscript


Özet:

chmod +x dosya → executable yapmak için.

Scriptlerde #!/bin/bash (veya #!/usr/bin/python3) gibi shebang olmalı.

./dosya veya PATH içindeki bir dizine koyarak çağırabilirsin.