# HotelUYU

> Dibuat oleh tim Mekatronika dan Kecerdasan Buatan 2021 UPI Purwakarta
>
> > - Reyhan Praditya Bagaskara - <reyhan_pb@upi.edu>
> > - [Lintang Gemilang](https://github.com/lintang2) - <lintanggmlng@upi.edu>
> > - [Muhammad Ihsan Hilmi](https://github.com/MIhsanHilmi) - <ihsanhilmi822@upi.edu>

## Daftar Isi

> 1. [Tentang](#Tentang)
> 2. [Rancangan Aplikasi](#rancangan-aplikasi)
> 3. [Panduan Instalasi](#panduan-instalasi)
> 4. [Kilasan](#Kilasan)
> 5. [Referensi](#Referensi)

## Tentang

> Problem: problem dalam pemesanan kamar hotel yang masih menggunakan kertas karna bisa saja kertas itu hilang dan data menjadi tidak aman, tidak efisien, dan memakan waktu yang tidak sedikit.
> 
> Solusi: dengan membuat aplikasi ini data yang dimasukan lebih aman dan jelas siapa yang memesan, memesan kamar tipe apa, dan kamar no berapa, lebih efisien dan tidak memakan waktu yang banyak.

## Rancangan Aplikasi

> 1. Flowchart
> ![flowchart](https://user-images.githubusercontent.com/105422801/173191737-b0f6f7bb-1b5a-4108-b8da-50fc69f9a84a.png)
> 2. ERD 
> ![ERD](https://user-images.githubusercontent.com/105422801/173192671-3d21db4e-bf5c-4f9f-af78-27b9172765c4.png)

## Panduan Instalasi

> Untuk menggunakan aplikasi ini 
> 1. Clone aplikasi dari github dengan command :
> `git clone https://github.com/MIhsanHilmi/HotelUYU.git`
> 2. Import HotelUYU.sql ke database server yang digunakan
> 3. Buka terminal/command prompt di dalam folder HotelUYU, atau buka terminal/command prompt dan ketik
> `cd {lokasi clone}\HotelUYU`
> 4. Buat virtual environment python dengan command :
> `py -m venv venv`
> 5. Jalankan virtual environment nya dengan command :
> `venv\Scripts\activate`
> 6. Install flask dan komponen komponen lain yang dibutuhkan dengan command :
> `pip install flask
   pip install flask-bootstrap
   pip install flask-mysqldb`
> 7. Run aplikasi dengan command : 
> `flask run`
> 8. Pada terminal/command promptnya, akan terlihat ip beserta port untuk mengakses aplikasi. Buka browser dan masukkan ip address beserta port yang tertera.
> 9. Login dengan user yang tersedia di database. Password bisa dilihat di file HotelUYU.sql

## Kilasan

> + Halaman Login Admin
  ![Halaman Login](https://user-images.githubusercontent.com/105422690/173188939-cffd9d6b-2d65-4a3a-af41-006e0c7d2e73.png)
> + Halaman Lihat Pesanan Kamar
  ![Halaman Lihat Pesanan Kamar](https://user-images.githubusercontent.com/105422690/173189058-40615ee3-4b09-4f76-810e-00cbb978af52.png)
> + Halaman Tambah Data Pesanan
  ![Halaman Tambah Data Pesanan](https://user-images.githubusercontent.com/105422690/173189203-64c3563c-db7a-4f0d-b80e-e947b5cc4768.png)

## Referensi

> Program ini dibuat dengan teknologi:
>
> - [Flask Web Framework](https://flask.palletsprojects.com/en/2.1.x/)
> - [Bootstrap CSS Framework](https://getbootstrap.com/)
> - [AdminLTE 3 Bootstrap Template](https://adminlte.io/)
>
> Special Thanks To:
>
> - Bapak Rezka Bunaiya Prayudha, S.T., M.Eng.
> - [StackOverflow](https://stackoverflow.com/)
