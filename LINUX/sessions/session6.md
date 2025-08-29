
# grep "^ca" /bin - HATALI KULLANIM

grep dosya içeriğini okur, dosya isimlerini değil
/bin bir dizin, dosya değil - o yüzden "Is a directory" hatası
^ca burada "ca ile başlayan satırları" arar (dosya isimleri değil!)

ls "^ca" - HATALI KULLANIM

ls dosya isimlerini listeler
Tırnak içinde yazdığınız için shell wildcard yorumlaması yapmaz
Literal olarak ^ca isimli bir dosya arar (böyle dosya yok)

DOĞRU KARŞILAŞTIRMA:
Dosya isimleri için:
ls ca*           # ca ile başlayan DOSYA İSİMLERİ
ls | grep "^ca"  # ca ile başlayan DOSYA İSİMLERİ (farklı yöntem)

Dosya içerikleri için:
grep "^ca" /etc/passwd    # Dosya içinde ca ile başlayan SATIRLAR
grep "ca" /etc/passwd     # Dosya içinde ca geçen SATIRLAR

# ls ca*

Shell ca* wildcard'ını genişletir → ls 
ca-legacy cal captoinfo cat catchsegv catman
Doğrudan dosya isimlerini listeler

ls | grep "^ca"

ls tüm dosyaları listeler (her satırda bir dosya ismi)
Bu liste pipe ile grep'e gönderilir
grep bu listeyi (dosya isimlerini) satır satır okur
^ca ile başlayan satırları (yani dosya isimlerini) filtreler

Anahtar nokta:
grep burada dosya içeriği değil, ls'nin çıktısını (dosya isimlerinin listesi) okuyor!

cd test
export TECHPRO=env.var
EDUCATION=shell.var
vim script2.sh
cat script2.sh 
echo " Normalde $TECHPRO değeri olarak env.var görmeliyiz. Ama shell değişkeni $EDUCATION değerini shell.var olarak  görmemeliyiz."
chmod +x script2.sh
./script2.sh
Normalde env.var değeri olarak env.var görmeliyiz. Ama shell değişkeni  değerini shell.var olarak  görmemeliyiz.
vim script2.sh
cat script2.sh 
EDUCATION=shell.var
echo " Normalde $TECHPRO değeri olarak env.var görmeliyiz. Ama shell değişkeni $EDUCATION değerini shell.var olarak  görmemeliyiz."
./script2.sh 
Normalde env.var değeri olarak env.var görmeliyiz. Ama shell değişkeni shell.var değerini shell.var olarak  görmemeliyiz.

# Hata değişken kullanımında! $(...) komut ikamesi için, değişkenler için ${} veya $ kullanılır.
Sorun:
bash$(TECHPRO)    #  HATALI - komut çalıştırmaya çalışır
$(EDUCATION)  #  HATALI - komut çalıştırmaya çalışır
Doğru kullanım:
bash${TECHPRO}    # DOĞRU - değişken değerini alır
${EDUCATION}  #  DOĞRU - değişken değerini alır
# veya
$TECHPRO      #  DOĞRU - basit kullanım
$EDUCATION    #  DOĞRU - basit kullanım
Script'inizi düzeltin:
bash# script2.sh dosyasını şöyle değiştirin:
echo "Normalde ${TECHPRO} değeri olarak env.var görmeliyiz. Ama shell değişkeni ${EDUCATION} değerini shell.var olarak görmemeliyiz."
Test edin:
Komut satırında:
echo "Normalde ${TECHPRO} değeri olarak env.var görmeliyiz. Ama shell değişkeni ${EDUCATION} değerini shell.var olarak görmemeliyiz."
Fark:

$(komut): Komut çalıştırır ve çıktısını alır
${degisken}: Değişkenin değerini alır
$degisken: Değişkenin değerini alır (basit form)