# proxy server ve reverse proxy nedir? 

1️⃣ Proxy Server (İleri Proxy)

Proxy server, istemci (client) ile internet arasına giren aracı sunucudur.
Yani kullanıcı doğrudan hedef siteye gitmez; önce proxy’ye gider, proxy onun yerine isteği gönderir.
Basit düşün:

Sen (client) → Proxy Server → Hedef Site (örneğin google.com)

Ne işe yarar?

Anonimlik (IP gizleme):
Proxy hedef siteye kendi IP’sini gösterir, kullanıcının gerçek IP’si gizlenir.

İçerik filtreleme:
Kurumsal ağlarda bazı sitelere erişimi engellemek için.

Cache (önbellekleme):
Sık kullanılan sayfaları saklayarak bant genişliğini azaltır.

Güvenlik:
Zararlı siteleri filtreleyebilir.

Trafik kontrolü:
Şirketlerde internet trafiği yönetiminde kullanılır.

Kullanılan Proxy Yazılımları:

Squid Proxy → En yaygın open-source proxy sunucusu.

Apache Traffic Server

Microsoft ISA / Forefront TMG

NGINX (forward proxy olarak da yapılandırılabilir)

2️⃣ Reverse Proxy (Ters Proxy)

Reverse proxy, bu sefer ters yönde çalışır:
İstemci bunu “asıl sunucu” sanır ama o aslında arka plandaki (backend) gerçek sunuculara istekleri yönlendirir.

Basit düşün:

Kullanıcı → Reverse Proxy → (1 veya daha fazla) Gerçek Web Sunucusu

Ne işe yarar?

Load Balancing (Yük Dengeleme):
Trafiği birden fazla sunucuya dağıtarak yükü dengeler.

Security (Güvenlik):
Gerçek sunucuların IP adresini gizler.

SSL Termination:
HTTPS sertifikalarını reverse proxy üzerinde yönetir, backend’e sade HTTP ile iletir.

Caching:
Statik içerikleri önbellekleyerek performansı artırır.

Compression ve Gzip:
Yanıtları sıkıştırarak trafiği azaltır.

Routing:
URL veya hostname’e göre farklı backend sunucularına yönlendirme yapar.

Kullanılan Reverse Proxy Yazılımları:

NGINX (en yaygın ve güçlü reverse proxy)

HAProxy (yük dengeleyici olarak mükemmel)

Apache HTTP Server (mod_proxy modülüyle)

Traefik (modern, container ve Kubernetes dostu reverse proxy)

AWS Application Load Balancer (ALB) da reverse proxy gibi davranır

3️⃣ Proxy vs Reverse Proxy (Kıyaslama)
Özellik	Proxy Server (Forward)	Reverse Proxy
Konum	Kullanıcı (client) tarafında	Sunucu (server) tarafında
Amaç	Kullanıcının internete çıkışı	Gelen isteklerin sunuculara yönlendirilmesi
Kime hizmet eder	Kullanıcıya	Sunucuya
Kullanım alanı	Şirket ağları, güvenlik, erişim kontrolü	Web siteleri, load balancing, SSL offloading
Gerçek sunucu IP’si	Görünür	Gizlenir
Örnek yazılım	Squid	NGINX, HAProxy

Gerçek Hayattan Örnek:

Proxy Server:
Okul ağı → Öğrenciler facebook.com’a gitmek ister ama okulun proxy’si engeller.
Yani proxy dış trafiği kontrol eder.

Reverse Proxy:
www.amazon.com’a girdiğinde aslında NGINX reverse proxy’ye ulaşırsın; o senin isteğini en uygun backend sunucuya yollar.
Yani reverse proxy gelen trafiği yönetir.

Özet:
Tür	Tanım	Örnek Kullanım	Örnek Yazılım
Proxy (Forward)	Kullanıcı → Proxy → İnternet	IP gizleme, erişim kontrolü	Squid, Apache Traffic Server
Reverse Proxy	Kullanıcı → Reverse Proxy → Sunucular	Load balancing, caching, SSL termination	NGINX, HAProxy, Traefik


