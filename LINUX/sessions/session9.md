
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


👉 Özet: Shell script = Linux komutlarını otomatikleştiren küçük progr