# ASCII ↔ Assembly bağlantısı biraz “bilgisayarın en temel çalışma şekli” ile ilgili. 

🔹 1. Assembly Nedir?

Assembly (Makineye Yakın Düşük Seviye Programlama Dili)

İnsanların doğrudan 10101011 gibi binary ile uğraşmasını kolaylaştırmak için çıkmış bir ara dil.

Her komut, işlemcinin anlayacağı makine kodunun neredeyse bire bir karşılığıdır.

Örn:

MOV AL, 41h   ; AL registerine 41h yükle
INT 21h       ; Ekrana yazdır


Bu kod aslında ekrana A yazdırır. Çünkü 41h → ASCII’de “A”.

Yani Assembly = İnsan için okunabilir hale getirilmiş makine kodları.

🔹 2. ASCII’nin Assembly ile İlişkisi

Bilgisayarın ekranına bir şey yazmak istediğinde, karakterlerin sayısal karşılığı (ASCII kodu) kullanılır.

Assembly dilinde sen "A" yazmazsın, 41h (hexadecimal) yazarsın.

İşlemci 41h’yi ekrana gönderir, ekran kartı “Bu 41h ASCII tablosunda A harfine karşılık geliyor” der ve A harfini gösterir.

Yani Assembly’de yazdığın şeyler çoğunlukla ASCII kodları üzerinden anlam kazanır.

🔹 3. Assembly Nerelerde Kullanılmıştır?

1950’ler – 1980’ler: İlk bilgisayarlarda yaygınca kullanıldı çünkü başka yüksek seviyeli diller yoktu.

MS-DOS programları: DOS döneminde yazılım ve oyunların çoğu Assembly ile yazıldı.

Sürücüler (driver): Donanımla doğrudan konuşmak gerektiğinde.

İşletim sistemi çekirdekleri: Linux kernel gibi sistemlerin bazı kritik kısımları.

Gömülü sistemler: Küçük çipler, mikrokontrolcüler (örneğin çamaşır makinesi, televizyon, araba beyni).

🔹 4. Hala Kullanılıyor mu?

Evet ama sınırlı:

Performans kritik kısımlar: Video codec’leri, şifreleme algoritmaları, işletim sistemi kernel optimizasyonları.

Gömülü sistemler / IoT: Küçük cihazlarda bellek ve hız kısıtlı olduğu için.

Hacking / Reverse engineering: Bir yazılımın içini anlamak için Assembly okunur.

Oyun motoru optimizasyonları: Grafik işleme için bazı kısımlar.

Ama günlük uygulama geliştirmede (web, mobil, masaüstü) artık C, Java, Python gibi diller tercih ediliyor.

🔹 5. Özet

ASCII: Karakterlerin sayısal kod karşılıkları (ör. A=65).

Assembly: Bu sayısal değerleri işlemciye anlatmanın en yakın yolu.

İlişki: Assembly → doğrudan ASCII kodlarını kullanarak karakterleri işler.

# Neden hâlâ bazı yerlerde Assembly kullanılıyor?
🔹 1. Neden Assembly Daha Hızlı?

Makine koduna en yakın dil olduğu için → Derleme sürecinde fazladan yorum/çevrim yapılmaz.

