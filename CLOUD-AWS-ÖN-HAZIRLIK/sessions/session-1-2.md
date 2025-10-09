
# Cloud (Bulut) nedir?
"Cloud" ya da Türkçesiyle "bulut", verilerin, yazılımların ve hizmetlerin internet üzerinden uzaktaki sunucularda barındırılması ve çalıştırılmasıdır. 
Kısaca, bilgisayarınıza yüklemeden uygulamalara erişebilir, dosyalarınızı saklayabilir, işlem gücü kullanabilirsiniz.

Cloud Türleri
Public Cloud (Genel Bulut): Amazon Web Services (AWS), Microsoft Azure, Google Cloud gibi herkesin kullanabileceği bulut altyapılarıdır.
Private Cloud (Özel Bulut): Sadece bir şirkete özel sunucularda barındırılan sistemlerdir.
Hybrid Cloud (Hibrit Bulut): Public + Private bulutun birlikte kullanılmasıdır.

"Cloud" aslında başka birinin bilgisayarıdır.
"Bulut" bir metafordur. Ama gerçekte, veriniz okyanusları geçen ışık paketleriyle dünyanın bir ucundaki gerçek bir bilgisayara ulaşıyor.

Why Cloud Computing? (Neden Bulut Bilişim?)
✅ Increases the value of the work
“Yapılan işin değerini artırır”
Cloud sayesinde yazılımlar daha hızlı geliştirilebilir, kullanıcıya daha iyi hizmet sunulur, böylece şirketin yaptığı işin kalitesi ve değeri artar.

✅ Zeitgeist (The spirit of the time)
“Zamanın ruhu”
Cloud, günümüz teknolojisinin bir gerekliliğidir. Artık şirketler fiziksel sunucu kurmak yerine çağın gereği olan esnek ve hızlı bulut altyapılarına yöneliyor.

✅ Cost reduction (pay as you go - source optimization)
“Maliyetlerin düşürülmesi (kullandığın kadar öde – kaynak optimizasyonu)”
Cloud ile sadece kullandığın kadar ödeme yaparsın. Örneğin sadece ayda 10 saatlik sunucu kullanıyorsan, 10 saate göre fatura gelir. Böylece gereksiz harcamalar azalır.

✅ Scalability need
“Ölçeklenebilirlik ihtiyacı”
Bulutta sistemlerini çok kolay büyütebilir (veya küçültebilirsin). Mesela bir e-ticaret sitesine Black Friday’de aniden milyonlarca kişi girerse, sistem kapasitesini otomatik artırabilirsin.

✅ Virtualization
“Sanallaştırma”
Bulut sistemlerinde fiziksel makineler tek tek kullanılmaz. Bir fiziksel sunucu, birden çok “sanal sunucu” gibi davranabilir. Bu sayede kaynaklar verimli kullanılır.

✅ Containerization Technology
“Konteyner teknolojisi (Docker gibi)”
Yazılımları taşınabilir küçük birimler hâlinde (container) çalıştırmak mümkündür. Cloud ortamı bu tür yapıları çok iyi destekler. Böylece kodun her yerde aynı çalışır.

✅ Software Development Cycle
“Yazılım geliştirme döngüsü”
Cloud, yazılım geliştirmeyi hızlandırır. Otomatik test, dağıtım (CI/CD), versiyonlama gibi işlemler cloud altyapısı üzerinde hızlı yapılır.

✅ From Monolithic to Microservices
“Tek parça (monolith) yapıdan mikro hizmetlere geçiş”
Eskiden yazılımlar tek parça hâlindeydi. Cloud ile artık yazılımlar küçük küçük bağımsız parçalar (microservices) hâlinde geliştiriliyor. Bu da esneklik, bakım kolaylığı ve ölçeklenebilirlik sağlar.

# Cloud Computing Nedir?

Cloud terimi, yerel bilgisayarınızda değil, internet üzerinde çalışan yazılım ve hizmetleri ifade eder.
Böylece verileri ve programları bilgisayarınızın sabit diskinde değil, internet üzerinden saklayabilir ve erişebilirsiniz.

Cloud Computing = Başka birinin bilgisayarında çalışan uygulama

Cloud Computing'in Açıklaması
Cloud Computing (Bulut Bilişim), bilgisayar kaynaklarının internet üzerinden hizmet olarak sunulması modelidir. Bu kavramı daha detaylı açıklayalım:
Temel Mantık: Geleneksel yaklaşımda yazılımları kendi bilgisayarımıza kurar, dosyalarımızı kendi diskimizde saklar ve işlemci gücümüzü kullanırız. Cloud computing'de ise bu kaynaklar uzak sunucularda bulunur ve internet üzerinden erişiriz.
Nasıl Çalışır: Örneğin Google Drive kullandığınızda dosyalarınız Google'ın sunucularında saklanır. Microsoft Office 365 kullandığınızda Word ve Excel programları bulutta çalışır. Netflix izlediğinizde videolar bulut sunucularından akış halinde gelir.

Ana Avantajları:

Herhangi bir cihazdan erişim imkanı
Otomatik yedekleme ve güvenlik
Büyük depolama kapasitesi
Güçlü işlem kapasitesi
Maliyet tasarrufu
Otomatik güncellemeler

Hizmet Modelleri:

SaaS (Software as a Service): Gmail, Dropbox gibi hazır uygulamalar
PaaS (Platform as a Service): Uygulama geliştirme platformları
IaaS (Infrastructure as a Service): Sanal sunucular ve altyapı hizmetleri

# "AWS için fiziksel, bizim için sanal" ne demek?
1. AWS için fiziksel:
Amazon Web Services (AWS), dünyanın birçok yerinde gerçek (fiziksel) veri merkezlerine sahiptir.
Bu veri merkezlerinde binlerce fiziksel sunucu (bilgisayar) çalışır.
Bu sunucuların soğutması, elektriği, güvenliği, donanımı gibi tüm altyapı sorumluluğu AWS’ye aittir.
2. Bizim için sanal:
Biz kullanıcılar olarak bu fiziksel sunuculara doğrudan erişmeyiz.
Onun yerine, AWS bize bu fiziksel makinelerin üzerinde çalışan sanal makineler (virtual machines) sunar.
Yani biz:
EC2 ile bir sanal sunucu kurarız,
EBS ile sanal disk kullanırız,
S3 ile sanal bir depolama alanına dosya yükleriz.
Ama aslında tüm bu hizmetler AWS’nin fiziksel makinelerinde çalışır.

# Web Sunucuları Nedir?
Web sunucuları, internetteki web sitelerinin çalışmasını sağlayan yazılımlardır (veya yazılım + donanım kombinasyonudur).
İstemciden (örneğin tarayıcıdan) gelen isteği alır,
İlgili içeriği (HTML, CSS, resim, veri vs.) geri gönderir.
Yani sen tarayıcıya www.ornek.com yazdığında, bu isteği arka planda web sunucusu karşılar ve ilgili sayfanın içeriğini sana döner.

En Popüler Web Sunucuları
Apache HTTP Server	Açık kaynak, çok yaygın, modüler	
Nginx (engine-x)	Hafif, hızlı, ters proxy ve yük dengeleme desteği güçlü	Yüksek trafikli siteler
Tomcat	Java tabanlı web uygulamaları için	JSP, Servlet uygulamaları

Web Sunucusu ile İstemci Arasındaki Akış
KULLANICI (Tarayıcı) → İstek gönderir → WEB SUNUCUSU → Sayfa içeriğini döner → KULLANICI
Örnek:
Kullanıcı: https://ornek.com/hakkimizda
Web sunucusu bu isteği alır.
Gerekirse veritabanına bağlanır.
HTML içeriği oluşturur ve gönderir.
Tarayıcıda sayfa görünür.

# web sunucuları nelerdir, ne işe yararlar
Web sunucuları, internet üzerinden web sayfalarını ve diğer web içeriklerini kullanıcılara sunan özel bilgisayar programları veya donanımlardır.
Web Sunucuları Nelerdir?
Web sunucusu, HTTP protokolü kullanarak web tarayıcılarından gelen istekleri karşılayan ve bu isteklere uygun yanıtları (HTML sayfaları, resimler, CSS dosyaları vb.) gönderen yazılım veya donanımdır. Temel olarak iki anlamda kullanılır:
Yazılım olarak: Apache HTTP Server, Nginx, Microsoft IIS, Apache Tomcat gibi programlar
Donanım olarak: Bu yazılımları çalıştıran fiziksel sunucu bilgisayarları
Ne İşe Yararlar?
Web sunucularının temel işlevleri şunlardır:
HTTP İsteklerini Karşılama: Kullanıcılar web tarayıcılarında bir adres yazdığında, sunucu bu isteği alır ve uygun yanıtı gönderir.
Statik İçerik Sunma: HTML dosyaları, CSS dosyaları, JavaScript dosyaları, resimler ve videolar gibi statik içerikleri tarayıcılara iletir.
Dinamik İçerik Üretme: PHP, Java, Python gibi programlama dilleri ile yazılmış uygulamaları çalıştırarak dinamik web sayfaları oluşturur.
Güvenlik Sağlama: SSL/TLS şifreleme, kimlik doğrulama ve yetkilendirme işlemlerini yönetir.
Yük Dengeleme: Çok sayıda kullanıcı isteğini farklı sunuculara dağıtarak performansı optimize eder.
Günlük Tutma: Gelen istekleri, hataları ve sistem durumunu kayıt altına alır.

