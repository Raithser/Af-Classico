Af Classico

Halo orang-orang berkelas
ini adalah repo untuk project Af Classico, sebuah aplikasi web sederhana berkelas bertemakan football shop dengan basis Django
Dibuat oleh M. Adella Fathir Supriadi (2406495640) dari kelas PBP D Fasilkom UI

👑👑👑 Link Deployment untuk para KING: https://m-adella-tugasindividu.pbp.cs.ui.ac.id/

---

Cara pengimplentasian checklist:
1. Inisialisasi Proyek Django
- Buka direktori utama
- Open terminal dan aktifkan virtual environment
- Install Django 
- Buat aplikasi baru bernama main
- Daftarkan main ke dalam installed apps di settings.py
2. Routing proyek Django
- Menambahkan path('', include('main.urls')) di urls.py project utama
- Membuat file urls.py di main
3. Membuat model
- menambahkan 

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
- lalu dimigrasikan
  
4. Membuat fungsi views.py
- Membuat fungsi show_main di views.py untuk merender template HTML
5. Membuat template
- Buat folder templates di dalam main
- Menambahkan main.html yang berisi konten yang akan ditampilkan di website
6. Deployment
- Push ke repo GitHub
- Deploy ke PWS

---


<img width="1920" height="1080" alt="Teks paragraf Anda" src="https://github.com/user-attachments/assets/d179b1d2-6fe7-47f5-ad6b-49c33f28312c" />



---

Peran settings.py dalam proyek Django

Dalam proyek Django, file settings.py adalah pusat pengaturan yang mengatur cara aplikasi berjalan. Semua hal penting ditulis di sini, mulai dari database yang dipakai, daftar aplikasi yang aktif, hingga tempat menyimpan file seperti gambar, CSS, atau JavaScript. Di dalamnya juga ada SECRET_KEY untuk keamanan, DEBUG untuk menentukan mode pengembangan atau produksi, serta ALLOWED_HOSTS yang mengatur siapa saja yang boleh mengakses aplikasi. Selain itu, settings.py juga mengatur middleware (lapisan yang memproses request dan response), template HTML, bahasa, zona waktu, sampai aturan keamanan password. Singkatnya, settings.py bisa dibilang adalah “otak” proyek Django, karena hampir semua pengaturan utama proyek ada di dalam file ini.

---

Cara kerja migrasi database di Django:
1. Buat atau lakukan edit pada models.py di direktori proyek
2. Jalankan:
	python manage.py makemigrations (Django membuat file migrasi)
3. Jalankan:
	python manage.py migrate (Django eksekusi intruksi ke database)
Migrasi akan membuat database tetap sinkron dengan kode yang ada

---

Kenapa Django cocok untuk menjadi framework pertama:
- Django memiliki banyak fitur siap pakai 
- Django memiliki pola struktur yang jelas (MVT)
- Dokumentasi Django salah satu yang terbaik di open source
- Banyak tutorial resmi + komunitas yang besar
- Django memiliki fitur keamanan bawaan
- Django auto generate halaman admin
- ORM memungkinkan mengakses database tanpa perlu paham SQL
- Dipakai dan diaplikasikan di dunia nyata
  
---

Feedback untuk asisten dosen:
Sudah sangat membantu




---
## README TUGAS 2

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery penting karena akan membuat pengalaman user yang mengunjungi website kita lebih baik. Data delivery yang kurang baik bisa jadi membuat latensi tinggi (10 detik ga respon-respon) yang akan membuat pengalaman user juga turun drastic untuk mengunjungi website kita Kembali
---
Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurutku JSON lebih baik dari pada XML. Hal ini dikarenakan JSON lebih mudah dibaca dan mirip dengan struktur objek di pemrograman sehari-hari, ini juga lah yang membuat kenapa JSON lebih popular dibanding XML yang lebih sulit dibaca.  
---
Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

is_valid() memiliki fungsi penting yang tidak bisa kita abaikan begitu saja. is_valid() akan mengecek apakah data yang dimasukkan oleh user masuk sesuai aturan validasi, ini membuat database memiliki data yang konsisten, mengurangi kesalahan input user, memberi keamanan tambahan, dan memberi feedback error
---
Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token penting karena ini akan mengamankan sesi login ke browser yang sedang kita akses. Jika kita tidak punya csrf_token, maka bisa ada penyerang yang bisa memanfaatkan hal tersebut dengan cara memanfaatkan session login aktif user saat ini
---
 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

1. menambahkan template utama yang berfungsi sebagai base template 
2. menambahkan arah direktori template tersebut ke DIRS di settings.py
3. menambahkan extends base html untuk setiap html baru yang dibuat
4. membuat form atau isian data yang nantinya akan diberi ke user
5. menambah fungsi dan menambah import di views.py
6. menambahkan url baru di urls.py di main dan mengimport fungsi yang seblumnya dibuat
7. edit main html untuk membuat tombol pengarah ke form.py yang sebelumnya sudah dibuat   
8. tambah berkas html sesuai dengan fungsi yang dibuat di views.py sebelumnya
9. tambah CSRF trusted origins di settings.py
10. tambahkan import di views.py dan buat fungsi baru untuk menampilkan versi XML atau JSON nya
11. tambah path baru di urls.py dan import juga
12. Melakukan add-commit-push ke GitHub
---


