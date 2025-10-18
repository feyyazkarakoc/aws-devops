
# Storage Classes (Depolama Sınıfları), verinin S3 üzerinde nasıl ve hangi maliyetle saklanacağını belirleyen sistemdir.

Aynı dosya (örneğin data.csv) bile farklı “storage class”larda farklı fiyat, erişim süresi ve dayanıklılıkla tutulabilir.

Temel mantık

S3’te veri türüne, erişim sıklığına ve dayanıklılık ihtiyacına göre farklı sınıflar vardır.

Sık erişilen veriler → pahalı ama hızlı depolar

Nadiren erişilen veriler → ucuz ama daha yavaş depolar


1. S3 Standard Class

S3’ün varsayılan ve en yaygın depolama sınıfıdır.
Sık erişilen dosyalar (örneğin web sitesi içerikleri, uygulama verileri) için kullanılır.
Yüksek erişilebilirlik (99.99%) ve dayanıklılık (11 dokuz = %99.999999999) sunar.
Veriler birden fazla Availability Zone (AZ) içinde otomatik olarak çoğaltılır.
Fiyatı diğer sınıflara göre yüksektir ama erişim süresi çok hızlıdır.

🟦 2. Reduced Redundancy Storage (RRS)

Artık eski ve önerilmeyen bir depolama sınıfıdır.
Veri kaybı riski biraz daha yüksek, çünkü veriler daha az kopya ile saklanır.
Maliyeti düşüktür, ama güvenlik ve dayanıklılık Standard kadar iyi değildir.
Eskiden geçici veya kolay yeniden üretilebilir veriler (örneğin cache dosyaları) için kullanılırdı.
Amazon artık bu sınıfı aktif olarak önermez.

🟨 3. S3 Standard-IA (Infrequent Access)

Nadiren erişilen ama gerektiğinde anında ulaşılması gereken veriler içindir.
Standard sınıfına göre daha ucuzdur, ancak erişim başına küçük bir ücret alınır.
Veriler çok dayanıklıdır (11 dokuz), çok AZ içinde saklanır.
Yedekleme dosyaları, raporlar veya eski log’lar için idealdir.
Hızlı erişim sağlar, sadece erişim maliyeti eklenir.

🟧 4. S3 One Zone-IA

Standard-IA gibidir ama verileri tek bir Availability Zone’da saklar.
Bu yüzden daha ucuzdur, ama veri kaybı riski biraz daha yüksektir.
Kritik olmayan veya kolayca yeniden oluşturulabilen veriler için uygundur.
Erişim hızı Standard kadar yüksektir.
Örneğin cache, geçici yedek veya test çıktıları gibi dosyalarda kullanılır.

🟪 5. S3 Intelligent-Tiering

Erişim sıklığı değişken olan veriler için otomatik optimizasyon sağlar.
AWS veriyi izler ve erişim azaldığında otomatik olarak daha ucuz “cold” katmana taşır.
Kullanıcı hiçbir şey yapmadan maliyet düşer.
Performans, Standard kadar hızlıdır.
Makine öğrenimi tabanlı maliyet optimizasyonu sağlar.

🧊 6. S3 Glacier Instant Retrieval

Arşiv veriler için tasarlanmıştır ama 1–2 saniyede erişim sunar.
Standard-IA’dan daha ucuzdur.
Uzun süre saklanacak ama bazen hızlı erişilmesi gereken veriler (ör. tıbbi kayıtlar, medya arşivleri) için uygundur.
Veri çok dayanıklıdır, çok AZ içinde saklanır.
Erişim başına ücret alınır.

❄️ 7. S3 Glacier Flexible Retrieval (eski “Glacier”)

Uzun süre saklanacak, nadiren erişilecek veriler içindir.
Üç erişim modu vardır: Expedited (1–5 dk), Standard (3–5 saat), Bulk (5–12 saat).
Çok düşük maliyetlidir, arşivleme için idealdir.
Yedekler, eski proje dosyaları, uyumluluk kayıtları gibi veriler için kullanılır.
Erişim süresi uzun olduğu için canlı sistemlerde kullanılmaz.

🕳️ 8. S3 Glacier Deep Archive

