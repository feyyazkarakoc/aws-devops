# GİT - GİTHUB Nedir 

1. GIT NEDİR?
Git, bir versiyon kontrol sistemidir (Version Control System - VCS).
Ne işe yarar?
Kod dosyalarının geçmişini tutar: Ne zaman, kim, ne değişiklik yaptı görebilirsin.
Kodları eski hallerine döndürebilirsin.
Aynı projede çalışan yazılımcılar birbirlerinin kodlarına zarar vermeden çalışabilir.
Herkes kendi bilgisayarında çalışır, bağımsız kopyalar üzerinde değişiklik yapar.
Offline çalışabilir: Git, yerel (local) çalışır.

Nerede çalışır?
Senin bilgisayarında (yerel) çalışır.
Komut satırından (git init, git commit, git status, vb.) kullanılır.

2. GITHUB NEDİR?
GitHub, Git ile çalışan bir uzak sunucudur (remote repository). GitHub bir web sitesidir: https://github.com
Ne işe yarar?
Git ile tuttuğun projeleri internet üzerinde saklamanı ve paylaşmanı sağlar.
Projeni yedekler, başka bilgisayarlardan erişmeni sağlar.
Diğer geliştiricilerle ortak çalışma yapmanı sağlar (Pull Request, Issue, vs).
Projeni herkesle paylaşabilir ya da gizli tutabilirsin.

Nerede çalışır?
İnternette çalışır (bir web sitesi).
GitHub Desktop, GitHub CLI veya doğrudan tarayıcı üzerinden kullanılabilir.

GIT vs GITHUB FARKI
Özellik	Git	GitHub
Ne?	Versiyon kontrol sistemi	Git depolarını barındıran site
Nerede çalışır?	Bilgisayarında (offline)	İnternette (online)
Ne işe yarar?	Kod geçmişini tutar, geri alma	Projeyi paylaşma, yedekleme
Kullanım Şekli	Komut satırı (terminal)

# Temel Git Ayarları (Kurulumdan Sonra)
Kullanıcı adı ve e-posta ayarı (zorunlu):

git config --global user.name "Ad Soyad"
git config --global user.email "mail@example.com"
git config --global color.ui true

# Yapılan Ayarları Kontrol Et:
Ben daha önce ayarları yapmıştım.
git config --global --list

C:\Users\Lenovo>git config --global --list
user.name=feyyazkarakoc
user.email=fyyzkrkc@gmail.com
color.ui=true

# Kıyaslama: lokal repository vs git repository, remote repository vs git directory
Git repository (repo)	Git tarafından takip edilen bir klasördür.	İçinde .git klasörü olan her klasör bir Git repository’dir.
Lokal repository	Senin bilgisayarındaki Git repository'dir.	Kendi bilgisayarında oluşturduğun veya klonladığın Git repo.
Remote repository	İnternette (örneğin GitHub, GitLab) bulunan Git repository'dir.	Uzak sunucuda barınır, başkalarıyla paylaşmak için.
Git directory	.git/ klasörüdür – repository'nin kalbidir.	Git’in metadata ve versiyon geçmişini tuttuğu gizli klasördür.

Örnekle Açıklayalım
Diyelim şu komutları çalıştırdın:
mkdir myproject
cd myproject
git init
myproject klasörü: Git Repository’dir (çünkü artık içinde .git/ klasörü var).

Bu repo senin bilgisayarında olduğu için: Lokal Repository.

.git/ klasörü: Git Directory'dir (Git’in tüm geçmişi, commit'leri, branch'leri buradadır).

Eğer bu projeyi GitHub’a atarsan: GitHub’daki hali Remote Repository olur.

Bağlantı Nasıl?
Git, şu üç yapı arasında çalışır:
         🖥️
     [Working Directory]
            ↓ git add
     [Staging Area (Index)]
            ↓ git commit
     [.git directory / Git repository]
            ↓ git push
     [Remote Repository (GitHub)]
Özetle:
Git repository → Genel isim. .git klasörü varsa bir klasör Git reposudur.

Lokal repository → Git reposunun bilgisayarındaki hali.

Remote repository → İnternetteki versiyonu (GitHub, GitLab).

Git directory → .git/ klasörüdür, Git’in beyni.



Git repository ve Git directory  aynı o halde

Çok iyi yakaladın — ama tamamen aynı değiller, aralarındaki fark çok küçük ama önemli. Kısaca şöyle açıklayalım:

Benzerlik:
Her Git repository, içinde bir .git/ klasörü (yani Git directory) barındırır.

Bu yüzden çoğu zaman ikisi aynı şeymiş gibi kullanılır çünkü:

.git/ klasörü varsa, orası bir Git repository'dir denir.

Farkı netleştirelim:
Git repository	.git/ klasörünü içeren tüm proje klasörüdür (örneğin: myproject/)
Git directory (.git/)	Sadece .git klasörüdür → tüm Git metadata, commit geçmişi, branch bilgileri burada saklanır

Örnek klasör yapısı:
myproject/              → Git repository (çalışma klasörü)
├── .git/               → Git directory
├── index.html
├── app.js
└── README.md
myproject/ → Git repository

.git/ → Git directory

Kısaca Akılda Tut:
Git repository: Projeyi tuttuğun klasörün tamamı.
Git directory: Git'in gizli beynidir, .git/ klasörü.

