
# Script dilleri
Script dilleri, genellikle derleme (compile) yerine yorumlama (interpret) yöntemiyle çalışan, daha çok otomasyon,
küçük görevler, web geliştirme gibi alanlarda kullanılan programlama dilleridir.

Yaygın Script Dilleri:
Script Dili	Kullanım Alanı
JavaScript	Web tarayıcıları, frontend & backend (Node.js)
Python	Otomasyon, veri analizi, web geliştirme, yapay zeka
Bash (veya Shell script)	Linux komutları ile otomasyon, sistem yönetimi
PowerShell	Windows sistem yönetimi, otomasyon
PHP	Web sunucu tarafı programlama

Script Dili Özellikleri:
Genelde yorumlanarak çalışır (derlenmez).

Daha az boilerplate (tekrarlayan) kod içerir.

Hızlı geliştirme ve test için uygundur.

Çoğu dinamik olarak tür belirler (int, string gibi yazmaya gerek kalmaz).

Not:
Script dilleri ile programlama dilleri arasındaki çizgi artık net değildir. Örneğin:

Python bir script dili olarak başlasa da artık büyük sistemlerde kullanılıyor.

JavaScript artık tarayıcı dışında (Node.js) da sistem uygulamalarında kullanılabiliyor.

# Derleme ve Yorumlama

1. Derleme (Compile) Nedir?
Derleme, bir programın kaynak kodunun (örneğin .java, .c, .cpp) önce tamamen makine diline çevrilmesi (bir kereye mahsus) işlemidir.

Örneğin:

Java → javac ile .java dosyası .class (bytecode) dosyasına çevrilir.

C → gcc ile .c dosyası .exe veya .out dosyasına çevrilir.

Avantajı: Program çalışmadan önce tamamen çevrilir, bu yüzden genellikle daha hızlı çalışır.
Dezavantajı: Derleme işlemi zaman alır, hata varsa çalıştırmadan önce öğrenirsin. 

2. Yorumlama (Interpret) Nedir?
Yorumlama, programın satır satır okunarak çalıştırılmasıdır. Önceden makine koduna çevrilmez.

Örneğin:

Python → python dosya.py dediğinde yorumlayıcı (interpreter) satır satır okur ve çalıştırır.

JavaScript → Tarayıcı veya Node.js anında kodu yorumlar.

Avantajı: Derlemeye gerek yok, hemen yaz ve çalıştır → hızlı test edebilirsin.
Dezavantajı: Her çalıştırmada yorumlandığı için biraz daha yavaştır.

Örnekle Anlatım:
Python (yorumlanır):
print("Merhaba")
Bu kodu direkt çalıştırırsın:
python dosya.py
Interpreter satır satır okur: önce print() fonksiyonunu görür ve "Merhaba" yazar.

C (derlenir):
c
#include <stdio.h>

int main() {
    printf("Merhaba");
    return 0;
}
Önce derlemen gerekir:
gcc dosya.c -o program
Sonra çalıştırırsın:
./program

Script Dilleri Neden Yorumlanır?
Kısa ve hızlı geliştirme için idealdir.

Web tarayıcıları gibi ortamlarda dinamik çalışmaları sağlar.

Script dillerinde genelde tek bir komutla çalıştırırsın, önce derlemene gerek kalmaz.

Özet:
Özellik	Derlenen Diller (C, Java)	Yorumlanan Diller (Python, JS)
Çalıştırmadan önce derleme	Gerekli	Gerekmez
Hız	Daha hızlı	Göreceli olarak yavaş
Hata tespiti	Derleme sırasında	Çalışma sırasında
Geliştirme hızı	Daha yavaş	Daha hızlı

#  "Dezavantajı: Derleme işlemi zaman alır, hata varsa çalıştırmadan önce öğrenirsin."

Bu kısmı şöyle açık ve doğru şekilde açıklayayım:

Aslında:
"Hataları çalıştırmadan önce öğrenmek", genelde bir avantajdır, dezavantaj değil.

