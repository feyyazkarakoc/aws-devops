
# Durum Analizi
1. git rm --cached . ne yaptı?

Bu komut dosyaları Index'ten (staging area) kaldırdı
Ama dosyalar hem Working Tree'de hem de commit'te kaldı
Sadece Git'in artık bu dosyaları takip etmemesini söyledin

2. git checkout 6271e7d ne yaptı?

Bu seni "detached HEAD" durumuna soktu
HEAD artık bir branch'i değil, direkt o commit'i işaret ediyor
Bu yüzden ((6271e7d...)) görüyorsun

Sorularının Cevapları
1. Dosyalar şimdi nerede?

Dosyalar hem Working Tree'de hem de local repository'de (commit içinde)
Working Tree: Fiziksel dosyalar hala orada
Repository: Commit içinde versiyonları saklanıyor

2. Neden git status'ta untracked gözüküyor?
git rm --cached . yaptığında şu oldu:
Working Tree: [dosyalar var] 
Index: [boş - dosyalar kaldırıldı]
Commit: [dosyalar var]
Git şimdi şunu düşünüyor:

"Bu dosyalar Working Tree'de var ama ben onları takip etmiyorum (untracked)"
Çünkü git rm --cached ile Index'ten kaldırdın

# git switch -c v1main komutunun ne yaptığını açıklayayım:
git switch -c v1main şu işlemleri yaptı:

Yeni branch oluşturdu: v1main adında
Bu branch'e geçti: Artık (v1main) branch'indesin
Detached HEAD durumundan çıktı: Artık ((6271e7d...)) değil, normal branch'tesin

Durum Değişimi
Önceki durum:
((6271e7d...)) ← Detached HEAD (tehlikeli)
Şimdiki durum:
(v1main) ← Normal branch (güvenli)

# .gitignore Dosyası Nedir?
.gitignore dosyası, Git’e hangi dosya ve klasörleri takip ETMEMESİ gerektiğini söyler.

Ne işe yarar?
Projendeki bazı dosyaların versiyon kontrolüne dahil edilmesini istemeyebilirsin. Örneğin:

Dosya / Klasör	Neden ignore edilir?
*.log	Log dosyaları sık sık değişir, gereksizdir
node_modules/	Büyük, dış bağımlılıklar – her yerde indirilebilir
*.class, *.pyc	Derlenmiş dosyalar, kaynak değil
secret.txt, .env	Şifre, API anahtarı içerir – güvenlik riski
/.idea/, /target/	IDE/derleyici dosyaları – kişiseldir

Nasıl Kullanılır?
Proje klasörüne .gitignore dosyası koy ve içine istemediğin dosya/klasörleri yaz:

Örnek .gitignore:

*.log
*.class
*.pyc
.idea/
target/
.env
Önemli Not:
.gitignore sadece henüz takip edilmeyen dosyaları etkiler.

Eğer bir dosya zaten git add ile izleniyorsa, .gitignore onu yok saymaz.

Çözüm:
İzlenen bir dosyayı .gitignorea eklemek istiyorsan:

git rm --cached dosya.txt
Sonra .gitignore içine yazarsın, artık takip edilmez.

Özet
Özellik	Açıklama
Amaç	Git’in takip etmeyeceği dosyaları belirtmek
Nerede kullanılır?	Proje kök klasöründe .gitignore dosyasında
Etki alanı	Yalnızca takip edilmeyen dosyalarda etkilidir
Örnekler	.env, *.log, node_modules/, *.class


# SSH ile clone yapmak

1. SSH Agent'ı Başlatmak
$ eval "$(ssh-agent -s)"
Agent pid 1934
Ne yaptın?
SSH bağlantılarında özel anahtarı bellekte saklayacak bir ajan (ssh-agent) başlattın.

eval "$(ssh-agent -s)" komutu, bu ajanı başlatır ve çalıştığını onaylayan Agent pid 1934 gibi bir çıktı verir.

Neden yaptın?
Her seferinde şifre girme derdi olmadan özel anahtarı otomatik kullandırmak için.

2. .ssh Klasörünü Listelemek
$ ls ~/.ssh
config  firstpem.pem  id_ed25519  id_ed25519.pub  known_hosts  known_hosts.old
Ne yaptın?
SSH anahtarlarının bulunduğu klasörü (~/.ssh) listeledin.

İçerik:

id_ed25519: Özel anahtar

id_ed25519.pub: Herkesle paylaşılabilen açık anahtar

config: SSH bağlantı ayar dosyası (varsa özel hostname vs.)

firstpem.pem: Muhtemelen önceki bir özel anahtar

known_hosts: Daha önce bağlanılan sunucuların güvenlik imzaları

