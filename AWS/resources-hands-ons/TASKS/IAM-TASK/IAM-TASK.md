# Task: IAM Role with S3 Full Access and EC2 Instances

## Goal:
1. Create an IAM Role with S3 Full Access.
2. Launch two EC2 instances:
   - One with the IAM Role attached.
   - One without any IAM Role.
3. Configure both instances using the given user data script and ensure HTTP port access.

---

## Steps:

### 1. Create an IAM Role:
- **Name**: `TechProS3Role`
- **Trusted Entity**: AWS services
- **Use Case**: EC2
- **Permissions**: S3FullAccess (AmazonS3FullAccess)

---

### 2. Launch Two EC2 Instances:
#### Instance 1: Without IAM Role
- **AMI**: Amazon Linux 2023
- **Instance Type**: t2.micro
- **IAM Role**: None
- **User Data**:
```bash
#!/bin/bash
yum update -y
yum install -y httpd
cd /var/www/html
aws s3 cp s3://techpro-role-task/index.html .
aws s3 cp s3://techpro-role-task/cat.jpg .
systemctl enable httpd
systemctl start httpd
```

---

#### Instance 2: With IAM Role
- **AMI**: Amazon Linux 2023
- **Instance Type**: t2.micro
- **IAM Role**: `TechProS3Role`
- **User Data**:
```bash
#!/bin/bash
yum update -y
yum install -y httpd
cd /var/www/html
aws s3 cp s3://techpro-role-task/index.html .
aws s3 cp s3://techpro-role-task/cat.jpg .
systemctl enable httpd
systemctl start httpd
```

---

### 3. Security Group Configuration:
- Allow **HTTP (Port 80)** and **SSH (Port 22)** for both instances.

---

### Expected Outcome:
1. Instance without IAM Role:
   - Unable to fetch files from the S3 bucket.
   - Web server fails to serve the page.
2. Instance with IAM Role:
   - Successfully fetches files from the S3 bucket.
   - Web server serves the page with `index.html` and `cat.jpg`.


# EC2 instance’a IAM rolü (IAM Role) atamak.
Bu rol, o EC2’nun AWS servislerine (S3, CloudWatch, DynamoDB, vs.) erişim izni olup olmadığını belirler.
Şimdi adım adım anlatayım 

EC2 oluştururken doğrudan rol atayabilirsin.
Ama aynı zamanda sonradan da atamak mümkündür.

1️⃣ Oluşturma sırasında (en yaygın yöntem)

EC2 Launch ekranında şu adımları takip edersin:

AWS Console → EC2 → Launch Instance

AMI, instance type, key pair, vs. seçtikten sonra

“Configure Instance Details” (veya “Advanced details”) bölümüne gel

Burada şu alanı görürsün:

IAM instance profile: [Select an IAM Role]


Açılır listeden mevcut bir IAM rolü seçebilirsin.

Bu rol EC2’ya bağlanır ve instance başlatıldığında otomatik olarak geçerli olur.
Yani EC2 içine aws s3 cp gibi komut yazdığında, Access Key/Secret Key girmene gerek kalmaz — çünkü rol zaten izin verir.

2️⃣ Sonradan atamak (var olan EC2’ya)

Bazen EC2’yu rol atamadan başlatırsın. Bu durumda sonradan da ekleyebilirsin 

EC2 Dashboard → Instances → Instance seç

Üst menüden: Actions → Security → Modify IAM Role

Açılan listeden bir IAM Role seç ve Save de.

Not:

EC2’yu yeniden başlatmana gerek yoktur.

Ancak IAM rolünün S3 erişimi varsa (AmazonS3ReadOnlyAccess gibi), sadece o izinlere göre işlem yapılabilir.

3️⃣ Eğer rol yoksa:

Rolü oluşturmak için şu yolu izlersin:

IAM → Roles → Create role

Trusted entity olarak “EC2” seç

İzin politikası (örneğin AmazonS3ReadOnlyAccess) ekle

İsmini ver → EC2-S3-Access-Role

Oluştur

Sonra EC2 launch ederken bu rolü seçebilirsin