Popüler Web Sunucuları

Apache HTTP Server: En yaygın kullanılan açık kaynak web sunucusu
Nginx: Yüksek performanslı, hafif web sunucusu ve ters proxy
Microsoft IIS: Windows tabanlı web sunucusu
Apache Tomcat: Java tabanlı web uygulamaları için servlet container
Node.js: JavaScript tabanlı web sunucusu

Web sunucuları modern internetin temel taşlarından biridir ve her web sitesinin arkasında mutlaka bir web sunucusu bulunur.

# Domain Nedir?
Domain (alan adı), internetteki web sitelerine kolayca ulaşmak için kullanılan isimdir.
Örnekler:
google.com
feyyaz.net
universite.edu.tr
Aslında her sitenin bir IP adresi vardır (örnek: 142.250.74.78) ama insanlar sayılarla değil, kelimelerle çalışmayı tercih eder.
Domain = bu sayısal adresin unutulması kolay halidir.

Domain olmadan site olur mu?
Evet, ama çok zor ulaşılır.
IP adresiyle siteye gidebilirsin ama: http://152.89.21.3
Bu kimseye hitap etmez. Domain, bu IP'ye bağlanan bir isim gibidir.

Domain Aldıktan Sonra Ne Gerekir?
Domain: feyyaz.com gibi ad
Hosting (veya cloud sunucu): Dosyaların duracağı yer
Web sitesi içeriği: HTML/CSS/WordPress...

# IP adresi = Server (Sunucu) adresidir.
IP Adresi Nedir?
IP adresi (Internet Protocol Address), internete bağlı her cihazın (bilgisayar, telefon, sunucu, modem...) benzersiz dijital adresidir.
İnternette veri gönderip almak için bu adres gerekir.

Server (Sunucu) Adresi midir?
Evet, bir web sitesinin barındırıldığı sunucunun IP adresidir.
Örneğin:
google.com'a girdiğinde aslında arka planda bu alan adı, şu IP adresine yönlenir:
142.250.74.78 (bu Google’ın bir sunucusudur)
Senin tarayıcın, bu IP adresine istek gönderir ve Google’dan veri alır.

Yani domain (alan adı), IP adresinin hatırlanması kolay hâlidir.
Tarayıcılar IP ile çalışır ama insanlar domain ile.

IP Adresi:	Gerçek sunucu (makine) adresi
Domain:	IP adresine takılmış kolay isim
Server:	IP adresine sahip fiziksel/sanal cihaz

# “Bir server'ın tek bir IP adresi varsa, o sunucuda birden fazla uygulama/web sitesi çalışıyorsa tarayıcı doğru uygulamaya nasıl ulaşır? Karışıklık nasıl önlenir?”
Cevap: Port numaraları ve alan adları (domain) sayesinde karışıklık olmaz.
1. Port Numaraları (Kapılar gibi)
Sunucuda her uygulama farklı bir port numarası dinler.
IP adresi ev gibiyse, port = o evdeki farklı odalar veya kapılar gibidir.
Örnek:
Uygulama	IP Adresi	Port
Web sitesi 1	203.12.45.7	80 (HTTP)
Web sitesi 2	203.12.45.7	8080
API sunucusu	203.12.45.7	3000
Veritabanı	203.12.45.7	5432 (PostgreSQL)

Tarayıcı veya istemci, hem IP'yi hem portu bilir, o yüzden doğru uygulamaya ulaşır.
Örnek: http://203.12.45.7:8080 dersek, doğrudan port 8080'deki uygulamaya gideriz.

2. Alan Adı (Domain) ve Sanal Hostlar (Virtual Hosts)
Portlar bazen yetmez. Bu yüzden aynı portta (mesela 80 veya 443) çalışan birden fazla siteyi ayırmak için "alan adları" kullanılır.
Web sunucusu (Apache, Nginx gibi) gelen isteğin hangi domain'den geldiğini görür ve ona göre doğru uygulamayı çağırır.
Örnek:
Aynı IP'de:
feyyaz.com → blog sitesi
kitaplik.feyyaz.com → kitap uygulaması
panel.feyyaz.com → yönetim paneli
Hepsi aynı IP'de, aynı portta olabilir ama gelen isteğin domain adına bakılarak yönlendirme yapılır.

Özetle:
Ne?	Ne işe yarar?
IP Adresi	Sunucuyu tanımlar
Port Numarası	Aynı sunucudaki farklı uygulamaları ayırır
Domain Adı (Host)	Aynı portta farklı siteleri ayırır
Web Sunucusu	Bu istekleri doğru klasöre veya uygulamaya yönlendirir

projenin application.properties dosyasına bakarak Swagger ve Postman üzerinden hangi porta istek attığını ve nasıl çalıştığını net şekilde anlayabiliriz.
server.port = 8080
Bu satır, Spring Boot uygulamanın kaç numaralı porttan çalışacağını belirler.
Yani:
Uygulamayı IntelliJ, Eclipse, VS Code veya terminalden run ettiğinde,
Spring Boot sunucusu (embedded Tomcat) http://localhost:8080 adresinden yayına başlar.

# Web tabanlı sistemin temel bileşenlerini (server ve ilgili terimleri) açıklıyorum. 
1. Client (İstemci)
Kullanıcının isteği başlattığı yerdir.
Örnek:
Tarayıcı (Chrome, Edge)
Postman
Mobil uygulama

Kullanıcı burada şunu yapar:
GET /students veya POST /login gibi istekleri başlatır.

2. Web Server (Web Sunucusu)
İstemciden gelen HTTP isteklerini ilk karşılayan sunucudur.
Örnekler:
Apache HTTP Server
Nginx
Spring Boot içinde gömülü gelen Tomcat

Ne yapar?
Statik içerik döner (HTML, resim, JS dosyası)
Veya istekleri Application Server’a (arka uca) yönlendirir

3. Application Server (Uygulama Sunucusu)
İşin mantığını (business logic) çalıştırır.
Spring Boot projen buradadır.
Burada controller, service, repository gibi yapıların çalıştığı yer burasıdır.
Genelde REST API’yi burada yazarsın.
Örnek port: localhost:8080

4. Database Server (Veritabanı Sunucusu)
Verilerin tutulduğu yerdir.
Örnekler:
PostgreSQL → Port: 5432
MySQL → Port: 3306
MongoDB → Port: 27017

Senin properties dosyanda bu satır vardı:
spring.datasource.url= jdbc:postgresql://localhost:5432/student_management_db1
Yani uygulaman, bu DB sunucusuna bağlanıyor.

5. Authentication Server (Kimlik Doğrulama Sunucusu)
Bazı sistemlerde kullanıcı girişlerini ve token üretimini ayrı bir servis yapar.
Senin projen JWT kullandığı için, bu iş uygulama sunucunda çözülüyor.
Ama büyük yapılarda bu iş OAuth / Keycloak / Auth0 gibi sistemlere devredilir.

6. File Server (Dosya Sunucusu)
Kullanıcılar dosya yüklüyorsa (PDF, resim vs.) bunlar dosya sunucusunda saklanabilir.
Örnekler:
Amazon S3
FTP sunucusu
Local klasör (küçük projelerde)

7. Logging / Monitoring / Log Server
Uygulamanın ne yaptığı, hata verip vermediği burada takip edilir.
Senin properties dosyanda şu satır vardı:
logging.file.name= log/studentmanagementapp.log

Gelişmiş sistemlerde şu sistemler kullanılır:
ELK Stack (Elasticsearch + Logstash + Kibana)
Grafana, Prometheus, Loki

8. Mail Server (E-Posta Sunucusu)
Şifre sıfırlama, kayıt onayı gibi durumlarda kullanıcıya mail göndermek için kullanılır.
Örnekler:
Gmail SMTP
SendGrid
Mailgun

9. DNS Server (Alan Adı Sunucusu)
Kullanıcı www.okulum.com yazınca bu alan adı, IP adresine çevrilir.
Bu çeviriyi DNS sunucuları yapar.
(İnternette gezinmenin görünmeyen kahramanıdır.)

# localhost Yazınca Ne Olur?
localhost aslında senin kendi bilgisayarını temsil eder.
Yani tarayıcıya:
http://localhost
yazarsan, bu şu anlama gelir:

