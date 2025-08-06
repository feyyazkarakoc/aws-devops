
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