S3’ün en ucuz depolama sınıfıdır.
Yılda bir-iki kez erişilen uzun vadeli arşivler için idealdir.
Geri alma süresi 12 ila 48 saat arasında değişir.
Dayanıklılığı çok yüksektir, birden fazla AZ’de saklanır.
Yasal kayıtlar, eski yedekler, arşivsel veriler için kullanılır.

| Senaryo                                | Uygun Storage Class                   |
| -------------------------------------- | ------------------------------------- |
| Web sitesinin görselleri               | S3 **Standard**                       |
| Aylık raporlar, az erişim              | **Standard-IA**                       |
| Yedekleme dosyaları, arşiv             | **Glacier** veya **Deep Archive**     |
| AI/ML modelleri, bazen erişilen        | **Intelligent-Tiering**               |
| Log dosyaları, gereksiz ama saklanmalı | **One Zone-IA** veya **Deep Archive** |


Kullanımı (örnek CLI komutu)
aws s3 cp myfile.txt s3://mybucket/ --storage-class STANDARD_IA

Bu komut myfile.txt dosyasını Infrequent Access sınıfında yükler.

# static website nedir, dinamik ile farkı nedir, s3 static website hosting nedir

🟩 Static Website (Statik Web Sitesi) nedir?

Statik web sitesi, içeriği önceden hazırlanmış ve sabit olan web sitelerdir.
Her kullanıcı siteye girdiğinde aynı HTML, CSS ve JavaScript dosyalarını görür.
Sunucu tarafında (backend) herhangi bir işlem yapılmaz.
Örneğin:

“Hakkımızda”, “İletişim”, “Portfolio” sayfaları olan basit bir site

Kişisel bloglar veya tanıtım sayfaları

Bu tür siteler genellikle sadece HTML, CSS ve JS dosyalarından oluşur.
İçerik değişikliği istiyorsan, dosyayı elinle güncellersin.

🟨 Dynamic Website (Dinamik Web Sitesi) nedir?

Dinamik web siteleri, her kullanıcıya farklı içerik gösterebilir.
Sunucu tarafında veritabanı + backend kodu (örneğin Java, Python, PHP) bulunur.
Kullanıcıdan gelen isteğe göre sayfa gerçek zamanlı oluşturulur.
Örneğin:

E-ticaret siteleri (kullanıcıya göre ürün listesi değişir)

Sosyal medya siteleri (her kullanıcı kendi gönderilerini görür)

Haber siteleri (veriler veritabanından çekilir)

| Özellik              | Statik Site                  | Dinamik Site                      |
| -------------------- | ---------------------------- | --------------------------------- |
| İçerik               | Sabit                        | Değişken (kullanıcıya göre)       |
| Backend              | Yok                          | Var (ör. Node.js, Java, PHP)      |
| Veritabanı           | Yok                          | Var (ör. MySQL, MongoDB)          |
| Performans           | Çok hızlı                    | Daha yavaş                        |
| Barındırma (Hosting) | Ucuz, basit                  | Daha karmaşık                     |
| Kullanım Alanı       | Blog, tanıtım, dokümantasyon | E-ticaret, sosyal medya, paneller |


☁️ S3 Static Website Hosting nedir?

AWS S3 (Simple Storage Service), sadece dosya depolamakla kalmaz;
statik web siteleri direkt olarak barındırmanı (host etmeni) de sağlar.

Yani senin sadece:

index.html

style.css

script.js

resim.png

gibi dosyaların varsa, bunları bir S3 bucket’a yüklersin,
ve “Static Website Hosting” özelliğini aktif edersin.

Sonra AWS sana bir URL verir:
🔗 http://mybucket.s3-website-us-east-1.amazonaws.com

Bu adres üzerinden site tamamen S3’ten yayınlanır.
Sunucu kurmana (Apache, Nginx, EC2) gerek kalmaz.
Ayrıca CloudFront ile hızlandırabilir, Route 53 ile özel domain bağlayabilirsin.

🎯 Avantajları

Sunucu yönetimi yok (serverless)

Çok hızlı (CDN ile entegre)

Ucuz (sadece depolama kadar ödersin)

Yüksek uptime

Kolay kurulum (2–3 tıklama)