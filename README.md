# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institute merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

Untuk menanggulangi permasalahan tersebut, Jaya Jaya Institut berencana menerapkan pendekatan berbasis data guna mengidentifikasi mahasiswa yang berisiko dropout sejak dini. Dengan demikian, institusi dapat memberikan intervensi dan pendampingan yang tepat waktu. Selain itu, mereka juga menginginkan sebuah dashboard interaktif yang dapat digunakan oleh pihak manajemen untuk memantau kinerja mahasiswa dan menyajikan informasi dalam bentuk yang mudah dipahami.

### Permasalahan Bisnis

- Tingginya angka siswa yang mengalami *dropout* yang menimbulkan kekhawatiran terhadap kualitas institusi dan efektivitas proses pendidikan yang berjalan.

- Ketiadaan sistem prediktif yang dapat mengenali siswa berisiko tinggi. 

- Kebutuhan akan visualisasi performa siswa yang informatif. Pihak manajemen membutuhkan *dashboard* untuk memantau perkembangan siswa secara berkala dan mengambil keputusan yang tepat berdasarkan data.


### Cakupan Proyek
- Melakukan eksplorasi dan analisis data performa mahasiswa.
- Membangun model machine learning untuk prediksi dropout.
- Membuat dashboard interaktif untuk memantau performa mahasiswa.
- Menyediakan prototipe aplikasi menggunakan Streamlit.
- Memberikan rekomendasi tindakan berdasarkan hasil analisis.

### Persiapan