Yüksek seviyeli diller (Java, Python, C#) genellikle:

Kütüphane yükler,

Sanal makine (JVM, .NET CLR) veya yorumlayıcı kullanır,

Bellekte ek veri yapıları oluşturur.

Assembly’de ise sen işlemciye bire bir ne yapacağını söylersin.

Örn: MOV AL, 1 → “AL register’ına 1 koy” → işlemci doğrudan uygular.

Yani “arada katman” yok → daha hızlı çalışır.

🔹 2. Neden Assembly Daha Az Yer Kaplar?

Yüksek seviyeli dillerde basit bir iş bile çok satırlık kod ve kütüphane yükü getirir.

Assembly’de sadece gereken komutları yazarsın → çok küçük boyutlu program çıkar.

Örnek:

C kodu:

printf("A");


→ derlendiğinde birkaç kilobaytlık dosya çıkar çünkü printf kütüphanesi yüklenir.

Assembly kodu:

MOV AH, 0Eh
MOV AL, 'A'
INT 10h


→ derlendiğinde sadece birkaç bayt olur.

🔹 3. Neden Küçük Cihazlarda (Gömülü/IoT) Önemli?

Mikrodenetleyiciler (Arduino, STM32 gibi) genelde çok küçük bellek ve işlemci gücüne sahiptir.

Örn: 8 KB RAM, 16 MHz CPU gibi.

Böyle sınırlı bir cihazda Java/Python çalıştırmak imkânsıza yakındır.

Ama Assembly ile yazarsan:

Program 2-3 KB yer kaplar,

Cihaz 16 MHz hızda bile gayet hızlı çalışır.

🔹 4. Özet

Assembly = Minimal + Direkt işlemciye talimat

Daha hızlıdır, çünkü aracı yok.

Daha küçüktür, çünkü kütüphane şişkinliği yok.

Ama zor ve karmaşıktır, o yüzden herkes kullanmaz.

# Aynı basit işi — ekrana “A” yazdırmak — hem Java ile hem de Assembly ile yapalım.

🔹 1. Java ile “A” yazdırma
public class Main {
    public static void main(String[] args) {
        System.out.print("A");
    }
}


Derlediğinde:

Kaynak dosya (Main.java): birkaç bayt (~100 byte civarı).

Bytecode dosyası (Main.class): ~1 KB.

Çalıştırmak için: JVM (Java Virtual Machine) gerekir. JVM kendisi yüzlerce MB’lık bir yazılımdır.

Yani senin kodun basit olsa bile, çalıştırmak için kocaman bir altyapı yüklenir.

🔹 2. Assembly ile “A” yazdırma (DOS örneği)
section .text
    global _start

_start:
    mov edx, 1        ; yazılacak uzunluk
    mov ecx, msg      ; yazılacak karakter adresi
    mov ebx, 1        ; stdout (ekran)
    mov eax, 4        ; sys_write çağrısı
    int 0x80          ; sistem çağrısı (Linux)

    mov eax, 1        ; sys_exit
    int 0x80

section .data
msg db 'A'


Derlediğinde:

Çalıştırılabilir dosya (a.out): 500–800 byte civarı.

Ekstra altyapı gerekmez → doğrudan CPU + işletim sistemi syscalls ile çalışır.

🔹 3. Dosya Boyutu Karşılaştırması

Java:

.class dosyası: ~1 KB

Ama JVM olmadan çalışmaz → JVM ~50–100 MB

Assembly:

Çalıştırılabilir dosya: ~0.5 KB

İşletim sistemi kernel’inin sunduğu servis dışında başka bir şeye ihtiyaç yok

Yani aynı iş için Java yüzlerce kat daha fazla kaynak tüketir.

🔹 4. Neden Böyle?

Java → “Yaz, her yerde çalıştır” felsefesi. Taşınabilirlik için JVM gibi dev bir katmana ihtiyaç var.

Assembly → “Doğrudan donanımla konuş”. Taşınabilir değildir ama hızlı ve küçüktür.

🔹 5. Özet

Java: Kolay, taşınabilir ama şişkin (JVM + kütüphaneler).

Assembly: Zor, donanım bağımlı ama inanılmaz küçük ve hızlı.

# Assembly’nin donanım bağımlı olması ne demek?

Assembly dili doğrudan işlemcinin (CPU) anlayabileceği makine komutlarına (0 ve 1’lere) en yakın seviyede bir dildir.

Her işlemcinin (Intel, AMD, ARM, MIPS, RISC-V…) farklı komut seti mimarisi (Instruction Set Architecture – ISA) vardır.

Örneğin:

Intel/AMD’nin kullandığı x86 / x86-64 komut seti

Telefonlarda, gömülü cihazlarda yaygın olan ARM komut seti

Akademik/prototip ortamlarda MIPS

Dolayısıyla Intel için yazılmış assembly kodu, ARM işlemcide çalışmaz. Çünkü talimatlar farklıdır.

Bu yüzden assembly donanım bağımlıdır:

Yazdığınız program sadece hedeflediğiniz CPU’nun komut setinde çalışır.

Başka bir donanım için yeniden yazmanız gerekir.

Yüksek seviyeli diller (Java, C, Python) neden bağımsız?

Java kodu → bytecode’a çevrilir, sonra JVM farklı platformlarda bunu çalıştırır.

C/C++ kodu → derleyici tarafından hedef donanım için assembly’ye çevrilir (ama siz kodu değiştirmeden derleyici bunu halleder).

Python → yorumlayıcı üstünde çalışır.

Bu yüzden yüksek seviyeli dillerle yazılan kodu farklı donanımlarda çok az değişiklikle çalıştırabilirsiniz. Ama assembly’de donanım değişirse sıfırdan yeniden yazmanız gerekir.

Örnek:

Aynı işlemi farklı işlemcilerde assembly ile yazalım:

x86 Assembly (Intel PC):

MOV AX, 5
ADD AX, 10


ARM Assembly (telefon işlemcisi):

MOV R0, #5
ADD R0, R0, #10


İkisi aynı işi yapıyor (5 + 10), ama komut adları ve yazım tamamen farklı.

# 1. Assembly → Makine Kodu İlişkisi

Bilgisayar donanımı sadece makine kodunu (binary, 0 ve 1) anlayabilir.

Assembly dediğimiz şey makine kodunun insana okunabilir hali (ör. MOV AX, 1 gibi).

Yani son aşamada her şey makine koduna çevrilmek zorunda.

Ama her dil önce assembly’ye çevrilmek zorunda değildir.

🔹 2. Dillerin Derlenme / Çalışma Yöntemleri
C / C++ (Derlenen diller)

C kodu → derleyici → Assembly → Makine kodu (binary, .exe).

Sonuçta senin bilgisayarın işlemcisine özel bir dosya oluşur.

Dolayısıyla derlenmiş diller genellikle assembly aşamasından geçer (derleyici arkada assembly üretebilir veya direkt binary üretebilir).

Java, C#, Python (Ara katmanlı veya yorumlanan diller)

Java:

Java kodu → Bytecode (platformdan bağımsız ara kod).

JVM (Java Virtual Machine) bunu alır, çalıştırırken ya yorumlar ya da JIT Compiler ile anında makine koduna çevirir.

Yani Java her platformda aynı bytecode ile çalışır, assembly’ye senin gözünden çevrilmez.

Python:

Python kodu → Bytecode (.pyc) → Python yorumlayıcısı (CPython) bunu satır satır çalıştırır.

Yine en sonda CPU’ya makine kodu gider ama doğrudan assembly yazılmaz.

C# (.NET):

C# → IL (Intermediate Language) → CLR (Common Language Runtime) → JIT Compiler → Makine kodu.

Yorumlanan Diller (JavaScript, PHP gibi)

Kaynak kod → Direkt yorumlayıcı (interpreter) → Çalışma anında satır satır makine koduna çevirilir.

Assembly dosyası oluşturulmaz.

🔹 3. Sonuç

Her şey en sonunda makine koduna dönüşür (aksi mümkün değil).

Ama her dil önce assembly’ye dönüşmez:

C/C++ gibi diller çoğunlukla assembly üzerinden gider.

Java, Python, C# gibi diller genellikle bytecode → JIT → makine koduna gider.

JavaScript, PHP gibi diller doğrudan yorumlanır.

Kısacası:

C/C++ → Derlenmiş assembly + binary.

Java/C# → Bytecode → JVM/CLR → JIT compiler ile makine kodu.

Python/JS → Bytecode veya direkt yorum → makine kodu.

# Dillerin Genel Ayrımı

Evet, diller genellikle üç ana kategoriye ayrılır:

🔹 Derlenen diller (Compiled languages)

Kod → Derleyici (compiler) → Makine kodu (binary).

Örn: C, C++, Go, Rust

Çok hızlı çalışırlar çünkü direkt işlemciye özel makine kodu üretilir.

🔹 Yorumlanan diller (Interpreted languages)

Kod → Yorumlayıcı (interpreter) → Satır satır çalıştırılır.

Örn: Python, JavaScript, PHP

Yavaş olabilir çünkü her satırda çeviri yapılır.

🔹 Ara katmanlı (Intermediate / VM-based languages)

Kod → Bytecode (platformdan bağımsız ara kod) → Sanal Makine (JVM, CLR) → Makine kodu.

Örn: Java, C#, Kotlin

Hem taşınabilirlik sağlar hem de JIT (Just-in-Time Compiler) sayesinde hız kazanır.

2. Neden ara katman var?

Ara katman (bytecode) kullanılmasının birkaç sebebi var:

Taşınabilirlik:
Java’nın sloganı: “Write once, run anywhere”.
(Bir kere yaz, her yerde çalıştır.)
→ Çünkü bytecode her cihazda aynı, sadece JVM farklı.

Güvenlik:
JVM/CLR kodu kontrol eder (hafıza taşmaları, tehlikeli işlemler).
Bu yüzden Java, C# genelde daha güvenlidir.

Performans optimizasyonu:
JIT Compiler çalışma anında kodu makine koduna çevirir, o anki cihazın işlemcisine özel hızlandırmalar yapar.

3. Neden direkt makine diline çevrilmiyor?

Platform bağımlılığı:
C++ derlersen, Windows için ayrı, Linux için ayrı, ARM için ayrı binary çıkarman gerekir.
Java’da buna gerek yok → bytecode her yerde aynı.

Esneklik:
Yorumlanan veya ara katmanlı dillerde programı çalışırken değiştirmek, hata ayıklamak daha kolay.

Ek güvenlik katmanı:
Direkt makine kodu CPU’ya emir verir, yanlışsa sistemi bozabilir.
JVM/CLR gibi sanal makineler bu riskleri azaltır.

Özet:

Derlenen = hızlı ama platforma bağımlı.

Yorumlanan = yavaş ama esnek.

Ara katmanlı = ikisinin ortası (hem taşınabilir hem optimize edilebilir).

# A sınıfı IP adresi ile ilgili her maddeyi tek tek açıklayayım:

🔹 1) “A Sınıfı Ağ adresi 1 bayt uzunluğundadır, ilk bit her zaman 0'dır”