Çünkü:

Derleyici (örneğin javac, gcc) programı çalıştırmadan önce tüm sözdizimi (syntax), tür (type) hatalarını yakalar.

Bu sayede daha sağlam ve güvenli kod yazarsın.

Örneğin: int x = "merhaba"; gibi bir hatayı daha çalıştırmadan fark edersin.

Peki Neden Orada “Dezavantaj” Demiş Gibi Oldum?
Cümle aslında iki farklı şey karışmış:

Zaman alması → Bu gerçekten dezavantajdır. (her değişiklikten sonra derlemen gerekebilir)

Hataları önceden yakalama → Bu avantajdır, ama yorumlayıcılara kıyasla bu daha "katıdır".

Bazı durumlarda geliştirici:

“Ben küçük bir şey deneyeceğim, hemen çalıştırmak istiyorum.”

Derleyici hata verirse sinir olabilir 

Bu açıdan "katılık" bazen esneklik kaybı gibi hissedilir ama bu aslında uzun vadede faydadır.

Doğrusu Nasıl Olmalıydı?
Şöyle demeliydim:

Dezavantaj: Derleme işlemi zaman alır.
Avantaj: Hataları çalıştırmadan önce fark edersin (daha güvenli kodlama sağlar).

Ek Bilgi:
Özellik	Derlenen Diller (Java, C)	Yorumlanan Diller (Python, JS)
Hataları görme zamanı	Derlemede (önceden)	Çalışma anında (run-time)
Geliştirme esnekliği	Daha katı, daha güvenli	Daha esnek ama hata riski var

# GNU nedir, Linux nedir, DevOps açısından ne işe yarar?

1. GNU Nedir?
GNU, “GNU's Not Unix” cümlesinin kısaltmasıdır.

Tanımı:
1983’te Richard Stallman tarafından başlatılan bir projedir.

Amacı: UNIX'e benzeyen ama tamamen özgür (free/libre) bir işletim sistemi oluşturmaktı.

GNU, işletim sisteminin kullanıcıya görünen üst katmanlarını (kabuk, editörler, derleyiciler vb.) içerir.

GNU Ne Sağlar?
bash, ls, cp, grep, cat gibi terminal komutları

GCC (C derleyicisi), GDB (debugger), make gibi geliştirme araçları

Temel Unix-like kullanıcı araçları ve kütüphaneler (örneğin glibc)

2. Linux Nedir?
Tanımı:
Linux, bir işletim sistemi çekirdeğidir (kernel).

1991 yılında Linus Torvalds tarafından yazılmıştır.

İşletim sisteminin "kalbidir", donanım ile yazılım arasındaki bağlantıyı sağlar.

Kernel ne yapar?
Bellek yönetimi

Dosya sistemi yönetimi

Donanım sürücüleriyle iletişim

Süreç (process) yönetimi

Peki GNU + Linux Nedir?
Tek başına Linux bir işletim sistemi değildir, sadece bir çekirdektir.

GNU araçları olmadan Linux kullanılamaz (sadece donanımın üstünde bir katman olur).

Birlikte: GNU/Linux = tam işleyen özgür işletim sistemi

Örnek: Ubuntu, Debian, Fedora gibi dağıtımlar aslında GNU/Linux dağıtımlarıdır.

3. DevOps Açısından GNU ve Linux’un Önemi
Neden DevOps'ta Çok Kullanılır?
Özellik	Açıklama
Sunucuların çoğu Linux'tur	AWS, Azure, GCP gibi bulut servisleri genelde Linux VM sağlar.
GNU araçları otomasyon için idealdir	bash, cron, awk, sed, grep gibi komutlar DevOps işlerinin temelini oluşturur.
Script yazımı kolaydır	Bash scriptleri ile yapılandırma, dağıtım, test süreçleri kolayca otomatikleştirilir.
Paket yönetimi vardır	apt, yum, dnf gibi araçlarla yazılım kurulumu otomatikleştirilebilir.
Yetki ve kullanıcı yönetimi güçlüdür	SSH, sudo, chmod, chown ile güvenli sunucu yönetimi yapılabilir.
Docker, Kubernetes gibi araçlarla uyumludur	Linux tabanlı konteyner altyapısı DevOps’un kalbidir.

