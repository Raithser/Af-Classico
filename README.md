Af Classico

Halo orang-orang berkelas
ini adalah repo untuk project Af Classico, sebuah aplikasi web sederhana berkelas bertemakan football shop dengan basis Django
Dibuat oleh M. Adella Fathir Supriadi (2406495640) dari kelas PBP D Fasilkom UI

👑👑👑 Link Deployment untuk para KING: https://m-adella-tugasindividu.pbp.cs.ui.ac.id/

-------------------------------------------------------------------------------------------------------------------------------

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

-------------------------------------------------------------------------------------------------------------------------------


<img width="1920" height="1080" alt="Teks paragraf Anda" src="https://github.com/user-attachments/assets/d179b1d2-6fe7-47f5-ad6b-49c33f28312c" />



-------------------------------------------------------------------------------------------------------------------------------

Peran settings.py dalam proyek Django

Dalam proyek Django, file settings.py adalah pusat pengaturan yang mengatur cara aplikasi berjalan. Semua hal penting ditulis di sini, mulai dari database yang dipakai, daftar aplikasi yang aktif, hingga tempat menyimpan file seperti gambar, CSS, atau JavaScript. Di dalamnya juga ada SECRET_KEY untuk keamanan, DEBUG untuk menentukan mode pengembangan atau produksi, serta ALLOWED_HOSTS yang mengatur siapa saja yang boleh mengakses aplikasi. Selain itu, settings.py juga mengatur middleware (lapisan yang memproses request dan response), template HTML, bahasa, zona waktu, sampai aturan keamanan password. Singkatnya, settings.py bisa dibilang adalah “otak” proyek Django, karena hampir semua pengaturan utama proyek ada di dalam file ini.

-------------------------------------------------------------------------------------------------------------------------------

Cara kerja migrasi database di Django:
1. Buat atau lakukan edit pada models.py di direktori proyek
2. Jalankan:
	python manage.py makemigrations (Django membuat file migrasi)
3. Jalankan:
	python manage.py migrate (Django eksekusi intruksi ke database)
Migrasi akan membuat database tetap sinkron dengan kode yang ada

-------------------------------------------------------------------------------------------------------------------------------

Kenapa Django cocok untuk menjadi framework pertama:
- Django memiliki banyak fitur siap pakai 
- Django memiliki pola struktur yang jelas (MVT)
- Dokumentasi Django salah satu yang terbaik di open source
- Banyak tutorial resmi + komunitas yang besar
- Django memiliki fitur keamanan bawaan
- Django auto generate halaman admin
- ORM memungkinkan mengakses database tanpa perlu paham SQL
- Dipakai dan diaplikasikan di dunia nyata
  
-------------------------------------------------------------------------------------------------------------------------------

Feedback untuk asisten dosen:
Sudah sangat membantu

-------------------------------------------------------------------------------------------------------------------------------
