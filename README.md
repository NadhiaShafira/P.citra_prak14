# 📸 Praktikum 14 - Deteksi Wajah Menggunakan Haar Cascade

## 👩‍🎓 Identitas Mahasiswa

| Keterangan           | Detail                                                    |
| -------------------- | --------------------------------------------------------- |
| 👤 Nama              | **Nadhia Shafira**                                        |
| 🆔 NIM               | **312410498**                                             |
| 🏫 Kelas             | **I241E**                                                 |
| 📚 Mata Kuliah       | **Pengolahan Citra**                                      |
| 👨‍🏫 Dosen Pengampu | **Dr. Muhamad Fatchan, S.Kom., M.Kom.**                   |
| 📝 Praktikum         | **Praktikum 14 - Deteksi Wajah Menggunakan Haar Cascade** |

---

# 🎯 Tujuan Praktikum

Praktikum ini bertujuan untuk memahami konsep **deteksi objek khususnya wajah manusia** menggunakan metode **Haar Cascade Classifier** yang tersedia pada library OpenCV. Selain itu, praktikum ini juga melatih kemampuan dalam mengakses webcam, melakukan pengolahan citra secara real-time, serta menyimpan hasil deteksi ke dalam file gambar.

---

# 📚 Dasar Teori

## 🤖 Apa itu Haar Cascade?

Haar Cascade merupakan metode deteksi objek berbasis **Machine Learning** yang dikembangkan oleh Paul Viola dan Michael Jones. Metode ini bekerja dengan cara menggunakan classifier yang telah dilatih sebelumnya untuk mengenali pola tertentu pada suatu objek.

Dalam praktikum ini, objek yang dideteksi adalah **wajah manusia** menggunakan file classifier:

```text
haarcascade_frontalface_default.xml
```

Classifier tersebut telah dilatih menggunakan ribuan gambar wajah positif dan negatif sehingga mampu mengenali bentuk wajah pada gambar maupun video secara real-time.

---

## 🖼️ Konsep Kerja Haar Cascade

Proses deteksi wajah menggunakan Haar Cascade dilakukan melalui beberapa tahapan:

### 1️⃣ Akuisisi Gambar

Sistem mengambil citra dari webcam atau file gambar.

### 2️⃣ Konversi Grayscale

Citra berwarna diubah menjadi grayscale agar proses komputasi lebih cepat.

### 3️⃣ Proses Deteksi

Classifier Haar Cascade mencari pola-pola wajah pada citra.

### 4️⃣ Penandaan Objek

Jika wajah ditemukan, sistem akan menggambar kotak (bounding box) pada area wajah.

### 5️⃣ Menampilkan Hasil

Hasil deteksi ditampilkan secara real-time pada layar.

---

# 🛠️ Tools dan Library yang Digunakan

| Software / Library | Fungsi                             |
| ------------------ | ---------------------------------- |
| 🐍 Python          | Bahasa pemrograman utama           |
| 📷 OpenCV          | Pengolahan citra dan deteksi wajah |
| 🔢 NumPy           | Operasi numerik dan array          |
| 📊 Matplotlib      | Visualisasi gambar                 |
| 💻 VS Code         | Editor kode                        |
| 📸 Webcam          | Sumber input video                 |

---

# 📂 Struktur Project

```text
face-detection-haar
│
├── data
│   └── haarcascade_frontalface_default.xml
│
├── assets
│   ├── 01_setup_project.png
│   ├── 02_deteksi_wajah_realtime.png
│   ├── 03_jumlah_wajah.png
│   └── 04_hasil_deteksi_foto.png
│
├── face_detect.py
├── deteksi_foto.py
├── foto.jpg
├── hasil_deteksi.jpg
└── README.md
```

---

# 📸 Hasil Persiapan Project

Pada tahap awal dilakukan pembuatan struktur folder project, instalasi library yang dibutuhkan, serta penambahan file Haar Cascade sebagai classifier untuk mendeteksi wajah.