# “Proxy” ve “Reverse Proxy” ağda hazır mı?

Hayır genelde hazır gelmezler, ama ağ katmanında kurulabilir veya servis olarak kullanılabilirler.
Yani iki senaryo vardır:

🅰️ Kurumsal Ağlarda (Proxy Server)

Şirketin ağı genellikle merkezi bir proxy üzerinden internete çıkar.

Bu proxy’yi ağ yöneticisi kurar (örneğin Squid, Bluecoat, Palo Alto vb.).

Yani senin bilgisayarın doğrudan internete çıkmaz; proxy’ye gider, o senin yerine çıkış yapar.

Kullanıcı (developer, çalışan) bu sistemi kendisi kurmaz, BT ekibi kurar.

Örnek:

Şirket ağı → Proxy → İnternet
Proxy erişim loglarını tutar, yasak siteleri engeller, trafik kontrol eder.

🅱️ Web / Uygulama Tarafında (Reverse Proxy)

Reverse proxy ise genelde biz geliştiriciler veya DevOps ekibi tarafından uygulama tarafına kurulur.

Örneğin:

AWS EC2 üzerine NGINX kurarsın, o senin uygulamana reverse proxy olur.

Ya da AWS Application Load Balancer (ALB) kullanırsın → o da bir reverse proxy’dir.

Örnek:

Kullanıcı → NGINX (reverse proxy) → Spring Boot uygulaması (Tomcat)

# İkisi aynı anda çalışabilir mi?

Evet ama farklı seviyelerde.

Proxy (forward) genellikle kullanıcı tarafında (network çıkışında) çalışır.

Reverse proxy genellikle sunucu tarafında (istek girişinde) çalışır.

Yani:

Client → Proxy Server → Internet → Reverse Proxy → Application Server


Her biri trafiğin farklı ucunda görev yapar:

Proxy: Kullanıcının internete çıkışını yönetir.

Reverse Proxy: İnternetten gelen trafiği yönetir.

Ama bu ikisi aynı sistemde genelde olmaz, farklı noktalarda olur.

# Her site/uygulama/mobil uygulamada var mı?

Cevap: Hayır, her zaman yok.
Ama büyük ölçekli olanların neredeyse hepsinde reverse proxy vardır.

Web siteleri:

Büyük sitelerde (%99’unda) reverse proxy vardır.
Örneğin:

Google → kendi özel reverse proxy sistemleri

Amazon, Netflix, YouTube → NGINX, HAProxy benzeri sistemler

Medium, GitHub → CDN + reverse proxy yapısı

Mobil uygulamalar:

Mobil uygulama API çağrıları da genelde reverse proxy üzerinden geçer.

Örneğin:

api.spotify.com çağrısı → reverse proxy → gerçek mikroservisler

Ama cihaz (mobil uygulama tarafı) proxy server kullanmaz; sadece kullanıcı ağında varsa (örneğin kurumsal Wi-Fi).

Küçük projeler:

Küçük web sitelerinde reverse proxy şart değildir, ama tavsiye edilir.

Örneğin:

Senin Spring Boot uygulaman doğrudan port 8080’de çalışabilir.

Ancak üretim ortamında genellikle önüne NGINX koyarsın → güvenlik, SSL, caching sağlar.

Gerçek hayatta kim ne kurar?
Katman	Kim kurar	Tür	Örnek
Kullanıcı ağı (şirket)	BT ekibi	Proxy Server	Squid, Bluecoat
İnternet önünde (web app)	DevOps / Developer	Reverse Proxy	NGINX, HAProxy, ALB
Mobil uygulama API	DevOps / Cloud	Reverse Proxy	API Gateway, Traefik

Özet Görünüm
[Kullanıcı]
   ↓
(Proxy Server - optional)
   ↓
Internet
   ↓
(Reverse Proxy)
   ↓
[Gerçek Web/Microservice Uygulaması]

