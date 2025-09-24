
# Watch, Star, ve Fork butonları çok sık karşımıza çıkar:

1. Star → Beğenmek, favorilere eklemek
Star = "Bu projeyi beğendim, ilgimi çekti."

Ne işe yarar?
Projeyi takip etmek zorunda kalmadan beğenmiş olursun.
Daha sonra profilinden kolayca erişebilirsin.
Proje sahibine "bu proje güzel" mesajı verir.
GitHub algoritmaları daha çok kişiye önerebilir.
Örnek:
Sen feyyazkarakoc/uyku-hesaplayici diye bir Java projesi yazdın.
Ben ilgimi çektiği için Star verdim.
Sen bunu profilinde görebilirsin: X kişi star verdi.

2. Watch → Proje bildirimlerini almak
Watch = "Bu projede bir şey değişirse haberim olsun."

Ne işe yarar?
Yeni issue, pull request, release gibi gelişmelerden e-posta/uyarı alırsın.
Aktif takip içindir (star gibi "beğen" değil, bildirim almak için).
Kullanım:
Özellikle katkı yaptığın veya dikkatle izlediğin bir projeye Watch konur.

Watch ayarları:

Not watching: Sadece seni ilgilendiren şeyler
Watching: Her şeyin bildirimi gelir
Ignore: Hiçbir bildirim gelmez

3. Fork → Kendi GitHub hesabına kopyalamak
Fork = Başkasının GitHub reposunu al, kendi hesabına kopyala

Ne işe yarar?
Projenin bağımsız bir kopyasını oluşturur.
Sen artık bu projeyi kendi içinde değiştirebilir, geliştirip GitHub’a push edebilirsin.
Ana projeye zarar vermez.
İstersen değişikliklerini pull request ile ana projeye teklif edebilirsin.

Örnek:
Senin projen: feyyazkarakoc/hava-tahmini-uygulamasi

Ben fork yaparsam:
→ chatgptuser/hava-tahmini-uygulamasi diye kendi hesabımda bir kopyası olur
Orada deney yaparım, sonra istersen sana katkı sunmak için pull request gönderirim.

Hepsi Arasındaki Farklar
Özellik	Açıklama
Star	Projeyi beğen, favori listene al
Watch	Projede olan bitenden haberdar ol (bildirim)
Fork	Projenin kendi hesabında bir kopyasını oluştur

Tipik Kullanım Sırası:
Star ver → “Bu güzelmiş” diye işaretle
Watch yap → “Değişiklik olursa bilmek istiyorum”
Fork et → “Kodla oynayacağım, katkı yapabilirim”

 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

# GitHub’da SSH Key ve Token Oluşturma Nedir?
GitHub’a iki farklı şekilde bağlanabilirsin:

1. HTTPS + Personal Access Token (PAT)
Eskiden kullanıcı adı + şifre ile erişiliyordu.
Artık şifre yerine Token kullanılıyor.

2. SSH Anahtar Çifti (ssh key)
Parola girmeden, daha güvenli bir şekilde terminalden bağlantı sağlar.

SSH Key Oluşturma (SSH ile GitHub’a Bağlanma)
A. Komut:
ssh-keygen
Bu komut, senin bilgisayarında bir anahtar çifti üretir:

id_rsa → gizli anahtar (private key)

id_rsa.pub → herkese açık anahtar (public key)

B. Adımlar:
Terminale ssh-keygen yaz → Enter’lara basarak geç.

Anahtarlar ~/.ssh klasörüne kaydedilir.

Şu komutla açık anahtarı kopyala:
cat ~/.ssh/id_rsa.pub
GitHub → Settings → SSH and GPG Keys → New SSH key
Açılan kutuya anahtarı yapıştır ve kaydet.

C. Artık:
GitHub’a parola yazmadan bağlanabilirsin:
git@github.com:USERNAME/REPO.git

Personal Access Token (PAT) Nedir?
GitHub, artık şifre yerine Token kullanmanı istiyor.

Örneğin:
git clone https://github.com/USERNAME/REPO.git
Seni şu şekilde sorularla karşılar:
Username:  feyyaz
Password:  (buraya GitHub şifresi yerine Token girilir!)