Örnek: DevOps Sürecinde Kullanımı
Bir web uygulaması CI/CD sürecinde:
Linux sunucuda çalışan uygulama

Bash scriptleriyle deploy işlemi

Cron ile düzenli görevler

Docker image’ı bir Linux dağıtımıyla hazırlanır (FROM ubuntu)

Monitoring için top, htop, journalctl kullanılır

Log analizi için grep, awk, sed gibi GNU araçları

Özetle:
Kavram	Tanım	DevOps'taki Rolü
GNU	Özgür yazılım araçları seti	Terminal komutları, scriptler, geliştirme araçları
Linux	Çekirdek (kernel)	Sunucuların çalıştığı altyapı
GNU/Linux	Tam işletim sistemi	DevOps süreçlerinin temel platformu

# UNIX nedir, neden “GNU's Not Unix” denmiş?

1. UNIX Nedir?
UNIX, 1969 yılında AT&T'nin laboratuvarlarında geliştirilen ilk modern işletim sistemlerinden biridir.

Çoklu kullanıcı, çoklu görev (multi-user, multitasking) destekleyen bir sistemdir.

Komut satırı tabanlıdır; güçlü metin işleme araçlarına sahiptir.

Sistemin çekirdeği, kabuğu (shell), yardımcı programları (ör. ls, cp, cat) vardır.

UNIX’in Özellikleri:
Hiyerarşik dosya sistemi (/home, /etc, /usr)

Her şey bir dosyadır felsefesi (cihazlar dahil)

Basit araçlar, birlikte çalıştırma (pipe |)

Kararlılık ve güvenlik

2. UNIX Neden Herkesin Kullanamadığı Bir Sistemdi?
UNIX’in Problemleri:
Ticariydi: Kaynak kodu kapalıydı, lisans ücreti gerekiyordu.

Dağıtımı sınırlıydı: Akademik çevrelerle sınırlıydı.

AT&T tarafından kontrol ediliyordu.

Bu kısıtlamalar nedeniyle özgür yazılım hareketini tetikledi.

3. GNU Neden “GNU's Not Unix”?
Anlamı:
"GNU's Not Unix", yani "GNU, Unix değildir" ifadesi, hem teknik hem felsefi bir mesajdır.

Neden Bu İsim?
Sebep	Açıklama
Özgürlük	GNU, UNIX'e benzer ama tamamen özgürdür. Kaynak kodu açık, değiştirmesi serbesttir.
Benzerlik	UNIX'e çok benzer çalışır (aynı komutlar, kabuk, yapılar), ama birebir aynı değildir.
Yasal Nedeni	UNIX bir ticari markaydı; GNU adında UNIX kelimesi geçemezdi. Bu yüzden "değiliz" demeleri gerekiyordu.

Yani:

"Biz UNIX gibi çalışıyoruz ama özgürüz, yasal olarak bağlı değiliz ve kendi topluluğumuz var."

Ayrıca isim bir kelime oyunu içerir → "GNU" bir rekürsif kısaltmadır:

GNU's Not Unix

Ek Bilgi: Linux + GNU = GNU/Linux
Linux çekirdeğini (kernel) aldığında, üzerine çalışan araçlar gerek.

GNU araçları (bash, gcc, ls, make, sed, awk, grep) bu boşluğu doldurdu.

Dolayısıyla:
GNU + Linux = GNU/Linux işletim sistemi
Bu yüzden bazı kişiler sadece “Linux” demeyin, “GNU/Linux” deyin der (özellikle Richard Stallman 😄).

