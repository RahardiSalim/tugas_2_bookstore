# README

Aplikasi Django yang telah di-deploy dapat diakses melalui tautan berikut:
[Link ke Aplikasi PWS](http://rahardi-salim-tugasbookstore.pbp.cs.ui.ac.id)

## 1. Cara Implementasi Checklist

1. **Membuat Proyek Django Baru**
     ```bash
     django-admin startproject book_store
     ```

2. **Membuat Aplikasi dengan Nama `main`**
   - Masuk ke direktori proyek:
     ```bash
     cd book_store
     ```
   - Membuat aplikasi baru dengan nama `main`:
     ```bash
     python manage.py startapp main
     ```

3. **Melakukan Routing pada Proyek**
   - Menambahkan aplikasi `main` ke dalam `INSTALLED_APPS` di `settings.py`:
     ```python
     INSTALLED_APPS = [
        ...
         'main',
     ]
     ```
   - Menambahkan routing di `urls.py` proyek:
     ```python
     from django.contrib import admin
     from django.urls import path, include

     urlpatterns = [
         path('admin/', admin.site.urls),
         path('', include('main.urls')),
     ]
     ```

4. **Membuat Model `Product`**
   - Di dalam `models.py` aplikasi `main`, buat model `Product` dengan atribut yang disebutkan:
     ```python
    from django.db import models

    class Product(models.Model):
        title = models.CharField(max_length=255)
        price = models.FloatField()
        description = models.TextField()

        # Additional Attributes
        author = models.CharField(max_length=255)
        publication_year = models.IntegerField()
        condition = models.CharField(max_length=50)
        image = models.ImageField(upload_to='book_images/', blank=True, null=True)

        def __str__(self):
            return self.title
     ```

5. **Membuat Fungsi di `views.py`**
   - Di `views.py` aplikasi `main`, buat fungsi yang mengembalikan template HTML:
     ```python
    from django.shortcuts import render
    from .models import Product as Book

    def show_main(request):
        books = Book.objects.all()

        context = {
            'books': books,
        }

        return render(request, "main.html", context)
     ```

6. **Membuat Routing di `urls.py` Aplikasi `main`**
   - Membuat file `urls.py` di dalam aplikasi `main` dan tambahkan routing:
     ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'bookstore'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
     ```

7. **Melakukan Deployment ke PWS**
   - **Buat akun dan login** di [PWS](https://pbp.cs.ui.ac.id).
   - **Buat proyek baru (tugasbookstore)** di halaman PWS, lalu simpan **Project Credentials**.
   - Tambahkan URL deployment PWS ke `ALLOWED_HOSTS` di `settings.py`:
     ```python
     ALLOWED_HOSTS = ["localhost", "127.0.0.1", "rahardi-salim-tugasbookstore.pbp.cs.ui.ac.id"]
     ```
   - Lakukan `git add`, `commit`, dan `push` perubahan ke GitHub.
   - Jalankan **Project Command** dari PWS, lalu jalankan:
     ```bash
    git remote add pws https://pbp.cs.ui.ac.id/rahardi.salim/tugasbookstore
    git branch -M master
    git push pws master
     ```
   - **Cek status deployment** di PWS, jika "Running," akses URL PWS.
   - Untuk update selanjutnya, cukup jalankan:
     ```bash
     git push pws main:master
     ```

## 2. Bagan dan Penjelasan Alur Request-Response

Client Request 
    | 
    v 
urls.py
    | 
    v 
views.py
    | 
    v 
models.py  
    | 
    v 
Template HTML
    | 
    v 
Client Response

**Penjelasan:**

- **`urls.py`**: File ini bertanggung jawab untuk mengatur routing URL. Ini menentukan URL mana yang akan memicu fungsi tertentu di views.py. Biasanya, menggunakan path atau re_path untuk menghubungkan URL ke view yang relevan.
- **`views.py`**: Di sini logika aplikasi diproses. Ketika sebuah request diterima, views.py akan mengambil data yang dibutuhkan (dari database melalui model, jika perlu) dan mengirimkannya ke template HTML atau mengembalikan response secara langsung.
- **`models.py`**: File ini digunakan untuk mendefinisikan model yang merepresentasikan struktur data dan skema database. Models berinteraksi dengan database untuk query, insert, update, atau delete data. Jika views.py membutuhkan data dari database, akan diakses melalui models.
- **Template HTML**: Template adalah tempat untuk merender data yang dipersiapkan di views.py. Dengan menggunakan template engine seperti Django template language (DTL), data dari views.py dapat ditampilkan ke pengguna dalam bentuk HTML.

## 3. Fungsi Git dalam pengembangan perangkat lunak

**Fungsi Git**: Git adalah sistem kontrol versi terdistribusi yang sangat populer dalam pengembangan perangkat lunak. Fungsinya adalah untuk memudahkan pengembang dalam mengelola perubahan kode dari waktu ke waktu, melacak siapa yang melakukan perubahan, dan memastikan bahwa semua kolaborator memiliki versi kode yang sama. Beberapa fungsi utama Git meliputi:

- **Manajemen Versi**: Git memungkinkan pengembang untuk menyimpan beberapa versi dari proyek mereka. Jika terjadi kesalahan dalam pengembangan, mereka dapat dengan mudah kembali ke versi sebelumnya tanpa kehilangan kemajuan.
- **Kolaborasi**: Git mendukung kolaborasi tim secara efektif. Pengembang dapat bekerja pada fitur yang berbeda secara bersamaan dan kemudian menggabungkannya menggunakan mekanisme branching dan merging.
- **Riwayat Perubahan**: Git menyimpan semua perubahan yang terjadi pada proyek, sehingga memungkinkan pengembang untuk melacak dan memeriksa apa yang telah diubah, kapan, dan oleh siapa. Ini sangat penting untuk menemukan dan memperbaiki bug atau konflik dalam kode.
- **Branching dan Merging**: Fitur branching memungkinkan pengembang untuk mengerjakan fitur atau perbaikan bug secara independen dari kode utama (main/master). Setelah selesai, perubahan dapat digabungkan kembali (merged) ke branch utama tanpa mengganggu alur kerja lainnya.
- **Distributed Version Control**: Setiap pengembang memiliki salinan penuh dari seluruh riwayat proyek, yang memungkinkan mereka bekerja secara offline dan kemudian melakukan sinkronisasi dengan repositori utama ketika kembali online.

## 4. Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django dijadikan framework awal untuk pembelajaran pengembangan perangkat lunak karena memiliki banyak fitur bawaan ("batteries-included") yang memudahkan pemula memahami berbagai aspek pengembangan web, seperti routing, autentikasi, dan keamanan. Django juga mendorong prinsip DRY (Don't Repeat Yourself), yang mengajarkan pengembangan kode yang efisien dan terstruktur. Selain itu, Django memiliki dokumentasi yang lengkap serta komunitas yang besar, sehingga memudahkan pemula untuk belajar dan mendapatkan bantuan ketika dibutuhkan.

## 5. Mengapa model pada Django disebut sebagai ORM?

Django ORM (Object-Relational Mapper) mengabstraksikan interaksi dengan database menjadi objek Python, sehingga pengembang dapat melakukan operasi database tanpa menulis SQL. ORM ini mendukung berbagai database dan memungkinkan pengelolaan relasi antar model dengan mudah, serta otomatisasi validasi dan migrasi data.