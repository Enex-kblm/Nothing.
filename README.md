# 🎭 Nothing - Aplikasi Deteksi Wajah Real-time

> *"Ketika wajah Anda terdeteksi, maka wajah Anda akan menjadi... nothing."*

## 📖 Deskripsi

**Nothing** adalah aplikasi computer vision yang unik dan menarik! Aplikasi ini menggunakan kamera untuk mendeteksi wajah secara real-time, kemudian "menyembunyikan" wajah yang terdeteksi dengan kotak hitam. Cocok untuk privasi, eksperimen, atau sekadar bersenang-senang!

## ✨ Fitur Utama

- 🎯 **Deteksi Wajah Real-time**: Menggunakan MediaPipe untuk deteksi wajah yang akurat
- 🖤 **Penyembunyian Otomatis**: Wajah yang terdeteksi akan ditutup kotak hitam
- 📊 **Monitor FPS**: Menampilkan frame rate secara real-time
- 🔧 **Margin Adaptif**: Kotak penyembunyian dengan margin yang dapat disesuaikan
- ⚡ **Performa Optimal**: Menggunakan buffer FPS untuk perhitungan yang stabil

## 🛠️ Teknologi yang Digunakan

- **Python 3.x** - Bahasa pemrograman utama
- **OpenCV** - Library computer vision untuk pemrosesan video
- **MediaPipe** - Framework ML Google untuk deteksi wajah
- **NumPy** - Komputasi numerik (dependency OpenCV)

## 📋 Persyaratan Sistem

- Python 3.7 atau lebih baru
- Webcam atau kamera eksternal
- Sistem operasi: Windows, macOS, atau Linux

## 🚀 Instalasi

1. **Clone repository ini:**
   ```bash
   git clone <repository-url>
   cd nothing-face-detection
   ```

2. **Install dependencies:**
   ```bash
   pip install opencv-python mediapipe
   ```

3. **Jalankan aplikasi:**
   ```bash
   python nothing.py
   ```

## 🎮 Cara Penggunaan

1. **Jalankan aplikasi** dengan perintah `python nothing.py`
2. **Posisikan wajah** di depan kamera
3. **Lihat magic happen!** - Wajah Anda akan otomatis disembunyikan
4. **Tekan 'q'** untuk keluar dari aplikasi

## ⚙️ Konfigurasi

Anda dapat menyesuaikan beberapa parameter dalam kode:

```python
# Confidence threshold untuk deteksi wajah
min_detection_confidence=0.5

# Margin kotak penyembunyian (20% dari ukuran wajah)
margin_w = int(box_w * 0.2)
margin_h = int(box_h * 0.2)

# Jumlah frame untuk rata-rata FPS
fps_history = deque(maxlen=10)
```

## 🎯 Use Cases

- **Privasi**: Sembunyikan identitas dalam video call atau streaming
- **Eksperimen**: Belajar computer vision dan deteksi wajah
- **Hiburan**: Efek visual yang menarik untuk konten kreatif
- **Demonstrasi**: Showcase teknologi AI dan ML

## 🔧 Troubleshooting

### Kamera tidak terdeteksi
```python
# Coba ganti index kamera
cap = cv2.VideoCapture(1)  # atau 2, 3, dst.
```

### FPS rendah
- Pastikan tidak ada aplikasi lain yang menggunakan kamera
- Tutup aplikasi yang tidak perlu
- Coba kurangi resolusi kamera

### Error import mediapipe
```bash
pip install --upgrade mediapipe
```

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b fitur-amazing`)
3. Commit perubahan (`git commit -m 'Tambah fitur amazing'`)
4. Push ke branch (`git push origin fitur-amazing`)
5. Buat Pull Request

## 📝 Roadmap

- [ ] Tambah efek blur selain kotak hitam
- [ ] Support multiple face detection
- [ ] Simpan video hasil processing
- [ ] GUI interface dengan tkinter
- [ ] Deteksi gesture untuk kontrol
- [ ] Filter dan efek tambahan

## 📄 Lisensi

Proyek ini menggunakan lisensi MIT. Lihat file `LICENSE` untuk detail lengkap.

## 👨‍💻 Pengembang

Dibuat dengan ❤️ menggunakan Python dan computer vision

---

**⭐ Jangan lupa beri star jika proyek ini bermanfaat!**

*"Sometimes the best way to see something is to make it disappear."*