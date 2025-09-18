
# komuttaki kullanımda davranış farklı değil, ama kullanım sonucu ve kısa devre (short-circuit) davranışı bazen kafa karıştırıyor.

cmd1 && cmd2 → cmd1 başarılıysa (exit 0) cmd2 çalışır. Aksi halde cmd2 çalışmaz.

cmd1 || cmd2 → cmd1 başarısızsa (exit ≠ 0) cmd2 çalışır. Aksi halde cmd2 çalışmaz.

! cmd → cmd’nin başarısını tersine çevirir (başarılıysa ! ile başarısız olur).

Shell, bu operatörlerde short-circuit yapar: gerektiği anda sonraki komutu çalıştırmayıp atlar.

Neden senin gözlemine uyar?

“and için 1. komut çalışırsa diğer çalışıyordu” → bu tam && davranışı: ls dosya && cat dosya — ls varsa başarılı olur (0), o zaman cat çalışır.

“ilk komut çalışmazsa ikinci komut çalışıyordu” → bu || davranışı: grep foo file || echo "yok" — grep hata verirse (eşleşme yok veya dosya yok) echo çalışır.

Dikkat: zincirlerdeki karışıklık

cmd1 && cmd2 || cmd3 yazdığında:

cmd1 başarılıysa cmd2 çalışır; sonra cmd2 başarısızsa cmd3 çalışır.

Yani cmd3 sadece cmd1 veya cmd2’nin başarısız olduğu durumlarda çalışabilir — bu bazen istenenden farklı olur.
Gruplamak için parantez veya if kullanmak daha güvenlidir.

# Linux’ta case yapısı, bash scriptlerde çok dallı koşul kontrolleri yapmak için kullanılır.
if-elif-else zincirinin daha temiz, okunabilir halidir.

Genel Söz Dizimi
case <değişken veya ifade> in
  kalıp1)
    komutlar
    ;;
  kalıp2)
    komutlar
    ;;
  kalıp3 | kalıp4)   # birden fazla eşleşme
    komutlar
    ;;
  *)
    varsayılan_komutlar
    ;;
esac


case ile esac arasında yazılır (tersi gibi düşün: if … fi gibi).

;; → her bir bloğun bittiğini gösterir.

* → default gibi, hiçbir kalıba uymayan durumlarda çalışır.

| → birden fazla kalıp tanımlamak için kullanılır.

Kalıplar wildcard mantığıyla çalışır (*, ?, [ ] kullanılabilir).

Wildcard Örneği
read -p "Bir dosya adı girin: " filename

case $filename in
  *.txt)
    echo "Bu bir metin dosyası"
    ;;
  *.sh)
    echo "Bu bir shell script dosyası"
    ;;
  *)
    echo "Bilinmeyen dosya türü"
    ;;
esac

Neden Kullanılır?

Çok sayıda koşulu daha temiz yazmak için (if … elif … elif … else yerine).

String pattern eşleşmesi gerektiğinde (ör. dosya uzantıları).

Okunabilirliği artırmak için.

# Bash dilinde 3 temel döngü vardır:

1. for loop

Bir liste veya aralık üzerinde döner.

Söz dizimi:

for var in liste
do
  komutlar
done


Örnek:

for i in 1 2 3 4 5
do
  echo "Sayı: $i"
done


C-style for (C diline benzer):

for ((i=1; i<=5; i++))
do
  echo "Sayı: $i"
done

2. while loop

Koşul doğru olduğu sürece çalışır.

Söz dizimi:

while [ koşul ]
do
  komutlar
done


Örnek:

i=1
while [ $i -le 5 ]
do
  echo "Sayaç: $i"
  ((i++))
done

3. until loop

Koşul yanlış olduğu sürece çalışır (while’ın tersi).

Söz dizimi:

until [ koşul ]
do
  komutlar
done


Örnek:

i=1
until [ $i -gt 5 ]
do
  echo "Sayaç: $i"
  ((i++))
done

4. select loop (bonus 😊)

Menü yapmak için kullanılır.

Örnek:

select meyve in Elma Muz Portakal
do
  echo "Seçtiniz: $meyve"
  break
done


Özet:

for → liste veya aralık döngüsü

while → koşul doğruysa çalışır

until → koşul yanlışsa çalışır

select → menü oluşturmak için

# Bash’te (varsayılan olarak) blok içinde tanımlanan değişkenler dışarıda da geçerlidir.

Senin örneğinde:

for i in {1..100}
do
    sum=$((sum+i))
done
echo "sum : $sum"


sum değişkeni for döngüsünün içinde oluşturuluyor.

Ama Bash tüm script boyunca aynı scope’u (alanı) kullanıyor. Yani döngü, if bloğu, case bloğu → hepsi aynı scope içinde.

Bu yüzden sum döngüden çıktıktan sonra da erişilebilir.

İstisna:

Eğer bir değişkeni local yaparsan, sadece o fonksiyon içinde geçerli olur:

myfunc() {
    local x=10
    echo "fonksiyon içi: $x"
}
myfunc
echo "fonksiyon dışı: $x"   # boş döner


Özet:

Bash’te bloklar scope oluşturmaz → değişken dışarıda da geçerlidir.

Fonksiyonlar scope oluşturur, ama orada da local kullanmazsan değişken dışarı sızar.
