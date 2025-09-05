
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

# Here Document (Heredoc) 

Komut:
cat << EOF > techproeducation.txt
Take a career voyage with us.
EOF

Ne oluyor burada?

cat << EOF

cat → normalde dosya içeriğini ekrana basar.

<< EOF → Here Document başlatır.

Yani “EOF satırını görene kadar, yazdığın her şeyi cat’e standard input (stdin) olarak ver” demek.

EOF burada delimiter (sınırlandırıcı). Sen bunu EOF, END, STOP, hatta MERHABA bile yapabilirsin. Standart olarak hep EOF kullanılır ama şart değil.

Örnek:

cat << SON
Merhaba Dünya
Linux güzeldir
SON


Çıktısı:

Merhaba Dünya
Linux güzeldir


> techproeducation.txt

Normalde cat çıktısını terminale (stdout) basardı.

> operatörü ile yönlendirdin → stdout’u techproeducation.txt dosyasına yaz.

Böylece ekrana basılmaz, dosyanın içine yazılır.

İçerik kısmı

Take a career voyage with us.


Bu satır(lar) cat’e stdin olarak gönderiliyor.

EOF (kapatıcı delimiter)

Burada heredoc bitiyor.

Shell “buraya kadar yazılanları cat komutuna input olarak ver” diyor.

Sonuç:

Dosyanın içeriği artık şöyle oldu:

cat techproeducation.txt

Take a career voyage with us.

Özet:

<< → heredoc başlatır (stdin’den komuta metin akışı verir).

EOF → sadece bir işaretçidir, ismi değiştirilebilir. “End Of File” anlamında kullanılır, ama sabit olmak zorunda değil.

> → çıktıyı dosyaya yönlendirir (overwrite eder).

Bu yöntem çok satırlı yazıları dosyaya gömmek için pratik bir yoldur.

Ekstra: Eğer dosyaya ekleme yapmak isteseydin >> kullanırdın:

cat << EOF >> techproeducation.txt
Yeni satır eklendi
EOF