“Tarayıcı, internete değil, bu bilgisayarın kendisine istek göndersin.”

Teknik Açıdan Ne Oluyor?
Tarayıcı localhost ifadesini görür.
Bilgisayarın hosts dosyasına bakar (orada şu vardır):
127.0.0.1   localhost
Yani localhost, IP adresi 127.0.0.1 ile eşleşir.

Sonuç olarak tarayıcı bu IP'ye istek gönderir:
http://127.0.0.1
Eğer bu IP’de (yani kendi bilgisayarında) bir web sunucusu çalışıyorsa (örneğin Spring Boot projen port 8080'de çalışıyorsa), cevap alırsın.

Örnek:
Senin Spring Boot projen şu satırı içeriyorsa:
server.port=8080
Tarayıcıya şu adresi yazarsın:
http://localhost:8080
Ve bu, senin kendi bilgisayarındaki Spring Boot uygulamasına istek gönderir.

Bonus Bilgi: localhost yerine IP yazarsan?
http://127.0.0.1:8080
Bu da aynı şeydir! Çünkü localhost = 127.0.0.1

# Cloud = Cloud Storage + Cloud Computing
Bu denklem, bulut teknolojisinin iki temel bileşeni olduğunu ifade eder.
Cloud Storage (Bulut Depolama):
Verilerin internet üzerinden uzaktaki sunucularda saklanmasıdır.
Cloud Computing (Bulut Bilişim):
Yazılım, işlem gücü, veritabanı, ağ gibi bilgi işlem kaynaklarının internet üzerinden hizmet olarak sunulmasıdır.
Sonuç:
Bulut teknolojisi dediğimiz şey, veri depolamayı (Cloud Storage) ve işlem yapmayı (Cloud Computing) bir araya getiren bir yapıdır. Bu sayede kullanıcılar hem verilerini güvenle saklayabilir hem de güçlü yazılımları internet üzerinden kullanabilir.

Spring Boot Uygulamasında Cloud Ne Demek?
Bir Spring Boot uygulamasını buluta taşıdığında ya da bulutta çalıştırdığında, genelde iki temel bileşen kullanırsın:
1. Cloud Storage (Bulut Depolama) – Verilerin Bulutta Saklanması
Spring Boot uygulamanda:
Dosyaları (PDF, resim, log vs.)
Veritabanı yedeklerini
Kullanıcıdan gelen verileri
yerel diske değil, bir bulut depolama servisine yüklersin.
Örnek:
AWS S3, Google Cloud Storage gibi yerlerde dosya saklamak.
Spring Boot’ta Amazon S3’e dosya yükleyen bir FileService sınıfı kullanırsın.
Uygulama, fiziksel bir sunucuda çalışsa bile, dosyalar uzaktaki bir sunucuda (cloud storage) tutulur.
amazonS3.putObject(new PutObjectRequest(bucketName, fileName, file));

2. Cloud Computing (Bulut Bilişim) – Uygulamanın Bulutta Çalıştırılması
Spring Boot uygulamanı:
AWS EC2, Google App Engine, Heroku, Azure App Service gibi platformlara deploy edersin.
Bu platformlar, senin yerine:
Sunucuyu kurar,
Kaynakları ayarlar (CPU, RAM),
Ölçeklemeyi ve yük dengelemeyi yapar.
Yani sen sadece kodunu yazarsın, bulut ise onu çalıştıracak altyapıyı sağlar.
Örnek:
Spring Boot jar dosyanı alıp Heroku'ya veya AWS Elastic Beanstalk’a gönderirsin.
Uygulama otomatik başlatılır, port ayarlanır ve internete açılır.

# Cloud Native - Cloud Agnostic
1. Cloud Native (Bulut Doğumlu)
Uygulama, baştan itibaren bulut ortamına uygun şekilde tasarlanır.
Özellikleri:
Mikroservis mimarisi ile yazılır.
Konteyner (Docker) içinde çalışır.
Kubernetes gibi orkestrasyon araçlarıyla kolay yönetilir.
CI/CD ile hızlı güncellenir.
Ölçeklenebilir, esnek, hızlı dağıtılır.

DevOps İçin Anlamı:
Pipeline’lar ile otomatik test ve deploy mümkün olur.
Ortamlar arası geçiş kolaydır.
Hatalar küçük servislerde kolay izlenebilir.
Uygulama canlıda sürekli evrim geçirir (Continuous Delivery).

2. Cloud Agnostic (Bulut Bağımsız)
Uygulama sadece bir bulut sağlayıcısına bağlı değildir. Herhangi bir bulut ortamında çalışabilir.

Özellikleri:
AWS, Azure, GCP fark etmeksizin taşınabilir.
Vendor lock-in (sağlayıcıya bağımlılık) riski düşer.
Açık standartlar ve container teknolojileri kullanılır.
Veritabanı, mesaj kuyruğu, cache gibi sistemler de bağımsız çözümlerle kurulur.

DevOps İçin Anlamı:
Maliyet optimizasyonu için farklı bulutlara taşınabilir.
Felaket durumunda farklı bölgelerde yeniden ayağa kaldırılabilir.
Taşınabilirlik yüksek olduğundan CI/CD pipeline'ları çok daha esnek olur.

"Kubernetes gibi orkestrasyon araçlarıyla kolay yönetilir."
Anlamı:
Uygulaman birden fazla parçadan oluşuyorsa (örneğin 5 farklı mikroservis), bunları Kubernetes gibi sistemler yardımıyla kolayca başlatabilir, durdurabilir, ölçekleyebilirsin.
Yani Kubernetes, bu parçaları otomatik olarak yönetir.
Basitçe düşün: Bilgisayarını açmak, kapatmak, bir programı yeniden başlatmak yerine; Kubernetes bunu otomatik yapar. Uygulama çalışmazsa tekrar başlatır, yoğunluk artarsa yeni kopyalar başlatır.

# "CI/CD ile hızlı güncellenir."
Anlamı:
CI = Continuous Integration → Kod değişikliği yaptığında otomatik test edilir.
CD = Continuous Delivery/Deployment → Kod başarılıysa otomatik olarak yayına alınır.
Basitçe düşün: Kodunu yazıp "push" ettiğinde sistem otomatik olarak:
Kodunu test eder.
Hata yoksa otomatik olarak uygulamayı günceller.

# "Pipeline’lar ile otomatik test ve deploy mümkün olur."
Anlamı:
Pipeline, bir işlemin adım adım otomatik yapılmasıdır.
Örnek:
Kod değişikliği oldu.
Test çalıştır.
Derle (build).
Yayına al.
Bu adımlar hep aynı sırayla ve otomatik çalışır → işte bu pipeline olur.

# "Uygulama canlıda sürekli evrim geçirir (Continuous Delivery)"
Anlamı:
Uygulama sürekli küçük güncellemelerle geliştirilir.
Devamlı canlıya (gerçek kullanıcıya) sunulur.
Büyük değişiklikler beklenmeden, her küçük geliştirme hemen yayınlanabilir.
Yani: Uygulaman sürekli canlıda gelişir, durmadan yenilenir.

# "Mesaj kuyruğu nedir?"
Anlamı:
Uygulamalar arasında mesaj gönderip almayı sağlayan bir sistemdir.
Biri mesaj bırakır, diğeri uygun olduğunda o mesajı alır.
Örnek:
Sipariş uygulaması "Yeni sipariş geldi" mesajını kuyruğa bırakır.
Fatura uygulaması o mesajı okur, fatura keser.

# "Taşınabilirlik yüksek olduğundan CI/CD pipeline'ları çok daha esnek olur."
Anlamı:
Uygulama bir bulut sağlayıcısına bağlı kalmadığında, yani taşınabilir olduğunda:
Her yerde çalışabilir (AWS, Azure, GCP, hatta kendi sunucun).
CI/CD süreçlerini her ortama kolayca uyarlayabilirsin.
Sonuç:
Birden fazla ortamda (test, canlı, yedek) otomatik dağıtım kurmak daha kolay olur.

# Cloud Teknolojisinin Dezavantajları
1. İnternet Bağımlılığı
Cloud sistemlerine erişmek için kesintisiz internet bağlantısı gerekir.
Yavaş ya da kopan bağlantı, veriye ve uygulamaya erişimi engeller.
Örnek: İnternetin gittiği bir anda S3 üzerindeki dosyaları alamazsın.
2. Gizlilik ve Güvenlik Riski
Veriler uzak sunucularda tutulur → bu da veri güvenliği endişesi doğurabilir.
Yanlış yapılandırma (örneğin S3 bucket'ı public açık bırakmak) büyük veri sızıntılarına yol açabilir.
DevOps’ta özellikle IAM (Identity and Access Management), şifreleme ve güvenlik politikaları kritik önemdedir.
3. Maliyet Kontrolü Zor Olabilir
Başta ucuz görünse de, uzun vadede trafik, depolama, işlem gücü gibi kaynaklar kontrolsüz kullanılırsa fatura kabarabilir.
"Kullandığın kadar öde" modelinde kullanımı takip etmezsen maliyet sürprizi yaşarsın.
Örnek: Log'lar temizlenmezse CloudWatch veya S3 maliyetleri hızla artabilir.
4. Vendor Lock-In (Sağlayıcıya Bağımlılık)
Bir servise (örneğin AWS Lambda, DynamoDB) çok entegre olursan → başka platformlara taşımak çok zor olabilir.
Cloud-native geliştirme bazen cloud-agnostic olmayı engeller.
Örnek: AWS Lambda fonksiyonunu GCP’ye taşımak zor ve zahmetli olabilir.
5. Performans Kontrolü Sınırlıdır
Uygulama bulutta paylaşımlı donanımda çalışabilir → bu da bazen gecikme, yavaşlık yaratabilir.
Ayrıca altyapı fiziksel olarak uzaksa latency (gecikme) artabilir.
Örnek: Türkiye'deki kullanıcılar için Frankfurt bölgesi bile gecikme yaratabilir.
6. Hukuki ve Yasal Riskler (Veri Egemenliği)
Verilerin farklı ülke sunucularında tutulması, bazı ülkelerde yasal sorunlara yol açabilir.
Özellikle sağlık, finans gibi sektörlerde bu çok önemlidir (örneğin KVKK, GDPR).
Örnek: Avrupa'daki bir müşterinin verisini ABD'de tutmak yasal olmayabilir.
7. Yedekleme ve Kurtarma Karmaşık Olabilir
Cloud servisleri yedekleme imkanı sunsa da, doğru yapılandırılmazsa felaket anında geri dönüş zorlaşabilir.
54415, versioning, lifecycle policy gibi özellikler manüel ayar gerektirir.

Özet Tablo:
Dezavantaj	Açıklama
İnternet bağımlılığı	Offline çalışamazsın
Güvenlik ve gizlilik riski	Veri sızıntısı olabilir
Maliyet sürprizleri	Takip edilmezse fatura artar
Vendor lock-in	Başka buluta geçmek zorlaşır
Performans sınırlamaları	Gecikme ve kaynak paylaşımı
Hukuki riskler	Veri lokasyonu yasalara aykırı olabilir
Kurtarma/yedekleme karmaşıklığı	Manuel ayar gerekebilir


# Bulutun Evriminde Rol Oynayan Yeni Konseptler
1. Virtualization (Sanallaştırma)
Nedir?
Tek bir fiziksel sunucuyu, birden fazla sanal sunucuya (VM) bölen teknolojidir.
Her VM, kendi işletim sistemine sahiptir ve bağımsız çalışır.
Bulut İçin Önemi:
Kaynakları daha verimli kullanmamızı sağladı.
Aynı fiziksel makinede birden fazla uygulama çalıştırabildik.
Cloud servis sağlayıcıları bu sayede müşterilere ayrı ayrı “sanal makineler” kiralamaya başladı.
Örneğin: AWS EC2 = Sanal makine mantığına dayanır.

2. Containerization (Konteynerleştirme)
Nedir?
Uygulamanın tüm bağımlılıklarıyla birlikte izole bir pakette çalışmasını sağlar (Docker gibi).
VM’den farkı: Konteynerler işletim sistemini paylaşır, daha hafif ve hızlıdır.
Bulut İçin Önemi:
Uygulamalar çok daha hızlı başlatılır/durdurulur
“Bir yerde çalıştı, ama burada çalışmıyor” sorunu ortadan kalktı
Konteynerler Kubernetes gibi sistemlerle kolayca yönetildi → Cloud Native mimarinin temelini oluşturdu
 Örneğin: Google Cloud Run = sadece konteyner çalıştırır.

3. Software Development Cycle (Yazılım Geliştirme Döngüsü)
Nedir?
Planlama → Kodlama → Test → Build → Deploy → İzleme → Güncelleme adımlarını kapsayan yaşam döngüsüdür.
DevOps ve CI/CD kavramları bu döngüyü otomatikleştirmeyi hedefler.

Bulut İçin Önemi:
Cloud ortamları, bu döngüyü hızlı ve otomatik hale getirmeyi sağladı.
“CI/CD Pipeline” kurarak test, build, deploy adımları tek tuşla veya otomatik yapılabilir hale geldi.
Bulutta bu döngüler çok daha çevik (Agile) hale geldi.

Örneğin: GitHub + Jenkins + AWS = tam otomatik yazılım yaşam döngüsü

4. Serverless (Sunucusuz Mimari)
Nedir?
Uygulamanı çalıştırmak için sunucu yönetmek zorunda kalmazsın.
Sadece fonksiyon yüklersin, sistem ihtiyaç duydukça çalıştırır.
Kullandığın kadar öde mantığına dayanır.

Bulut İçin Önemi:
Altyapı yönetme derdini ortadan kaldırdı.
Geliştirici sadece kod yazar, dağıtımı cloud yapar.
Çok hızlı, esnek ve ölçeklenebilir çözümler mümkün hale geldi.

Örneğin: AWS Lambda, Google Cloud Functions, Azure Functions

Nasıl Rol Oynadılar? Özetle:
Konsept	Buluta Katkısı
Virtualization	Sunucu kaynaklarını bölüştürerek bulut altyapısını başlattı
Containerization	Hafif, taşınabilir, hızlı uygulamalar sağladı
Yazılım Döngüsü	CI/CD ile otomasyon ve hız kazandırdı
Serverless	Altyapı derdini ortadan kaldırdı, sadece kod odaklı geliştirme

# Container (Konteyner) Teknolojisi Nedir?
Konteyner, bir yazılım uygulamasını ve onun çalışması için gereken her şeyi (kütüphaneler, ayarlar, dosyalar) birlikte izole bir şekilde paketleyen bir teknolojidir.
Yani:
"Uygulamanın yanına ihtiyaç duyduğu her şeyi koyar, bir kutuya (container) koyarsın ve her ortamda aynı şekilde çalıştırırsın."
Neden Geliştirildi?
Eskiden uygulama geliştiriciler:
“Benim makinemde çalışıyor, senin makinede çalışmıyor” sorunu yaşıyordu.
Çünkü her bilgisayarda farklı Java versiyonu, farklı ayarlar, farklı işletim sistemleri vardı.
Container sayesinde bu sorun ortadan kalktı.

Container Özellikleri:
Özellik	Açıklama
Hafif	Sanal makinelere göre çok daha küçük ve hızlıdır.
Taşınabilir	Geliştirici ortamında nasıl çalışıyorsa sunucuda da öyle çalışır.
İzole	Her container kendi ortamında çalışır, dış dünyadan bağımsızdır.
Hızlı Başlar	Birkaç saniyede ayağa kalkar.

Docker Nedir?
Docker, konteyner teknolojisini kullanan ve konteyner oluşturmak, çalıştırmak, dağıtmak için kullanılan en popüler araçtır.
Yani:
Docker = Konteyner üretici ve yöneticisi.

Docker sayesinde:
Uygulamanı Dockerfile ile tanımlarsın,
docker build ile bir image (görüntü) üretirsin,
docker run ile container başlatırsın.

Örnek: Spring Boot Uygulamasını Container’a Almak
Uygulaman için Dockerfile yazarsın:
FROM openjdk:17
COPY target/myapp.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
Docker Image Oluşturursun:
docker build -t my-spring-app .
Container Olarak Çalıştırırsın:
docker run -p 8080:8080 my-spring-app
Ve artık Spring Boot uygulaman bir container içinde, başka hiçbir şeye ihtiyaç duymadan çalışır!

Fark: Container vs. Sanal Makine (VM)
Özellik	Sanal Makine	Container
İşletim Sistemi	Her biri ayrı işletim sistemi çalıştırır	Aynı işletim sistemini paylaşırlar
Ağırlık	Ağır (GB boyutunda)	Hafif (MB düzeyinde)
Başlatma Süresi	Dakikalar	Saniyeler


# Amazon API Gateway, özellikle cloud + microservice + DevOps dünyasında önemli bir bileşendir. 
Amazon API Gateway Nedir?
Amazon API Gateway, AWS üzerinde API'ler (REST, HTTP veya WebSocket) oluşturmanı, yayınlamanı, yönetmeni ve güvenliğini sağlamanı sağlayan tam yönetilen (managed) bir hizmettir.
Yani:
Kullanıcılar ile arkadaki servisler (örneğin Lambda, EC2, başka microservice'ler) arasında köprü görevi gören bir API kapısıdır.
Ne İşe Yarar?
Uygulama istemcileri (mobil, web, Postman) → API Gateway → arka uç servisleri (backend)
Arka uç servisleri: AWS Lambda, EC2, Fargate, başka bir HTTP endpoint, vs.
Şöyle düşün:
Senin API'lerin bir apartman dairesi gibi.
API Gateway ise o apartmana gelenlerin geçtiği güvenlik kapısı + yönlendirici + trafik kontrol noktasıdır.

Neleri Sağlar?
Özellik	Açıklama
Routing (Yönlendirme)	Gelen istekleri doğru servise yollar. Örn: /users → Lambda A, /orders → Lambda B
Rate Limiting (Sınırlama)	Belirli sürede kaç istek yapılabileceğini kontrol eder.
Authentication	JWT, OAuth2, IAM gibi yöntemlerle kimlik doğrulama sağlar.
Monitoring	CloudWatch ile API çağrıları izlenebilir, loglanabilir.
Caching	Sık gelen cevapları önbelleğe alarak performans artırır.
Security (WAF ile)	Web saldırılarına karşı koruma sağlar (XSS, SQLi vb).

Kullanım Senaryosu (Basit Örnek):
Kullanıcı → API Gateway → Lambda → DynamoDB
Kullanıcı, GET /products isteği atar.
API Gateway bu isteği alır ve bir Lambda fonksiyonuna yönlendirir.
Lambda DynamoDB'den ürünleri çeker.
Sonuç API Gateway üzerinden kullanıcıya geri döner.

Avantaj:
Sen altyapı kurmak zorunda kalmazsın.
API Gateway her şeyi otomatik yönetir (güvenlik, performans, log, izleme).
Ne Zaman Kullanılır?
Mikroservis mimarilerinde
Mobil veya web uygulamaları için tek giriş noktası gerektiğinde
Serverless mimarilerde (Lambda + DynamoDB gibi)
API güvenliği ve ölçeklenebilirlik istendiğinde

Bonus: API Gateway + Spring Boot?
Spring Boot API’n varsa:
EC2, Elastic Beanstalk veya Fargate gibi servislerde çalıştırabilirsin.
API Gateway bu Spring Boot uygulamasının endpointlerine yönlendirme yapabilir.

Örnek:
POST https://myapi.execute-api.eu-central-1.amazonaws.com/prod/register
→ yönlendirilir → Spring Boot REST Controller

Özet
Özellik	Açıklama
Hizmet Türü	Tam yönetilen (managed)
Amaç	API'leri yayınlama, yönetme ve güvenli hale getirme
Çalıştığı Yapılar	REST, HTTP, WebSocket
Desteklediği Backend'ler	Lambda, EC2, Fargate, başka bir HTTP servis


# Kendi Microservice Mimarinde Amazon API Gateway Nerede Yer Alır?
Senin şu anki yapın büyük ihtimalle şöyle:
Kullanıcı → (Senin yazdığın) API Gateway (örneğin Spring Cloud Gateway)
             ↓
Discovery Service (Eureka)
             ↓
2 adet microservice (örneğin UserService, ProductService)
             ↑
Config Service (ortak yapılandırma)
Şimdi bu yapıyı cloud'a taşıdığında, Amazon API Gateway nereye girer?
1. Amazon API Gateway, senin yazdığın Spring Gateway’in yerine geçebilir.
Senin Spring Cloud Gateway şu an:
Routing yapıyor,
Belki auth, rate limit, log gibi işler yapıyor.
Amazon API Gateway, bunu bulutta senin yerine yapabilir.
Yani:
"Spring Gateway’i Amazon’a devrediyorsun."
Artık şuna dönüşür:
Kullanıcı → ☁️ Amazon API Gateway
             ↓
AWS'deki microservislerin
Eğer Spring Gateway’e özel bir şeyler yaptıysan, istersen onu da tutabilirsin. Ancak Amazon API Gateway çok daha güçlü, esnek ve yönetilen bir çözüm sağlar.

2. Ne zaman devreye girer?
Amazon API Gateway, uygulamanı AWS’ye deploy ettiğinde devreye girer. Yani:
Cloud ortamına geçince:
EC2’ye, Fargate’e, Lambda’ya uygulamanı yükledin →
Kullanıcılar doğrudan IP ile değil, API Gateway ile erişir.
Neden?
Doğrudan EC2’ye erişim: güvensiz, esnek değil
API Gateway ile erişim: güvenli, izlenebilir, cache, auth yapılabilir


Alternatif:
Spring Cloud Gateway’i Amazon EC2’ye kurar, Amazon API Gateway kullanmadan da devam edebilirsin.
Ama:
Trafik kontrolü
Rate limiting
JWT auth
API loglama
DDoS koruması
gibi işlerde Amazon API Gateway çok daha hazır çözümler sunar.

Özetle:
Soru	Cevap
API Gateway uygulamamda nereye girer?	Spring Gateway'in yerine geçebilir (cloud'da)
Ne zaman kullanılır?	Uygulaman AWS'ye yüklendiğinde, dış dünyaya açmak için
Spring Gateway kalabilir mi?	Evet, ama yönetim işlerini AWS’ye bırakmak istersen çıkarabilirsin
Avantajı ne?	Güvenlik, ölçeklenebilirlik, auth, rate limit, log gibi işleri senin yerine yapar

# Serverless Nedir?
Serverless, geliştiricilerin uygulama yazarken sunucu kurmak, yapılandırmak veya yönetmek zorunda kalmadığı bir cloud mimarisidir.
Yani:
"Kodunu yaz, yükle, çalıştır. Altyapıyı düşünme. Sunucu hala var ama sen hiç uğraşmazsın."
En Önemli Özelliği:
Sadece çalıştığında ödeme yaparsın.
Kodun çağrılmadığı sürece sistem kaynak tüketmez, fatura işlemez.
Nasıl Çalışır?
Sen küçük bir fonksiyon (örneğin getUserById) yazarsın.
Bunu AWS Lambda gibi bir serverless platforma yüklersin.
Kullanıcı bir istek gönderdiğinde sistem bu fonksiyonu otomatik çalıştırır, cevap verir ve kaynağı otomatik serbest bırakır.
Hiçbir zaman "sunucu kaç CPU olmalı, belleği ne kadar olmalı" gibi şeylerle uğraşmazsın.

Gerçek Hayattan Benzerlik:
Düşün ki bir restoranın var:
Klasik sistemde: Her zaman açık mutfak var, çalışanlar maaş alır, elektrik gideri sürekli var.
Serverless sistemde: Sipariş gelince şef mutfağa girer, yemeği yapar, sonra çıkar. Sadece çalıştığında maliyet olur.

Serverless ile Yapabileceklerin:
Platform	Serverless Karşılığı	Açıklama
AWS	Lambda	Fonksiyon yükle, otomatik çalıştır
Azure	Azure Functions	Aynı mantık
Google Cloud	Cloud Functions	Serverless fonksiyon mantığı
API yönetimi	AWS API Gateway	Serverless API yönetimi
Veritabanı	DynamoDB, Firebase (serverless DB)	Otomatik ölçeklenir, yönetilmez
Dosya depolama	S3 (statik dosyalar için serverless)	Web sayfası barındırma dahil

Avantajları:
Avantaj	Açıklama
Sunucu yönetimi yok	Altyapı işleri AWS’e ait
Ucuz	Sadece çalıştığı sürece ücret ödersin
Hızlı dağıtım	Küçük fonksiyonlar hemen çalışır
Otomatik ölçekleme	Trafik artınca AWS otomatik kapasiteyi artırır
Kolay entegrasyon	Diğer AWS servisleriyle uyumlu çalışır

Dezavantajları (Gerçekçi Bakış):
Dezavantaj	Açıklama
Karmaşık mimari	Mikro düzeyde birçok fonksiyon olunca yönetimi zorlaşabilir
Soğuk başlatma	Uzun süre çağrılmayan fonksiyonlar ilk çalışmada yavaş olabilir
Zaman sınırlamaları	Lambda örneğin 15 dakika çalışabilir maksimum
Debug/log zorluğu	Geleneksel uygulamalara göre hata ayıklamak farklıdır

Örnek:
Geleneksel Spring Boot REST API:
java
@GetMapping("/hello")
public String hello() {
    return "Hello world!";
}
Bu uygulamayı sunucuya deploy etmen gerekir, 7/24 çalışır.

Aynı işin Serverless Lambda versiyonu:
java
public class HelloHandler implements RequestHandler<Object, String> {
    public String handleRequest(Object input, Context context) {
        return "Hello world!";
    }
}
Bu kod sadece çağrıldığında çalışır, sonra kapanır. Sunucu yok, sürekli çalışma yok, maliyet düşük.

Özetle:
Serverless = Kodu çalıştır, sunucuyu unut, altyapıyla uğraşma.
Sunucu hala vardır, ama sen yönetmezsin.
AWS Lambda gibi servislerle en iyi şekilde uygulanır.
Maliyet, yönetim yükü ve zaman açısından çok avantajlıdır.

# Sanallaştırmanın Açıklaması
Bu tanımlar, sanallaştırma teknolojisinin temel mantığını açıklıyor:
Temel Kavram: Sanallaştırma, tek bir fiziksel sunucu üzerinde birden fazla sanal işletim sisteminin (guest sistemler) aynı anda çalışmasını sağlar. Bu sanal sistemlerin her biri, fiziksel makinenin kaynaklarını (işlemci, bellek, disk) paylaşır.
Nasıl Çalışır: Görselde de görüldüğü gibi, geleneksel mimaride her uygulama kendi işletim sistemi ve donanımına ihtiyaç duyar. Sanallaştırmada ise Virtual Machine Monitor (VMM) veya Hypervisor adı verilen bir yazılım katmanı, tek fiziksel donanım üzerinde birden fazla sanal makine oluşturur.
Pratik Faydalar:
Kaynak Verimliliği: Tek bir güçlü sunucu, birden fazla zayıf sunucu yerine kullanılabilir. Örneğin, 16 çekirdekli bir sunucuda 4 farklı sanal makine çalıştırabilirsiniz.
Maliyet Tasarrufu: Fiziksel sunucu sayısı azalır, elektrik tüketimi düşer, veri merkezi alanı daha verimli kullanılır.
Esneklik: Bir sanal makine bozulursa sadece o makine etkilenir, diğerleri çalışmaya devam eder.
Kolay Yönetim: Sanal makineler kolayca kopyalanabilir, taşınabilir veya yedeklenebilir.
Örnek Senaryo: Bir şirketin web sunucusu, veritabanı sunucusu ve mail sunucusu olsun. Sanallaştırma ile bu üç farklı sistem, tek bir fiziksel sunucu üzerinde üç ayrı sanal makine olarak çalışabilir.
Bu teknoloji, cloud computing'in temel taşlarından biridir ve kaynak paylaşımını maksimum verimlilikle yapar.

# Bulut bilişim dünyasında sıkça duyulan IaaS, PaaS ve SaaS, üç temel hizmet modelidir. 
Bunları anlamak, cloud teknolojilerini sağlıklı kavraman açısından çok önemlidir.
1. IaaS – Infrastructure as a Service
“Altyapı hizmeti olarak” bulut servisi
Nedir?
Sana sunucu (server), depolama (disk), ağ (network) gibi altyapıyı sağlar.
Ama işletim sistemi, yazılım kurulumu ve bakım senden sorumludur.
Ne yaparsın?
Kendi işletim sistemini kurarsın (örneğin Ubuntu).
Veritabanını ve uygulamanı kendin kurarsın.
Yani bir sanal makine (VM) gibi düşün.
Örnek:
AWS EC2
Azure Virtual Machines
Google Compute Engine
Özet:
Sunucuyu ben alırım, yazılımı ben yüklerim.

2. PaaS – Platform as a Service
“Platform hizmeti olarak” bulut servisi
Nedir?
Sana sadece altyapı değil, bir çalıştırma platformu da sunar.
Uygulamanı yükleyip hemen çalıştırabilirsin; sistem güncellemeleri, yapılandırma AWS'e aittir.
Ne yaparsın?
Uygulamanı (örneğin bir Spring Boot JAR dosyasını) verirsin, o gerisini halleder.
Sunucu açmak, port ayarlamak, patch çekmek gibi şeylerle uğraşmazsın.
Örnek:
AWS Elastic Beanstalk
Heroku
Google App Engine
Özet:
Ben sadece uygulamamı veririm, altyapıyı cloud yönetir.

3. SaaS – Software as a Service
“Yazılım hizmeti olarak” bulut servisi
Nedir?
Hazır bir yazılım ürününü internet üzerinden kullanırsın.
Kod yazmana, deploy etmene, sunucu açmana gerek yoktur.
Ne yaparsın?
Sadece tarayıcıdan girer, kullanırsın.
Güncelleme, bakım, yedekleme her şey cloud sağlayıcısı tarafından yapılır.
Örnek:
Google Docs / Gmail
Zoom
Microsoft 365
Trello, Notion
Özet:
Hazır uygulamayı kullanırım, hiçbir teknik işe karışmam.

Günlük Hayattan Tatlı Bir Örnek:
Haydi pizza üzerinden düşünelim 

Model	Kim ne yapar?
IaaS	Hamuru, fırını sen alırsın. Pizzayı kendin yaparsın.
PaaS	Hazır fırınlı mutfağa gidersin, sadece pizzayı yaparsın.
SaaS	Pizzayı sipariş edersin, sıcak sıcak önüne gelir.

Karşılaştırma Tablosu:
Özellik	IaaS	PaaS	SaaS
Donanım	Sağlanır	Sağlanır	Sağlanır
İşletim Sistemi	Sen kurarsın	Sağlanır	Sağlanır
Uygulama	Sen geliştirirsin	Sen geliştirirsin	Hazırdır
Kullanıcı Kontrolü	En fazla kontrol	Orta düzeyde	En az kontrol
Örnek	AWS EC2	AWS Beanstalk	Gmail, Google Docs

Hatırlaması Kolay:
IaaS = Sunucu senin kontrolünde
PaaS = Kod senin, platform onların
SaaS = Her şey onların, sen sadece kullanırsın

# AWS'de Temel Altyapı Kavramları
1. Region (Bölge)
Nedir?
AWS’nin dünya üzerindeki coğrafi bölgeleridir.
Her region, bağımsız çalışan veri merkezleri (availability zone'lar) içerir.

Örnek region'lar:
eu-central-1 → Frankfurt
us-east-1 → Virginia
eu-west-3 → Paris
me-central-1 → Dubai

Region seçerken genelde kullanıcına en yakın olanı seçersin, çünkü:
Gecikme (latency) az olur.
Veri yasalarına (KVKK, GDPR vs.) uyarsın.

2. Availability Zone (AZ) – Erişilebilirlik Alanı
Nedir?
Her region, 2 ila 6 adet availability zone (AZ) içerir.
Her AZ, bir veya daha fazla veri merkezinden (data center) oluşur.
AZ’ler birbirinden fiziksel olarak ayrıdır, ama birbirine çok hızlı ağlarla bağlıdır.
Amaç: Bir AZ çökerse, diğer AZ’ler çalışmaya devam etsin.

Örnek:
eu-central-1 (Frankfurt Region) şunları içerir:
eu-central-1a
eu-central-1b
eu-central-1c

3. Data Center (Veri Merkezi)
Nedir?
Fiziksel sunucuların, disklerin, ağ donanımlarının bulunduğu gerçek binalardır.
Her AZ, bir veya birden fazla data center içerir.
Bu veri merkezleri:
Yüksek güvenliklidir (biyometrik kapılar, kamera, elektrik yedekleri vs.)
Fiziksel felaketlere karşı dayanıklıdır.
Amaç: Donanım seviyesinde bile sorun çıksa, uygulaman çalışmaya devam etsin.

Kavramlar Arası İlişki:
  ├── 🧩 AZ (Availability Zone) - en az 2
  │     ├── 🏢 Data Center - 1 veya daha fazla

Örnek: Frankfurt (eu-central-1)
Region: eu-central-1 (Frankfurt)
  ├── AZ: eu-central-1a → 2 veri merkezi
  ├── AZ: eu-central-1b → 1 veri merkezi
  ├── AZ: eu-central-1c → 3 veri merkezi

Bu yapı sayesinde:
Yüksek erişilebilirlik (high availability)
Felaket kurtarma (disaster recovery)
Otomatik yedekleme ve ölçeklenme sağlanır.

Neden Bu Kadar Katman Var?
Katman	Amaç
Region	Veri egemenliği, coğrafi yakınlık
AZ	Fiziksel yedeklilik, kesintisiz çalışma
Data Center	Donanım seviyesinde güvenlik, yedekleme


# Edge Location (Uç Lokasyon) Nedir?
Edge Location, AWS’nin dünyanın dört bir yanına yayılmış küçük veri noktalarıdır ve genelde:
Kullanıcılara en yakın yerden içerik sunmak (CDN),
İstekleri hızla karşılamak için kullanılır.

Yani:
"Edge Location = AWS’in kullanıcılara en yakın noktadaki hızlı hizmet istasyonu"

Region vs AZ vs Edge Location Karşılaştırması
Kavram	Amaç	Nerede Kullanılır?
Region	Büyük coğrafi bölge (şehir gibi)	Uygulamanın ana merkezi
AZ (Zone)	Region içi fiziksel veri merkezi	Uygulama çalıştırma/yedekleme
Edge Location	İçeriği son kullanıcıya hızlı ulaştırmak	CDN, DNS, video, önbellekleme

Neden Gerek Var?
Diyelim ki web siten Frankfurt'taki Region'da barınıyor (örneğin S3).
Ama kullanıcı İstanbul’da.
Her istek Frankfurt’a gitse:
Gecikme olur (latency),
Sayfa yavaş açılır.
İşte burada Edge Location devreye girer:
AWS, senin verini önbelleğe alır,
İstanbul’daki kullanıcıya İstanbul’a en yakın Edge Location üzerinden gösterir.

Hangi Servisler Edge Location Kullanır?
AWS Servisi	Açıklama
Amazon CloudFront	En çok bilinen kullanım. CDN (Content Delivery Network) olarak statik dosyaları (HTML, JS, resim vs.) en yakın edge location'dan sunar.
AWS Global Accelerator	Trafiği en hızlı yoldan yönlendirir.
Amazon Route 53	DNS isteklerini en hızlı yanıtlayan edge noktasından çözümler.
Lambda@Edge	Edge Location'da çalışan mini fonksiyonlardır (Serverless mantığı).

Edge Location Sayısı ve Dağılımı
AWS 2024 itibariyle 300+ edge location işletiyor.
Bunlar 90'dan fazla şehirde, 50+ ülkede bulunuyor.
İstanbul’da da edge location var 
(CDN veya DNS istekleri için kullanıcıya çok düşük gecikmeyle cevap verilebilir.)

Özet:
Terim	Açıklama
Edge Location	Kullanıcıya en yakın noktadan içerik sunan AWS noktasıdır
Amaç	Hızlı içerik dağıtımı, düşük gecikme (latency), CDN
Kullanan Servisler	CloudFront, Route53, Lambda@Edge

# Spring uygulamanın veri katmanı ile AWS'de nasıl çalışacağın, bulut ortamına geçişin en önemli adımlarından biridir. 
1. Spring Uygulamanın Veri Katmanı
Senin şu ana kadar yaptığın:
java
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByUsername(String username);
}
Bu Repository yapısı genellikle bir SQL veritabanına (MySQL, PostgreSQL, H2 vs.) bağlı olur.

Ya da NoSQL kullandıysan:
MongoDB gibi
Redis gibi

2. Peki AWS’de Ne Olacak?
AWS’de de veritabanı kullanırsın, ama veritabanını artık kendin kurmazsın.
Bunun yerine AWS'in sunduğu hazır veritabanı servislerini kullanırsın.
Yani:
AWS’de de veritabanı var ama artık sunucusunu kurmaz, ayarlarla uğraşmazsın.
AWS senin için yönetir.
AWS’de Kullanabileceğin Veritabanları
AWS Servisi	Türü	Ne İçin Uygun?
RDS	SQL (MySQL, PostgreSQL, Oracle, MariaDB, SQL Server)	Geleneksel Spring projeleri için 
Aurora	SQL (PostgreSQL veya MySQL uyumlu)	Daha hızlı, daha dayanıklı RDS alternatifi
DynamoDB	NoSQL (Key-Value & Document)	MongoDB veya Cassandra alternatifi
DocumentDB	NoSQL (MongoDB uyumlu)	MongoDB gibi çalışır
ElastiCache	NoSQL (Redis, Memcached)	Cache amaçlı
Timestream	Zaman serisi veritabanı	IoT, sensör verileri için

En Çok Kullanılan 2 Alternatif
1. Amazon RDS (SQL)
MySQL, PostgreSQL gibi klasik veritabanlarını AWS senin yerine kurar ve yönetir.
Spring Boot projenle tıpkı lokaldeki gibi kullanabilirsin.
Örnek application.properties:
properties
spring.datasource.url=jdbc:postgresql://your-db-name.rds.amazonaws.com:5432/mydb
spring.datasource.username=admin
spring.datasource.password=secret
Hiçbir fark yok. Sadece bağlantı adresi artık AWS RDS URL'si.

2. DynamoDB (NoSQL)
AWS'nin tamamen yönetilen NoSQL veritabanı.
Spring Data DynamoDB veya AWS SDK ile erişebilirsin.
Anahtar-değer, belge bazlı veri saklamak için çok hızlıdır.
Ama: DynamoDB ile JPA gibi SQL ilişkileri kurmak zordur.
Bu yüzden genelde sade ve hızlı veri erişimi gereken yerlerde tercih edilir.
Özetle:
Soru	Cevap
Spring uygulamam veri kaynağına nasıl bağlanacak?	Eskisi gibi ama URL artık AWS'deki veritabanına ait
Yeni veritabanı mı kullanacağız?	Evet, ama türü benzer (RDS = SQL, DynamoDB = NoSQL)
Kodda büyük değişiklik olur mu?	Hayır, Spring Data ile RDS kullanıyorsan aynen devam

Karar Kriteri
Durumun	Kullanılacak DB
SQL ilişkisel veri yapısı	 Amazon RDS (MySQL/PostgreSQL)
JSON belge saklama, NoSQL yapı	 DynamoDB veya DocumentDB
Spring Boot + JPA kullanıyorsan	 RDS (en uyumlu)

Örnek Senaryo
Spring Boot uygulamanı EC2’ye ya da ECS’ye deploy ettin, ve RDS kullandın.
UserRepository aynen çalışır, sadece application.properties şöyle değişir:
properties
spring.datasource.url=jdbc:mysql://aws-rds-endpoint:3306/usersdb
spring.datasource.username=admin
spring.datasource.password=strongPassword
Hepsi bu. Uygulaman AWS’ye taşınmış olur ama Repository katmanında büyük değişiklik gerekmez.

# Spring uygulamanda şimdiye kadar:
SQL: MySQL, PostgreSQL gibi ilişkisel veritabanlarını
NoSQL: MongoDB gibi belge tabanlı veritabanlarını
lokal ya da kendi sunucularında kullandın.
Peki AWS’ye geçince bu değişir mi?
Cevap:
Hayır, prensip olarak değişmez; ama araçlar değişebilir.
AWS’de de SQL ve NoSQL veritabanları vardır ama AWS bunları senin yerine yönetir (managed service).

AWS’de Veritabanı Kullanımı: Genel Mantık
Spring uygulamanda @Repository interface'lerin hâlâ geçerli olur.
Ama veri nereden gelir?
Artık veri:
EC2’de kurulu bir MySQL'den değil,
AWS’nin yönetilen bir veritabanı servisinden gelir.

1. AWS’de SQL Veritabanları (Relational – RDS)
AWS RDS (Relational Database Service):
AWS’in MySQL, PostgreSQL, Oracle, MSSQL gibi ilişkisel veritabanlarını senin yerine kurup yönettiği servistir.
Avantaj:
Sunucu kurmazsın.
Yedekleme, ölçekleme, bakım AWS tarafından yapılır.
Örnek:
@Repository
public interface UserRepository extends JpaRepository<User, Long> {}
Bu repository hâlâ çalışır.
Yalnızca application.properties içinde şunu yazarsın:
spring.datasource.url=jdbc:mysql://your-db-name.abcdefg.us-east-1.rds.amazonaws.com:3306/yourdb
spring.datasource.username=admin
spring.datasource.password=pass123

2. AWS’de NoSQL Veritabanları
DynamoDB
AWS'nin MongoDB gibi belge tabanlı NoSQL veritabanıdır.
Hızlıdır, ölçeklenebilirdir.
JSON benzeri yapıdadır.
Spring Data DynamoDB veya AWS SDK ile kullanılabilir.
Örnek:
@DynamoDBTable(tableName = "Users")
public class User { ... }
public interface UserRepository extends CrudRepository<User, String> {}
Alternatif olarak MongoDB de kullanmak istersen:
AWS'de Amazon DocumentDB (MongoDB uyumlu) kullanılabilir.

Uygulaman Değişecek mi?
Katman	Değişiklik
@Repository	Aynı kalır
Entity/model	Aynı kalır
DB bağlantısı	Sadece application.properties içinde url, username, password kısmı değişir
SQL mi NoSQL mi?	İhtiyacına göre karar verirsin – AWS ikisini de destekler

Kısaca: AWS'de Kullanabileceğin DB Servisleri
Tür	Servis Adı	Açıklama
SQL	Amazon RDS	MySQL, PostgreSQL, Oracle vb. destekler
SQL	Amazon Aurora	RDS’nin gelişmiş versiyonu (çok hızlı)
NoSQL	Amazon DynamoDB	Anahtar-değer + belge tipi veri
NoSQL	Amazon DocumentDB	MongoDB uyumlu
In-Memory	Amazon ElastiCache	Redis, Memcached destekli – önbellekleme için


# EC2 de AWS’nin bir servisidir.
Ama:
EC2 = AWS’nin "sanal sunucu" (virtual machine) servisidir
RDS = AWS’nin "yönetilen veritabanı" (managed database) servisidir
Bu ikisi farklı seviyede hizmet sunar. Şöyle ayrıştıralım:
EC2 (Elastic Compute Cloud) nedir?
EC2, AWS'nin sana sunduğu boş bir sanal makinedir (Linux/Windows).
İçine istediğin yazılımı sen kurarsın:
Java, Python
MySQL, PostgreSQL, MongoDB
Apache, Nginx
Her şeyi sen yönetirsin:
Güncellemeler
Yedekleme
Yama (patch)
Çökme durumunda kurtarma
Yani EC2 kullanarak MySQL kurarsan, tıpkı kendi bilgisayarına kurmuşsun gibi sen sorumlusun.

RDS (Relational Database Service) nedir?
RDS, AWS'nin sana sunduğu tamamen yönetilen veritabanı servisidir.
Örnek olarak MySQL, PostgreSQL, Oracle gibi veritabanlarını seçersin
AWS:
Sunucu açar
Veritabanını kurar
Yedekleme, patch, disk yönetimi gibi işleri otomatik yapar
Failover, multi-AZ gibi yüksek erişilebilirlik özellikleri sunar
Sen sadece bağlantı adresi ve şifre ile bağlanırsın. Kurulum, bakım, güvenlik duvarı gibi şeylerle uğraşmazsın.

# Şu anda dünyadaki tüm yazılımlar cloud'da çalışmıyor. 
Ama gidişat büyük ölçüde cloud'a doğru:
Şu Anki Gerçek: Herkes Cloud'da Değil
Halen kullanılan sistem türleri:
Sistem Türü	Açıklama
On-Premise (lokal)	Şirketin kendi binasında, kendi sunucularında çalışan sistemler (özellikle eski yazılımlar)
Private Cloud	Şirketin kendi içinde kurduğu özel cloud altyapısı
Public Cloud	AWS, Azure, GCP gibi büyük sağlayıcılarda çalışan sistemler
Hybrid	Hem cloud hem lokal sunucular bir arada kullanılıyor

Gerçek Hayat Rakamları (2024-2025)
Dünya genelinde yaklaşık %60-70 oranında şirket cloud kullanıyor. Ama bu:
Ya tamamen cloud (örnek: Netflix, Spotify),
Ya da kısmi cloud (örnek: bankalar, devlet kurumları)
IDC raporuna göre:
2025 yılına kadar yazılım harcamalarının %85’inin cloud tabanlı olması bekleniyor.

# Spring Boot Projelerinde "JAR" Ne Demek?
Sen jar seçtiğin zaman, Spring Boot sana tüm uygulamanı ve bağımlılıklarını tek dosyada toplayan bir çalıştırılabilir uygulama üretir:
Örn: okul-yonetim-sistemi-1.0.0.jar
Bu .jar dosyası aslında bir mini sunucu gibi çalışır. İçinde Tomcat gömülüdür.
Yani ayrı bir sunucu kurmana gerek yoktur.

IntelliJ'de Run Butonuna Basmak Ne Yapar?
Aslında IntelliJ arkada şunu yapıyor:
mvn clean install ya da ./mvnw package gibi komutla .jar dosyası üretiyor
Sonra bu JAR'ı Java komutuyla çalıştırıyor:
java -jar target/okul-yonetim-sistemi-1.0.0.jar
Sen farkında olmadan IntelliJ bu adımları senin yerine otomatik yapıyor.

Elle JAR Üretip Çalıştırmak (Önemli Adım!)
Spring Boot projenin içinde terminal aç ve şunu çalıştır:
bash
./mvnw clean package
Bu komut ne yapar?
Tüm projeni derler
target/ klasörü altında .jar dosyasını üretir
Sonra bu jar'ı bağımsız çalıştırabilirsin:
bash
java -jar target/okul-yonetim-sistemi-1.0.0.jar
Bu adımı öğrenmen çok önemli çünkü:
Cloud’a yüklemeden önce dosya üretmen gerekir
Docker image oluştururken bu .jar dosyasını kullanırsın
CI/CD pipeline’ında .jar üretip deploy edersin
Test Et: Kendi Ürettiğin .jar dosyasını çalıştır
Terminalden mvnw clean package de
target/ klasörüne gir
.jar dosyasını bul
java -jar ... komutuyla çalıştır
Aynı Swagger, Postman endpoint'leri çalışacak 

Özetle:
Konu	Açıklama
JAR seçmek	Uygulamanı tek dosyada çalıştırılabilir hale getirir
Run butonu	IntelliJ arkada bu jar'ı üretip çalıştırır
Manuel jar üretimi	Gerçek deploy süreci için çok önemlidir
java -jar ...	Uygulamanı IntelliJ olmadan da çalıştırmanın yoludur

# AWS Local Zones Nedir?
AWS Local Zones, AWS’in merkezi region’larının çok uzağındaki şehirlerde, son kullanıcıya daha yakın konumlara küçük veri merkezleri kurarak çok düşük gecikme (latency) ile hizmet verdiği yapılardır.
Neden Vardır?
Region'lar genellikle ülke bazlı kurulur (örneğin: Frankfurt, Paris, Virginia).
Ama bu region’dan çok uzakta olan kullanıcılar için:
Uygulama yavaş olabilir (20-100 ms gecikme)
Özellikle video, oyun, canlı yayın gibi servislerde gecikme sorun yaratır
İşte bu nedenle AWS bazı büyük şehirlerde "Local Zone" kurar → bu sayede:
Kullanıcıya 1-10 ms arası ultra hızlı tepki süresi verir (neredeyse lokal gibi).

Türkiye'de AWS Local Zone Var mı?
Evet!
2022'de AWS Local Zone İstanbul açıldı.
Bu sayede Türkiye'deki yazılımlar (oyunlar, medya uygulamaları vs.) için AWS Region’lara kıyasla çok daha düşük gecikme sağlanabiliyor.
Örn: Trendyol ya da bir Türk oyun firması, Frankfurt region yerine İstanbul Local Zone kullanarak daha düşük gecikmeyle servis sunabilir.

Soru	Cevap
Local Zone nedir?	AWS’in, büyük region’lardan uzak şehirlerde kurduğu küçük veri merkezleri
Ne işe yarar?	Uygulamayı kullanıcıya daha yakın çalıştırarak düşük gecikme sağlar
Hangi uygulamalarda önemli?	Oyun, video, canlı yayın, ML gibi hızlı tepki gerektiren sistemlerde
Türkiye’de var mı?	 Evet, İstanbul’da Local Zone var

# AWS Shared Responsibility Model Nedir?
AWS ile müşteriler, cloud güvenliği konusunda sorumluluğu paylaşır.
Bazı şeylerden AWS sorumludur, bazı şeylerden ise sen (müşteri/yazılımcı) sorumlusun.
İki Temel Sorumluluk Alanı
1. Security of the Cloud → AWS Sorumluluğunda
Yani: “Cloud altyapısının güvenliği”
AWS şunlardan sorumludur:
Fiziksel veri merkezleri
Sunucular, depolama cihazları
Ağ donanımı
Hypervisor (sanal makine katmanı)
Bakım, yedekleme, elektrik, soğutma, yangın güvenliği
AWS bunları yönetir, senin erişimin yoktur.

2. Security in the Cloud → Müşteri (Sen) Sorumluluğunda
Yani: “Cloud içinde oluşturduğun sistemin güvenliği”
Senin sorumlulukların:
Uygulama güvenliği (örneğin Spring Boot API’ne gelen istekleri kontrol etmek)
Veritabanı şifreleri, bağlantı ayarları
IAM kullanıcı izinleri
S3 bucket erişim politikaları
EC2 instance güvenlik grubu (Security Group)
Verilerin şifrelenmesi (Encryption)
Yani senin kurduğun her şeyin konfigürasyon, erişim ve içerik güvenliği senin sorumluluğundadır.

Grafikle Gösterelim:
lua
|-------------------------------------|
|        AWS Sorumluluğu             |
|-------------------------------------|
| - Fiziksel altyapı (data center)   |
| - Donanım (sunucu, ağ)             |
| - Sanallaştırma (Hypervisor)       |
| - Altyapı güvenliği                |
|-------------------------------------|
|        Müşteri Sorumluluğu         |
|-------------------------------------|
| - Uygulama (kod güvenliği)         |
| - Veritabanı şifreleri             |
| - IAM kullanıcı ve roller          |
| - S3 erişim izinleri               |
| - Ağ yapılandırması (VPC, SG)      |
|-------------------------------------|
Örneklerle Pekiştirelim:
Durum	Kim sorumlu?	Açıklama
AWS veri merkezine saldırı olursa	AWS	Fiziksel güvenlik onların işi
Veritabanı şifresini GitHub'a attın	Sen	IAM, şifre güvenliği senin işin
S3 bucket herkes tarafından erişilebilir oldu	Sen	Erişim politikasını sen yazdın
Sunucularda güvenlik açığı varsa (patch yapılmadıysa)	Sen (EC2’de ise)	EC2 instance senin kontrolünde
Uygulama hatalı input kabul etti	Sen	Spring Boot içinde validation sana ait
