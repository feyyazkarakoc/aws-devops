
# Shell Script Nedir?

Shell: Komut satırında yazdığın her şeyi yorumlayan programdır. (örn. bash, sh, zsh).

Script: İçinde birden çok komut bulunan dosya.

Yani Shell Script → Linux komutlarını, kontrol yapıları (if, loop vs.), fonksiyonları bir dosyada yazıp çalıştırmak.

Programlama gibi çalışır, ama aslında shell’in komutlarını otomatikleştirir.

1. Shell Script Nasıl Yazılır?

Dosya oluştur:

nano script.sh


İçine yaz:

#!/bin/bash
echo "Merhaba, bu benim ilk scriptim!"


#!/bin/bash → shebang denir. Bu dosyanın hangi shell ile çalışacağını söyler.

echo → ekrana yazdırır.

Çalıştırılabilir yap:

chmod +x script.sh


Çalıştır:

./script.sh

2. Script’te Kullanılan Yapılar
Değişkenler
#!/bin/bash
NAME="Ahmet"
echo "Merhaba $NAME"

Kullanıcıdan girdi almak
#!/bin/bash
echo "Adınızı girin: "
read AD
echo "Merhaba $AD"

İf yapısı
#!/bin/bash
if [ -f "dosya.txt" ]; then
  echo "dosya var"
else
  echo "dosya yok"
fi


-f → dosya var mı kontrol eder.

-d → dizin var mı.

-eq, -lt, -gt → sayısal karşılaştırmalar.

Döngü (for, while)
#!/bin/bash
for i in 1 2 3 4 5
do
  echo "Sayı: $i"
done

#!/bin/bash
sayi=1
while [ $sayi -le 5 ]
do
  echo "Sayı: $sayi"
  ((sayi++))
done

Fonksiyonlar
#!/bin/bash
selamla () {
  echo "Merhaba $1"
}
selamla "Linux"

3. Script Kullanım Alanları

Sistem yönetimi (backup, log temizleme, servis kontrolü).

Otomasyon (aynı komutları sürekli çalıştırmak yerine script).

Kurulum scriptleri.

DevOps / CI/CD ortamlarında pipeline scriptleri.

Cron ile zamanlanmış görevler.

4. İyi Uygulamalar (Best Practice)

Scriptin en başına #!/bin/bash ekle.

set -e → hata olduğunda script dursun.

set -u → tanımsız değişken kullanıldığında hata versin.

Değişkenleri "$VAR" şeklinde tırnakla kullan, boşluklardan dolayı sorun çıkmaz.

Log tut (örn. echo "..." >> log.txt).

Küçük Örnek: Backup Scripti
#!/bin/bash
SOURCE="/home/ec2-user"
TARGET="/tmp/backup_$(date +%F).tar.gz"

tar -czf $TARGET $SOURCE

echo "Backup tamamlandı: $TARGET"

Özet: Shell script = Linux komutlarını otomatikleştiren küçük programcıklar. Programlama diline çok benziyor ama aslında shell komutlarının yazılıp sırayla çalıştırılması.

# Sorun PATH'e dosya ile dizin karıştırmanızda:
Yanlış kullanım:
export PATH=$PATH:/home/ec2-user/first.sh
                                 ^^^^^^^^
                                Bu bir DOSYA!
PATH sadece DİZİNLER içerir, dosyalar değil!
Doğru kullanım:
export PATH=$PATH:/home/ec2-user
Bu bir DİZİN!
PATH nasıl çalışır:
PATH'te dizinler listelenir:
echo $PATH
/usr/bin:/bin:/usr/local/bin:/home/ec2-user
Komut aradığında:

first.sh komutu çalıştırılır
System her PATH dizininde arar:

/usr/bin/first.sh var mı?
/bin/first.sh var mı?
/usr/local/bin/first.sh var mı?
/home/ec2-user/first.sh var mı?  BULDU!



Özet:

PATH = dizinler listesi
Dosya yolu değil, dizin yolu eklenir
System o dizinlerde çalıştırılabilir dosyalar arar

YANLIŞ:
export PATH=$PATH:/home/ec2-user/first.sh  # Dosya yolu

DOĞRU:  
export PATH=$PATH:/home/ec2-user           # Dizin yolu

# 6. madde açıklaması:
"num1 ve num2 değişkenlerini kullanıcıdan almak yerine Komut satırı argümanlarından İletilecek şekilde değiştirin"
Yani:
Şu anki hali (kullanıcıdan input):
read -p "Birinci sayıyı giriniz : " num1
read -p "İkinci sayıyı giriniz : " num2
İstenen hali (komut satırı argümanı):
num1=$1    # İlk argüman
num2=$2    # İkinci argüman
Kullanım farkı:
Eski yöntem:
./math2.sh
Script çalışır, sizden sayı ister:
"Birinci sayıyı giriniz : " 15
"İkinci sayıyı giriniz : " 14
Yeni yöntem:
./math2.sh 15 14
Sayıları komut satırında veriyorsunuz
Script sormuyor, direkt alıyor
Argümanlar:

$1 = ilk argüman (15)
$2 = ikinci argüman (14)
$0 = script adı (math2.sh)

Özet: read komutlarını kaldırıp num1=$1 ve num2=$2 kullanacaksınız!

# Linux’ta betik (script), kabuk (shell) tarafından çalıştırılabilecek komutların bir dosya içinde topluca yazılmış hâlidir.

Yani normalde terminalde tek tek yazacağın komutları, sırayla bir dosyaya koyup çalıştırmana olanak tanır.
En çok kullanılan betikler bash script’lerdir (.sh uzantılı dosyalar).