<img width="1085" height="945" alt="Screenshot 2025-09-17 024802" src="https://github.com/user-attachments/assets/d50fb195-3713-4d39-99f7-a96a4e6d1bb3" />
<img width="1120" height="908" alt="Screenshot 2025-09-17 024809" src="https://github.com/user-attachments/assets/b6f50a78-ee42-4115-9526-7b5ddf649cf3" />
<img width="1064" height="910" alt="Screenshot 2025-09-17 024814" src="https://github.com/user-attachments/assets/efbeecbd-1fd0-48bc-a443-90af63503384" />
<img width="1021" height="926" alt="Screenshot 2025-09-17 024755" src="https://github.com/user-attachments/assets/d8187f40-b085-4f8e-9ac4-43bd15af12b2" />

---
Feedback untuk asisten dosen:
Sudah sangat membantu

---
## TUGAS 3

Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

Django AuthenticationForm adalah form bawaan Django yang dipakai untuk proses login. Lokasinya ada di django.contrib.auth.forms. Proses login ini termasuk Validasi username dan password, Penanganan error otomatis, Integrasi dengan sistem autentikasi Django. AuthenticationForm ini memiliki banyak kelebihan, diantaranya: 
- Sudah terintegrasi dengan user model Django
- Validasi otomatis (username exists, password correct)
- Security features built-in (hashing, sanitization)
- Customizable (bisa ditambah field/validasi)
- Error handling yang baik

Selain kelebihan-kelebihan tersebut, AuthenticationForm ini juga memiliki kekurangan yaitu: 
- Terikat dengan Django (kurang fleksibel untuk sistem external)
- Defaultnya sederhana (perlu customization untuk fitur kompleks)
- Limited fields (hanya username/password defaultnya)
---
Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?

Autentikasi (Authentication): proses memverifikasi identitas user ➝ Contoh: apakah username dan password cocok?. Otorisasi (Authorization): proses menentukan apa yang boleh dilakukan user setelah ia terautentikasi ➝ Contoh: user ini boleh akses dashboard admin atau tidak? 

Untuk implementasi di Django. Autentikasi: ditangani oleh django.contrib.auth {authenticate(), login()}, sedangkan Otorisasi: ditangani dengan sistem permissions dan groups {@login_required, @permission_required}.

Autentikasi bisa dianalogikan sebagai cek identitas, sedangkan otorisasi adalah cek hak akses

---
Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Cookies
Kelebihan:
- Disimpan di client - Tidak bebani server
- Cepat - Tidak perlu query database
- Work dengan load balancing - Stateless 
Kekurangan:
- Size terbatas (~4KB per cookie)
- Rentan security risks (XSS, theft)
- User bisa disable/ubah cookies
- Hanya bisa simpan string

Session
kelebihan: 
- Aman - Data disimpan di server
- Kapasitas besar - Tidak terbatas seperti cookies
- Bisa simpan data kompleks (object, list, dll)
- Auto-expire berdasarkan Waktu
Kekurangan:
- Butuh storage server (database, cache)
- Performance impact (harus query ke database)
- Scalability issues (untuk aplikasi distributed)
---
Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Cookies masih memiliki beberapa celah keamanan. Celah keamanan yang dimiliki cookies, diantaranya: 
- XSS (Cross-Site Scripting) - Cookie bisa dicuri via JavaScript
- Session Hijacking - Penyeran mencuri session cookie
- Man-in-the-Middle - Cookie intercepted di jaringan
- CSRF (Cross-Site Request Forgery) - Request palsu dengan cookie user

Django menangani celah-celah tersebut dengan beberapa cara, yaitu:
- Django set cookie sessionid sebagai HttpOnly
- Bisa diatur SESSION_COOKIE_SAMESITE untuk mencegah CSRF lintas domain
- Django mendukung SESSION_COOKIE_SECURE = True (hanya terkirim lewat HTTPS)
- Django punya CSRF protection middleware (csrftoken)
---
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.

1. membuat fungsi register di views.py, lalu membuat html baru di templates untuk register ini, tambahkan juga import di urls.py di direktori main dan di urlpatterns agar user dapat mengakses html nya
2. ulangi Langkah 1 untuk login dan logout
3. tambahkan otorisasi di views.py main, yaitu import login_required
4. di showmain dan showproduct tambahkan login_required untuk otorisasi

5. di views.py main tambahkan import baru untuk cookie
6. ubah kode di fungsi login_user agar menyimpan cookie dengan nama last_login yang isinya timestamp terakhir login
7. tambahkan variable baru di show_main untuk last_login cookies nya
8. ubah fungsi logout agar menghapus cookie saat pengguna logout
9. tambahkan visual sesi terakhir login dengan mengedit main.html di main templates