Özet
Kavram	Açıklama
UNIX	1969'da Bell Labs tarafından geliştirilen ticari ve kapalı kaynaklı işletim sistemi
GNU	UNIX'e benzer ama özgür, açık kaynaklı işletim sistemi araçları projesi
GNU's Not Unix	Hem felsefi hem yasal olarak: "UNIX gibi ama özgür ve bağlı değiliz" demektir


# unix hala kullanımda mı?
UNIX hâlâ kullanımda, ama sınırlı alanlarda ve daha çok özel kurumsal/altyapı sistemlerinde.

1. UNIX Nerelerde Hâlâ Kullanılıyor?
Kullanım Alanı	Açıklama
Kurumsal Sunucular	Büyük bankalar, telekom şirketleri, eski veri merkezleri
Ağ cihazları ve altyapı	Switch, router gibi cihazların işletim sistemleri genellikle UNIX tabanlıdır
Ulaşım ve endüstriyel sistemler	Havaalanı sistemleri, tren sinyalizasyon sistemleri
Tıbbi cihazlar / laboratuvar sistemleri	Özel cihazlara gömülü işletim sistemi olarak

2. Hangi UNIX Tabanlı Sistemler Kullanılıyor?
Sistem	Açıklama
AIX	IBM’in UNIX’i – genellikle büyük sunucularda
HP-UX	Hewlett-Packard’ın UNIX sürümü – veri merkezlerinde
Solaris	Oracle’ın UNIX’i – özellikle SPARC işlemcilerle birlikte
BSD Türevleri	FreeBSD, NetBSD, OpenBSD – UNIX benzeri, açık kaynak sistemler

Not: BSD'ler teknik olarak UNIX değildir ama UNIX'e çok yakındır.

3. Neden Artık Çok Yaygın Değil?
Sebep	Açıklama
Pahalı lisans	UNIX sistemleri ücretlidir (AIX, HP-UX gibi)
Eski yapı	Daha zor yönetilir, güncellenmesi ve ölçeklendirmesi zordur
Linux’un yükselişi	Açık kaynak, esnek, güçlü topluluk desteği → birçok yerde Linux'a geçildi

4. UNIX mi, Linux mu?
Özellik	UNIX	Linux
Lisans	Ticari (genellikle kapalı kaynak)	Açık kaynak, özgür
Günümüzde kullanım	Eski sistemler, kurumsal sunucular	Her yerde: sunucular, telefonlar, IoT
Gelişim hızı	Yavaş	Çok hızlı, aktif topluluk

Sonuç:
UNIX hâlâ yaşıyor ama yeni sistemlerde çok nadir kullanılıyor.

Yerini büyük ölçüde Linux (özgür ve esnek olduğu için) aldı.

DevOps, bulut bilişim, modern web sunucuları, konteyner sistemleri (Docker, Kubernetes) artık Linux tabanlı çalışıyor.

# İşletim Sistemi (OS) Nedir?
İşletim sistemi, bilgisayarın:

Donanımı (CPU, RAM, disk vs.) ile

Yazılımları (programlar, uygulamalar)

arasındaki köprüdür.

Operating System → İşletim Sistemi

OS Ne İşe Yarar?
Görev	Açıklama
Donanımı yönetir	Bellek, işlemci, disk gibi kaynakları kontrol eder
Programları çalıştırır	Uygulamalar arasında adil kaynak dağıtımı yapar
Dosya sistemini yönetir	Dosyaların okunması/yazılması, dizin yapıları
Kullanıcı arayüzü sağlar	Terminal, masaüstü ortamı, pencere sistemi
Güvenlik ve izinler	Kim, neyi, ne kadar kullanabilir kontrol eder

Örnek İşletim Sistemleri:
Tür	Örnek
Masaüstü	Windows, macOS, Linux
Mobil	Android (Linux tabanlı), iOS (Darwin tabanlı)
Sunucu	Ubuntu Server, Red Hat, CentOS
Gömülü sistem	RTOS, VxWorks, Raspberry Pi OS

