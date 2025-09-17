
# komuttaki kullanımda davranış farklı değil, ama kullanım sonucu ve kısa devre (short-circuit) davranışı bazen kafa karıştırıyor.

cmd1 && cmd2 → cmd1 başarılıysa (exit 0) cmd2 çalışır. Aksi halde cmd2 çalışmaz.

cmd1 || cmd2 → cmd1 başarısızsa (exit ≠ 0) cmd2 çalışır. Aksi halde cmd2 çalışmaz.

! cmd → cmd’nin başarısını tersine çevirir (başarılıysa ! ile başarısız olur).

Shell, bu operatörlerde short-circuit yapar: gerektiği anda sonraki komutu çalıştırmayıp atlar.

Neden senin gözlemine uyar?

“and için 1. komut çalışırsa diğer çalışıyordu” → bu tam && davranışı: ls dosya && cat dosya — ls varsa başarılı olur (0), o zaman cat çalışır.

“ilk komut çalışmazsa ikinci komut çalışıyordu” → bu || davranışı: grep foo file || echo "yok" — grep hata verirse (eşleşme yok veya dosya yok) echo çalışır.

Dikkat: zincirlerdeki karışıklık

cmd1 && cmd2 || cmd3 yazdığında:

cmd1 başarılıysa cmd2 çalışır; sonra cmd2 başarısızsa cmd3 çalışır.

Yani cmd3 sadece cmd1 veya cmd2’nin başarısız olduğu durumlarda çalışabilir — bu bazen istenenden farklı olur.
Gruplamak için parantez veya if kullanmak daha güvenlidir.