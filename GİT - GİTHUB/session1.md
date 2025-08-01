
# BRANCH (DAL) NEDİR?
Branch, projenin bağımsız bir “kopyasında” çalışmanı sağlar.
Ana koddan ayrılıp değişiklik yaparsın, sonra geri birleştirebilirsin.
Ana kod bozulmaz.
Farklı özellikleri farklı branch’lerde geliştirirsin.
İşi bitirince merge (birleştirme) yaparsın:

# HASH (KOMİT KİMLİĞİ) NEDİR?
Her git commit yaptığında Git, bu commit'e özel bir kimlik numarası (hash) verir.
Bu hash:
40 karakterlik hexadecimal (16’lık sistem) bir koddur.
Her commit’i benzersiz şekilde tanımlar.
Örnek:
git log
Görürsün:
commit f3d42c1a97eab89913bb7e6b3a9c45e72f94d62d
Author: Feyyaz Karakoç
Date:   Sun Jul 6 17:30:00 2025 +0300
"Kullanıcı girişi özelliği eklendi"
Buradaki f3d42c1... → bu commit’in hash kodudur 
Kısaltılmış haliyle (f3d42c1) de referans verilebilir.
Ne işe yarar?
Spesifik bir commit’i bulmak için kullanılır.

Geri dönmek, revert etmek, cherry-pick yapmak gibi işlemlerde kullanılır.

# git log → Projedeki tüm commit geçmişini gösterir.
Her commit için şu bilgileri verir:
commit hash (benzersiz ID)
Author (kim yaptı)
Date (ne zaman yaptı)
Commit mesajı (ne yaptı)

git log yazdık:
commit f199df47ab7531839d1478339e70a0e10057ec1a (HEAD -> master)
Author: feyyazkarakoc <fyyzkrkc@gmail.com>
Date:   Mon Jul 7 22:56:59 2025 +0300

    v1

Git Log Ne İçin Kullanılır?
Amaç	                                         Nasıl Yardımcı Olur?
Geçmişi takip etmek	                        Kim ne zaman ne değişiklik yapmış?
Hatalı commit’i bulmak	                    Hangi commit'ten sonra bozuldu?
Geri almak/revert yapmak için	              Hash ID ile hedef commit bulunur
Merge veya branch geçmişini analiz etmek	  Hangi branch nereden ayrıldı?

# Neden “staging area” diye bir ara katman daha var?
staging area, commit öncesi "ön izleme" yapmanı sağlar.
Yani: "Hangi değişiklikleri commit etmek istiyorum?" sorusunu sana sorar.

Working Directory (Çalışma Alanı)	Senin dosyaları değiştirdiğin yer (örneğin VS Code).
Staging Area (Geçici Alan)	Commit'e eklemek istediklerini seçtiğin yer.
Local Repository (Yerel Repo)	git commit ile giden yer. Geçmiş burada tutulur.

Tüm dosyaları değil, sadece seçtiğini commit edebilmek için.
Commit'lerin üzerinde daha fazla kontrol sahibi olmak için.

Eğer staging area olmasaydı:
git commit tüm değişiklikleri doğrudan alırdı.
Dosya dosya kontrol etmek mümkün olmazdı 
Hatalı commit'ler olurdu (örneğin yarım işler, debug kodları vs.)

# git log --oneline komutu, Git geçmişini kısa ve sade bir formatta gösterir.
git log --oneline → Her commit’i tek satırda, kısa hash + mesaj olarak gösterir.
Neden Kullanılır?
Daha temiz, daha okunabilir geçmiş için.

Özellikle çok commit olan projelerde karmaşayı azaltır.

# git diff → Değişiklik yaptığın dosyaları gösterir ama henüz commit etmediğin farkları gösterir.
Yani:
Çalışma alanı (working directory) ile
staging area (geçici alan) arasındaki farkı gösterir.

 # git checkout Ne Yapar? 
 git checkout <branch-ismi>       # O branch’e geçer 
 git checkout <commit-hash>       # Belirli bir commit’e geçer (detached HEAD) 
 git checkout -b <yeni-branch>    # Yeni bir branch oluşturur ve geçer  
 Yani: Dal (branch) veya Belirli bir commit'e geçmeni sağlar.

 # HEAD -> master Ne Demek? 
 9eedd63 (HEAD -> master) deneme Buradaki anlam: HEAD → Git’in şu anda baktığı (yani aktif) commit. 
 master → Ana branch’in ismi. HEAD -> master → Şu anda master branch’inin ucundasın (yani en son commit’i bu).  
 Başka bir deyişle: HEAD, master branch’inin gösterdiği commit’i işaret ediyor.      
 Git durumu: ((9eedd63...)) → Şu anda bir branch’te değil, belirli bir commit’te (yani detached HEAD durumundasın)