Kısaca:
OS = Operating System = İşletim Sistemi
Bilgisayarın beynidir, her şeyi o yönetir.

İşletim sistemi (OS) dünyadaki kullanım paylarına genel hatlarıyla bakacak olursak:

1. Dünyada İşletim Sistemi Kullanım Dağılımı (2025)
Toplam Cihazlar (Masaüstü, Mobil, Tablet)
Android (Linux tabanlı): ~46%

Windows: ~25%

iOS + iPadOS (Apple mobil): ~18%

macOS (masaüstü Apple): ~6%

Diğerleri (Linux masaüstü, Unix benzeri vb.): ~5% 


Mobil Cihazlarda (Akıllı Telefon & Konsol)
Android: ~72%

iOS: ~28%

Diğerleri: çok düşük (KaiOS, Samsung OS vb.) 

Masaüstü ve Dizüstü Bilgisayarlarda
Windows: ~70–72%

macOS (Apple): ~9–13%

Linux (masaüstü): ~4%

Chrome OS: ~1–2%

Diğer / Bilinmeyen: ~6–9% 


2. Sunucu & Süper Bilgisayarlar
Süper bilgisayarlarda: %100 Linux tabanlı dağıtımlar kullanılıyor 

Server (sunucu) pazarı:

Linux: ~62–65%

Windows Server: ~20–25%

Unix sistemleri (AIX, Solaris, HP‑UX): ~5–7%

BSD, özel ana bilgisayar sistemleri vb.: ~5% kadar 

Özet Tablo
Segment	OS Türü	Pazar Payı
Genel cihazlar (mobil+masaüstü+tablet)	Android	~46%
Windows	~25%
iOS/iPadOS	~18%
macOS	~6%
Diğer (Linux masaüstü, Unix vb.)	~5%

Mobil	Android	~72%
iOS	~28%

Masaüstü/Dizüstü	
Windows	~70–72%
macOS	~9–13%
Linux	~4%

Sunucular / Süper Bilgisayarlar	
Linux	~62–65% / %100 süper bilgisayar
Windows Server	~20–25%
Unix / BSD	~5–7%

3. Ana Eğilimler ve Yorum
Android, mobil dünyada bir numara; hem ucuz hem de çok sayıda cihazda yer alıyor.

Windows, masaüstü dünyasına hâkim olmaya devam ediyor.

Linux, masaüstü pazarında küçük bir paya sahip olsa da sunucu, süper bilgisayar ve bulut altyapılarında lider konumda.

Unix tabanlı ticari işletim sistemleri (AIX, HP‑UX, Solaris vb.), genelde eski kurumsal sistemlerde kalmış durumda, payları %5–7 seviyesinde.

macOS, prestijli kullanıcı tabanında (özellikle yaratıcı sektörler) güçlü ama masaüstünde Windows’ın oldukça gerisinde.

Kapanış Notu
Mobilde Android, masaüstünde Windows, sunucuda ve bilimsel sistemlerde Linux öne çıkıyor.

Unix türevleri (AIX, Solaris, BSD) daha sınırlı kurumsal ya da endüstriyel alanlarda kalmış durumda.

Gelecekte Linux’un sunucu ve masaüstü alanında daha da güçlenmesi bekleniyor; Windows 11 geçişleri ve Android’in yaygınlığı ise mobilde sürecek.

# Components of linux 

1. USER (Kullanıcı)
Sistemi kullanan kişidir.

Uygulamalarla (Applications) etkileşime girer.

Komut verir, programları çalıştırır.

2. Applications (Uygulamalar)
Kullanıcının doğrudan kullandığı programlardır. Örnek:

Web tarayıcı

LibreOffice, GIMP

Kod editörleri, oyunlar vs.

Uygulamalar, kullanıcının ihtiyaç duyduğu işleri yapar.

Bu uygulamalar, çalışmak için Shell ve Kernel ile dolaylı olarak iletişim kurar.

