
# Host, Hypervisor, Guest
1️⃣ Host (veya Host Server)

Fiziksel makine / sunucu anlamına gelir.

İçinde işletim sistemi, CPU, RAM, disk vs. gibi donanımlar vardır.

Örneğin: Bir veri merkezinde duran gerçek sunucu kasası → bu host server.

Sanallaştırma (virtualization) yapılırken bu fiziksel kaynaklar parçalanıp farklı sanal makineler (VM) arasında paylaştırılır.

Kısaca: "Ev sahibi". Misafirlere (guest VM’lere) ortam sağlayan ana makine.

2️⃣ Hypervisor

Host’un kaynaklarını bölüştürüp sanal makineleri çalıştıran yazılım katmanıdır.

Hypervisor olmadan host üzerinde birden çok VM çalıştıramazsın.

Türleri:

Type 1 (Bare-metal): Direkt fiziksel donanım üzerinde çalışır. (VMware ESXi, Microsoft Hyper-V, Xen, KVM)

Type 2 (Hosted): Normal işletim sistemi üstünde çalışır. (Oracle VirtualBox, VMware Workstation)

Örnek: Senin bilgisayarına VirtualBox kurup içine Ubuntu VM açman → VirtualBox burada hypervisor.

3️⃣ Guest (veya Guest VM)

Hypervisor tarafından oluşturulan sanal makinelerdir.

Her biri ayrı bir işletim sistemi çalıştırır (Linux, Windows vb.).

Host’un donanım kaynaklarını hypervisor aracılığıyla kullanır.

AWS EC2 instance’larını düşünebilirsin → onlar aslında guest VM’lerdir.

Kısaca: "Misafir". Host’un kaynaklarını kiralayıp çalışan sanal sistem.

AWS’de bağlantı:

AWS veri merkezindeki fiziksel host server → donanım.

Bu donanımın üstünde çalışan hypervisor → sanallaştırma katmanı (AWS kendi Xen/KVM tabanlı hypervisor kullanıyor).

Senin oluşturduğun EC2 instance → guest VM.