IPv4 adresleri 32 bit uzunluğundadır (4 bayt = 4×8 bit).

Bu 32 bit içinde, ilk kısım (ilk bayt) IP’nin hangi sınıfa ait olduğunu belirler.

A sınıfında: İlk 8 bit (1 bayt) ağ adresini, kalan 24 bit host adresini temsil eder.

Ayrıca A sınıfı adreslerin ilk biti her zaman 0’dır → bu, “ben A sınıfıyım” demek için kullanılan işarettir.

🔹 2) “Maksimum 2^7 = 128 A Sınıfı ağ oluşturulabilir”

İlk bayt 8 bit uzunluğunda.

Ama A sınıfında ilk bit sabit (0) olduğu için geriye sadece 7 bit kalır.

7 bit ile oluşturulabilecek ağ sayısı: 2^7 = 128.
Yani A sınıfında 128 farklı ağ tanımlanabilir.

🔹 3) “Maksimum 2^24 = 16.777.214 ana bilgisayar (ayrılmış 2 adres hariç)”

A sınıfında:

1 bayt → ağ adresi.

3 bayt (24 bit) → host (bilgisayar, cihaz) adresleri için.

24 bit ile oluşturulabilecek adres sayısı: 2^24 = 16.777.216.

Fakat her ağda:

