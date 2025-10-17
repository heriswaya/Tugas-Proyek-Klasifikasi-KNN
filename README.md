# Proyek Klasifikasi Hewan dengan K-NN Sederhana

## Deskripsi Singkat

Program ini adalah implementasi sederhana dari algoritma K-Nearest Neighbors (k-NN) untuk memprediksi apakah seekor hewan adalah kucing atau anjing berdasarkan data berat (dalam kg) dan tinggi (dalam cm).

Proyek ini dibuat untuk memenuhi tugas dari Digital Bootcamp AI PRIMA pada tanggal 11 Oktober 2025.

## Tujuan Proyek

Tujuan utama dari proyek ini adalah untuk menerapkan konsep-konsep dasar pemrograman Python sesuai dengan kriteria tugas yang diberikan, yaitu:

* Program terdiri dari minimal **2 modul** (`main.py` dan `knn_functions.py`).
* Menggunakan struktur **kondisional** (`if-else`) dan **looping** (`while`, `for`).
* Menggunakan tipe data **list** dan **dictionary** untuk mengelola data.
* Memiliki mekanisme **error handling** (`try-except`) untuk validasi input pengguna.
* Menerima **input dari pengguna** secara interaktif.

## Cara Menjalankan Program

1.  Pastikan Python sudah terpasang di komputermu.
2.  Clone repository ini ke komputermu.
    ```bash
    git clone [https://github.com/heriswaya/Tugas-Proyek-Klasifikasi-KNN.git](https://github.com/heriswaya/Tugas-Proyek-Klasifikasi-KNN.git)
    ```
3.  Masuk ke direktori proyek yang sudah di-clone.
    ```bash
    cd Tugas-Proyek-Klasifikasi-KNN
    ```
4.  Jalankan file `main.py` melalui terminal atau command prompt.
    ```bash
    python main.py
    ```
5.  Ikuti instruksi yang muncul di terminal untuk memasukkan data berat dan tinggi hewan.

## Struktur File

* `main.py`: File utama yang berfungsi sebagai antarmuka dengan pengguna. File ini menangani proses input, menampilkan menu, dan memanggil fungsi dari modul lain.
* `knn_functions.py`: Modul yang berisi logika inti dari algoritma k-NN. Di dalamnya terdapat data latih (`DATA_LATIH`) dan fungsi-fungsi untuk menghitung jarak serta melakukan prediksi.

## Contoh Penggunaan

Berikut adalah contoh interaksi saat program dijalankan:

```
--- Program Prediksi k-NN Sederhana ---
Masukkan data baru untuk diprediksi:
Masukkan Fitur 1 (berat badan (kg)): 4.5
Masukkan Fitur 2 (tinggi badan (cm)): 26

==> Hasil Prediksi: Label data baru adalah 'Kucing'

Ingin prediksi lagi? (y/n): y

--- Program Prediksi k-NN Sederhana ---
Masukkan data baru untuk diprediksi:
Masukkan Fitur 1 (berat badan (kg)): 14
Masukkan Fitur 2 (tinggi badan (cm)): 43

==> Hasil Prediksi: Label data baru adalah 'Anjing'

Ingin prediksi lagi? (y/n): n
Terima kasih telah menggunakan program ini!
```
