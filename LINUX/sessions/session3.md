
# Text Editörü Nedir?

Text editor (metin düzenleyici), düz metin dosyalarını (plain text) yazmaya ve düzenlemeye yarayan yazılımdır.

Programcılar, konfigürasyon dosyaları, kaynak kodları, notlar vb. işler için kullanır.

Word gibi ofis programlarından farkı: sadece düz metinle çalışır, biçimlendirme (bold, italik, tablo vb.) yoktur.

Örnek text editörler:

Basit: Notepad (Windows), nano (Linux)

Gelişmiş: Vim, Emacs, Sublime Text, VS Code

Vim Nedir?

Vim: Vi IMproved (Geliştirilmiş Vi) demektir.

1976’da yazılan vi editörünün geliştirilmiş, güçlü versiyonudur.

Neredeyse tüm Linux/Unix sistemlerinde kurulu gelir.

Hafif, hızlı ve terminal üzerinden çalışır.

Vim’in Çalışma Mantığı

Vim normal bir editör gibi sadece yazma modunda değildir. Modlarla çalışır:

Normal Mod (başlangıç modu)

Komut verirsin (sil, kopyala, yapıştır, arama vs.).

Örn: dd → satırı siler.

Insert Mod (yazma modu)

Yazı yazmak için bu moda geçilir.

Normal modda i tuşuna bas → Insert moda geçersin.

Esc → tekrar Normal moda dönersin.

Command-line Mod (komut satırı modu)

Dosya üzerinde işlem yapmak için.

: ile girilir.

:w → dosyayı kaydet

:q → çık

:wq → kaydet ve çık

:q! → kaydetmeden çık

Örnek Kullanım
vim deneme.txt   # dosyayı aç
i                # Insert moda gir (yazı yazabilirsin)
<Esc>            # Normal moda dön
:wq              # kaydet ve çık

Avantajları

Çok hızlıdır (özellikle büyük dosyalarda).

Terminal üzerinden çalıştığı için her yerde kullanılabilir.

Kod yazmaya özel güçlü kısayollar ve eklentiler içerir.

Dezavantajları

Öğrenmesi zordur, çünkü mod mantığı ilk başta kafa karıştırıcıdır.

Menü, buton yoktur → tamamen klavye kısayollarıyla çalışır.

# PS1="\[\e[1;32m\]\u@\h:\[\e[1;34m\]\w\[\e[m\]\$ "        
Bu komut, bir terminalde (genellikle Bash veya Zsh gibi) kullanılan bir prompt (komut istemi) ayarını tanımlar. 
PS1, bir kullanıcının terminalde gördüğü ana komut istemini temsil eder.

Komutun detaylarına bakalım:

"\[\e[1;32m\]": Bu kısım, terminaldeki yazının rengini yeşil yapmak için kullanılır.
\u: Kullanıcının adını gösterir.
@\h: Makinenin adını gösterir.
\e[1;34m: Yazının rengini mavi yapmak için kullanılır.
\w: Kullanıcının bulunduğu dizini gösterir.
\e[m: Yazı rengini varsayılan hale döndürür.
\$: Kullanıcının normal bir kullanıcı mı ( $ ) yoksa root kullanıcı mı ( # ) olduğunu gösterir.
Bu komut, terminalde kullanıcı adı, makine adı ve mevcut dizini belirli renklerde göstererek daha okunaklı bir görünüm sağlar.

Bu bir test dosyasıdır.
Nano ile metin düzenlemek kolaydır.