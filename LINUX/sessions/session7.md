
# .bashrc dosyasına MY_VAR2=LinuxIsGreat yazma ile export MY_VAR3="LinuxIsGreat" yazma arasında fark var mı?

Evet, büyük fark var!

Fark:
MY_VAR2=LinuxIsGreat (export olmadan)
Shell değişkeni (local variable)
Sadece mevcut shell'de görünür
Alt process'lere geçmez (subshell, script'ler göremez)
export MY_VAR3="LinuxIsGreat"
Environment değişkeni
Alt process'lere geçer (subshell, script'ler görür)
Sistem genelinde erişilebilir
Test edelim:
bashrc'ye ekleyin:
echo 'MY_VAR2=LinuxIsGreat' >> ~/.bashrc
echo 'export MY_VAR3="LinuxIsGreat"' >> ~/.bashrc
source ~/.bashrc  # Yeniden yükle
Mevcut shell'de ikisi de görünür:
echo $MY_VAR2    # LinuxIsGreat
echo $MY_VAR3    # LinuxIsGreat

Alt shell'de test:
bash -c 'echo MY_VAR2: $MY_VAR2'    # Boş!
bash -c 'echo MY_VAR3: $MY_VAR3'    # LinuxIsGreat

Script'te test:
echo 'echo "MY_VAR2: $MY_VAR2"' > test.sh
echo 'echo "MY_VAR3: $MY_VAR3"' >> test.sh
test.sh
MY_VAR2: (boş)
MY_VAR3: LinuxIsGreat

# Farklar
1. .bashrc içine şunu yazmak:
MY_VAR2=LinuxIsGreat


Bu sadece shell değişkeni tanımlar.

Yani bu değişken sadece tanımlandığı shell oturumunda geçerli olur.

echo $MY_VAR2 yazdığında görürsün.

Ama child process (alt süreçler) bu değişkeni göremez (örn: başka bir script veya komut çalıştırdığında).

2. .bashrc içine şunu yazmak:
export MY_VAR3="LinuxIsGreat"


Bu hem shell değişkeni tanımlar hem de onu environment variable yapar.

Yani sadece bulunduğun shell’de değil, o shell’den doğan alt süreçler de bu değişkeni görür.

Örneğin python, bash script, veya başka bir program bu değişkene erişebilir.

3. Terminale direkt export ile değişken tanımlamak:
export TESTVAR=Hello


Bu da geçerli oturum (shell instance) için environment variable oluşturur.

Hiçbir yere (dosyaya) kaydedilmez.

Yeni bir terminal açarsan, o terminal sıfırdan başlar → bu değişkeni bulamazsın.

4. Neden .bashrc içine yazıyoruz?

.bashrc her yeni bash açıldığında otomatik çalıştırılır.

O yüzden .bashrc içine yazılan değişkenler kalıcı olur (her yeni oturumda tekrar tanımlanır).

Terminale direkt export yazarsan, sadece o oturum için geçerlidir → kapatınca kaybolur.