known_hosts.old: Eski yedek hali

3. SSH Anahtarını SSH-Agent’a Eklemek
$ ssh-add ~/.ssh/id_ed25519
Identity added: /c/Users/Lenovo/.ssh/id_ed25519 (Lenovo@DESKTOP-2V0GJ1I)
Ne yaptın?
id_ed25519 adındaki özel SSH anahtarını ssh-agent’a tanıttın.

Artık bu terminal oturumunda SSH bağlantıları bu anahtarı otomatik kullanabilir.

Bu adım olmazsa GitHub bağlantısı şu hatayı verebilir:

Permission denied (publickey)

4. SSH ile GitHub Reposunu Klonladın
$ git clone git@github.com:feyyazkarakoc/example1.git
Cloning into 'example1'...
...
Ne yaptın?
GitHub’daki example1 reposunu SSH protokolüyle bilgisayarına kopyaladın.

Artık example1 adında bir klasörde, tüm versiyon geçmişiyle bu repo yerel olarak var.

Neden SSH kullandın?
HTTPS yerine SSH ile klonladığın için kullanıcı adı/parola gerekmedi.

Daha güvenli, otomatik bağlantı yapılabilir.

Özetle Neler Yaptın?
Adım	Açıklama
eval "$(ssh-agent -s)"	SSH anahtarlarını yöneten ajanı başlattın
ls ~/.ssh	SSH anahtarlarını ve ayarları kontrol ettin
ssh-add ~/.ssh/id_ed25519	Anahtarı SSH agent’a ekledin (bağlantılar için hazır hale getirdin)
git clone git@github.com:...	GitHub reposunu SSH ile klonladın

# peki bundan sonra süreklii ssh ile pull ve push olacak mı yoksa her seferinde tanıtmalı mıyım
Cevap: bağlantının nasıl kurulduğuna ve sistem ayarlarına bağlı.

1. Şu anda yaptığın sistemde (Windows + Git Bash):
Durum:
Sen şu an Git Bash ile çalışıyorsun ve komutları şu sırayla yazdın:

eval "$(ssh-agent -s)" → SSH ajanı başlattın.

ssh-add ~/.ssh/id_ed25519 → Anahtarı ajan’a tanıttın.

git clone git@... → SSH üzerinden klonladın.

Bundan sonra:
Aynı terminal açık kaldığı sürece → pull, push işlemlerin sorunsuz çalışır.

Bilgisayarı kapatıp yeniden açarsan veya terminali kapatıp açarsan → SSH ajan yeniden başlatılmalı ve anahtar yeniden eklenmeli.

Bunu her seferinde yapmamak için ne yapılabilir?
Yöntem 1: Otomatik tanıma (şifre sormayan anahtarlar için)
SSH anahtarını şifresiz oluşturduysan (ssh-keygen sırasında boş geçtin)
→ .ssh/config dosyasına şu satırları eklersen, Git otomatik kullanır:
 ~/.ssh/config

Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
  AddKeysToAgent yes
Bu dosya yoksa oluşturabilirsin (touch ~/.ssh/config).

Yöntem 2: ssh-agent ve ssh-add işlemini otomatikleştirmek
~/.bash_profile veya ~/.bashrc dosyasına şunları ekle:
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
Bu sayede her Git Bash açıldığında SSH anahtarı otomatik tanınır.

Eğer Anahtar Şifrelendiyse (Passphrase varsa):
Her terminalde şifre girmen gerekir, ama bu da sadece ssh-add sırasında olur.


# peki yazılım firmalarında ssh kullanılır dedin çoğunlukla.  git hub kullanılırken takımdakiler yöntem biri mi ikiyi mi kıullanır

Yazılım firmalarında, SSH kullanımı neredeyse standarttır çünkü:

HTTPS’e göre daha güvenlidir

Her geliştiriciye özel kimlik doğrulama sağlar

Şifre girme derdi yoktur (anahtar ayarı düzgünse)

Peki firmalarda SSH ile kullanımda hangi yöntem tercih edilir?
Cevap: Yöntem 1 + Anahtar yöneticisi (ssh-agent)
Yöntem 1 (SSH config ile otomatik tanıma)
.ssh/config dosyasına IdentityFile tanımlanır.
Geliştirici bir kere ayarlar, sonra sürekli ssh-add yazmasına gerek kalmaz.

Bu yöntem:

Kurumsal firmalarda ve

geliştirici ekiplerinde

en yaygın kullanılan yöntemdir. Çünkü:

Otomatikleşmiştir.

Kod yazanı yormaz.

pull/push komutları doğrudan çalışır.

Yöntem 2 (Her terminalde ssh-agent başlatmak)
Bu yöntem daha çok kişisel bilgisayarlarda veya geçici çözümler için tercih edilir.

