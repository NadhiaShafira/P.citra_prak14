import cv2

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    'data/haarcascade_frontalface_default.xml'
)

# Baca gambar
img = cv2.imread('foto.jpg')

# Ubah ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Deteksi wajah
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5
)

# Gambar kotak
for (x, y, w, h) in faces:
    cv2.rectangle(
        img,
        (x, y),
        (x+w, y+h),
        (0, 255, 0),
        2
    )

# Simpan hasil
cv2.imwrite('hasil_deteksi.jpg', img)

print("Deteksi berhasil disimpan!")