3. Utilities (Araçlar / Yardımcı Programlar)
Sistemin yönetimi için kullanılan temel komutlar ve araçlardır.

Örnek: ls, cp, mkdir, top, ps, df, grep vs.

Bunlar, Shell üzerinden çalıştırılır.

Kullanıcı, bu araçlarla sistemi yönetebilir.

4. Shell
Komut yorumlayıcısıdır.

Kullanıcının yazdığı komutları alır ve kernel’a iletir.

Örnek Shell türleri:

bash, zsh, sh, fish

Shell, kullanıcı ile kernel arasında bir köprü gibidir.

5. Kernel (Çekirdek)
Linux’un beyni ve en kritik kısmıdır.

Donanımı doğrudan kontrol eder.

Görevleri:

Bellek yönetimi (RAM)

Dosya sistemi yönetimi

Süreç (process) yönetimi

G/Ç (girdi/çıktı) yönetimi

Donanım sürücülerini çalıştırmak

Uygulamalardan gelen istekleri alır, donanıma iletir, sonucu geri yollar.

6. Hardware (Donanım)
Fiziksel parçalar: CPU, RAM, disk, klavye, ekran, ağ kartı vs.

Kernel, donanım üzerinde tam yetkiye sahiptir ve her şey buraya kadar iner.

Özet Akış:
USER
 ↓
Applications / Utilities
 ↓
Shell
 ↓
Kernel
 ↓
Hardware
Bu Yapının Önemi:
Linux sistemlerde bu yapı sayesinde güvenlik, stabilite ve esneklik sağlanır.

Kullanıcı, donanıma doğrudan değil, kontrollü katmanlar üzerinden ulaşır.

Her katmanın ayrı görevi vardır ve görev dağılımı net ayrılmıştır.

# Distro Nedir? (Linux Dağıtımı)
Distro, Linux çekirdeğini alıp onun çevresine:

Masaüstü ortamı (örnek: GNOME, KDE),

Paket yöneticisi (örnek: APT, YUM),

Sistem araçları (örnek: kurulum aracı, yazılım merkezi),

Varsayılan uygulamalar (örnek: tarayıcı, metin editörü)

gibi bileşenleri ekleyerek oluşturulan kullanıma hazır Linux işletim sistemidir.

Her dağıtımın amacı, hedef kitlesi ve özellikleri farklıdır:

Kimisi yeni başlayanlar için kolaydır.

Kimisi sistem yöneticileri veya sunucular içindir.

Kimisi özelleştirme meraklıları için yapılandırılabilir yapıdadır.

Popüler Linux Dağıtımları (Kısaca Açıklamalar)
Hangi Dağıtım Ne İçin Uygun?
Kullanım Amacı	Önerilen Distro
Yeni başlayan	Ubuntu, Mint
Geliştirici	Fedora, Manjaro
Sunucu	Debian, RHEL, Alma
Kurumsal/Şirket içi	RHEL, openSUSE
Hafif sistemler	Mint, Manjaro XFCE

# Open source (Açık kaynak), bir yazılımın kaynak kodunun herkese açık ve erişilebilir olduğu bir yazılım geliştirme yaklaşımıdır. 
Bu, isteyen herkesin:

Yazılımın kodunu görüntüleyebileceği,

Kodu indirip çalıştırabileceği,

Hataları düzeltebileceği veya özellik ekleyebileceği,

Kendi ihtiyaçlarına göre özelleştirebileceği anlamına gelir.

Örnek Açık Kaynak Yazılımlar
Yazılım	Açıklama
Linux	Açık kaynak işletim sistemi çekirdeği
Firefox	Açık kaynak web tarayıcı
LibreOffice	Microsoft Office alternatifi
VS Code	Microsoft destekli açık kaynak editör
Apache	Web sunucusu yazılımı