1 adres “network ID” için ayrılır (örneğin 10.0.0.0).

1 adres “broadcast” için ayrılır (örneğin 10.255.255.255).
Bu yüzden kullanılabilir host sayısı: 16.777.214.

🔹 4) “İlk bit her zaman 0'dır, ardından 00000000 = 0, 01111111 = 127”

İlk bayt 8 bit’tir.

İlk bit her zaman 0 olduğu için kalan 7 bit 0–127 arasında değer alabilir:

00000000 → 0

01111111 → 127

🔹 5) “00000000 ve 01111111 adresleri sırasıyla varsayılan rota ve sorun giderme için ayrılmıştır”

İlk bayt = 00000000 → yani 0.x.x.x adresleri. Bu adresler ağlarda default route (varsayılan yol) testlerinde kullanılır.

İlk bayt = 01111111 → yani 127.x.x.x adresleri. Bu adresler loopback (geri dönüş / troubleshooting) için ayrılmıştır.

En bilinen örneği: 127.0.0.1 = localhost (kendi bilgisayarını test etmek için).

🔹 6) “Yani A Sınıfı ağ adresleri 1-126 ile başlar”

0 ve 127 özel amaçlara ayrıldığı için kullanılamaz.

Geriye 1’den 126’ya kadar kalan ilk bayt değerleri kalır.
Yani:

1.0.0.0 – 126.0.0.0 arası IP blokları → A sınıfıdır.

Özet:

A sınıfı, çok büyük ağlara ayrılmıştır (her ağda milyonlarca host olabilir).

İlk baytı 1–126 arasında olan IP adresleri A sınıfına aittir.

0.x.x.x ve 127.x.x.x özel amaçlıdır.

# Özel amaç için (0 ve 127) için ayrılmış host sayısı 2*16.777.214 mi?


🔹 1) A sınıfında ağ sayısı hesabı

İlk bayt: 8 bit

İlk bit = 0 → geriye 7 bit kaldı → 2^7 = 128 ağ

Ama 0.x.x.x ve 127.x.x.x blokları özel amaçlı:

0.0.0.0/8 → varsayılan rota (default route) / “bu ağ” anlamında

