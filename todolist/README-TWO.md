 # Tugas 6
 
 
 ### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
 Asynchronous programming adalah model programing yang dapat dijalankan secara paralel tanpa perlu menunggu satu program selesai dijalankan untuk menjalankan satu program lainnya atau bersifat multithreaded.
 Sedangkan synchronus programming adalah program yang berjalan secara berurutan, suatu program akan dijalankan ketika suatu program sudah selesai dijalankan. Synchronous programming merupakan model programming yang bersifat single-thread.
 

 ### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
 Event-Driven Programming adalah paradigma pemrograman di mana program akan dijalankan berdasarkan event yang terjadi. Contoh event adalah tombol yang diklik atau kursor mouse yang digerakkan. Ketika suatu event terjadi, maka program atau function akan dijalankan. Penerapan pada tugas ini adalah pada saat menekan atau menclick add task maka fungsi langsung dijalankan
 
 
 ### Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX terjadi ketika program tidak perlu mereload halaman ketika program mendapatkan request dari user. Contoh penerapan pada tugas ini dapat dilihat ketika menambahkan sebuah task baru yang mana program akan langsung menambahkan task tanpa perlu mereload halaman.
 
 ### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
 Yang saya lakukan untuk AJAX GET adalah saya menggunakan endpoint /todolist/json yang berisi data todolist sebagai tujuan request method GET yang akan saya buat. Pada todolist.html, saya membuat fungsi yang akan melakukan request ke endpoint /todolist/json dan data yang diperoleh akan diiterasi menjadi elemen html yang nantinya ditambahkan di halaman web. Fungsi tersebut harus selalu di-load setiap kali pengguna mengakses halaman html tersebut.
Selanjutnya untuk AJAX POST saya membuat views yang akan membuatkan objek Task dan mengembalikan JsonResponse sebagai nilai kembaliannya. Nantinya, json tersebut akan diterima oleh template HTML yang sesuai, yakni todolist.html. Setelah itu, saya juga menambahkan path yang mengarahkan kepada views tersebut di urls.py. Untuk setiap kembalian dari views akan diproses di dalam todolist.html menjadi card yang akan ditampilkan di halaman web. Selain itu, saya juga membuat modal untuk menambahkan task dengan menggunakan bootstrap.
