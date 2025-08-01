

# SSH Nedir?
SSH = Secure Shell
Uzak bir sunucuya (örneğin EC2 instance’a) şifreli, güvenli bir terminal bağlantısı kurmak için kullanılan protokoldür.
Yani:
Başka bir bilgisayarda (sunucuda) çalışıyorsun ama sanki kendi bilgisayarınmış gibi komutlar yazabiliyorsun.
SSH Ne İşe Yarar?
Amaç	Açıklama
Uzak sunucuya bağlanmak	Örn: EC2 instance’a erişmek
Kod çalıştırmak / deploy yapmak	Örn: Spring Boot uygulamanı başlatmak
Paket kurmak / log bakmak	Örn: Java, Docker kurmak
Log dosyalarını incelemek	Uygulama hatalarını kontrol etmek

SSH Bağlantısı Nasıl Çalışır?
SSH ile bağlanmak için genelde şu bilgilere ihtiyacın olur:
Uzak sunucunun IP adresi
Bir SSH anahtarı (genellikle .pem uzantılı özel anahtar dosyası)
Giriş yapılacak kullanıcı adı (örneğin: ec2-user, ubuntu, root)
Komut Örneği:
ssh -i anahtar-dosyasi.pem ec2-user@13.57.123.45
Bu komutla sen kendi bilgisayarından → EC2 instance’ına terminalden bağlanırsın.

SSH Güvenli midir?
Evet çünkü:
Şifre yerine genelde özel anahtar (private key) kullanılır
Tüm iletişim şifrelenmiştir
AWS EC2 instance’larına varsayılan olarak sadece SSH portu (22) açıktır

Gerçek Hayat Senaryosu
Diyelim Spring Boot uygulamanı EC2’ye deploy ettin:
ssh ile EC2’ye bağlanırsın
java -jar okul-yonetim.jar komutuyla çalıştırırsın
Uygulama logs vs. terminalde görünür
Gerekirse nano veya vim gibi editörlerle konfigürasyon dosyalarını düzenlersin

Özet
Konu	Açıklama
SSH	Uzak sunucuya güvenli bağlantı kurma protokolü
Kullanım alanı	EC2, VPS, sunucu yönetimi, deploy
Ne gerekiyor?	IP adresi, SSH key, kullanıcı adı
Kullanımı	ssh -i key.pem user@ip şeklinde komut

# Key Pair Nedir?
Key Pair = Anahtar Çifti demektir.
Uzak bir sunucuya (örneğin EC2) şifre yerine güvenli bir şekilde bağlanmanı sağlayan iki parçalı bir dijital kimliktir.

İki Parçası Vardır:
Private Key (gizli)	Senin bilgisayarında (.pem dosyası)	SSH bağlantısı yaparken kullanılır
Public Key (açık)	Sunucuda (örneğin EC2 üzerinde)	Kimliğini doğrulamak için gereken açık anahtar
Bu ikili birlikte çalışır:
Sen SSH ile sunucuya bağlanırken, sunucu public key’i ile kontrol eder → senin private key’in uyuyorsa bağlantıya izin verir.

Neden Kullanılır?
Şifre kullanmadan, daha güvenli bir şekilde oturum açmak için.
Çünkü:
Şifre tahmin edilebilir → ama key pair çok daha güçlü
Private key sadece sende olur
AWS gibi platformlar güvenliği bu şekilde sağlar

EC2 Oluştururken Key Pair Ne Demek?
EC2 başlatırken şunu görürsün:
"Select an existing key pair or create a new one"
Bu şu anlama gelir:
EC2’ye SSH ile bağlanmak için ya:
Daha önce oluşturduğun bir key pair’i seç
Ya da “Create new key pair” diyerek .pem uzantılı özel anahtar indir (sadece bir kere verilir)

Dikkat!
.pem dosyası kaybolursa	EC2’ye SSH ile bağlanamazsın (erişim yok olur)
.pem dosyası paylaşılmaz	Çünkü gizlidir, sadece senin bilgisayarında olmalı
Yeni key oluşturmak gerekirse	EC2'yi stop edip yeni bir key ile AMI’den yeni instance üretmen gerekebilir

Örnek Kullanım:
ssh -i "feyyaz-key.pem" ec2-user@13.59.12.34
Bu komut:
feyyaz-key.pem → senin özel anahtarın (private key)
ec2-user → AWS Amazon Linux kullanıcısı
13.59.12.34 → EC2 IP adresi

Özetle:
Key Pair	SSH bağlantısı için gerekli dijital kimlik çifti
Private Key	Sadece sende olan gizli dosya (.pem)
Public Key	AWS EC2 üzerinde duran açık anahtar
Kullanım amacı	Şifresiz ama güvenli bağlantı kurmak

# Bölgesel Farklılıklar:
US East (N. Virginia) - us-east-1:
En eski ve en kapsamlı bölge
Tüm instance type'ları (t2, t3, t4g)
Tüm kaynaklarınız burada
Key pair'lar burada kayıtlı

Europe (Stockholm) - eu-north-1:
Nispeten yeni bölge (2018)
Sadece yeni nesil instance'lar (t3, t4g)
Kaynaklarınız yok (farklı bölge)
Key pair'lar ayrı tutulur

AWS Bölge Mantığı:
Kaynak Bağımsızlığı:
Key pair'lar bölgeye özel
Instance'lar bölgeye özel
Security group'lar bölgeye özel
AMI'ler bölgeye özel