127.0.0.0/8 → loopback (kendine bağlanma, test için)

Bu yüzden kullanılabilir ağ sayısı 128 – 2 = 126 olur.

🔹 2) Ayrılan host sayısı meselesi

Her kullanılabilir ağ → 16.777.214 host verir.

Ama 0.x.x.x ve 127.x.x.x zaten hiç host için kullanılmaz.
Yani onlar baştan komple rezerve edilmiştir.

Dolayısıyla “2 × 16.777.214 host ayrıldı” diye saymayız.
Çünkü host ayrımı tek tek yapılmaz, tüm ağ bloğu özel olarak işaretlenmiştir.

🔹 3) Özet

Toplam: 128 ağ × 16.777.214 host = ~2.1 milyar host

Kullanılabilir: 126 ağ × 16.777.214 host = ~2.1 milyar host (ama biraz daha az)

0.x.x.x ve 127.x.x.x blokları komple ayrıldığı için oradaki hostlara hiç ulaşamayız.

Yani aslında özel amaç için ayrılan host sayısını hesaplamıyoruz, çünkü 2 ağ bloğu baştan kullanılmaz diye kabul ediliyor.

# Localhost nedir?

localhost bir özel isimdir (hostname).

Bilgisayarının kendi kendisini işaret eder.

Yani sen tarayıcıya http://localhost yazdığında, aslında "bu isteği kendi bilgisayarıma gönder" diyorsun.

🔹 127.0.0.1 nedir?

Bu da loopback IP adresidir (IPv4 için).

localhost isminin çözülmüş halidir.

Yani localhost yazınca → işletim sistemi hosts dosyasında → 127.0.0.1’e çevirir.

localhost ve 127.0.0.1 genelde aynı şeydir.

🔹 Neden kullanıyoruz?

Spring Boot projeni çalıştırdığında uygulama kendi bilgisayarında bir server açar.
Mesela:

Tomcat started on port(s): 8080


Bu demek ki:

IP: 127.0.0.1 veya localhost

Port: 8080

URL: http://localhost:8080

Yani senin uygulaman dış dünyaya değil, kendi bilgisayarına hizmet veriyor.

🔹 127.0.0.1 dışında başka loopback var mı?

Evet

127.0.0.0/8 bloğu tamamen loopback için ayrılmıştır.

Yani 127.0.0.2, 127.1.1.1 vs. hepsi yine senin bilgisayarını gösterir.

Ama en çok 127.0.0.1 kullanılır.

🔹 Özet

localhost = bilgisayarın kendi ismi.

127.0.0.1 = aynı iş, ama sayısal adres (loopback).

Spring projelerinde http://localhost:8080 → aslında http://127.0.0.1:8080.

# “localhost – private IP – public IP” üçlüsünü karıştırmaman çok önemli.
🔹 1. Localhost (127.0.0.1)

Senin bilgisayarının kendi kendisine konuşması.

Yani dışarıya hiç çıkmadan, içeride kendi CPU/RAM/OS üzerinde döner.

Örnek: http://localhost:8080 → Spring Boot uygulaman kendi bilgisayarında açılır.

Bu adresi sadece sen görebilirsin. Ağdaki başka kimse bu adrese ulaşamaz.

🔹 2. Private IP (örnek: 192.168.1.101)

Modem/router, LAN’daki (ev/ofis içindeki) cihazlara dağıttığı IP’dir.

Örnek: Bilgisayar → 192.168.1.101, Telefon → 192.168.1.102.

Bu adresler dışarıdan internette görünmez, sadece yerel ağda geçerlidir.

Yani aynı Wi-Fi’deki başka biri http://192.168.1.101:8080 yazarsa, senin bilgisayarında çalışan Spring Boot uygulamasına bağlanabilir (güvenlik izinleri açıksa).

🔹 3. Public IP (örnek: 78.173.11.70)

ISS (Türk Telekom, Superonline, vs.) sana dış dünyada görünmen için verdiği adrestir.

İnternete çıktığında, Google, YouTube, ChatGPT vb. siteler seni bu IP’den görür.

Dışarıdaki herkesin gördüğü tek adres budur.

Ama dikkat: Genelde modem NAT yapar → evde 5 cihazın olsa bile dışarıda hepsi tek public IP üzerinden görünür.

