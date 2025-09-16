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

===============================================================================================================================
README TUGAS 2

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery penting karena akan membuat pengalaman user yang mengunjungi website kita lebih baik. Data delivery yang kurang baik bisa jadi membuat latensi tinggi (10 detik ga respon-respon) yang akan membuat pengalaman user juga turun drastic untuk mengunjungi website kita Kembali
-------------------------------------------------------------------------------------------------------------------------------
Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurutku JSON lebih baik dari pada XML. Hal ini dikarenakan JSON lebih mudah dibaca dan mirip dengan struktur objek di pemrograman sehari-hari, ini juga lah yang membuat kenapa JSON lebih popular dibanding XML yang lebih sulit dibaca.  
-------------------------------------------------------------------------------------------------------------------------------
Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

is_valid() memiliki fungsi penting yang tidak bisa kita abaikan begitu saja. is_valid() akan mengecek apakah data yang dimasukkan oleh user masuk sesuai aturan validasi, ini membuat database memiliki data yang konsisten, mengurangi kesalahan input user, memberi keamanan tambahan, dan memberi feedback error
-------------------------------------------------------------------------------------------------------------------------------
Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token penting karena ini akan mengamankan sesi login ke browser yang sedang kita akses. Jika kita tidak punya csrf_token, maka bisa ada penyerang yang bisa memanfaatkan hal tersebut dengan cara memanfaatkan session login aktif user saat ini
-------------------------------------------------------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------------------------------------------------------


<img width="1021" height="926" a<img width="1085" height="945" alt="Screenshot 2025-09-17 024802" src="https://github.com/user-attachments/assets/d50fb195-3713-4d39-99f7-a96a4e6d1bb3" />
lt="Screenshot 2025-09-17 024755" src="https://github.com/user-attachments/assets/c63a2542-ffc8-46b9-983c-1a10fc88dbca" />
<img width="1120" height="908" alt="Screenshot 2025-09-17 024809" src="https://github.com/user-attachments/assets/b6f50a78-ee42-4115-9526-7b5ddf649cf3" />
<img width="1064" height="910" alt="Screenshot 2025-09-17 024814" src="https://github.com/user-attachments/assets/efbeecbd-1fd0-48bc-a443-90af63503384" />

-------------------------------------------------------------------------------------------------------------------------------
Asdos sudah membantu dan keren
-------------------------------------------------------------------------------------------------------------------------------