# git switch - ne işe yarar?
git switch -
En son bulunduğun branch'e geri döner.
Ama dikkat:
git switch - sadece branch'ler arasında çalışır.
Yani:
main → feature/login → switch - → geri döner	
main → bir commit hash’i → switch - →  HATA	

Sorun: Sen branch değil, commit hash arasında dolaşıyorsun
Bu senin konsol geçmişinden açık:
git checkout 6ac194d → direkt commit’e geçtin (detached HEAD)
git commit -m "notlar" → bu yeni commit oldu: a26d22c
Sonra tekrar git checkout 6ac194d yaptın
Sonra git switch - dedin
Git hata verdi:
fatal: a branch is expected, got commit 'a26d22c...'
Çünkü: a26d22c bir branch değil → sadece bağlantısız (orphan) bir commit
Git "branch'e geçmeni bekliyordum ama sen bana commit hash verdin" diyor.

Uyarıda ne diyor?
Warning: you are leaving 1 commit behind, not connected to any of your branches:
a26d22c notlar
If you want to keep it by creating a new branch, this may be a good time
to do so with:

git branch <new-branch-name> a26d22c
Bu önemli: Git sana diyor ki:
Eğer bu commit’i kaybetmek istemiyorsan, ona bir isim (branch) ver:
git branch yeni-branch-adi a26d22c
Sonra bu branch'e geçebilirsin:
git switch yeni-branch-adi

# git switch -c Dev_A komutunu kullandın ve şu anda şunu yaptın:

git switch -c Dev_A
Anlamı:
Şu anda bulunduğun commit (6ac194d) üzerinden
Dev_A adında yeni bir branch oluşturdun
Ve bu yeni branch’e geçtin
Artık durumun:
Yeni bir branch’in var: Dev_A

HEAD bu branch’in ucunda
Commit yaparsan, artık Dev_A branch’i üzerinden ilerleyecek
Detached HEAD durumu sona erdi 

Kontrol etmek için:
git branch
Bu komut sana şunu gösterecek:
* Dev_A
  master
Yıldız * hangi branch'te olduğunu gösterir (şu an Dev_A)

İpucu:
Artık Dev_A branch’inde olduğuna göre:
Yeni özellikler ekleyebilirsin
Değişiklik yapıp commit edebilirsin
Daha sonra master ile birleştirebilirsin (git merge)


#  git branch Nedir?
Git’teki tüm dalları (branch) listeleyen, yeni branch oluşturan veya silen komuttur.
Neden Branch Kullanılır?
Git’te farklı fikirleri ayrı ayrı geliştirmek için branch kullanılır.
Ana kod → main veya master
Özellik geliştirme → feature/login, dev_ui, fix-bug-12 gibi ayrı branch'lerde yapılır

Sonra birleştirilir (merge)

Temel Kullanımlar
1. Tüm branch’leri listele:e
git branch
Örnek çıktı:
* Dev_A
  master
→ * işareti, şu an aktif olduğun branch’i gösterir (örnekte Dev_A)

2. Yeni bir branch oluştur:
git branch yeni_branch
Bu sadece branch oluşturur ama geçmez.

3. Branch oluştur ve geç:
git switch -c yeni_branch
veya:
git checkout -b yeni_branch   # eski yöntem

4. Bir branch’i sil:
git branch -d branch_ismi
-d = delete
Git sana uyarı verir: Eğer branch’te commit edilmemiş şeyler varsa, silme!

Zorla silmek istersen:
git branch -D branch_ismi

Bu satırı conflict olması için yazıyuoruz.
# git merge Nedir?
git merge, bir branch’teki değişiklikleri başka bir branch ile birleştirir.

Mesela:
Sen Dev_A branch’inde yeni özellikler geliştirdin.
Bu özelliği artık master (ana dal) ile birleştirmek istiyorsun. İşte burada git merge devreye girer.

BASİT SENARYO (Adım Adım)
Adım 1: Branch’leri Oluştur
git switch -c Dev_A
Yeni branch oluştur ve içine geç.
echo "Deneme" > dosya.txt
git add .
git commit -m "Dev_A branchinde dosya eklendi"
Adım 2: master branch'ine dön
git switch master
Adım 3: Dev_A branch’ini master ile birleştir
git merge Dev_A
ÇIKTI:
Updating 9eedd63..a26d22c
Fast-forward
dosya.txt | 1 +
NE OLDU?
Sen şu an master branch’indeydin.
Dev_A branch’indeki değişiklikleri master içine kopyaladın.
Artık master branch’inde dosya.txt var.

GRAFİKSEL GÖRÜNÜM
Başlangıç:
master:   A → B
Dev_A:         → C (dosya eklendi)

Merge Sonrası:
master:   A → B → C
Dev_A:             ↑
Yani C commit’i artık master'da da var.