Aralarındaki farkı özetle:
Tür	Kime ait?	Kim görebilir?	Örnek
localhost	Sadece senin bilgisayarın	Sadece sen	127.0.0.1
private IP	Ev/iş ağındaki cihaz	Aynı LAN’daki cihazlar	192.168.x.x
public IP	Modem/ISS üzerinden dış dünya	Tüm internet	78.173.x.x
🔹 Örnek senaryo

Sen Spring Boot uygulamasını açtın: http://localhost:8080
→ Sadece sen görebilirsin.

Senin bilgisayarının LAN IP’si: 192.168.1.101
→ Aynı Wi-Fi’deki arkadaşın http://192.168.1.101:8080 ile görebilir.

Sen modem port forwarding ayarı yaparsan, public IP üzerinden de çalışır:
→ http://78.173.11.70:8080 → dışarıdaki herkes bağlanabilir.

# RFC 1918 ve özel (private) IP adresi aralıkları nedir?
RFC 1918, 1996 yılında yayınlanan bir standarttır ve özel (private) IP adresi aralıklarını tanımlar.
Günlük Hayat Benzetmesi:
javaŞehir İçi Telefon Numaraları vs Uluslararası Numaralar:

Public IP = +90 532 123 4567 (Dünyanın her yerinden aranabilir)
Private IP = Dahili 1234 (Sadece şirket içinde geçerli)

Ofiste "1234'ü ara" dediğinde herkes anlar
Dışarıdan "1234" dersen anlamsız!
Özel IP Aralıkları:
javaRFC 1918 Tanımlı Private IP Aralıkları:

┌──────────┬────────────────────────┬────────────────┬──────────────┐
│  Class   │      IP Aralığı        │   CIDR         │  Host Sayısı │
├──────────┼────────────────────────┼────────────────┼──────────────┤
│ Class A  │ 10.0.0.0 -             │ 10.0.0.0/8     │ 16,777,216   │
│          │ 10.255.255.255         │                │              │
├──────────┼────────────────────────┼────────────────┼──────────────┤
│ Class B  │ 172.16.0.0 -           │ 172.16.0.0/12  │ 1,048,576    │
│          │ 172.31.255.255         │                │              │
├──────────┼────────────────────────┼────────────────┼──────────────┤
│ Class C  │ 192.168.0.0 -          │ 192.168.0.0/16 │ 65,536       │
│          │ 192.168.255.255        │                │              │
└──────────┴────────────────────────┴────────────────┴──────────────┘

Neden Private IP Kullanılır?
1. IPv4 Adres Tükenmesi Problemi:
IPv4 Toplam Adres: 2^32 = 4,294,967,296 adres
Dünya Nüfusu: ~8 milyar insan
IoT Cihazlar: Milyarlarca

Problem: Her cihaza public IP vermek imkansız!

Çözüm: Private IP + NAT

2. Güvenlik:
Public IP (88.245.22.19):
- İnternet'ten direkt erişilebilir
- Hack denemeleri
- Port taramaları
- DDoS saldırıları

Private IP (192.168.1.100):
- İnternet'ten direkt erişilemez
- Modem/Firewall arkasında korumalı
- Dış dünya bu IP'yi göremez

3. Maliyet:
Public IP:
- ISP'den kiralanır
- Aylık ücret
- Her cihaz için ayrı maliyet

Private IP:
- Ücretsiz
- İstediğin kadar kullan
- Sadece bir public IP yeter

Gerçek Hayat Senaryosu:
Ev Ağı Örneği:
İNTERNET (Public)
    │
    │ Public IP: 88.245.22.19
    ▼
┌─────────────────┐
│   MODEM/ROUTER  │ NAT Yapıyor
│  192.168.1.1    │
└─────────────────┘
    │
    ├── 192.168.1.10  (Laptop)
    ├── 192.168.1.20  (Telefon)
    ├── 192.168.1.30  (Tablet)
    ├── 192.168.1.40  (Smart TV)
    └── 192.168.1.50  (Akıllı Buzdolabı)

Tek public IP (88.245.22.19) → 5 cihaz çalışıyor!

Şirket Ağı Örneği:
ŞİRKET AĞI:
10.0.0.0/8 → Ana network
├── 10.1.0.0/16 → İstanbul Ofisi (500 çalışan)
├── 10.2.0.0/16 → Ankara Ofisi (300 çalışan)
└── 10.3.0.0/16 → İzmir Ofisi (200 çalışan)