![Persiapan Project](https://github.com/NadhiaShafira/P.citra_prak14/blob/3036110c22fafa92c975168d4a34453555d5f518/assets/01_setup_project.png.png)

---

# 🚀 Program 1 - Deteksi Wajah Realtime Menggunakan Webcam

## 📌 Kode Program

```python
import cv2

face_cascade = cv2.CascadeClassifier(
    'data/haarcascade_frontalface_default.xml'
)

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0,255,0),
            2
        )

    cv2.imshow("Deteksi Wajah", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
```

---

## 🔍 Penjelasan Program

### 📥 Import Library

```python
import cv2
```

Digunakan untuk mengakses seluruh fungsi OpenCV yang berkaitan dengan pengolahan citra dan video.

### 📂 Memuat Haar Cascade

```python
face_cascade = cv2.CascadeClassifier(...)
```

Digunakan untuk memanggil classifier wajah yang telah dilatih sebelumnya.

### 📷 Membuka Webcam

```python
video = cv2.VideoCapture(0)
```

Mengakses kamera utama perangkat.

### ⚫ Konversi Grayscale

```python
gray = cv2.cvtColor(...)
```

Mengubah citra RGB menjadi grayscale agar proses deteksi lebih cepat.

### 😀 Deteksi Wajah

```python
faces = face_cascade.detectMultiScale(...)
```

Mendeteksi lokasi wajah pada setiap frame video.

### 🟩 Membuat Bounding Box

```python
cv2.rectangle(...)
```

Memberikan kotak hijau pada wajah yang berhasil dideteksi.

### 🖥️ Menampilkan Hasil

```python
cv2.imshow(...)
```

Menampilkan hasil deteksi secara real-time.

---

## 📸 Hasil Deteksi Wajah Realtime

![Deteksi Wajah Realtime](https://github.com/NadhiaShafira/P.citra_prak14/blob/4eaf318bc985d5d11df5eeed040a624b00190984/assets/02_deteksi_wajah_realtime.png)

### ✅ Analisis Hasil

* 😀 Sistem berhasil mendeteksi wajah secara real-time.
* 📷 Webcam dapat diakses dengan baik.
* 🟩 Bounding box muncul pada area wajah.
* ⚡ Proses berjalan secara cepat dan responsif.

---

# 🚀 Program 2 - Menampilkan Jumlah Wajah yang Terdeteksi

## 📸 Hasil Program

![Jumlah Wajah](assets/03_jumlah_wajah.png)

---

## 🔍 Analisis Hasil

Fitur tambahan berhasil menampilkan jumlah wajah yang terdeteksi pada layar.

### Keuntungan fitur ini:

* 👥 Mengetahui jumlah wajah secara langsung.
* 📊 Menambah informasi hasil deteksi.
* 🚀 Membuat sistem lebih interaktif.

Contoh tampilan:

```text
Jumlah Wajah : 1
```

atau

```text
Jumlah Wajah : 2
```

jika terdapat lebih dari satu wajah pada frame.

---

# 🚀 Program 3 - Deteksi Wajah Pada Gambar

Program ini digunakan untuk mendeteksi wajah pada file gambar yang telah disimpan sebelumnya.

---

## 📸 Hasil Deteksi Gambar

![Hasil Deteksi Foto](assets/04_hasil_deteksi_foto.png)

---

## 🔍 Analisis Hasil

Pada pengujian ini sistem berhasil:

* 📥 Membaca file gambar.
* 😀 Mendeteksi area wajah.
* 🟩 Memberikan bounding box pada wajah.
* 💾 Menyimpan hasil deteksi ke file baru.

File output yang dihasilkan:

```text
hasil_deteksi.jpg
```

---

# 📊 Hasil Pengujian

| No | Pengujian                 | Hasil      |
| -- | ------------------------- | ---------- |
| 1  | Membaca file Haar Cascade | ✅ Berhasil |
| 2  | Membuka webcam            | ✅ Berhasil |
| 3  | Deteksi wajah realtime    | ✅ Berhasil |
| 4  | Menampilkan jumlah wajah  | ✅ Berhasil |
| 5  | Deteksi wajah pada gambar | ✅ Berhasil |
| 6  | Menyimpan hasil deteksi   | ✅ Berhasil |

---

# 🎯 Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa metode **Haar Cascade Classifier** mampu digunakan untuk mendeteksi wajah manusia baik pada citra statis maupun video real-time. Implementasi menggunakan OpenCV berjalan dengan baik dan berhasil menampilkan area wajah menggunakan bounding box. Selain itu, sistem juga dapat menghitung jumlah wajah yang terdeteksi serta menyimpan hasil deteksi ke dalam file gambar.

Praktikum ini memberikan pemahaman mengenai konsep dasar deteksi objek, pengolahan citra digital, serta implementasi Computer Vision menggunakan Python dan OpenCV.

---

# 📖 Referensi

1. OpenCV Documentation. https://opencv.org
2. OpenCV Haar Cascade Classifier Documentation.
3. Modul Praktikum Pengolahan Citra Digital.
4. Artikel "Bangun Alat Pengenalan Wajah Anda Sendiri Dengan Python".
5. Praktikum Haar Cascades for Object Detection.