10. tambahkan import user di models.py main 
11. tambahkan variable Bernama user untuk menghubungkan user dengan model di class product
12. penghubungan ini bermanfaat untuk setiap product terasosiasi dengan seorang user

![WhatsApp Image 2025-09-23 at 17 40 19_7327d0cd](https://github.com/user-attachments/assets/7879c5bc-b932-4af8-8536-f06c19468ed0)

![WhatsApp Image 2025-09-23 at 17 40 36_998f71c1](https://github.com/user-attachments/assets/c9dfb5b0-4479-40c2-979c-2503fe8b99f4)

---
Feedback untuk asisten dosen:
Sudah sangat membantu

---
# Tugas 4
---
## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Dalam CSS, urutan prioritas selector ditentukan oleh konsep spesifisitas yang menghitung bobot masing-masing selector. Secara berurutan dari prioritas tertinggi ke terendah adalah: deklarasi !important, inline style yang ditulis langsung pada elemen HTML, selector ID, selector class/attribute/pseudo-class, dan terakhir selector element/pseudo-element. Jika terdapat beberapa selector dengan bobot sama, yang muncul terakhir dalam stylesheet yang akan diterapkan. Memahami urutan prioritas ini sangat penting untuk menghindari konflik style dan memastikan tampilan yang konsisten sesuai desain yang direncanakan.

---
## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Responsive design menjadi konsep kritis dalam pengembangan web modern karena semakin beragamnya perangkat yang digunakan untuk mengakses internet. Dengan responsive design, sebuah website dapat menyesuaikan layout, ukuran teks, dan gambarnya secara otomatis berdasarkan ukuran layar perangkat pengguna. Contoh aplikasi yang sudah menerapkan responsive design adalah Tokopedia dan Netflix, yang menawarkan pengalaman optimal baik di desktop maupun mobile. Sebaliknya, banyak website pemerintah atau sistem legacy yang belum responsive, menyebabkan pengguna mobile harus melakukan zoom dan scroll horizontal yang mengganggu pengalaman. Responsive design tidak hanya meningkatkan user experience, tetapi juga berpengaruh pada SEO karena search engine seperti Google memberikan prioritas lebih tinggi pada website mobile-friendly.

---
## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Dalam model kotak (box model) CSS, margin, border, dan padding memiliki fungsi berbeda meskipun semuanya berhubungan dengan ruang di sekitar elemen. Margin adalah jarak di luar elemen, berfungsi memberi ruang antara satu elemen dengan elemen lainnya. Border adalah garis tepi yang mengelilingi elemen, biasanya bisa diatur ketebalan, warna, dan jenis garisnya. Sedangkan padding adalah jarak antara konten elemen dengan border, sehingga memberi ruang di dalam elemen. Misalnya pada sebuah "<div>", margin akan mengatur jarak kotak itu dengan elemen lain, border menjadi bingkai kotaknya, dan padding memberi ruang agar teks di dalamnya tidak menempel langsung pada border.

---
## Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox dan grid adalah dua teknik modern dalam CSS untuk mengatur tata letak. Flexbox berfungsi untuk mengatur elemen dalam satu dimensi, bisa berupa baris horizontal atau kolom vertikal. Dengan flexbox, developer mudah membuat elemen sejajar, memberi jarak otomatis, atau meratakan item ke tengah, sehingga cocok untuk navbar, tombol sejajar, atau layout sederhana. Grid layout lebih canggih karena mendukung tata letak dua dimensi, yakni baris dan kolom sekaligus. Dengan grid, kita bisa membuat layout kompleks seperti galeri foto, dashboard, atau halaman majalah digital. Intinya, flexbox lebih cocok untuk kontrol satu arah, sedangkan grid lebih cocok untuk struktur dua arah yang lebih kompleks.

---
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.

1. tambahkan tag viewport agar web dapat menyesuaikan ukuran untuk platform berbeda, tambahkan juga script tailwind di base.html nya
2. tambahkan fungsi edit product di views.py main, buat berkas html nya di main/templates, tambah juga import di urls.py main dan pathnya di urlpattern
3. edit main.html di main/templates agar bisa nampilin tombol editnya
4. ulangi Langkah 2 & 3 untuk fungsi delete news
5. buat navbar.html di templates root (tempat base.html), tautin navbar.html ke main.html di main/templates pakai include
6. di settings.py tambahkan Middleware whitenoise, pastiin juga konfig STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL sudah benar
7. buat berkas baru Bernama static di root, lalu tambahkan berkas css, di berkas itu tambahkan file css 
8. hubungkan file css tersebut ke base.html
9. Styling navbar, css global tadi, login , dan regist html
10. buat html baru untuk styling productnya di main/templates
11. styling product detail, create product, dan edit product

---
## Feedback untuk asisten dosen:
Sudah sangat membantu