Yani:

Bootcamp öğrencisi

Junior geliştirici

Tek başına çalışan biri

için çalışır, ama her terminalde tekrar çalıştırmak gerekebilir.

Büyük ekiplerde ne olur?
Her geliştiriciye bir SSH anahtarı oluşturulur.

.ssh/config dosyası ayarlanır.

(Opsiyonel olarak) ssh-agent sistem başlatıldığında otomatik devreye alınır.

Git işlemleri şeffaf şekilde çalışır (şifre ya da token girmeden).

# git remote -v komutunun boş dönmesinin nedeni
senin o anda bulunduğun klasörün (example7) bir Git deposu (repository) olmaması veya clone işleminin aslında başka bir klasöre yapılmış olmasıdır.

Senin komutlarını adım adım açıklayalım:

1. Bu komutu çalıştırdın:
git clone https://github.com/feyyazkarakoc/b-303-deneme.git
Bu komut, GitHub’daki b-303-deneme adlı repoyu bulunduğun dizine, yani:

~/Desktop/github day3/example7/

altına yeni bir klasör olarak b-303-deneme/ klasörünü oluşturdu ve oraya klonladı.

2. Ama sen sonra bu dizindesin:
Lenovo@DESKTOP-2V0GJ1I MINGW64 ~/Desktop/github day3/example7 (v1main)
Yani hâlâ example7 klasöründesin, klonlanan repo dizinine girmedin.

Çözüm:
Klonladığın klasöre girip tekrar komutu çalıştır:
cd b-303-deneme
git remote -v
Bu durumda şöyle bir çıktı alırsın:
origin  https://github.com/feyyazkarakoc/b-303-deneme.git (fetch)
origin  https://github.com/feyyazkarakoc/b-303-deneme.git (push)

Kısa Özet:
git clone yeni bir klasör oluşturur.

Sen hâlâ eski klasördeysen, orada .git yoktur → git remote -v boş olur.

Doğru klasöre (cd b-303-deneme) geçersen, git komutları düzgün çalışır.



# origin bir alias (takma ad)'dır, branch değildir.

Nedir bu origin?
origin  https://github.com/feyyazkarakoc/b-303-deneme.git (fetch)
origin  https://github.com/feyyazkarakoc/b-303-deneme.git (push)
origin, Git’in uzaktaki (remote) depo adresi için verdiği varsayılan takma addır (alias).

GitHub'dan bir repo klonladığında, o adres otomatik olarak "origin" ismiyle kaydedilir.

Böylece her seferinde uzun URL’yi yazmak zorunda kalmazsın.

Peki alias ne işe yarar?
Sen şu komutu yazabilirsin:

git push origin main
Bu, şu demektir:

"main isimli branch'i origin isimli uzak sunucuya (yani GitHub’daki şu adrese) gönder."

Uzun haliyle yazmak gerekseydi:

git push https://github.com/feyyazkarakoc/b-303-deneme.git main
ama origin sayesinde bu kolaylaşır.

Kısaca:
Terim	Anlamı
origin	GitHub’daki uzak adresin takma adı (remote alias)
main	Branch (dal) adı

git remote -v	Uzaktaki repo adreslerini ve takma adlarını listeler

İstersen origin yerine farklı bir ad bile verebilirsin:

git remote add benimgithub https://github.com/feyyazkarakoc/b-303-deneme.git
Sonra:
git push benimgithub main
Ama çoğu zaman origin kullanılır, standarttır.

# Sen şunu yaptın:

Bir GitHub reposunu (b-303-deneme) klonladın.
→ Git otomatik olarak ona origin adını verdi.

Sonra o kopyayı başka bir uzak repoya (b-303-deneme2) da göndermek istedin.
→ Ona da sen kendin kendirepom adını verdin.
→ Böylece artık iki farklı uzak adresin (remote) olmuş oldu.

O yüzden git remote -v çıktısı şöyle:

kendirepom  https://github.com/feyyazkarakoc/b-303-deneme2.git (fetch)
kendirepom  https://github.com/feyyazkarakoc/b-303-deneme2.git (push)
origin      https://github.com/feyyazkarakoc/b-303-deneme.git (fetch)
origin      https://github.com/feyyazkarakoc/b-303-deneme.git (push)
Burada:

Remote Adı	Açıklama
origin	Orijinal klonladığın repo (b-303-deneme)
kendirepom	Senin sonradan eklediğin başka bir uzak repo (b-303-deneme2)

Şimdi ne işe yarar?
Artık iki farklı repoya kod gönderebilirsin:

Eski repo'ya (origin):
git push origin main
Yeni repo'ya (kendirepom):
git push kendirepom main