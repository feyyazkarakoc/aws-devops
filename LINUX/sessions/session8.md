
# linuxta  stdin, stdout, stderr nedir?

1. Standart giriş / çıkış akışları (file descriptor’lar)

Her process (program) çalıştığında Linux ona 3 tane varsayılan kanal (stream) açar:

İsmi	File Descriptor	Açıklama
stdin	0	Standart giriş → programın kullanıcıdan veya başka bir programdan okuduğu veri
stdout	1	Standart çıkış → programın normal çıktıları
stderr	2	Standart hata → programın hata mesajları

2. Daha anlaşılır şekilde

stdin (0) → “Input” (kullanıcının klavyeden girdiği veya başka bir programın pipe ile gönderdiği şey).

cat


yazınca klavyeden ne yazarsan stdin’den okunur.

stdout (1) → Normal çıktılar buradan akar.

echo "Merhaba Dünya"


ekrana yazılır çünkü varsayılan olarak stdout terminale bağlıdır.

stderr (2) → Hata mesajları buradan akar.

ls /olmayan/klasor


→ hata çıktısı stderr’den gelir.

3. Neden ayrı?

Çünkü stdout ve stderr’i ayrı yönlendirebilirsin:

Örnek:
ls /etc > out.txt

Normal çıktıyı out.txt dosyasına kaydeder (stdout).

ls /olmayan/klasor 2> err.txt

Hata çıktısını err.txt dosyasına kaydeder (stderr).

ls /etc /olmayan/klasor > out.txt 2> err.txt

Normal çıktı out.txt’ye, hatalar err.txt’ye gider.

ls /etc /olmayan/klasor > all.txt 2>&1

stdout ve stderr birleşip aynı dosyaya gider.

4. Kısacası:

stdin (0) → programın girdiği şey

stdout (1) → programın doğru çıktıları

stderr (2) → programın hata çıktıları