Kısa Özet:
Bağlantı Türü	Kullanım	Güvenlik	Şifre İster mi?
HTTPS + Token	https://github...	Orta	Evet (Token girilir)
SSH	git@github...	Yüksek	Hayır (Anahtarla giriş)

Bonus Örnek:
SSH ile klonlamak:
git clone git@github.com:USERNAME/REPO.git
HTTPS + Token ile klonlamak:
git clone https://github.com/USERNAME/REPO.git
Parola yerine GitHub → Personal Access Token kısmından aldığın değeri girersin.

# Senin komutlarına ve çıktına göre:

Bir klasörde (D:\AWS DEVOPS\CLOUD - AWS) zaten bir Git repository var.

git remote -v çıktısına göre bu klasör GitHub’daki şu uzak repoya bağlı:
https://github.com/feyyazkarakoc/cloud-aws-notlar.git
Bu bağlantı HTTPS bağlantısı kullanıyor.

Peki "PAT mi kullanılıyor?" sorusunun cevabı:
Eğer bu uzak repo'ya HTTPS ile push yapabiliyorsan, GitHub senden artık şifren yerine PAT (Personal Access Token) ister.
Ama sen bu token’ı her push’ta elle yazmıyorsan, şu iki şeyden biri oluyordur:

1. Credential Manager (Windows) otomatik hatırlıyor olabilir
İlk kez git push yaparken kullanıcı adını ve PAT token’ını girmişsindir.

Windows Git Credential Manager bu bilgiyi kaydetmiştir.

Sonraki push işlemlerinde senden istemez çünkü otomatik kullanır.

Denemek istersen:
git credential-manager-core list
ya da
git config --global credential.helper
2. Senin yerine HTTPS yerine SSH kullanılmış olabilirdi — ama bu örnekte kullanılmamış
Senin bağlantın:
https://github.com/... → Bu HTTPS kullanıyor.

Eğer bağlantın şöyle olsaydı:
git@github.com:... → Bu SSH kullanıyor olurdu.

PAT Otomatik mi giriliyor?
Evet, bir kez girip kaydettiysen, Git o token’ı arka planda otomatik kullanır.
Eğer hiç token girmediysen ama push yapabiliyorsan, o zaman bir SSH anahtarı kullanıyor olabilirsin (muhtemelen sen değil, kurs hocan ayarlamıştır).

Kendini test et:
Aşağıdaki komutu çalıştır:
git config --list --show-origin
Çıktıda şuna benzer bir şey var mı bak:
credential.helper=manager-core
Bu varsa, Git push sırasında kullanıcı adı + PAT bilgini otomatik hatırlıyor demektir.

Sonuç:
Durum	Anlamı
https:// bağlantısı	HTTPS üzerinden erişiyorsun
Push yapabiliyorsan	Ya token girdin, ya da Git bunu hatırlıyor
Her push'ta şifre istemiyorsa	Token (PAT) bir kere girildi ve Git bunu hatırlıyor

# Çıktıya göre senin bilgisayarında:
file:C:/Program Files/Git/etc/gitconfig credential.helper=manager
görünüyor. Bu satır şunu gösteriyor:

Senin Git kurulumun "Credential Manager" kullanıyor.
Bu da şu demek:

Daha önce git push komutunu ilk kez çalıştırdığında GitHub kullanıcı adını ve şifre yerine PAT (Personal Access Token)'i girmişsin.

Windows Git Credential Manager bu bilgiyi kaydetmiş.

Artık her push’ta otomatik olarak o PAT’i kullanıyor, sana sormuyor.

