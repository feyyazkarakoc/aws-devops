
# “Launch Template” konusu DevOps, AWS Cloud Architect ve Practitioner rollerinde tamamen farklı derinlikte ele alınır: 

Launch Template Nedir?

Launch Template, bir EC2 instance başlatma “reçetesidir” (şablonudur).
Yani şunu tanımlar:

Hangi AMI (image) kullanılacak,

Hangi instance type (t2.micro, m5.large...),

Key pair,

Security group,

IAM role,

User data (bootstrap script),

Storage volume ayarları,

Network ayarları (subnet, VPC vs.)

Yani manuel EC2 oluşturmak yerine, bu bilgileri bir şablonda tutarsın ve otomatik, tutarlı, tekrar edilebilir instance’lar oluşturursun.

1️⃣ AWS Practitioner (Temel Düzey – İşlevi Anlama Odaklı)

Bakış açısı: “Launch Template nedir, neden var?”

Amaç: EC2 başlatmayı kolaylaştırmak ve standartlaştırmak.

Kullanıcı: Teknik olmayan ama AWS kullanmayı bilen kişiler (örneğin proje yöneticisi).

Mantık:

Tek tek EC2 ayarı yapmaya gerek kalmasın.

Her defasında aynı yapı (örneğin aynı AMI, aynı güvenlik kuralları).

Cost optimization (örneğin uygun instance’ı otomatik seçmek).

Kavrayacağı düzey:

Launch Template = EC2 başlatma ayarlarını kaydeden bir şablondur, zamandan ve hatadan tasarruf sağlar.

2️⃣ DevOps Engineer (Otomasyon & CI/CD Odaklı)

Bakış açısı: “Bunu nasıl otomatikleştiririm?”

DevOps açısından Launch Template:

Infrastructure as Code (IaC) mantığının bir parçasıdır.

Auto Scaling Group (ASG), Elastic Load Balancer (ELB) ve CI/CD pipeline ile entegre çalışır.

User Data içine bash script koyarak, instance ilk açıldığında otomatik kurulum (örneğin yum install nginx) yapar.

Versioning destekler → her değişiklikte yeni bir sürüm oluşturabilirsin (v1, v2, ...).

Terraform, CloudFormation, Ansible gibi araçlarla otomatik olarak oluşturulabilir.

DevOps için kritik kullanım örnekleri:

Jenkins pipeline’da yeni sürüm deploy edileceğinde Launch Template v3 kullan.

Auto Scaling Group’a “latest template version” bağla → yeni sürümde otomatik scale.

Rolling update yap → sıfır kesintiyle yeni versiyon instance’lara geçiş.

Kavrayacağı düzey:

Launch Template = Otomatik ölçeklenen, versiyonlanabilen, CI/CD süreçlerinde kullanılan EC2 yapılandırma şablonudur.

3️⃣ Cloud Architect (Mimari & Tasarım Odaklı)

Bakış açısı: “Bu yapıyı nasıl en verimli, güvenli ve ölçeklenebilir hale getiririm?”

Cloud Architect açısından Launch Template:

Mimari yapı taşıdır.

Auto Scaling Group, Spot Fleet, ECS Cluster gibi yapılarda “template reference” olarak kullanılır.

Şirket genelinde standart EC2 kurulum politikaları uygulanır (örneğin her template’te aynı IAM rolü, aynı tagging politikası).

Template’ler multi-region ve multi-account ortamlarda versiyon kontrolüyle yönetilir.

Security compliance (örneğin AMI’lerin CIS-hardened olması) kontrol edilir.

Lifecycle management (örneğin her 6 ayda bir AMI güncellemesi + template güncellemesi).

Kavrayacağı düzey:

Launch Template = EC2 altyapısının güvenli, standart ve ölçeklenebilir yönetimi için kullanılan temel yapı taşıdır.