Her ofis kendi private ağında çalışıyor
Dışarıya tek public IP ile çıkıyorlar
NAT (Network Address Translation) ile Çalışma:
Private → Public Dönüşümü:
İç Ağdan İnternet'e:
┌─────────────────────────────────────────────────────────┐
│ Private Network              NAT              Internet  │
├─────────────────────────────────────────────────────────┤
│ 192.168.1.10:5000  →  Router  →  88.245.22.19:12345    │
│ 192.168.1.20:6000  →  Router  →  88.245.22.19:23456    │
│ 192.168.1.30:7000  →  Router  →  88.245.22.19:34567    │
└─────────────────────────────────────────────────────────┘

Router NAT Table:
┌────────────────────┬──────────────────────┐
│ Private            │ Public               │
├────────────────────┼──────────────────────┤
│ 192.168.1.10:5000  │ 88.245.22.19:12345   │
│ 192.168.1.20:6000  │ 88.245.22.19:23456   │
│ 192.168.1.30:7000  │ 88.245.22.19:34567   │
└────────────────────┴──────────────────────┘
İnternet'ten Cevap Geldiğinde:
javaGoogle → 88.245.22.19:12345
Router NAT Table'a bakıyor: "Bu 192.168.1.10:5000'e gitmeli"
Router → 192.168.1.10:5000

Dış dünya 192.168.1.10'u hiç görmedi!
Private IP'nin Özellikleri:
Avantajları:
java1. IPv4 Adres Tasarrufu:
   - Milyarlarca cihaz aynı private IP'leri kullanabilir
   - Örn: Tüm evlerde 192.168.1.1 kullanılabilir

2. Güvenlik:
   - İnternet'ten direkt erişilemez
   - Firewall koruması

3. Esneklik:
   - İstediğin gibi yapılandır
   - ISP'den bağımsız

4. Maliyet:
   - Ücretsiz
   - Sınırsız kullanım

Dezavantajları:
1. Direkt İnternet Erişimi Yok:
   - NAT gerekli
   - Router şart

2. Peer-to-Peer Zorlukları:
   - İki private IP direkt konuşamaz
   - Port forwarding gerekebilir

3. Server Hosting Zorluğu:
   - Dışarıdan erişilecek server için port açmak lazım

Hangi IP Aralığı Ne Zaman Kullanılır?
10.0.0.0/8 - Büyük Organizasyonlar:
Çok sayıda cihaz/subnet gerektiğinde
Büyük şirketler, üniversiteler, veri merkezleri

Örnek:
10.1.0.0/16  → İstanbul kampüsü
10.2.0.0/16  → Ankara kampüsü
10.3.0.0/16  → İzmir kampüsü
...
10.255.0.0/16 → 255. kampüs (teorik)
172.16.0.0/12 - Orta Boy Organizasyonlar:
java// Orta ölçek şirketler
Şubeli firmalar, orta boy veri merkezleri

Örnek:
172.16.0.0/24  → Muhasebe departmanı
172.16.1.0/24  → IT departmanı
172.16.2.0/24  → Satış departmanı
192.168.0.0/16 - Küçük Ağlar:
java// En yaygın kullanım
Ev ağları, küçük ofisler, modemler

Örnek:
192.168.1.0/24 → Çoğu ev modemi
192.168.0.0/24 → Bazı modemler
192.168.2.0/24 → Guest network

Özet:
RFC 1918 Private IP'ler:

İnternet'te yönlendirilmez
Her ağda aynı IP'ler kullanılabilir
NAT ile public IP'ye çevrilir
IPv4 adres kıtlığına çözüm
Güvenlik sağlar
Ücretsizdir

Pratikte: Evdeki/ofisteki tüm cihazlar private IP kullanır, router NAT yaparak hepsini tek public IP ile internete bağlar.

# 1) Private IP dışında kalanlar → Public IP midir?

Evet 

Private IP blokları (10.x.x.x, 172.16–31.x.x, 192.168.x.x) ve birkaç özel rezerv (örneğin 127.0.0.1 → localhost) internet üzerinde yönlendirilmez.

Geri kalan tüm IP adresleri → Public (genel) IP’dir ve internette benzersiz olmalıdır.

🔹 2) Public IP’yi kim veriyor?

Hiyerarşi şöyle işler:

ICANN / IANA → Dünya çapında IP adreslerini yönetir.

RIR (Regional Internet Registry) → Bölgesel dağıtım yapar.

RIPE NCC → Avrupa / Türkiye

ARIN → Kuzey Amerika

APNIC → Asya-Pasifik …

ISP (İnternet Servis Sağlayıcı, mesela Türk Telekom, Superonline, Vodafone) → IP bloklarını müşterilerine dağıtır.