Özetle:
Soru	Cevap
Push yaparken ne kullanılıyor?	Personal Access Token (PAT)
Neden her seferinde sormuyor?	Çünkü credential.helper=manager ile bu bilgi kaydedilmiş
SSH mi kullanılıyor?	Hayır. Çünkü bağlantı HTTPS (https://github.com/...)

Ekstra bilgi: PAT nerede kayıtlı?
Windows’ta şuraya gidebilirsin:
Denetim Masası → Kullanıcı Hesapları → Kimlik Bilgileri Yöneticisi (Credential Manager)

Orada git:https://github.com gibi bir kayıt görebilirsin.

# SSH'nin açılımı:

SSH = Secure Shell

Ne işe yarar?
SSH, internet üzerinden bir bilgisayara güvenli (şifreli) şekilde:

Bağlanmanı,

Komut göndermeni,

Dosya transferi yapmanı sağlar.

Git ile ne alakası var?
GitHub’a ya da başka bir Git sunucusuna SSH ile bağlanırsan:

Her seferinde kullanıcı adı / şifre / PAT girmene gerek kalmaz.

Bir kere anahtar çifti (SSH key) oluşturursun → public key GitHub’a eklenir, private key bilgisayarında kalır.

Bundan sonra otomatik olarak tanınır.

SSH ile bağlantı örneği:
git@github.com:USERNAME/REPO.git
Bu yapı görünüyorsa SSH ile bağlanıyorsun demektir.
Eğer şöyle görünüyorsa:
https://github.com/USERNAME/REPO.git
Bu HTTPS bağlantısıdır, şifre/PAT ister.

#  Firmalarda pratikte hangisi daha çok kullanılır?
%90 SSH kullanılır.
Sebebi:

Bir kere kurarsın, sürekli şifre girmek zorunda kalmazsın.

Komut satırında ve otomasyonlarda çok daha pratiktir.

Güvenlidir (anahtar çiftine dayanır, token sızmaz).

CI/CD sistemleri, deployment işlemleri, sunucu erişimi gibi yerlerde standarttır.

PAT (Personal Access Token) ne zaman kullanılır?
PAT genellikle:

HTTPS üzerinden erişim gerekiyorsa (örneğin bazı IDE’ler veya API çağrıları).

Ya da kullanıcı SSH kurulumu bilmediğinde geçici çözüm olarak kullanılır.

GitHub API’si gibi yerlerde de bazen token zorunludur.

Ama:

PAT her 1 yıl (veya daha kısa) sürede yenilenmek zorundadır, SSH ise tek seferliktir.

Kısaca karşılaştırma:
Özellik	SSH	PAT
Kurulum	Biraz uğraş ister	Daha kolay
Şifre/token girme	Gerek yok	Her push/pull işleminde gerekir
Pratiklik	 En pratik	Elde yazılmalı veya cache’lenmeli
Güvenlik	Anahtar çiftine dayalı (çok güvenli)	Token sızarsa riskli
Yenileme	Yok (tek seferlik)	Var (örneğin 1 yılda bir)
Şirket tercihleri	Yaygın	Az, genelde kullanıcı tercihidir

Sonuç:
Kurumsal firmalarda ve profesyonel projelerde SSH kullanılır.
Token daha çok kişisel kullanımda veya acil durum çözümüdür.

# Hazır Git Komutlarının Açıklaması
GitHub'ta repo oluşturduğunda sana gösterilen hazır komutlar, yerel (bilgisayarındaki) klasörü 
GitHub’taki uzaktaki repo (remote repository) ile eşleştirmek ve ardından gönderip (push) senkronize etmek içindir.

echo "# b-303-deneme" >> README.md
README.md adında bir dosya oluşturur ve içine başlık olarak # b-303-deneme yazar.
(Markdown formatında bir açıklama dosyası.)

git init
Mevcut klasörü bir Git deposu haline getirir.
Artık bu klasörde yapılan değişiklikler takip edilebilir.

git add README.md
README.md dosyasını sahneye (staging area) ekler.
Yani bu dosya bir sonraki commit’e dahil edilir.

git commit -m "first commit"
Değişiklikleri kalıcı olarak yerel Git geçmişine kaydeder.
"first commit" mesajı, bu commit’in açıklamasıdır.

git branch -M main
Mevcut branch'in adını main yapar.
Eskiden master olurdu, artık main daha çok kullanılıyor.

git remote add origin https://github.com/feyyazkarakoc/b-303-deneme.git
GitHub’taki uzak (remote) repo ile bağlantı kurar.
origin adıyla bu bağlantı tanımlanır.

git push -u origin main
Yerel main branch’ini, origin (yani GitHub’daki repo) ile senkronize eder.
-u parametresi, bundan sonra sadece git push yazdığında nereye push edeceğini hatırlatır.

# origin Ne Demek?
origin, uzaktaki (remote) deponun takma adıdır (alias).
Yani:
git remote add origin https://github.com/feyyazkarakoc/b-303-deneme.git
Bu komut şunu söyler:

“GitHub’daki şu URL’ye origin adını veriyorum. Bundan sonra orasıyla çalışacağım.”

İstersen bu ismi başka bir şey de yapabilirdin:
git remote add benimrepo https://github.com/....
Ama origin kelimesi evrensel bir alışkanlıktır, o yüzden herkes onu kullanır.

# -u Ne Demek?
-u kısa hali, uzun hali: --set-upstream.

Şunu yapar:

“Bu branch ile bu uzak branch’i birbirine bağla. Bundan sonra sadece git push yazarsam nereye push edeceğimi otomatik bil.”

Yani şu komutta:
git push -u origin main
Bu şu anlama gelir:

“main branch’imi origin’deki main branch’ine gönder, ve bundan sonra bu eşleştirmeyi hatırla.”

Böylece sonraki push'larda şunu yazman yeterli olur:
git push

Özet Tablo
Komut	Açıklama
origin	Uzak repoya verilen takma ad
-u veya --set-upstream	İki branch’i kalıcı olarak eşleştir

# git pull Ne İşe Yarar?
git pull
GitHub’daki (remote) değişiklikleri kendi bilgisayarındaki klasöre indirir ve birleştirir (merge).

Örneğin:

Sen GitHub’ta bir dosyayı düzenledin.

Ama bilgisayarındaki klasör hâlâ eski hâlinde.

git pull yazarsan, GitHub’taki son hal bilgisayarına gelir.

#  git fetch Nedir?
git fetch komutu, Git'te başkalarının yaptığı değişiklikleri almanı sağlar ama çalışma alanını hemen etkilemez. 
git fetch, uzak (remote) repodaki son değişiklikleri kendi yerel Git veritabanına indirir, ama:

Çalıştığın branch'e dokunmaz.

Dosyalarını güncellemez.

Sadece arka planda yeni commit'leri indirir.

git fetch vs git pull
Komut	Ne yapar?
git fetch	Uzak repodaki değişiklikleri indirir ama dosyaları güncellemez
git pull	fetch + merge yapar. Değişiklikleri indirir ve çalışma alanına uygular

Ne Zaman git fetch Kullanılır?
Başkası repoya commit attı mı diye bakmak istersen:
git fetch
Ama kendi branch'ini değiştirmeden sadece ne olmuş görmek istersen.

Örn: GitHub'tan başkası bir PR açtı → git fetch origin ile onun branch’ini görürsün.
Kullanım Örnekleri
1. Sadece fetch
git fetch
Uzak repo (default: origin) içindeki tüm branch’lerdeki son değişiklikleri indirir.

2. Sadece belli branch’i fetch
git fetch origin main
Sadece origin reposundaki main branch'ini indirir.

3. Sonra karşılaştırma
git log HEAD..origin/main
Senin branch’inden sonra origin/main branch’ine gelen commit’leri listeler.

Hatırlaman için özet cümle:
git fetch sadece haber getirir, ama evini değiştirmez.
git pull hem haberi getirir hem de evini değiştirir (birleştirir).


# git fetchten sonra merge mı yapılmalı
git fetch yaptıktan sonra değişiklikleri kendi branch'ine uygulamak istiyorsan, elle merge ya da rebase yapmalısın.

git fetch → sonra ne?
git fetch, sadece uzak repodaki değişiklikleri indirir, ama kendi branch'ine uygulamaz. O yüzden, sonra senin kararın: Birleştirecek misin, sadece bakacak mısın?

Devam senaryoları:
1. merge ile birleştirmek
git fetch
git merge origin/main
Bu, senin branch’ini origin/main ile birleştirir.
Eğer branch’in main ise ve GitHub'da güncel main varsa, onu alırsın.

2. rebase ile üzerine yazmak (daha temiz tarih)
git fetch
git rebase origin/main
Senin commit'lerini, origin/main üzerine sıfırdan ekler.
Bu, commit geçmişini daha düz ve temiz yapar ama dikkatli olunmalı.

3. Hiçbir şey yapmadan sadece kontrol etmek
git fetch
git log HEAD..origin/main
Bu komut, senin branch’in ile origin/main arasında fark var mı, gösterir.

Özet
Komutlar	Ne işe yarar?
git fetch	Uzak repodaki değişiklikleri indirir
git merge origin/main	O değişiklikleri kendi branch’ine uygular
git rebase origin/main	Temiz tarih ile birleştirir
git pull	fetch + merge birlikte yapar

Ne zaman fetch + merge yaparsın?
Takımda çalışıyorsan ve başkaları yeni commit attıysa,

Otomatik pull yapmak istemiyorsan,

Önce neler değişmiş görmek istiyorsan.

# "Temiz tarih" ve "rebase ile üzerine yazmak" ne demek?
Önce Git'te "commit tarihi" nasıl görünür?
Git'te her yaptığın değişiklik bir committir.
Bunlar sırayla aşağıdaki gibi görünür:
A - B - C      ← main (GitHub'daki)
       \
        D - E  ← senin branch'in (local)
Sen GitHub’daki main’den çatallanıp (branch) kendi değişikliklerini (D, E) yapmışsın.
Bu sırada GitHub’daki main ilerlemiş (C commit’i gelmiş).

1. git merge ile birleştirirsen
git fetch
git merge origin/main
Git, yeni bir "birleştirme commit’i" oluşturur:
A - B - C ----- G  ← HEAD (merge commit)
       \     /
        D - E
Bu durumda commit geçmişin biraz karmaşık olur çünkü:

Hem senin commit’lerin (D, E) hem de birleştirme (G) görünür.

2. git rebase ile birleştirirsen
git fetch
git rebase origin/main
Git, senin commit’lerini (D, E) sanki C’den sonra yapılmış gibi yeniden yazar:
A - B - C - D' - E'   ← HEAD (rebase sonrası)
D', E' = D, E commit’lerinin yeniden yazılmış halleri (ID'leri değişir)

Sanki hiç ayrı branch yokmuş gibi, dümdüz ve tertemiz bir sıra

Peki "temiz tarih" ne demek?
Commit geçmişi dümdüz gider, dallanma veya karışıklık olmaz.

Bu, özellikle:

Takım projelerinde,

Açık kaynak kodlarda,

Okunabilirliği yüksek tutmak isteyenlerde

çok tercih edilir.

Sonuç olarak:
Yöntem	Geçmiş (tarih) nasıl görünür?	Avantajı	Dezavantajı
merge	Dal gibi birleşir (merge commit oluşur)	Kolay, güvenli	Commit geçmişi dağınık olabilir
rebase	Düz, sıralı ve temiz görünür	Temiz commit tarihi	Commit ID değişir, dikkat ister


# git clone <URL> komutu ne yapar?
Sen git clone https://github.com/kurs/proje.git komutunu yazıp çalıştırdığında, Git şu 3 işlemi otomatik olarak yapar:

1. Uzak (remote) Git reposunu indirir.
GitHub'daki projenin içeriğini (dosyaları) alır.

2. .git klasörünü de indirir.
Bu klasör git reposunun kalbidir. İçinde commit geçmişi, branch bilgileri, HEAD vs. bulunur.

Yani senin local bilgisayarındaki klasör artık bir Git reposudur.

3. Remote bağlantı (origin) ayarı yapar.
git remote -v yazarsan, GitHub’daki URL'yi origin adıyla bağlamış olur.

Böylece git push, git pull gibi işlemleri otomatik o repoya yaparsın.

Örnek: VSCode veya Bash terminalinde
Sen VSCode terminaline şunu yazdığında:
git clone https://github.com/feyyazkarakoc/cloud-aws-notlar.git
Sonuçta:

Yeni bir klasör oluşur:
cloud-aws-notlar/

Ve bu klasörün içinde:

.git/ ← (❗GİZLİ klasördür, ama Git için en kritik yer burasıdır)

README.md, main.py vs... gibi proje dosyaları olur.

SONUÇ:
Evet, git clone komutuyla gelen dosya bir Git reposudur.
İçinde .git klasörü mutlaka vardır, bu yüzden git status, git log, git push gibi komutlar hemen çalışır.

# Konsolda gördüğün bu satır:
Lenovo@DESKTOP-2V0GJ1I MINGW64 ~/Desktop/b-303-deneme2
şu anlama gelir:

Bu satır hangi klasörde olduğunu gösteriyor:
Sen şu an C:\Users\Lenovo\Desktop\b-303-deneme2 klasöründesin.

Terminalde ~ sembolü, genellikle "C:\Users\Lenovo" anlamına gelir.

Peki bu klasör bir Git reposu mu?
Bunu anlamanın kesin yolu, şu komutları yazmaktır:
git status
Eğer şu hatayı verirse:
fatal: not a git repository (or any of the parent directories): .git
Bu klasörde .git klasörü yoktur yani bu klasör bir Git reposu değildir.

Bir klasörü Git reposu yapmak için:
Bu klasörde şu komutu yazmalısın:
git init
Sonra git status dediğinde artık şu yazar:
On branch master
No commits yet
nothing to commit
Ve .git/ adında gizli bir klasör oluşur. Bu klasör, git geçmişini ve ayarlarını tutar.

Kendi testin için önerim:
VSCode veya Bash terminalinde yeni bir klasör oluştur:
mkdir test-git
cd test-git
git status dene:
git status   #  Hata verir çünkü git reposu değildir
git init ile git reposu yap:
git init
git status   #  Artık çalışır


# $ cd b-303-deneme

Lenovo@DESKTOP-2V0GJ1I MINGW64 ~/Desktop/b-303-deneme2/b-303-deneme (main) --->>>    main e geçti


Evet, çok güzel fark ettin:
Sen b-303-deneme klasörüne geçtiğinde prompt şu hale geldi:

(main)
Bu da demektir ki:

Bu klasör artık bir Git reposudur.
Yani içinde .git adlı gizli bir klasör var. Git tarafından izlenen bir klasöre girdin.

Peki neden (main) yazdı?
Bu, Git deposunun şu anda main adlı bir branch (dal) üzerinde olduğunu gösterir.

Özetle:
Gözlem	Anlamı
(main)	Bu klasör bir git reposu ve şu an main branch'indesin.
.git klasörü var	Git, bu klasörde tüm geçmişi ve yapılandırmayı tutuyor.
git status çalışır	Çünkü klasör bir Git reposudur.

# Linode Nedir?
Linode, geliştiriciler ve sistem yöneticileri için bulut tabanlı sanal sunucular (VPS – Virtual Private Server) sağlayan bir platformdur. 2022'de Akamai tarafından satın alınmıştır. Temel olarak, bir veri merkezinde sanal bir sunucu kiralayarak kendi uygulamanızı, web sitenizi, API'nizi, oyun sunucunuzu vb. çalıştırmanızı sağlar.


Temel Özellikleri:
VPS (Virtual Private Server): Her kullanıcıya ayrılmış kaynaklarla (CPU, RAM, disk) sanal bir sunucu sunar.

Root erişimi: Sunucunun tam kontrolü sizde olur (SSH ile giriş yapıp her şeyi siz kurarsınız).

Uygulama barındırma: Web siteleri, veritabanları, arka plan servisleri, oyun sunucuları, API’ler, cron job’lar vs.

Yüksek Performanslı SSD diskler ve DDoS koruması.

Data center seçenekleri: Avrupa, ABD, Asya gibi bölgelerde lokasyon seçilebilir.

Pay-as-you-go: Kullandığın kadar öde modeliyle çalışır.

"Development Linode" Ne Demek?
"Development Linode" ifadesi, genelde geliştirme amaçlı oluşturulmuş bir Linode sunucusunu ifade eder. Yani:

Canlı (production) sistemlerden ayrı olarak,

Geliştirme veya test ortamı olarak kullanılan bir sunucudur.

Örneğin:

Yeni bir web uygulaması geliştiriyorsanız, bunu ilk olarak development linode üzerinde test edersiniz.

CI/CD süreçlerinde otomatik deployment için development sunucusu olarak kullanılır.

Linode Alternatifleri
Linode’un benzeri diğer VPS sağlayıcıları şunlardır:

Platform	Açıklama
DigitalOcean	Geliştiriciler için popüler, arayüzü kullanıcı dostudur.
Vultr	Daha küçük bütçelere uygun seçenekleri de var.
AWS EC2	Çok daha fazla özellik ve esneklik sunar ama yönetimi daha karmaşıktır.
Hetzner	Avrupa'da popüler, fiyat/performans oranı yüksektir.

Ne İçin Kullanabilirsin?
Web sitesi host etmek (PHP, Node.js, Django vb.)

REST API sunmak

Docker/Kubernetes ortamları kurmak

Next.js, Spring Boot projelerini deploy etmek

Öğrenme/deneme amaçlı Linux sunucu kullanımı

Uygulamalarda yük testi yapmak








