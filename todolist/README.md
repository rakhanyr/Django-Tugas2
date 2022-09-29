# TUGAS 4

link heroku app: https://tugas2-rakhan.herokuapp.com/todolist/

1. CSRF adalah singkatan dari Cross Site Request Forgery. Kegunaan dari CSRF token adalah sebagai sebuah string random yang akan digenerate setiap kali halaman form dibuka. Token dari CSRF akan dikirmkan secara sembunyi dalam bentuk pada bagian Form HTML yang dikirimkan menggunakan metode POST. Biasanya {% csrf_token %} ditempatkan dalam HTML sebelum input dan lokasi mana-pun di mana data yang dapat dikontrol user disematkan dalam HTML. Hal tersebut dilakukan untuk meminimalisir atau menjaga dari penyerangan-penyerangan yang dilakukan oleh penyerang web dalam kata lain adalah sebagai pengamanan. Pengvalidasian user yang mempunyai kewenangan dalam mengakses web dapat berjalan sehingga tidak akan mudah untuk di retas oleh hacker. Jika tidak ada token tersebut maka pengvalidasian tidak berjalan dengan baik.
 
 
2. Bisa, pembuatan form secara manual dapat dilakukan dengan menggunakan tag. Tag-tag yang dapat digunakan adalah seperti tag input, select, option dan semacamnya. Dengan tag-tag tersebut dapat ditambahkan dengan atribut-atribut yang diinginkan dan akan menjadi sebuah variabel dari form tersebut.

 

3. Prosesnya adalah ketika user memasukkan dan memberikan data dengan menklik tombol, browser akan memberikan renspose berupa POST request yang selanjutnya akan di arahkan ke views.py untuk menjalan fungsi yang diminta dengan disesuaikan juga dengan models.py. Kemudian hasil dari input user tersebut akan disimpan ke dalam database. Data yang telah disimpan selanjutnya dapat diaksin oleh user dan juga dapat dilihat pada halaman html.


4. Langkah pertama adalah dengan membuat aplikasi todolist melalui startapp.
Setelah itu adalah menambahkan path yang dibutuhkan kedalam urls.py agar dapat diakses. path yang dibutuhkan adalah aplikasi todolist. Selanjutnya pada models.py ditambahkan kelas task yang berisikan atribut-atribut yang dibutuhkan oleh aplikasi dan dilakukan migrations. 
Selanjutnya adalah membuat fungsi-fungsi yang dibutuhkan seperti register,login,logout dan data yang untuk ditampilkan pada views.py. Selanjutnya menambahkan urls untuk fungsi-fungsi tersebut.
Kemudian membuat templates-templates html untuk menampilkan bentuk atau model halaman yang diinginkan yang ada tombol serta akses untuk fungsi-fungsi yang telah dibuat sebelumnya. 
Terakhir adalah dengan melakukan push dan commit serta deploy ke aplikasi heroku.