Senin modemine → ISP tarafından bir public IP atanır.

🔹 3) Public IP sabit mi, değişiyor mu?

Eğer statik IP satın almadıysan → modemine dinamik (değişken) IP atanır.

Bu IP genelde modemi kapatıp açtığında veya belirli aralıklarla değişir.

O yüzden bugün 88.245.22.19 görürsün, yarın başka bir public IP alabilirsin.

Ama “private IP” (192.168.x.x) genellikle modem içindeki DHCP havuzuna göre hep aynı kalır (mesela bilgisayarına sürekli 192.168.1.101 verir).

🔹 4) Özet

Private IP → sadece yerel ağda kullanılır, dünyada tekrar edebilir.

Public IP → internette benzersizdir, ISP tarafından atanır.

Modeminin public IP’si genelde dinamik olduğu için değişebilir.

# IP Routing (Yönlendirme)

Routing: Bir paketin kaynak IP’den hedef IP’ye giderken hangi yol üzerinden gitmesi gerektiğini bulma işidir.

Bunu yapan cihaz: Router (Yönlendirici).

Router’ın içinde Routing Table (Yönlendirme Tablosu) bulunur.

Örneğin:

Senin bilgisayarın 192.168.1.10, YouTube’un IP’si 142.250.190.78.

Sen paketi modemine yollarsın → modem “Routing Table”a bakar → “Bu IP’ye internet üzerinden gitmeliyim” diyerek ISP’ye yollar.

ISP’nin router’ları da aynı şekilde bakarak en iyi yolu seçer.

🔹 Routing Türleri

1. Statik Routing

Yönetici, yönlendirme tablosuna elle yollar yazar.

Örn: ip route add 192.168.2.0/24 via 192.168.1.1

Avantajı: Basit, küçük ağlarda kullanılabilir.

Dezavantajı: Ağ büyüyünce yönetmek imkânsız olur (elle her şeyi değiştirmek gerek).

2. Dinamik Routing

Router’lar kendi aralarında routing protokolleri ile konuşur, en iyi yolları otomatik öğrenir.

Avantaj: Büyük ağlarda esneklik, otomatik güncelleme.

Dezavantaj: CPU, RAM kullanır; yanlış ayar yapılırsa döngüye girebilir.

🔹 Dinamik Routing Protokolleri
RIP (Routing Information Protocol)

En eski protokollerden biri.

Distance Vector algoritması kullanır.

“En kısa yol”u sadece hop sayısı (kaç router geçileceği) üzerinden hesaplar.

Maksimum 15 hop → yani büyük ağlarda kullanılamaz.

Avantaj: Basit.

Dezavantaj: Yavaş, ölçeklenmez.

OSPF (Open Shortest Path First)

Link State algoritması kullanır.

“En iyi yol”u band genişliği, gecikme, maliyet gibi metriklerle hesaplar.

Büyük kurumsal ağlarda yaygın.

RIP’ten çok daha akıllı ve hızlıdır.

Router’lar, birbirlerine “topoloji haritası” gönderir, herkes aynı ağ haritasına sahip olur.

BGP (Border Gateway Protocol) → Internet’in Omurgası

İnternet servis sağlayıcıların birbirine bağlanmasında kullanılan protokol.

“Benim elimde şu IP blokları var” diye duyuru yapar.

İnternetin bugünkü hali BGP olmasa olmazdı.

BGP olmasa Google, YouTube, Facebook’a giden yollar bilinmezdi.

🔹 Yönlendirmede Önemli Kavramlar

Default Route (Varsayılan Yol)

Router “hangi IP’ye gideceğini bilmiyorsa” paketi bu yola yollar.

Ev modemindeki varsayılan yol: ISP.

Administrative Distance (AD)

Aynı hedefe birden fazla yol varsa, hangi kaynağın güvenilir olduğunu seçmek için kullanılır.

Örn: Statik route AD=1, OSPF AD=110 → router önce statik route’a güvenir.

Metric (Metrik)

Protokoller yolu değerlendirirken farklı metrikler kullanır.

RIP → hop sayısı, OSPF → cost, BGP → politika.

CIDR (Classless Inter-Domain Routing)

IP’lerin sınıflara (A, B, C) sıkışmadan, /prefix şeklinde yazılması.

Örn: 192.168.1.0/24.

Route Aggregation (Özetleme)

Birden fazla alt ağı tek bir daha büyük blokla özetleme.

Router tablolarını küçültür.