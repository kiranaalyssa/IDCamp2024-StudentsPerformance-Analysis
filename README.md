# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech - Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan yang telah berdiri sejak tahun 2000. Institusi ini telah menghasilkan banyak lulusan berprestasi dengan reputasi yang baik di berbagai bidang. Namun, terdapat pula sejumlah siswa yang tidak berhasil menyelesaikan pendidikannya (dropout).

**Tingginya angka dropout** menjadi tantangan besar bagi institusi pendidikan. Oleh karena itu, Jaya Jaya Institut berupaya mendeteksi secara dini mahasiswa yang berisiko mengalami dropout, agar mereka dapat menerima bimbingan dan pendampingan khusus.

## Permasalahan Bisnis
Untuk mengatasi permasalahan tersebut, Jaya Jaya Institut berupaya mengenali lebih awal mahasiswa yang berpotensi mengalami dropout. Dengan begitu, institusi dapat memberikan perhatian dan dukungan khusus yang dibutuhkan agar siswa tetap termotivasi dan mampu menyelesaikan pendidikannya. Beberapa pertanyaan bisnis yang dirangkum sebagai acuan untuk menghasilkan solusi, sebagai berikut:
1. Bagaimana distribusi status mahasiswa secara keseluruhan?
2. Program studi mana yang paling banyak mengalami dropout?
3. Apakah status pernikahan memengaruhi tingkat dropout?
4. Apakah terdapat perbedaan dropout antara laki-laki dan perempuan?
5. Apakah penerima beasiswa cenderung lebih kecil kemungkinannya untuk dropout?

## Cakupan Proyek
Proyek ini bertujuan untuk mengembangkan solusi berbasis data dalam mendeteksi pola mahasiswa yang berpotensi mengalami dropout. Cakupan utama proyek meliputi:
* Pengembangan model Machine Learning untuk memprediksi status mahasiswa, apakah akan dropout atau tidak.
* Pembuatan dashboard interaktif yang menyajikan visualisasi distribusi pola mahasiswa berdasarkan statusnya (dropout, graduate, enroll), guna mempermudah analisis dan pengambilan keputusan.

## Persiapan
Dataset dibawah ini berasal dari sebuah institusi pendidikan tinggi dan berisi data mahasiswa dari berbagai program studi. Informasi yang tersedia meliputi data awal pendaftaran (riwayat akademik, demografi, dan faktor sosial-ekonomi) serta performa akademik mahasiswa pada akhir semester pertama dan kedua. Dataset digunakan untuk membangun model klasifikasi yang memprediksi kemungkinan mahasiswa dropout atau lulus.

Sumber Data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

Setup Environment:

Proyek ini dapat dijalankan dengan dua cara, yaitu secara lokal atau menggunakan Google Colab.

**Opsi 1:** Ikuti perintah berikut untuk menjalankan proyek secara lokal (Terminal / Shell).
```
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```
**Opsi 2:** Jika ingin menjalankan proyek ini di Google Colab, cukup jalankan perintah berikut di awal notebook.
```
pip install streamlit==1.45.1 pandas==2.2.3 numpy==2.2.5 joblib==1.5.0 scikit-learn==1.6.1 seaborn==0.13.2 matplotlib==3.10.0
```
## Business Dashboard
Dashboard ini dirancang untuk membantu mengidentifikasi pola dan karakteristik mahasiswa yang memiliki kemungkinan besar untuk mengalami dropout. Dengan menampilkan metrik kunci (KPI) serta visualisasi interaktif, dashboard ini memudahkan pengguna dalam memahami distribusi dan tren data mahasiswa berdasarkan berbagai atribut. Dashboard ini terbagi menjadi dua bagian utama:

**1. Key Performance Indicators (KPI)**
Bagian ini menampilkan metrik utama terkait data mahasiswa secara ringkas, yaitu:
* Total Students: Jumlah seluruh mahasiswa yang terdaftar di institusi.
* Total Student Dropout: Jumlah mahasiswa yang tercatat telah melakukan dropout.
* Student Dropout Rate: Persentase mahasiswa yang dropout dibandingkan total siswa.
* Total Scholarship Holders: Jumlah mahasiswa yang menerima beasiswa.
* Average Student Grade: Nilai rata-rata dari seluruh mahasiswa berdasarkan data akademik semester.

**2. Visualisasi Data Menggunakan Diagram**
Bagian ini menyajikan visualisasi untuk menggambarkan distribusi siswa dropout berdasarkan beberapa kategori penting, yaitu:
* Student Status Distribution: Pie chart yang menampilkan distribusi status mahasiswa (dropout, graduate, enroll) secara keseluruhan.
* Student Dropout by Course Category: Bar Chart yang menampilkan jumlah mahasiswa dropout berdasarkan kategori atau program studi yang diambil.
* Student Dropout by Marital Status: Bar chart yang membandingkan tingkat dropout antara maha siswa berdasarkan status pernikahan.
* Student Dropout by Gender: Pie Chart yang menunjukkan perbandingan jumlah mahasiswa dropout berdasarkan jenis kelamin.
* Student Dropout by Scholarship Holder: Bar Chart yang menjelaskan apakah status penerima beasiswa berpengaruh terhadap kemungkinan mahasiswa mengalami dropout.

Berikut link dashboard: https://lookerstudio.google.com/reporting/41969044-3c4c-4d4b-96c0-53c219c67a43

## Menjalankan Sistem Machine Learning
Sistem Machine Learning ini dirancang untuk memprediksi status mahasiswa berdasarkan data yang tersedia, seperti nilai akademik, status beasiswa, dan faktor lainnya.

Aplikasi ini memungkinkan pengguna untuk memasukkan data mahasiswa secara manual, lalu mendapatkan hasil prediksi apakah mahasiswa tersebut berstatus dropout, masih aktif (enrolled), atau telah lulus (graduate).

Untuk menjalankan aplikasi ini secara lokal, jalankan file app.py dengan perintah berikut:
```
streamlit run app.py
```
Berikut link sistem machine learning: https://students-performance-analysis.streamlit.app/

## Conclusion
1. Program studi **Course Management (Evening Attendance), Nursing, dan Journalism** menjadi tiga jurusan dengan tingkat dropout mahasiswa tertinggi.
2. Mahasiswa dengan status **single** memiliki kecenderungan dropout yang lebih tinggi dibandingkan dengan status lainnya.
3. Jumlah mahasiswa **perempuan** menunjukkan angka dropout yang sedikit lebih tinggi. Namun demikian, jumlah mahasiswa laki-laki yang mengalami dropout juga cukup banyak.
4. Mahasiswa yang **tidak menerima beasiswa** menunjukkan tingkat dropout yang lebih tinggi daripada yang menerima beasiswa.

## Rekomendasi Action Items
* **Fokus pada Program Studi dengan Dropout Tinggi**: Lakukan evaluasi dan intervensi khusus di jurusan Course Management (Evening Attendance), Nursing, dan Journalism untuk memahami penyebab dropout dan mengembangkan program pendukung seperti bimbingan akademik atau motivasi.

* **Buat Program Pendukung untuk Mahasiswa dengan Status Single (Semua Gender):** Kembangkan layanan konseling dan komunitas pendukung yang ditargetkan secara khusus bagi mahasiswa dengan status single, baik laki-laki maupun perempuan, untuk membantu mengurangi risiko dropout.

* **Perluas Akses Beasiswa dan Bantuan Finansial:** Tingkatkan sosialisasi dan perluasan program beasiswa agar lebih banyak mahasiswa bisa mendapat dukungan finansial, sehingga dapat menurunkan angka dropout akibat kendala ekonomi.
