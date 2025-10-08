
# IAM (Identity and Access Management) Nedir?

IAM, AWS kaynaklarına kimlerin (kullanıcı, servis, uygulama) erişeceğini
ve ne yapabileceğini (izinler/policies) kontrol etmeni sağlayan bir güvenlik servisidir.

Yani IAM ile “Kime ne kadar yetki vereyim?” sorusunun cevabını belirlersin.

1. User (Kullanıcı)

AWS hesabında oluşturduğun bireysel kullanıcı hesaplarıdır.

Her kullanıcının kendi giriş bilgileri (şifre, access key) olur.

Kullanıcı, konsoldan (GUI) veya programatik olarak (CLI/SDK) giriş yapabilir.

İki tür erişim vardır:
Erişim Türü	Açıklama
Console Access	AWS web arayüzünden giriş yapma (kullanıcı adı + şifre)
Programmatic Access	CLI veya SDK üzerinden erişim (Access Key ID + Secret Key)
Örnek:

Bir şirkette:

Feyyaz → Developer

Zeynep → Tester
Bu kişilerin her biri için ayrı IAM user oluşturulur.

2. User Group (Kullanıcı Grubu)

Benzer roller veya görevleri olan kullanıcıları gruplandırırsın.

Yetkiyi gruba verirsin, kullanıcılar otomatik olarak o yetkileri alır.

Örnek:
Grup	Policy (Yetki)
Developers	EC2, S3 erişimi
Testers	Sadece S3 read erişimi
Admins	FullAccess

Böylece 10 kullanıcı varsa, her birine ayrı policy vermek yerine,
gruba dahil edersin, yönetim kolaylaşır.

3. Role (Rol)

Bu en kritik kavramlardan biridir.

Bir role kullanıcı değil, AWS servisi veya uygulama bürünür.

Role, bir geçici kimlik gibidir.

Örneğin bir EC2 instance’ın, S3’e erişmesi gerekiyorsa:

EC2’ye bir IAM Role atanır.

O role’nin içinde “S3’e erişim izni” vardır.

EC2 artık S3’e güvenli şekilde erişebilir, şifre/anahtar gerekmez.

Avantaj:

Güvenlik açısından access key kullanmazsın.

EC2, Lambda, ECS gibi servisler için idealdir.

Örnek:
Role Adı	Policy
EC2-S3-Access	S3FullAccess
Lambda-DynamoDB-Role	DynamoDBWriteAccess

4. Policy (Yetki Belgesi)

Policy = “Bu kişi ne yapabilir, ne yapamaz?”ı belirleyen JSON belgesi.

Her policy, şu 4 şeyi içerir:

Alan	Açıklama
Effect	Allow veya Deny
Action	Hangi işlemler? (s3:PutObject, ec2:StartInstances vs.)
Resource	Hangi kaynakta? (arn:aws:s3:::mybucket/*)
Condition	Opsiyonel ek kural (örneğin IP veya zaman şartı)
Örnek Policy:
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::feyyaz-bucket/*"
    }
  ]
}


Bu policy diyor ki:

Bu kullanıcı S3’teki feyyaz-bucket içindeki dosyaları okuyabilir ve yükleyebilir.

IAM’de Yetki Mantığı (Kural)

Varsayılan olarak herkesin erişimi YOKTUR.

Yani AWS, “deny by default” ilkesini uygular.
Sen açıkça “Allow” demedikçe hiçbir şey yapılamaz.

Yetki sırası:

Explicit Deny → her zaman baskındır

Explicit Allow → izin verir

Varsayılan Deny → hiçbir şey tanımlanmadıysa erişim yoktur

Gerçek Hayatta Örnek Senaryo

Bir şirket düşün:

Kullanıcı	Rolü	Yetkisi
Ali	Developer	EC2 ve S3 erişimi
Ayşe	Tester	Sadece S3 read
EC2 Instance	Role: EC2-S3-Access	S3 write izinli

IAM yapısı:

2 user: Ali, Ayşe

2 group: Developers, Testers

1 role: EC2-S3-Access

3 policy:

S3ReadOnlyAccess

S3FullAccess

EC2FullAccess

Özet Görsel Mantık
User  --> Group  --> Policy
Role  --> Policy


Kullanıcılar ve roller, policy’lerle izin kazanır.
Ama kullanıcılar aynı zamanda gruplar aracılığıyla da policy’lere sahip olabilir.

# Programmatic access, SDK ve Boto3 
1. Programmatic Access (Programatik Erişim)

Bu, AWS kaynaklarına kod yazarak erişmek anlamına gelir.
Yani AWS Management Console’a (web arayüzüne) girip elle tıklamak yerine,
API, CLI veya SDK kullanarak AWS servislerini yönetirsin.

Örnek:

EC2 instance başlatmak istiyorsun:

Konsolda tıklayarak yapabilirsin (manual access)

Ama programatik erişimle kod yazarak veya komutla yaparsın 

aws ec2 start-instances --instance-ids i-1234567890abcdef0


İşte bu programmatic accesstir.

Bunun için AWS sana Access Key ID ve Secret Access Key verir.
Bu iki anahtar, senin hesabına kimlik doğrulaması sağlar (şifre gibi).

2. SDK (Software Development Kit)

Bir SDK, yazılımcılara AWS servislerine kolayca bağlanmak için hazır kütüphaneler sunar.
Yani “her şeyi sıfırdan HTTP isteğiyle yazmak” yerine, SDK kullanırsın.

Örnek SDK’lar:

AWS SDK for Java

AWS SDK for Python (Boto3)

AWS SDK for JavaScript / Node.js

AWS SDK for Go, C#, PHP …

Bu SDK’lar, AWS API’lerini kolaylaştırılmış fonksiyonlara dönüştürür.

Örnek (Python SDK — Boto3):

import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='my-demo-bucket')


Bu satır aslında arkada AWS S3 API çağrısı yapar ama sen API yazmadan işini halledersin.

3. Boto3 (AWS SDK for Python)

Boto3, AWS’in Python için resmi SDK’sıdır.

Python kodu yazarak EC2, S3, DynamoDB, Lambda gibi servisleri kontrol etmeni sağlar.

Otomasyon, DevOps scriptleri, data processing, backup gibi işlemler için çok kullanılır.

Örnek:

import boto3

ec2 = boto3.resource('ec2')

Yeni bir EC2 instance oluştur
instance = ec2.create_instances(
    ImageId='ami-0abcdef12345',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)
print("Yeni EC2 başlatıldı:", instance[0].id)


Bu kod, web arayüzüne hiç girmeden EC2 makinesi oluşturur 

4. Hepsi nasıl bağlantılı?
Kavram	Ne işe yarar	Örnek
Programmatic Access	AWS’i kodla yönetmeni sağlar	Access key ile CLI veya SDK üzerinden erişim
SDK	API’leri kolaylaştıran kütüphaneler	AWS SDK for Python (Boto3)
Boto3	AWS SDK for Python’un özel adı	boto3.client('s3') ile bucket oluşturma
Access Key / Secret Key	Programatik erişim için kimlik doğrulaması	CLI veya Boto3 kullanırken gerekir
Gerçek Senaryo:

Sen bir Spring Boot uygulaması geliştiriyorsun.
Uygulamanın dosyaları AWS S3’e yüklensin istiyorsun.
Seçeneklerin:

Web arayüzünden elle yüklemek (manuel, zahmetli)

Programmatic access kullanmak 

Java SDK (AWS SDK for Java) kullanırsın.

Access key ve secret key tanımlarsın.

Kodla dosyayı otomatik olarak S3’e gönderirsin.

# Gerçek hayatta AWS konsol, cli ve sdk nasıl kullanılır?
Küçük işler için Console,
Büyük, profesyonel işler için SDK veya CLI kullanılır.

1. AWS Management Console (Web Arayüzü)

Tarayıcıdan girersin (aws.amazon.com → Console).

Tıklayarak EC2 oluşturur, S3’te dosya yüklersin, IAM kullanıcı ekler vs.

Görseldir, çok kolaydır, öğrenme ve test aşaması için idealdir.

Gerçek Hayatta Nerede Kullanılır?

Yeni başlayan geliştiriciler

Küçük test ortamları

Acil veya manuel işlemler

Avantajı: Kolay, tıklayarak her şeyi görebilirsin
Dezavantajı: Tek tek yapmak zorundasın, otomasyon yok

2. AWS CLI (Command Line Interface)

Konsoldaki işleri komut satırıyla yapmanı sağlar.

Konsolda tıklamak yerine tek bir komutla yaparsın.

Otomatikleştirilebilir (ör. script yazarsın, her gün yedek alınır).

Örnek:

aws s3 cp myfile.txt s3://my-bucket/


Bu tek satır, konsolda 5-6 adım tıklamayı yapar.

Gerçek Hayatta Nerede Kullanılır?

DevOps, SRE (Site Reliability Engineer), System Admin

CI/CD (GitHub Actions, Jenkins) süreçlerinde

Otomatik deploy ve yedekleme işlemlerinde

Avantajı: Hızlı, script yazılabilir
Dezavantajı: Yeni başlayanlar için gözle görülemez, ezber zor

3. AWS SDK (örn. Boto3, Java SDK)

Kod içinde AWS servislerini kullanmanı sağlar.

Yani uygulamanın bir parçası olur.

Örnek:
Bir web uygulaması kullanıcının yüklediği dosyayı doğrudan S3’e yüklerse,
arka planda kodda şöyle bir SDK çağrısı vardır:

s3Client.putObject("my-bucket", "file.png", fileInputStream);


Bu işlem AWS Console’da elle yapılmaz — uygulama kodu otomatik yapar.

Gerçek Hayatta Nerede Kullanılır?

Backend uygulamaları (Spring Boot, Django, Node.js)

Otomasyon scriptleri

Mikroservisler

Avantajı: Tam otomasyon, ölçeklenebilirlik
Dezavantajı: Kod bilgisi gerekir