Open sources Server Applications Örnekleri
Uygulama	Açıklama
Apache HTTP Server	En popüler açık kaynak web sunucularından biri
Nginx	Hafif, hızlı ve ters proxy olarak da kullanılır
MySQL	Açık kaynak ilişkisel veritabanı sistemi
Samba	Windows sistemlerle dosya/paylaşım uyumluluğu sağlar
Redis	Bellek içi (in-memory) veritabanı ve önbellek

# FSF (Free Software Foundation) ve OSI (Open Source Initiative), özgür yazılım ve açık kaynak dünyasında çok önemli iki kuruluştur. 
Ancak amaçları ve yaklaşımları farklıdır:

FSF (Free Software Foundation) – Özgür Yazılım Vakfı
Kuruluş: 1985 yılında Richard Stallman tarafından kuruldu.

Amaç: Yazılımın kullanıcı özgürlüklerine odaklanmasını savunur.

Özgürlük tanımı: Bir yazılımın özgür olması için şu dört özgürlüğü sağlaması gerekir:

Programı herhangi bir amaçla çalıştırma özgürlüğü.

Programın nasıl çalıştığını inceleyip, onu değiştirme özgürlüğü.

Kopyalarını dağıtma özgürlüğü.

Geliştirilmiş hâllerini dağıtma özgürlüğü.

Anahtar kelime: freedom (özgürlük)
Kullandıkları lisanslar: GNU GPL (en yaygını), LGPL, AGPL vb.
FSF yazılımların ahlaki bir sorumlulukla paylaşılmasını savunur.

OSI (Open Source Initiative) – Açık Kaynak Girişimi
Kuruluş: 1998 yılında Bruce Perens ve Eric Raymond tarafından kuruldu.

Amaç: Açık kaynak yazılım modelini ticari dünyaya ve kurumlara tanıtmak.

Açık kaynak tanımı: Kaynak kodunun erişilebilir olması ve belirli kriterleri sağlaması.

10 kriteri olan Open Source Definition belgesini yayınlamıştır.

Anahtar kelime: pragmatizm (pratiklik)
OSI, etik veya özgürlükten çok kalite, işbirliği ve şeffaflık gibi avantajlara odaklanır.

FSF ve OSI Farkı
Özellik	FSF (Free Software)	OSI (Open Source)
Odağı	Kullanıcı özgürlüğü	Yazılım geliştirme modeli
Terminoloji	"Free Software" (özgür yazılım)	"Open Source" (açık kaynak)
Yaklaşım	Ahlaki ve felsefi	Pratik ve ticari
Lisans Örnekleri	GNU GPL, AGPL	MIT, Apache, BSD, GPL

# Package management tools (paket yönetim araçları),
Bir işletim sisteminde yazılım paketlerini (programları, kütüphaneleri vs.):

kurmak (install)

güncellemek (update)

kaldırmak (remove)

bağımlılıkları yönetmek (başka bir paketin çalışması için gereken diğer paketleri bulup kurmak)

gibi işlemleri kolayca yapmanı sağlayan yazılımlardır.

Bazı Popüler Paket Yönetim Araçları:
Araç İsmi	Kullanıldığı Sistem	Açıklama
apt	Debian, Ubuntu gibi	.deb paketleri yönetir
yum	Eski CentOS, RHEL	.rpm paketleri yönetir
dnf	Yeni Fedora, RHEL	yum’un gelişmiş halidir
pacman	Arch Linux	Basit ve hızlıdır
zypper	openSUSE	.rpm tabanlıdır
snap	Ubuntu (Snapcraft)	Paket + bağımlılıkları bir arada sunar
flatpak	Tüm Linux dağıtımları	Uygulamayı izole çalıştırır

Her dağıtımın bir paket deposu (repository) vardır. Yani, paketler internet üzerinden indirilecek birer raf gibi düşünülür.

Bazı paketler grafik arayüzle de yönetilebilir (örnek: Ubuntu Software Center, Synaptic vs.)

# Shell Nedir?
Shell, kullanıcı ile işletim sistemi arasında bir arayüz görevi gören bir programdır. Komutları alır, işletim sistemine iletir ve sonucu kullanıcıya gösterir.

