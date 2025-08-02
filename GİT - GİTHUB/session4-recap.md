
# Bu komutlar dosya oluşturma, görüntüleme ve düzenleme işlemlerinde sıkça kullanılan temel komutlardır. 
touch README.md
Ne yapar:
Boş bir dosya oluşturur. Eğer README.md isimli dosya zaten varsa, dosyanın "son değiştirilme tarihini" günceller.

Gerçek hayatta ne işe yarar:
Projeye dokümantasyon başlatmak için kullanılır. README.md genellikle bir projenin tanıtım yazısıdır.

DevOps için önemi:
Pipeline’larda veya build script’lerinde gerekli dosyaların oluşturulması gerekebilir. Otomasyonlarda sık kullanılır.

echo "# AWS Project" > README.md
Ne yapar:
"# AWS Project" yazısını alır ve README.md dosyasının içine yazar (önceki içeriği siler).

Gerçek hayatta nasıl kullanılır:
Hızlıca bir dosyaya içerik eklemek için kullanılır. Örneğin, projenin başlığı için.

DevOps için önemi:
Script'ler ile dosya içeriklerini otomatik yazmak gerektiğinde sık kullanılır.

cat README.md
Ne yapar:
README.md dosyasının içeriğini terminalde gösterir.

Gerçek kullanım:
Hızlıca bir dosyanın içeriğine bakmak için kullanılır.

DevOps açısından:
Log dosyalarını veya config dosyalarını terminalden hızlıca görmek istenirse kullanılır. CI/CD hatalarında faydalıdır.

code main.py
Ne yapar:
VSCode yüklü ise main.py dosyasını VSCode ile açar. Eğer dosya yoksa yeni bir main.py dosyası oluşturup açar.

Gerçek kullanım:
Kod yazmaya başlamak için dosyayı hızlıca editörde açmak.

DevOps yönüyle:
Script yazımı, otomasyon araçları (bash, Python scriptleri gibi) için gerekli dosyaları açıp düzenlemek için kullanılır.

echo ile >> ne işe yarar?
echo "metin" > dosya.txt
Dosyaya yeni içerik yazar, önceki içeriği siler.
echo "metin" >> dosya.txt
Dosyanın sonuna ekleme yapar, önceki içerik korunur.
DevOps'ta kullanım örnekleri:
echo "export PATH=$PATH:/usr/local/bin" >> ~/.bashrc
Kullanıcının PATH değişkenine bir yol eklerken .bashrc dosyasına yeni satır olarak yazar.