MERGE CONFLICT (ÇAKIŞMA) OLABİLİR Mİ?
Evet. Eğer aynı satırı iki branch'te de değiştirdiysen çakışma olur.

Git şöyle der:
Auto-merging dosya.txt
CONFLICT (content): Merge conflict in dosya.txt
Automatic merge failed; fix conflicts and commit the result.
Çözüm:
Dosyayı aç, çatışan yerleri düzenle
git add dosya.txt
git commit -m "Çakışma çözüldü"

ÖZET
Komut	Açıklama
git merge branch_adi	O branch’in değişikliklerini şu anki branch’e getirir
git switch master → git merge Dev_A	Dev_A’daki kodları master’a kat
Çakışma olursa	Manuel çözmen gerekir

Merge Türleri
Tür	Ne zaman olur?	Açıklama
Fast-forward	master ilerlememişse	Commit doğrudan kopyalanır
Merge commit	İki branch’te ayrı commit varsa	Ortak commit yaratılır
Conflict	Aynı satır iki yerde değiştiyse

# Git’te dosya takibi yaparken üç önemli alan vardır:
Head: Mevcut dallanmadaki en son commit'i temsil eder. Üstteki yeşil "Head" kutusu, dalın en son durumunu gösterir.
Index (Staging Area): Değişikliklerin commit edilmeden önce hazırlandığı alan. Mavi kutu, "git add" ile eklenen dosyaları içerir.
Working Tree: Yerel dosya sisteminizdeki çalışma dosyalarını temsil eder. Mor kutu, şu anda düzenlediğiniz veya değiştirdiğiniz dosyaları içerir.
İlişkiler ve Komutlar:
git diff HEAD~: Head ile bir önceki commit arasındaki farkları gösterir.
git diff --cached HEAD~: Index ile bir önceki Head arasındaki farkları gösterir.
git diff HEAD: Working Tree ile Head arasındaki farkları gösterir.
git diff: Working Tree ile Index arasındaki farkları gösterir.
git diff --cached: Index ile Head arasındaki farkları gösterir.

# Git’te 3 temel alan nedir?
1. Working Tree (Çalışma Dizini)
Bilgisayarında dosyaların açık hali. Kod yazdığın yer.
Örnek: main.java, uyku.py gibi dosyalar
Senin doğrudan düzenlediğin yerdir.

2. Index / Staging Area
Commit edilmek üzere hazırlanan (add yapılan) dosyaların geçici alanı.

Örnek:
git add dosya.java
Bu dosya artık "index"te bekliyor. Yani commit edilmek için sıraya alındı.

3. HEAD
Son yapılan commit’in işaretçisi (en güncel commit).
HEAD = "Şu an projenin neresindeyiz?" sorusunun cevabıdır.
Başka bir branch’e geçtiğinde HEAD orayı işaret eder.

Bağlantıları:
Working Tree  <--(git add)--  Index  <--(git commit)--  HEAD

git diff komutları ne yapar?
1. git diff
Working Tree ile Index arasındaki farkları gösterir.
(Yani henüz git add yapılmamış değişiklikleri gösterir.)

Soru: “Dosyada bir şey değiştirdim ama add yapmadım. Ne değişti?”

2. git diff --cached
(veya git diff --staged)
Index ile HEAD (yani son commit) arasındaki farkları gösterir.
(git add yapıldı ama commit yapılmadıysa burası farkı gösterir.)

Soru: “Add yaptım ama commit etmedim. Commit’e neler gidecek?”

3. git diff HEAD
Working Tree ile HEAD (yani son commit) arasındaki farkları gösterir.
(Tüm değişiklikleri gösterir: add yapılmış ve yapılmamış fark etmez.)

Soru: “Şu anki dosyalarım, son commit’e göre nasıl farklı?”

4. git diff HEAD~
Bir önceki commit (HEAD~) ile şu anki çalışma dizinindeki farkları gösterir.

Soru: “Son bir commit’ten bu yana neler değişti?”
(Eğer HEAD yerine HEAD~2 yazarsan 2 commit önceyle kıyaslar.)

5. git diff --cached HEAD~
Bu çok nadiren kullanılır ama anlamı:
HEAD~ commit'inden bu yana index'te hangi değişiklikler yapılmış, onu gösterir.

Yani:
HEAD~: 1 commit önceki hali
--cached: staging area (index)
İkisini karşılaştırır.
Bu komut özel kıyaslamalar için kullanılır.

Özet Tablo:
Komut	Karşılaştırma
git diff	Working Tree vs Index
git diff --cached	Index vs HEAD
git diff HEAD	Working Tree vs HEAD (tüm farklar)
git diff HEAD~	HEAD~ vs Working Tree
git diff --cached HEAD~	HEAD~ vs Index