Sumber data: [students' performance](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv)

## Setup Environment

Untuk menjalankan proyek prediksi risiko dropout mahasiswa **Jaya Jaya Institut**, pastikan dependensi yang tertulis di requirements.txt sudah terinstall dengan perintah berikut:

```bash
pip install -r requirements.txt
```



### Struktur File

```
project/
│
├── df_student_labeled.xlsx     # Dataset untuk visualisasi dashboard dan referensi penamaan fitur pada Streamlit
├── app.py                         # Aplikasi Streamlit (antarmuka pengguna)
├── model_logreg.pkl                # Model Logistic Regression 
├── scaler.pkl                      # Scaler 
├── requirements.txt               # Daftar dependensi Python
├── README.md                      # Penjelasan proyek
└── notebook/                      # Notebook eksplorasi dan modeling
```

## Business Dashboard

Dashboard ini dirancang untuk memberikan pemantauan dan analisis menyeluruh terhadap data mahasiswa dalam sebuah institusi pendidikan, dengan fokus utama pada status enrolled, graduate, dan dropout. Dashboard ini sangat berguna bagi manajemen untuk mengambil keputusan berbasis data dalam meningkatkan kualitas dan efisiensi pendidikan.

 🎯 Tujuan Utama

- Memantau performa institusi pendidikan berdasarkan status mahasiswa.
- Mengidentifikasi faktor-faktor yang berkontribusi terhadap dropout.
- Mendukung pengambilan keputusan berbasis data untuk perbaikan program akademik dan kebijakan pendukung.

---

 🧩 Fitur Utama

### 1. **Filter Interaktif**
- **Institusi dan Gender**: Pengguna dapat memfilter data berdasarkan jenis institusi (misalnya: International) dan jenis kelamin. Hal ini memudahkan segmentasi data sesuai kebutuhan analisis.

### 2. **Ringkasan Indikator Kinerja (KPI)**
- Menyediakan statistik cepat mengenai jumlah total mahasiswa, jumlah mahasiswa aktif (enrolled), dropout, dan lulusan (graduate).
- Berfungsi sebagai ringkasan kondisi akademik saat ini secara keseluruhan.

### 3. **Analisis Dropout**
- Menggambarkan berbagai faktor yang berhubungan dengan mahasiswa yang dropout, seperti:
  - **Usia saat pendaftaran**
  - **Status beasiswa**
  - **Status hutang**
  - **Program studi dengan tingkat dropout tertinggi**
- Fungsi ini membantu manajemen memahami pola dropout yang terjadi dan faktor penyebabnya.

### 4. **Distribusi Mahasiswa**
- Menampilkan distribusi atau komposisi status mahasiswa secara keseluruhan untuk memahami proporsi antara yang lulus, dropout, dan masih aktif.

### Link Akses Dashboard (jika sudah tersedia online):

> [Dashboard Dropout - Jaya Jaya Institut](https://lookerstudio.google.com/reporting/ebad17d7-f032-4538-9b85-0a1649b80587)

---
## Menjalankan Sistem Machine Learning

Sistem prediksi dropout dibuat berbasis **Streamlit**, yang mengintegrasikan model machine learning Logistic Regression.

### Cara Menjalankan

1. Jalankan perintah berikut di terminal:

```bash
streamlit run app.py
```

2. Aplikasi akan terbuka di browser lokal (biasanya di: `http://localhost:8501`)

### File Penting

* `app.py`: Antarmuka pengguna berbasis Streamlit
* `model_logreg.pkl `: Model Logistic Regression
* `scaler_pca.joblib`: Scaler
* `df_student_labeled.xlsx`: referensi penamaan fitur pada streamlit

### Link Akses Prototype

> [Prototype Prediksi Dropout Streamlit](https://ds2submission-fauzan.streamlit.app/)

---

## Conclusion

1. **Tingkat Dropout Cukup Tinggi**  
   Dari total 4.424 mahasiswa, sekitar **32,1% mengalami dropout**. Ini menunjukkan adanya masalah signifikan dalam retensi mahasiswa yang perlu ditelusuri lebih lanjut penyebabnya, baik dari faktor akademik, keuangan, atau lainnya.

2. **Mahasiswa Internasional Cenderung Lebih Rentan Terhadap Masalah Keuangan**  
   - Persentase mahasiswa internasional dropout yang memiliki utang mencapai **46,9%**, jauh lebih tinggi dibandingkan mahasiswa non-internasional (**21,4%**).  
   - Hal ini menunjukkan bahwa faktor **biaya pendidikan dan akses ke bantuan keuangan** bisa menjadi beban besar bagi mahasiswa internasional.

3. **Usia Rawan Dropout Adalah 19–21 Tahun**  
   - Sebagian besar mahasiswa yang dropout berada di kisaran usia tersebut, yang biasanya merupakan tahun-tahun awal kuliah.
   - Ini menunjukkan perlunya **pendampingan lebih intensif di awal masa studi**, termasuk orientasi, bimbingan akademik, dan pengenalan fasilitas kampus.

4. **Jurusan Tertentu Menjadi Titik Konsentrasi Dropout**  
   - Jurusan **Manajemen (terutama kelas malam)**, **Keperawatan**, dan **Komunikasi** secara konsisten memiliki angka dropout tertinggi, baik pada mahasiswa internasional maupun non-internasional.
   - Hal ini bisa disebabkan oleh:
     - Beban kerja kuliah yang tinggi,
     - Kurangnya minat atau ketidaksesuaian dengan jurusan,
     - Jadwal kelas yang bentrok dengan pekerjaan (terutama kelas malam).



### Rekomendasi Action Items

Berikut beberapa rekomendasi tindakan yang dapat diambil oleh institusi pendidikan untuk mengatasi permasalahan dropout dan meningkatkan kinerja pendidikan:

- **Perkuat Program Bimbingan Akademik di Tahun Pertama**  
  Fokuskan intervensi pada mahasiswa usia 18–21 tahun dengan menyediakan mentor akademik, sesi konsultasi rutin, serta orientasi kehidupan kampus yang intensif.

- **Evaluasi dan Revitalisasi Kurikulum di Jurusan dengan Dropout Tinggi**  
  Tinjau ulang struktur dan beban studi pada jurusan seperti Manajemen, Keperawatan, dan Komunikasi. Pastikan kurikulum relevan, fleksibel, dan mendukung keberhasilan mahasiswa.

- **Perluas Akses Beasiswa dan Dukungan Keuangan**  
  Bangun sistem beasiswa dan pinjaman pendidikan yang lebih inklusif, khususnya bagi mahasiswa internasional dan kelompok rentan secara ekonomi.

- **Lakukan Survei Rutin Kepuasan Mahasiswa**  
  Dapatkan masukan langsung dari mahasiswa terkait pengalaman belajar, kesulitan, dan saran perbaikan guna merancang kebijakan yang tepat sasaran.