Özetle:
Soru	Cevap
Ağda hazır mı?	Proxy genelde BT tarafından kuruludur, reverse proxy’yi biz kurarız.
Aynı anda çalışır mı?	Evet, ama farklı uçlarda (biri kullanıcı tarafı, diğeri sunucu tarafı).
Her sitede var mı?	Büyük sitelerde mutlaka reverse proxy vardır; küçüklerde opsiyonel.
Kim kurar?	Proxy’yi ağ yöneticisi, reverse proxy’yi backend/devops ekibi.

# nginx nedir? Nerelerde kulanılır? Devops ve aws'de nasıl kurulur?
 1️⃣ NGINX Nedir?

NGINX, bir yüksek performanslı web sunucusu (web server) ve reverse proxy (ters vekil) yazılımıdır.
Açılımı: Engine X → “enjin-eks” şeklinde okunur.

Temel amaçları:

Web sayfalarını hızlı şekilde sunmak

Yük dengeleme (load balancing) yapmak

Reverse proxy görevi görmek

Güvenlik, caching ve SSL yönetimi sağlamak

2️⃣ Nerelerde Kullanılır?
Kullanım Alanı	Açıklama	Örnek
Web Server	HTML, CSS, JS gibi statik dosyaları doğrudan sunar	Basit web sitesi host etme
Reverse Proxy	Kullanıcıdan gelen isteği arka uçtaki (backend) uygulamalara yönlendirir	Spring Boot, Node.js, Python API’leri için
Load Balancer	Trafiği birden fazla backend’e dağıtır	Mikroservis yapılarında
SSL Termination	HTTPS trafiğini NGINX’te bitirip backend’e sade HTTP ile iletir	Sertifika yönetimi
Caching & Compression	Yanıtları sıkıştırır ve önbellekler	CDN benzeri performans artışı
Security Layer	IP bazlı erişim kısıtlaması, rate limiting, DDoS koruması	Web application firewall öncesi katman

3️⃣ NGINX Nerelerde Kullanılır (Gerçek Hayat)

Amazon, Netflix, GitHub, Dropbox, WordPress.com, Cloudflare, Twitch gibi dev sitelerin hepsinde NGINX kullanılır.

Neredeyse tüm modern DevOps / Cloud mimarilerinde (özellikle AWS, Kubernetes, Docker) bir reverse proxy veya ingress controller olarak NGINX vardır.

4️⃣ DevOps’ta NGINX’in Rolü

DevOps dünyasında NGINX şu görevlerde kullanılır:

CI/CD sonrası uygulamayı yayınlamak (deployment):
Spring Boot veya Node.js uygulaman çalışıyor → NGINX onu dış dünyaya açar.

User → NGINX (port 80) → Backend (port 8080)

Reverse Proxy ve Load Balancing:
Trafiği birden fazla backend instance’a yönlendirir.

SSL Sertifika Yönetimi:
HTTPS trafiğini terminate eder, Let’s Encrypt entegrasyonu kolaydır.

Container ve Kubernetes Dünyası:
NGINX genellikle “ingress controller” olarak görev yapar.
(Yani dışarıdan gelen trafiği cluster içindeki servislere yönlendirir.)

5️⃣ AWS Üzerinde NGINX Kurulumu

AWS’de NGINX genellikle bir EC2 instance üzerinde kurulur.
Adım adım anlatayım 

Adım 1: EC2 Oluştur

Amazon Linux 2 veya Ubuntu 22.04 seç.

Security Group’ta port 80 (HTTP) ve 22 (SSH)’u aç.

SSH ile bağlan.

Adım 2: NGINX Kur
Ubuntu:
sudo apt update
sudo apt install nginx -y

Amazon Linux:
sudo amazon-linux-extras install nginx1 -y

Adım 3: Servisi Başlat
sudo systemctl start nginx
sudo systemctl enable nginx

Adım 4: Test Et

Tarayıcıda şunu yaz:

http://<ec2-public-dns>


“Welcome to NGINX!” sayfası çıkarsa her şey tamam 

6️⃣ Reverse Proxy Örneği (Spring Boot ile)

Spring Boot uygulaman EC2’de localhost:8080’de çalışıyor diyelim.
NGINX’in konfigürasyonunu şöyle yaparsın

Dosya: /etc/nginx/sites-available/default

server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}


Sonra NGINX’i yeniden başlat:

sudo systemctl restart nginx


Artık:

http://ec2-public-dns


adresine girdiğinde Spring Boot uygulaman çalışır.
NGINX istekleri 8080’e yönlendirdiği için dış dünyadan direkt backend görünmez.

7️⃣ Kısaca Özet
Özellik	Açıklama
Yazılım Türü	Web server ve reverse proxy
Kurulum Alanı	EC2, Container, Kubernetes
Görevleri	Reverse proxy, load balancing, SSL termination, caching
Popüler Olduğu Yerler	AWS, Azure, Google Cloud, Docker, K8s
Alternatifleri	Apache HTTP Server, HAProxy, Traefik

# Apache nedir, Nerelerde kulanılır, devops ve Aws'de nasıl kurulur, Nginx ile farkı nedir?
Apache Nedir?

Apache HTTP Server, kısaca Apache,
web sitelerini ve web uygulamalarını internete sunmak için kullanılan açık kaynaklı bir web sunucusudur.
1995’te geliştirildi, hâlâ en popüler web sunucularından biridir.
Apache Software Foundation tarafından geliştirilmektedir.

Ne İşe Yarar?

Bir web server, gelen HTTP isteklerini (request) alır ve uygun yanıtı (response) döner.
Apache, bu işi yapan yazılımdır.

Örneğin:

Kullanıcı → Tarayıcıdan www.ornek.com’a istek gönderir
↓
Apache Server isteği alır
↓
İlgili HTML dosyasını, resimleri veya uygulama çıktısını bulur
↓
Tarayıcıya geri gönderir (response)

Nerelerde Kullanılır?

Web sitelerini yayınlamak (WordPress, PHP siteleri, HTML siteleri)

Backend uygulamalarına gelen istekleri yönetmek

Local development (örneğin XAMPP veya MAMP içinde)

Kurumsal web servislerinde (örneğin Java web uygulamaları)

Apache Nasıl Çalışır?

Apache her isteği işlemek için ayrı bir process (veya thread) oluşturur.
Bu modelin adı:

“Process-based architecture”

Bu, çok sayıda eşzamanlı istekte CPU ve bellek kullanımını artırır.
Yani çok trafik varsa Apache biraz daha fazla kaynak tüketir.

DevOps ve AWS’de Apache Kurulumu
🔹 Linux (Ubuntu) Üzerinde:
sudo apt update
sudo apt install apache2 -y
sudo systemctl enable apache2
sudo systemctl start apache2


Sonra tarayıcıya gidip:

http://<EC2-public-ip>


dediğinde “Apache2 Ubuntu Default Page” görürsün.

🔹 AWS EC2’de:

Bir EC2 Instance (örneğin Ubuntu) oluştur.

Security Group’ta 80 numaralı portu (HTTP) aç.

SSH ile bağlan.

Yukarıdaki komutları çalıştır.

Tarayıcıdan EC2’nin public IP’sine git → Apache sayfası gelir.

Nginx vs Apache Karşılaştırması
Özellik	Apache	Nginx
Çalışma mantığı	Her istek için ayrı thread/process açar	Asenkron, event-driven model (çok daha verimli)
Performans	Düşük trafikte iyi	Yüksek trafikte çok daha iyi
Statik dosyalar (CSS, JS, img)	İyi	Çok hızlı
Dinamik içerik (PHP, Java)	PHP modülüyle doğrudan çalışabilir	Genellikle backend’e (ör. Apache, Gunicorn) proxy olur
Konfigürasyon dosyası	.htaccess dosyaları	nginx.conf
Kullanım alanı	PHP siteleri, klasik web projeleri	Modern web app, load balancing, reverse proxy
Bellek kullanımı	Fazla	Daha az
Kurumsal popülerlik	Eski sistemlerde çok yaygın	Yeni sistemlerde tercih ediliyor

Gerçek Hayatta Nasıl Kullanılır?

Tek başına Apache → klasik web siteleri (örneğin WordPress)

Tek başına Nginx → modern microservice mimarilerinde

Birlikte:
En yaygın senaryo:

Nginx (reverse proxy)
     ↓
 Apache (uygulama sunucusu)


