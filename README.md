# PraktikumPBL02-ALTA2A1-SatriaBayuAnanta(036)
Repository ini berisi hasil praktikum UAS mata kuliah Algoritma dan Struktur Data (ALTA) yang berfokus pada pengelolaan database menggunakan SQLite3 dan bahasa pemrograman Python.  
Seluruh kode ditulis dan dijalankan secara modular (terpisah per file) untuk menunjukkan pemahaman terhadap operasi CRUD (Create, Read, Update, Delete) dan Search.

Database yang digunakan: **cars.db**  
Tabel utama: **TBCars**

#Urutan Eksekusi Normal:
1. CreateTable.py = buat tabel dengan menjalankannya cukup sekali saja.
2. InsertData.py = menambahkan isi data dari isi tabel.
3. SelectData.py = untuk memverifikasi data yang sudah masuk.
4. UpdateData.py = untuk mengubah data berdasarkan ID.
5. SelectData.py = untuk mengecek hasil perubahan (update).
6. DeleteData.py = untuk menghapus data berdasarkan ID.
7. SelectData.py = untuk melihat hasil setelah penghapusan.
8. SearchData.py = untuk mencari data tertentu berdasarkan ID.

#Urutan Eksekusi Versi Tambahan:
1. CreateTable.py = buat tabel dengan menjalankannya cukup sekali saja (jika sudah membuat dengan cara sebelumnya, maka biarkan saja dan langsung lanjut langkah kedua).
2. InsertData.py = menambahkan isi data dari isi tabel.
3. SelectData.py = untuk memverifikasi data yang sudah masuk.
4. UpdateData.py = untuk mengubah data berdasarkan ID.
5. SelectData.py = untuk mengecek hasil perubahan (update).
6. InsertData1.py = karena saya ingin membuat ulang datanya dan menambahkan beberapa isi datanya seperti ID 102 dan ID 103.
7. Selectdata.py = untuk mengecek hasil data baru yang sudah masuk.
8. DeleteData.py = untuk menghapus data berdasarkan ID (disini saya ingin menghapus ID 102), namun tanpa print hasilnya diterminal sehingga harus cek kembali ke SelectData.py.
9. SelectData.py = untuk melihat hasil setelah pengahapusan ID 102.
10. DeleteData1.py = untuk menghapus data berdasarkan ID (ID 103), namun pada kode ini akan menampilkan hasilnya diterminal dengan memasukan select * from pada kolom editor dan print(k.fetchall()).
11. InsertData1.py = insert lagi dengan menghapus kembali semua data pada tabel **TBCars** dan membuat ulang isi datanya.
12. SearchData.py = untuk mencari data tertentu berdasarkan ID (disini saya ingin mencari isi data yang diwakili oleh ID 101).
13. SearchData1.py = untuk mencari data tertentu berdasarkan ID (disini saya ingin mencari isi data yang diwakili oleh ID 102).

Seluruh file pada repository ini merupakan hasil dari Praktikum UAS PBL02 yang mengimplementasikan operasi database menggunakan SQLite3 dan Python.
Semua script telah diuji dan berjalan dengan baik secara terpisah sesuai fungsi masing-masing.
Diharapkan repository ini dapat menjadi referensi dalam memahami dasar pengelolaan database menggunakan Python.

Terima kasih.

# Authors:
Nama  : Satria Bayu Ananta

Nim   : 241080200036

Prodi : Informatika - Universitas Muhammadiyah Sidoarjo

Tahun : 2024/2025
