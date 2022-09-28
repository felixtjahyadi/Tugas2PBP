1. CRSF adalah serangan yang membuat pengguna internet  tanpa sadar mengirimkan request (permintaan) kepada suatu aplikasi website melalui aplikasi website yang sedang digunakan. CSRF token adalah suatu nilai yang bersifat unik, rahasia, dan tidak terduga. CSRF token memiliki kegunaan untuk mencegah serangan CSRF (Cross-Site Request Forgery) yang akan membuat penyerang tidak mungkin mengirimkan permintaan palsu pada aplikasi website. Jika tidak ada token tersebut, akan terjadi error dan browser tidak bisa memberikan akses valid kepada pengguna.

2. Iya kita tetap dapat membuat form walau tidak menggunakan suatu generator. Secara gambaran besarnya, pembuatan suatu form secara manual memerlukan segala hal yang menyusun suatu form tersebut, mulai dari judul form, judul setiap parameter input yang dibutuhkan, field atau tempat input, dan tidak lupa format atau style dari tulisan, tata letak, dan fitur lainnya seperti tombol-tombol yang dibutuhkan beserta link ke halaman untuk tombol tersebut. Kita harus mengetahui dasar dari penyusunan secara HTML untuk dapat membuat form tersebut yang kemudian akan menghubungkannya dengan views dan models.

3. Pertama user perlu memasukkan atau mengisi form yang akan di submit. Data dalam form tersebut kemudian di post. Kemudian data akan diolah oleh views untuk disesuiankan dengan model, apabila valid maka akan di save data tersebut ke database. Data tersebut kemudian dapat diproses dengan views untuk diberikan ke HTML.

4. Cara setiap poin:
Poin 1 = Membuat aplikasi dengan menjalankan python manage.py startapp todolist dalam virtual enviroment dalam folder tugas
Poin 2 = Menambahkan urls.py untuk todolist dan melakukan path di urls.py untuk todolist dan juga project_django
Poin 3 = Membuat model Task dengan isi user, date, title, description dengan user menggunakan ForeignKey untuk parameter user yang di import, date menggunakan DateTimeField dan di setting untuk waktu saat ini, title menggunakan CharField, dan description menggunakan TextField.
Poin 4 = Melakukan implementasi registrasi, login, logout sama halnya dengan Lab sebelumnya yaitu membuat fungsi registrasi, login, dan logout beserta HTML registrasi dan login.
Poin 5 = Membuat sebuah todolist.html yang akan menerima username dari user yang menggunakan, tombol-tombol bersangkutan (Tambah Task Baru dan logout), dan sebuah tabel yang berisi date, title, dan description dari task.
Poin 6 = Membuat form dengan membuat dua file yaitu forms.py dan task_create.html, forms.py akan berisikan query atau hal-hal yang akan diambil setelah POST, lalu task_create.html berisikan suatu format form yang akan diisi oleh user.
Poin 7 = Melakukan routing dengan menghubungkan fungsi dalam urls.py milik todolist dengan melakukan path ke masing-masing fungsi.
Poin 8 = Dikarenakan secret masih sama untuk aplikasi Heroku, bisa langsung melakukan add, commit, dan push pada cmd.
Poin 9 = Melakukan registrasi sebanyak 2 kali dan mengisi atau menambahkan task data sebanyak 3 kali.

LINK: https://tugaspbp2.herokuapp.com/todolist/