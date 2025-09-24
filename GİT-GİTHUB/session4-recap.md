
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

# git branch -a çıktısı
Tüm yerel (local) ve uzak (remote) branch’leri gösterir:

feature-setup         ← senin şu an aktif olduğun yerel branch
main                  ← bu da başka bir yerel branch
remotes/origin/main  ← bu ise uzak (remote) sunucudaki main branch

Açıklamalar:
1. feature-setup (yerel branch)
Senin bilgisayarında oluşturduğun ve şu an üzerinde çalıştığın branch.

2. main (yerel branch)
Ana branch’inin yerel kopyası. Bu da bilgisayarında mevcut.

3. remotes/origin/main (uzak branch)
GitHub (veya başka bir uzak repo) üzerindeki main branch’in son hali. origin uzak reposunun adı.

Farklar:
main senin bilgisayarında (local).

remotes/origin/main, uzak sunucuda (remote).

feature-setup senin yeni açtığın yerel bir feature branch’i.

Ekstra Bilgi:
Bir branch’in yerel veya uzak olması, onun nerede tutulduğunu gösterir:

Branch	Tür	Nerede?
main	Yerel	Senin PC'nde
remotes/origin/main	Uzak	GitHub’da vb.
feature-setup	Yerel	Senin PC'nde

# setup.sh nedir?
Bu komut:
echo "echo 'Setting up AWS Resources...'" > setup.sh
şunu yapar:

setup.sh adında bir shell script dosyası oluşturur.

İçine şunu yazar:
echo 'Setting up AWS Resources...'

setup.sh → Shell Script (sh uzantısı)
.sh uzantılı dosyalar bash (veya shell) komutlarını barındıran script dosyalarıdır.

İçinde Linux/Mac terminal komutları yazar. Windows’ta Git Bash gibi araçlarla çalıştırılır.

Bu script’i çalıştırmak için genelde şunu yaparsın:
bash setup.sh

#  .log Uzantılı Dosya Nedir?
.log, log (kayıt) dosyasıdır.
.log uzantılı dosyalar çok yaygın ve gerçek projelerde aktif olarak kullanılan dosyalardır. 
Genelde bir uygulama, sistem, ya da script çalışırken olan biteni içine yazar:

Hatalar (errors)

Bilgilendirme mesajları (info)

Uyarılar (warnings)

Başarı/başarısızlık çıktıları

Örnek bir app.log içeriği şöyle olabilir:
2025-08-04 15:32:01 INFO  - Application started
2025-08-04 15:32:05 ERROR - Failed to connect to database
2025-08-04 15:32:10 INFO  - Retrying connection...

Gerçek Projelerde Kullanımı
Evet, .log dosyaları ciddi projelerde mutlaka vardır. Örneğin:

Kullanım Alanı	Açıklama
Backend uygulamaları	Spring Boot, Django, Node.js gibi sistemler log dosyalarına yazar.
DevOps / Sunucu tarafı	Apache, Nginx, Docker log yazar (/var/log/...).
Test çıktıları	JUnit veya pytest test loglarını dosyaya basar.
Deployment işlemleri	CI/CD süreçlerinde her aşama loga yazılır.

Ne İşe Yarar?
Hata takibi: Uygulamada bir sorun çıktığında log dosyası açılır.

Debug: Geliştirici olarak ne olup bittiğini anlamak için.

Monitoring: Log dosyaları analiz edilip sistemin sağlığı takip edilir (örn: ELK stack – Elasticsearch, Logstash, Kibana).

Audit (Kayıt): Kim ne zaman ne yaptı takibi.

VS Code ve IntelliJ .log Dosyalarını Tanır mı?
Evet, ikisi de tanır:

IDE/Editör	.log dosyasını açar mı?	Renkli gösterim?	Canlı izleme?
VS Code	Evet	Evet (bazı eklentilerle)	Evet: “Log File Highlighter”, “Log Viewer” eklentileri
IntelliJ IDEA	Evet	Evet (özellikle Spring Boot loglarında iyi çalışır)	Evet (Run > Show Logs ile)

İPUCU: IntelliJ, logback.xml veya log4j2.xml gibi yapılandırma dosyalarıyla birlikte log seviyelerini detaylı yönetir (INFO, DEBUG, ERROR vb).

Sonuç
.log dosyaları ciddi projelerin vazgeçilmezidir.

Hem geliştirici hem DevOps için sistem aynasıdır.

VS Code ve IntelliJ bu dosyaları rahatça açar ve işler.



# .log Dosyalarının Oluşma Süreci
1. Geliştirici .log dosyasını elle oluşturmaz
Geliştirici genelde .log uzantılı dosyayı direkt oluşturmaz.

Onun yerine, geliştirici uygulamaya bir loglama mekanizması entegre eder.
Bu mekanizma kendi kendine .log dosyasını oluşturur ve yazar.

Örnek: Java (Spring Boot) İçin Log İşleyişi
Geliştirici şunları yapar:
Bir log kütüphanesi seçer (örneğin: Logback, Log4j2, SLF4J)

application.properties veya logback-spring.xml dosyasında konfigürasyon yazar:
application.properties
logging.file.name=logs/app.log
logging.level.root=INFO

Uygulama çalıştıkça:
/logs/app.log dosyası otomatik oluşturulur.

İçine şu tarz loglar otomatik olarak yazılır:
2025-08-04 15:21:01 INFO  - Started MainApplication in 2.345 seconds
2025-08-04 15:21:03 WARN  - User not found for ID: 42

Başka Örnekler (Framework ve Dil Bazlı)
Dil/Framework	Loglama Kütüphanesi	.log nasıl oluşur?
Java (Spring)	Logback, Log4j2, SLF4J	config dosyası belirler, otomatik yazar
Python	logging (standart modül)	logging.basicConfig(...) ile ayarlanır
Node.js	Winston, Bunyan	.log dosyasına yazacak şekilde yapılandırılır
C# (.NET)	NLog, Serilog	config ile .log dosyasına yazar

Geliştirici Ne Zaman Log Dosyasına Müdahale Eder?
Durum	Geliştirici Ne Yapar?
Normal işleyiş	Sadece logger.info(), logger.error() gibi kodlarla log yazar. Dosyaya kendisi dokunmaz.
Hata/Debug analizi	.log dosyasını açıp inceler.
Test/Deneme	Bazen elle küçük bir .log dosyası oluşturup test eder.
Temizlik	Çok büyük .log dosyaları silinir veya arşivlenir.

Özetle
.log dosyasını geliştirici yazmaz, sistem oluşturur ve doldurur.

Geliştirici sadece ne yazılacağını belirler (logger.info(...) gibi).

.log dosyaları otomatik oluşturulur ve yazılır (loglama kütüphaneleri sayesinde).

VS Code ve IntelliJ gibi IDE'ler logları güzelce gösterir, renkler vs. de desteklenebilir.