Böylece Nginx dış trafiği yönetir, Apache arka planda dinamik içeriği üretir.

AWS ve DevOps Dünyasında Kullanımı

EC2’de web sunucusu kurmak için

Load balancer veya reverse proxy olarak (özellikle Nginx)

CI/CD pipeline sonrası deployment aşamasında uygulamayı sunmak için

Docker container’larında (örneğin Apache + PHP image)

Özetle:
Özellik	Apache	Nginx
Model	Process/thread tabanlı	Event tabanlı
Trafik yönetimi	Orta ölçek	Yüksek ölçek
Dinamik içerik	Direkt destekler	Proxy üzerinden iletir
Statik içerik	Orta hız	Çok hızlı
Kullanım alanı	Klasik web projeleri	Modern microservice mimarileri

# Her Linux dağıtımı (distro) farklı bir “aileye” aittir ve farklı bir paket yöneticisi (package manager) kullanır.

Aşağıda senin için en temel distroları ailelerine göre sade bir tabloyla anlattım:

1️⃣ Debian Ailesi

En popüler masaüstü ve sunucu distrosudur.
Ubuntu da bu ailenin bir türevidir.

Distro	         Türevi	        Paket Yöneticisi	               Paket Uzantısı	          Komut Örnekleri
Debian	        Ana dağıtım	     apt (Advanced Package Tool)	         .deb	                sudo apt install nginx
Ubuntu	        Debian tabanlı	  apt	                                 .deb	                sudo apt update
Kali Linux	     Debian tabanlı	  apt	                                 .deb	                sudo apt install nmap
Linux Mint	     Ubuntu tabanlı	  apt	                                 .deb	                sudo apt install firefox

Not: Ubuntu gibi distrolarda .deb uzantılı paketler kullanılır.

2️⃣ Red Hat (RHEL) Ailesi

En çok kurumsal sunucularda ve DevOps ortamlarında (AWS, Docker, Kubernetes) kullanılır.
Amazon Linux, Fedora, CentOS da bu ailedendir.

Distro	                              Türevi	               Paket Yöneticisi	         Paket Uzantısı	          Komut Örnekleri
RHEL (Red Hat Enterprise Linux)	      Ana dağıtım	            yum / dnf	               .rpm	                   sudo yum install httpd
CentOS Stream	                        RHEL tabanlı	         dnf	                     .rpm	                   sudo dnf update
Fedora	                              RHEL tabanlı	         dnf	                     .rpm	                   sudo dnf install git
Amazon Linux 2023	                     Fedora tabanlı	         dnf	                     .rpm	                   sudo dnf install nginx
Oracle Linux	                        RHEL tabanlı	         dnf	                     .rpm	                   sudo dnf install java

Not: Yeni nesil RHEL tabanlı sistemlerde yum artık dnf’nin alias’ıdır.
Yani yum yazarsan arkada dnf çalışır.

# “Amazon Linux 2023 (AL2023)” aslında Amazon’un kendisinin geliştirdiği özel bir Linux dağıtımıdır (distro).
Yani evet — bu da bir Linux dağıtımıdır, tıpkı Ubuntu, CentOS, Fedora veya Debian gibi.

Ama diğerlerinden biraz farklı:
AWS’in EC2 ortamlarına tam optimize edilmiş, güvenlik, performans ve kararlılık odaklı özel bir sürümüdür.

1️⃣ Amazon Linux 2023 Nedir?

AWS tarafından geliştirilen bir Linux dağıtımıdır.

Fedora / RHEL (Red Hat Enterprise Linux) tabanlıdır.

Tamamen open source ve AWS servisleriyle (EC2, ECS, Lambda, Systems Manager, vb.) tam uyumludur.

Amazon’un önceki sürümü Amazon Linux 2 idi → 2023 sürümü onun yerini aldı.

2️⃣ Hangi Paket Yöneticisini (Package Manager) Kullanır?

Amazon Linux 2023, dnf tabanlıdır.

Yani:

dnf → evet (varsayılan)

yum → çalışır ama aslında yum komutunu yazarsan arka planda dnf’yi çağırır.