# README

Aplikasi Django yang telah di-deploy dapat diakses melalui tautan berikut:
[Link ke Aplikasi PWS](http://rahardi-salim-tugasbookstore.pbp.cs.ui.ac.id)

# TUGAS 2

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
- **`Template HTML`**: Template adalah tempat untuk merender data yang dipersiapkan di views.py. Dengan menggunakan template engine seperti Django template language (DTL), data dari views.py dapat ditampilkan ke pengguna dalam bentuk HTML.

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

# TUGAS 3

## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery sangat penting dalam pengimplementasian sebuah platform karena memungkinkan transfer data antara server dan klien secara efisien. Tanpa data delivery, sebuah platform tidak akan mampu menyediakan informasi dinamis atau interaktif kepada pengguna. Data delivery mencakup pengiriman data dari server ke klien (seperti tampilan halaman web) maupun dari klien ke server (seperti form submission). Implementasi ini penting untuk berbagai jenis aplikasi yang membutuhkan interaksi real-time, personalisasi, dan validasi data secara langsung. Data delivery juga memastikan bahwa pengguna dapat berkomunikasi dengan platform secara efektif, memungkinkan fungsionalitas yang lebih interaktif dan dinamis, misalnya dalam aplikasi e-commerce, platform media sosial, atau layanan SaaS.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Secara umum, JSON (JavaScript Object Notation) dianggap lebih baik dibandingkan XML (Extensible Markup Language) dalam konteks pengiriman data pada web modern. Hal ini karena beberapa alasan:

Simplicity (Kesederhanaan): JSON lebih sederhana dan mudah dibaca dibandingkan XML. JSON memiliki sintaks yang lebih ringkas karena tidak memerlukan tag pembuka dan penutup seperti XML.

Effisiensi: JSON menghasilkan ukuran data yang lebih kecil dibandingkan XML, sehingga lebih cepat untuk di-parse dan ditransfer di jaringan.

Native Support: JSON didukung secara native oleh banyak bahasa pemrograman, terutama JavaScript, yang membuatnya mudah digunakan dalam aplikasi web modern. Sementara XML memerlukan parsing yang lebih kompleks.

Struktur Data: JSON mendukung struktur data seperti array dan objek dengan lebih natural, sedangkan XML lebih berfokus pada struktur dokumen hierarkis.

JSON lebih populer dibandingkan XML karena faktor kesederhanaan, kecepatan, dan dukungan yang luas dalam pengembangan aplikasi web. Sebagian besar API modern menggunakan JSON karena kemudahan integrasinya dengan framework front-end.

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django digunakan untuk memeriksa apakah data yang di-submit melalui form memenuhi syarat validasi yang telah didefinisikan. Method ini melakukan dua hal penting:

Validasi data: Django memeriksa setiap field dalam form berdasarkan aturan validasi yang ditentukan di model atau form itu sendiri, misalnya apakah field yang diisi sesuai dengan tipe data yang diharapkan.

Membersihkan data: Jika validasi berhasil, method ini juga akan membersihkan data yang dimasukkan, mengubahnya ke format yang dapat digunakan lebih lanjut dalam aplikasi.

Kita membutuhkan method ini untuk memastikan bahwa data yang dikirim oleh pengguna valid sebelum diproses lebih lanjut (misalnya disimpan ke database). Jika method ini tidak digunakan, aplikasi bisa mengalami masalah seperti crash akibat data yang tidak sesuai, atau lebih buruk lagi, menerima input yang bisa membahayakan keamanan sistem.

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token (Cross-Site Request Forgery token) adalah token keamanan yang digunakan untuk melindungi aplikasi dari serangan CSRF. CSRF adalah jenis serangan di mana seorang penyerang mencoba mengirimkan permintaan palsu atas nama pengguna yang sudah terautentikasi, tanpa sepengetahuan pengguna.

Jika kita tidak menambahkan csrf_token pada form, maka aplikasi Django menjadi rentan terhadap serangan ini. Penyerang dapat memanfaatkan sesi aktif pengguna dan mengirimkan permintaan berbahaya (misalnya, transfer dana atau perubahan pengaturan akun) tanpa persetujuan pengguna.

Dengan menambahkan csrf_token, server akan memverifikasi bahwa permintaan tersebut benar-benar berasal dari form yang dibuat oleh aplikasi, sehingga serangan semacam ini dapat dicegah.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### 5.1 Membuat Input Form untuk Menambahkan Objek Model:
- Saya membuat form untuk setiap model yang ada (Author, Publisher, Category, Product(Book), Customer, Order, OrderItem, Review) dan memasukan field field apa saja yang perlu di input pada forms.py .
- Saya membuat views baru seperti create_author, create_publisher, dan lainnya, yang menggunakan form ini untuk menangani input dari pengguna. Jika form valid, data akan disimpan ke database, dan pengguna akan diarahkan ke halaman yang sesuai (seperti author_list).
- Setiap view dihubungkan dengan template HTML sederhana yang menampilkan form untuk memasukkan data.

### 5.2 Menambahkan 4 Fungsi Views untuk Menampilkan Objek dalam Format XML dan JSON:

- Saya menambahkan 4 views baru: dua untuk menampilkan semua objek dalam format JSON dan XML (book_list_json, book_list_xml), dan dua lainnya untuk menampilkan objek spesifik berdasarkan ID dalam format JSON dan XML (book_detail_json, book_detail_xml).
- Untuk JSON, saya menggunakan JsonResponse untuk mengonversi queryset menjadi JSON. Sedangkan untuk XML, saya menggunakan Django's serializers.serialize() untuk mengonversi queryset menjadi XML.
- Pada view book_detail_json dan book_detail_xml, saya memanfaatkan get_object_or_404() untuk mengambil objek berdasarkan ID, dan kemudian menampilkan data dalam format yang sesuai.

### 5.3 Membuat Routing URL untuk Masing-masing Views:

- Saya menambahkan routing untuk setiap view yang telah dibuat ke dalam urls.py. Contohnya, untuk JSON dan XML, saya membuat route /books/json/ dan /books/xml/ untuk menampilkan semua data buku, serta /books/json/<uuid:id>/ dan /books/xml/<uuid:id>/ untuk menampilkan data buku berdasarkan ID. URL ini memastikan bahwa setiap permintaan yang masuk dapat diarahkan ke view yang sesuai, baik untuk form input maupun untuk menampilkan data dalam format yang diminta.

## POSTMAN LINK

[![XML](./Tugas3MediaFolder/XML.png)]()
[![XML with ID](./Tugas3MediaFolder/XMLwithID.png)]()
[![JSON](./Tugas3MediaFolder/JSON.png)]()
[![JSON with ID](./Tugas3MediaFolder/JSONwithID.png)]()

# TUGAS 4

## 1. Perbedaan antara `HttpResponseRedirect()` dan `redirect()`

### `HttpResponseRedirect()`
`HttpResponseRedirect` adalah kelas Django yang mengembalikan respons HTTP 302, mengarahkan pengguna ke URL yang ditentukan. Ini adalah cara manual untuk melakukan redirect di Django dan memerlukan URL yang dihasilkan atau dikodekan secara eksplisit.

**Karakteristik**:
- Memerlukan URL tujuan dalam bentuk string secara manual.
- Digunakan jika ingin mengendalikan lebih banyak aspek dari response.

### `redirect()`
`redirect()` adalah shortcut yang disediakan oleh Django untuk melakukan redirect dengan lebih sedikit kode. Selain menerima string URL, `redirect()` juga dapat menerima nama view dan argumen untuk memudahkan pembuatan URL dinamis.

**Karakteristik**:
- Dapat menerima string URL, nama view, atau bahkan objek model, dan akan otomatis melakukan resolusi URL.
- Lebih fleksibel dan user-friendly, lebih sering digunakan dalam praktik karena memudahkan pengelolaan URL.

## 2. Cara Kerja Penghubungan Model `Product` dengan `User`

Dalam Django, model `Product` dapat dihubungkan dengan model `User` (biasanya dari `django.contrib.auth.models.User`) melalui beberapa tipe relasi, tergantung pada kebutuhan aplikasi. Misalnya:

### **ForeignKey Relationship**
Jika setiap produk dimiliki oleh satu pengguna, kita dapat menggunakan ForeignKey:
```python
from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
```

### **ManyToManyField**
Jika suatu produk bisa dimiliki oleh lebih dari satu pengguna (misalnya wishlist atau shared ownership), kita dapat menggunakan ManyToManyField:
```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
```

### Cara Kerja:
- **ForeignKey**: Relasi satu ke banyak, di mana satu produk dimiliki oleh satu pengguna.
- **ManyToManyField**: Relasi banyak ke banyak, di mana satu produk bisa dimiliki oleh banyak pengguna dan satu pengguna bisa memiliki banyak produk.


## 3. Perbedaan antara Authentication dan Authorization

### **Authentication (Otentikasi)**
Otentikasi adalah proses memverifikasi identitas pengguna, biasanya dengan cara memeriksa kredensial seperti username dan password. Otentikasi menjawab pertanyaan: *Apakah pengguna ini adalah siapa yang mereka klaim?*

### **Authorization (Otorisasi)**
Otorisasi adalah proses menentukan hak akses pengguna setelah identitas mereka diverifikasi. Ini menjawab pertanyaan: *Apa yang diizinkan pengguna ini untuk lakukan?*

### **Proses Saat Pengguna Login**
1. **Otentikasi**: Saat pengguna memasukkan kredensial, Django akan memverifikasi melalui sistem otentikasinya, biasanya mencocokkan username dan password.
2. **Otorisasi**: Setelah pengguna berhasil masuk (authenticated), Django menggunakan sistem izin (permissions) untuk menentukan apa yang diizinkan pengguna tersebut lakukan.

### **Implementasi di Django**
- Django menyediakan sistem otentikasi bawaan dengan model `User` dan `authenticate()`.
- Django menggunakan sistem `permissions` dan `groups` untuk menangani otorisasi. Izin dapat ditentukan pada level objek dan model.

## 4. Bagaimana Django Mengingat Pengguna yang Telah Login?

Django menggunakan **session** dan **cookies** untuk mengingat pengguna yang telah login. Setelah pengguna berhasil login, Django menyimpan informasi sesi pada server dan mengirimkan cookie ke browser pengguna yang berisi ID sesi.

### **Cara Kerja**:
1. Saat pengguna login, Django membuat record sesi di server (misalnya di database).
2. Django mengirimkan cookie yang berisi session ID ke browser pengguna.
3. Setiap kali pengguna mengunjungi situs, browser mengirimkan cookie ini kembali ke server sehingga Django dapat mengidentifikasi pengguna berdasarkan ID sesi tersebut.

### **Kegunaan Lain dari Cookies**
- **Menyimpan preferensi pengguna**: Misalnya, bahasa pilihan atau tema.
- **Melacak aktivitas pengguna**: Digunakan untuk analitik atau personalisasi iklan.
- **Otentikasi**: Cookies dapat digunakan untuk mempertahankan sesi login atau token autentikasi.

### **Keamanan Cookies**
Tidak semua cookies aman untuk digunakan, terutama jika cookies tidak dienkripsi atau tidak menggunakan protokol aman seperti HTTPS. Jenis cookies:
- **Session Cookies**: Lebih aman karena hanya bertahan selama sesi browsing aktif.
- **Persistent Cookies**: Bertahan setelah sesi berakhir dan berpotensi menjadi target serangan.
- Cookies harus ditandai sebagai `HttpOnly` untuk mencegah akses melalui JavaScript dan `Secure` untuk hanya dikirim melalui koneksi HTTPS.

Berikut adalah langkah-langkah detail untuk mengimplementasikan checklist yang diberikan berdasarkan kode dan aplikasi Django yang sudah kamu buat:

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### **Langkah 1: Mengimplementasikan Fungsi Registrasi, Login, dan Logout**
1. **Fungsi Registrasi**: 
   - Tujuan dari fungsi ini adalah untuk memungkinkan pengguna baru membuat akun. Saya menggunakan `UserCreationForm` bawaan dari Django, yang menyediakan form pendaftaran standar.
   - Ketika form valid, saya memanggil `form.save()` untuk menyimpan pengguna baru dan kemudian mengarahkan pengguna ke halaman login.
   
   **Kode**:
   ```python
   def register(request):
       form = UserCreationForm()

       if request.method == "POST":
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               messages.success(request, 'Your account has been successfully created!')
               return redirect('bookstore:login')
       context = {'form': form}
       return render(request, 'register.html', context)
   ```

2. **Fungsi Login**:
   - Menggunakan `AuthenticationForm` untuk menangani login pengguna. Ketika form valid dan kredensial benar, saya memanggil `login()` untuk membuat sesi pengguna dan menyimpan `last_login` di cookie menggunakan `response.set_cookie()`.
   
   **Kode**:
   ```python
   def login_user(request):
       if request.method == 'POST':
           form = AuthenticationForm(data=request.POST)
           if form.is_valid():
               user = form.get_user()
               login(request, user)
               response = HttpResponseRedirect(reverse("bookstore:show_main"))
               response.set_cookie('last_login', str(datetime.datetime.now()))
               return response
       else:
           form = AuthenticationForm(request)
       context = {'form': form}
       return render(request, 'login.html', context)
   ```

3. **Fungsi Logout**:
   - Setelah pengguna logout, cookie `last_login` dihapus, dan sesi pengguna juga dihapus menggunakan fungsi `logout()`.
   
   **Kode**:
   ```python
   def logout_user(request):
       logout(request)
       response = HttpResponseRedirect(reverse('bookstore:login'))
       response.delete_cookie('last_login')
       return response
   ```

### **Langkah 2: Membuat Dua Akun Pengguna dan Tiga Dummy Data**
1. **Membuat Akun Pengguna**:
   - Setelah menambahkan fitur registrasi, saya mendaftarkan dua akun pengguna baru melalui halaman registrasi di aplikasi Django.
   
2. **Menambahkan Dummy Data Produk**:
   - Saya membuat tiga produk dummy untuk setiap pengguna menggunakan form `ProductForm`. Form tersebut mengisi informasi produk seperti nama, harga, brand, dan kategori yang dikaitkan dengan pengguna yang sedang login.

   [![2User](./Tugas3MediaFolder/2User.png)]()
   [![6Dummy](./Tugas3MediaFolder/6Dummy.png)]()

### **Langkah 3: Menghubungkan Model `Product` dengan `User`**
- Model `Product` telah memiliki ForeignKey yang menghubungkan produk ke `User`. ForeignKey ini berfungsi agar setiap produk dapat dihubungkan dengan pengguna tertentu yang membuat atau mengunggah produk tersebut.
  
  **Kode pada model `Product`**:
  ```python
  class Product(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      ...
  ```

- Pada saat produk dibuat menggunakan form `ProductForm`, saya menetapkan bahwa `product.user` diisi dengan `request.user` (pengguna yang sedang login).
  
  **Kode**:
  ```python
  def create_product(request):
      if request.method == 'POST':
          form = ProductForm(request.POST, request.FILES)
          if form.is_valid():
              product = form.save(commit=False)
              product.user = request.user  # Set the product owner to the logged-in user
              product.save()
              form.save_m2m()
              return redirect('bookstore:product_list')
      else:
          form = ProductForm()
      return render(request, 'product_form.html', {'form': form})
  ```

### **Langkah 4: Menampilkan Detail Informasi Pengguna yang Sedang Login**
- Pada halaman utama (`show_main`), saya menampilkan detail pengguna yang sedang login, seperti username. Saya juga memanfaatkan cookies untuk menampilkan kapan terakhir kali pengguna login (`last_login`).
  
  **Kode**:
  ```python
  @login_required(login_url='/login')
  def show_main(request):
      products = Product.objects.all()
      context = {
          'products': products,
          'last_login': request.COOKIES.get('last_login', 'Never'),
          'name': request.user.username,
      }
      return render(request, "main.html", context)
  ```

### **Langkah 5: Penerapan dan Penggunaan Cookies**
- Saat pengguna login, saya menyimpan `last_login` dalam bentuk cookie di browser mereka. Cookie ini digunakan untuk menampilkan waktu terakhir kali pengguna login di halaman utama aplikasi.
- Penggunaan cookie pada aplikasi ini terbatas pada penyimpanan informasi sederhana seperti waktu login terakhir. Cookies yang digunakan adalah `session cookies` yang akan dihapus saat pengguna logout atau menutup browser.

  ```python
  response.set_cookie('last_login', str(datetime.datetime.now()))
  ```