Shell’ler ikiye ayrılır:

CLI (Command Line Interface) → Metin tabanlı (örneğin: Bash, Zsh)

GUI (Graphical User Interface) → Grafik arayüz (örneğin: Windows Explorer)

Bash Nedir?
Bash (Bourne Again SHell), en yaygın kullanılan Linux shell’idir.
sh (Bourne Shell) kabuğunun gelişmiş bir versiyonudur.

Bash’in özellikleri:

Komut geçmişi tutar

Otomatik tamamlama yapar (TAB tuşu)

Değişken tanımlama destekler

Script (betik) yazmaya uygundur

Örnek:
echo "Merhaba dünya"
Bu komut Bash üzerinden çalıştırıldığında ekrana "Merhaba dünya" yazar.

Kıyaslama:
Özellik	Shell	Bash
Tanım	Genel isim	Spesifik bir shell türü
Görev	Komutları işletim sistemine iletmek	Popüler, gelişmiş bir shell olarak bunu yapar
Örnekler	Bash, Zsh, Fish, Csh	Bash

Özet:
Shell: Komutların çalıştığı arayüzdür.

Bash: En yaygın kullanılan shell türüdür, özellikle Linux’ta.

Shell tam olarak ne yapar?
Yazdığınız komutu alır (örneğin: ls -l),

Komutu parçalar ve yorumlar,

İlgili programın (örneğin ls komutu) binary dosyasını (çalıştırılabilir dosya) bulur,

Onu çalıştırır,

Sonuçları ekrana yansıtır.


# Binary dosyası nedir?
Linux (ve Unix benzeri) işletim sistemlerinde binary dosyaları, makine tarafından çalıştırılabilir program dosyalarıdır. 
Genellikle /bin, /usr/bin, /sbin, /usr/sbin gibi dizinlerde bulunur.

Shell → Binary nasıl işler?
Sen bir terminale örneğin:
ls -l
yazdığında, bu işlem şu şekilde gerçekleşir:

Shell (örneğin bash), senin yazdığın komutu alır (ls -l).

Shell, PATH ortam değişkenine bakarak ls komutunun çalıştırılabilir (binary) dosyasını arar.

Genellikle /bin/ls dizininde bulunur.

Binary dosyası (/bin/ls) çalıştırılır, sistem çağrıları (system calls) kullanılarak dosya listesi elde edilir.

Sonuç terminalde gösterilir.

Binary dosyası nasıl görünür?
Eğer bir binary dosyasını bir metin editörüyle açarsan okunamaz, çünkü:

İnsan için değil, CPU için yazılmıştır.

ASCII karakterler değil, makine dili (ikili – binary) kodlaması içerir.

Örneğin:
cat /bin/ls
ya da
hexdump -C /bin/ls | head
Bu gibi komutlarla içeriği görebilirsin ama anlamlı olmaz. Çıktı şu tarz olur:

7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00  | .ELF............
Burada .ELF başlığı dikkat çeker. Bu, Linux sistemlerinde yaygın olan ELF (Executable and Linkable Format) formatıdır. Yani bu dosya çalıştırılabilir bir dosyadır.

Özet:
Shell, yazdığın komutu alır.

İlgili binary dosyasını bulur ve çalıştırır.

Binary dosyası işletim sistemi ve donanım tarafından yürütülür.

# Komut satırında which ls komutunu kullanarak ls komutunun hangi dosya tarafından çalıştırıldığını bulmuş oldun:

/usr/bin/ls
Bu şu anlama gelir:

Sen ls yazınca, shell (örneğin bash) bu komutun binary dosyasını /usr/bin/ls yolunda buluyor.

Bu dosya bir binary (çalıştırılabilir) dosyadır ve içinde makine diliyle yazılmış komutlar vardır.

Shell, bu binary dosyayı çalıştırarak terminale klasör içeriğini listeliyor.
