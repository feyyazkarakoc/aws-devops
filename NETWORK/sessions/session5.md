# Neden n = 4 ve neden 16 alt ağ?
 İhtiyaç Duyulan Host Sayısına Göre
 IP ; 192.168.1.0/24
 Bilgi Sist. Dep.= 12 Kişi

İhtiyaç: 12 host.

Host biti sayısını h kabul edelim. Gereken koşul: 2^h - 2 ≥ 12 (network ve broadcast adresleri ayrıldığı için).

h = 3 → 2^3 - 2 = 6 (yetmez)

h = 4 → 2^4 - 2 = 14 (yeterli)

Dolayısıyla her alt ağ için 4 host biti gerekiyor.

Orijinal /24’te host bitleri = 8. Yeni host biti = 4 ⇒ 4 bit hostlardan ağ bitlerine kaydırıldı (borrowed bits = 8 - 4 = 4).

Alt ağ sayısı = 2^(borrowed bits) = 2^4 = 16.

Yeni prefix = 32 - h = 32 - 4 = /28. Yani her subnet /28 olur (16 adres, 14 kullanılabilir host).

Aşağıda 192.168.1.0/24 içindeki 16 yeni /28 alt ağın network adresleri ve bunların binary gösterimleri (dotted binary) yer alıyor. Ayrıca her satırda kullanılabilir host aralığı ve broadcast verildi.

Not: ilk üç oktet sabit:
192 = 11000000 , 168 = 10101000 , 1 = 00000001

	Network (decimal /28)	Network (binary dotted)	Usable IP aralığı	Broadcast
1	192.168.1.0 /28	11000000.10101000.00000001.00000000	192.168.1.1 - 192.168.1.14	192.168.1.15
2	192.168.1.16 /28	11000000.10101000.00000001.00010000	192.168.1.17 - 192.168.1.30	192.168.1.31
3	192.168.1.32 /28	11000000.10101000.00000001.00100000	192.168.1.33 - 192.168.1.46	192.168.1.47
4	192.168.1.48 /28	11000000.10101000.00000001.00110000	192.168.1.49 - 192.168.1.62	192.168.1.63
5	192.168.1.64 /28	11000000.10101000.00000001.01000000	192.168.1.65 - 192.168.1.78	192.168.1.79
6	192.168.1.80 /28	11000000.10101000.00000001.01010000	192.168.1.81 - 192.168.1.94	192.168.1.95
7	192.168.1.96 /28	11000000.10101000.00000001.01100000	192.168.1.97 - 192.168.1.110	192.168.1.111
8	192.168.1.112 /28	11000000.10101000.00000001.01110000	192.168.1.113 - 192.168.1.126	192.168.1.127
9	192.168.1.128 /28	11000000.10101000.00000001.10000000	192.168.1.129 - 192.168.1.142	192.168.1.143
10	192.168.1.144 /28	11000000.10101000.00000001.10010000	192.168.1.145 - 192.168.1.158	192.168.1.159
11	192.168.1.160 /28	11000000.10101000.00000001.10100000	192.168.1.161 - 192.168.1.174	192.168.1.175
12	192.168.1.176 /28	11000000.10101000.00000001.10110000	192.168.1.177 - 192.168.1.190	192.168.1.191
13	192.168.1.192 /28	11000000.10101000.00000001.11000000	192.168.1.193 - 192.168.1.206	192.168.1.207
14	192.168.1.208 /28	11000000.10101000.00000001.11010000	192.168.1.209 - 192.168.1.222	192.168.1.223
15	192.168.1.224 /28	11000000.10101000.00000001.11100000	192.168.1.225 - 192.168.1.238	192.168.1.239
16	192.168.1.240 /28	11000000.10101000.00000001.11110000	192.168.1.241 - 192.168.1.254	192.168.1.255

(Kalın yapılan son oktet kısmı, o alt ağın network adresinin son oktetinin binary'sidir.)

Ek Notlar

Her /28 blok 16 IP içerir: 2^4 = 16. Bunların 2 tanesi rezerve (network + broadcast), 14 tane kullanılabilir (ki 12 kişi için rahat yeterli).

Eğer ileride büyüme olacaksa ilave host ihtiyaçlarına göre daha az subnet daha fazla host veren bir plan gerekebilir (ör. /27 verir 30 usable).

Hocanın bulduğu n = 4 burada host bitleri anlamında: yeni host biti sayısı 4 (=14 usable). Borrowed bits = 4, subnets = 16.

# “host” kelimesi bilgisayar ağlarında, sunucularda ve hatta günlük IT kullanımında farklı anlamlarda karşımıza çıkıyor.

1️⃣ Host (Bilgisayar Ağlarında)

Host = “Ağa bağlı her cihaz”.

Bilgisayar, telefon, tablet, yazıcı, hatta IoT cihazı (kamera, akıllı priz vs.) olabilir.

Yani “her IP adresi alabilen cihaz” aslında bir host.
🔹 Örn: Senin laptopun da bir host, Google’ın sunucusu da.

2️⃣ Host (Sunucu / Server Kavramında)

Bazen “host” kelimesi sunucu (server) anlamında da kullanılır.

Çünkü o cihaz (sunucu) üzerinde başka yazılımlar veya servisler çalışır.
🔹 Örn: “mail host” dediğimizde aslında mail server (e-posta sunucusu) kastedilir.

3️⃣ Hosting (Web Hosting)

Hosting: Bir web sitesini ya da uygulamayı internette erişilebilir hale getirmek için kullanılan hizmettir.

Web siteni dosyaları (HTML, CSS, resimler, veritabanı) bir sunucuda (host üzerinde) barındırılır.

Kullanıcı tarayıcıdan senin sitene girdiğinde, hosting firması sunucusundaki dosyaları gönderir.
🔹 Örn: “GoDaddy’den hosting aldım.” = Web sitesi dosyaların GoDaddy’nin sunucularında tutuluyor.

4️⃣ Virtual Hosting / Shared Hosting

Aynı fiziksel sunucuda birden fazla site barındırılabilir.

Örn: Senin web siten host1.example.com, arkadaşınınki host2.example.com olabilir.

İkisi de aynı fiziksel makinada ama farklı domain/subdomainlerle yayın yapıyor.

5️⃣ Hosting ile Cloud / VPS Farkı

Shared Hosting: Küçük siteler için, aynı makineyi yüzlerce kişi paylaşır.

VPS Hosting: Fiziksel sunucunun içinde sanal makineler. Daha fazla özgürlük.

Dedicated Hosting: Tüm sunucu sadece sana ait.

Cloud Hosting: Tek bir makineye değil, bulut altyapısına dağılmış. Daha esnek.

6️⃣ Host File (Bilgisayardaki hosts Dosyası)

Bilgisayarda C:\Windows\System32\drivers\etc\hosts dosyası vardır.

Burada IP ↔ Domain eşleştirmeleri yapabilirsin.

Örn: 127.0.0.1 facebook.com yazarsan → Tarayıcı Facebook’a gitmeye çalıştığında kendi bilgisayarına döner, yani siteye giremezsin.

7️⃣ Diğer Kullanımlar

Virtual Host: Apache/Nginx’te farklı domainleri tek sunucuda yönetmek.

Game Hosting: Oyun sunucusu kiralamak.

Mail Hosting: E-posta hizmetini sağlayan sunucu.

Özet:

Host: Ağa bağlı cihaz.

Hosting: Bir sunucu üzerinde servis (web, mail, oyun vs.) barındırma.

Host (server anlamında): Bazen doğrudan “sunucu” demek.