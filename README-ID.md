# Start Scheduler

[English](README.md) | **Bahasa Indonesia**

> 📥 **Download Aplikasi Siap Pakai**: Dapatkan file `.exe` terbaru dari [Releases](https://github.com/kitokato77/start-scheduler-app/releases/latest)

Aplikasi Python untuk mengelola dan menjalankan aplikasi secara otomatis saat Windows startup dengan sistem queue/antrian.

## Fitur

- 🚀 **Autostart dengan Queue System**: Menjalankan aplikasi secara berurutan dengan menunggu aplikasi sebelumnya berjalan terlebih dahulu
- 🎨 **GUI User-Friendly**: Interface grafis yang mudah digunakan dengan tkinter
- ⚙️ **Konfigurasi Fleksibel**: Atur delay antar aplikasi dan interval pengecekan
- 📝 **Manajemen Aplikasi**: Tambah, hapus, dan atur urutan aplikasi dengan mudah
- 🔄 **Drag & Drop Order**: Pindahkan aplikasi ke atas atau bawah untuk mengatur prioritas
- 💾 **Auto-Save**: Konfigurasi tersimpan otomatis ke file JSON
- 🪟 **Windows Startup Integration**: Daftarkan ke startup Windows dengan satu klik
- ✅ **Status Monitoring**: Pantau status setiap aplikasi (Menunggu, Berjalan, Error)
- 🌐 **Multi-Bahasa**: Mendukung Bahasa Inggris dan Indonesia (deteksi otomatis)

## Cara Kerja

1. Aplikasi membaca daftar executable dari `config.json`
2. Saat startup, aplikasi menjalankan program pertama dalam antrian
3. Menunggu hingga program tersebut benar-benar berjalan (proses terdeteksi)
4. Setelah delay yang ditentukan, menjalankan aplikasi berikutnya
5. Proses berlanjut hingga semua aplikasi dalam daftar telah dijalankan
6. Aplikasi manager akan otomatis tertutup setelah selesai (jika dijalankan dari startup)

## Instalasi

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Jalankan Aplikasi

```bash
python autostart_manager.py
```

## Cara Penggunaan

### Menambah Aplikasi

1. Klik tombol **"➕ Tambah Aplikasi"**
2. Pilih file executable (.exe) yang ingin dijalankan saat startup
3. Aplikasi akan ditambahkan ke daftar

### Mengatur Urutan

1. Pilih aplikasi dalam daftar
2. Klik **"⬆️ Naik"** untuk memindahkan ke atas (prioritas lebih tinggi)
3. Klik **"⬇️ Turun"** untuk memindahkan ke bawah

**Catatan**: Aplikasi paling atas akan dijalankan pertama kali

### Menghapus Aplikasi

1. Pilih aplikasi yang ingin dihapus
2. Klik tombol **"🗑️ Hapus"**

### Pengaturan

- **Delay antar aplikasi**: Waktu tunggu (detik) setelah aplikasi berjalan sebelum menjalankan aplikasi berikutnya
- **Interval cek aplikasi**: Seberapa sering (detik) memeriksa apakah aplikasi sudah berjalan
- **Bahasa**: Pilih bahasa interface (English atau Bahasa Indonesia)
- Klik **"💾 Simpan Pengaturan"** setelah mengubah nilai

### Menguji AutoStart

Klik **"▶️ Mulai AutoStart"** untuk mencoba menjalankan semua aplikasi dalam daftar tanpa harus restart komputer.

### Daftarkan ke Windows Startup

1. Klik **"⚙️ Daftarkan ke Windows Startup"**
2. Aplikasi akan otomatis berjalan setiap kali Windows dimulai
3. Untuk menghapus dari startup, klik **"❌ Hapus dari Windows Startup"**

## Struktur File

```
autostart-app/
├── autostart_manager.py   # File utama aplikasi
├── config.json             # Konfigurasi daftar aplikasi
├── requirements.txt        # Dependencies Python
├── README.md              # Dokumentasi (English)
└── README-ID.md           # Dokumentasi (Bahasa Indonesia)
```

## Format config.json

```json
{
  "apps": [
    {
      "name": "Aplikasi1",
      "path": "C:\\Path\\To\\App1.exe",
      "status": "Menunggu"
    },
    {
      "name": "Aplikasi2",
      "path": "C:\\Path\\To\\App2.exe",
      "status": "Menunggu"
    }
  ],
  "delay_between_apps": 3,
  "check_interval": 2,
  "language": "id"
}
```

## Compile ke EXE

Untuk mengubah aplikasi Python menjadi file EXE yang standalone:

### 1. Install PyInstaller

```bash
pip install pyinstaller
```

### 2. Compile

```bash
pyinstaller --onefile --windowed --icon=app.ico --name="StartScheduler" autostart_manager.py
```

**Parameter:**
- `--onefile`: Membuat satu file EXE
- `--windowed`: Tanpa console window (GUI only)
- `--icon`: Tambahkan icon (opsional)
- `--name`: Nama file EXE

### 3. Hasil

File EXE akan tersedia di folder `dist/StartScheduler.exe`

**Catatan**: Pastikan file `config.json` berada di folder yang sama dengan EXE

## Troubleshooting

### Aplikasi tidak terdeteksi berjalan

- Tingkatkan nilai **"Interval cek aplikasi"**
- Beberapa aplikasi memerlukan waktu lebih lama untuk start

### Aplikasi tidak berjalan otomatis

- Pastikan sudah klik **"Daftarkan ke Windows Startup"**
- Cek Task Manager → Startup untuk memverifikasi
- Jalankan aplikasi sebagai Administrator jika diperlukan

### Error "Access Denied"

- Jalankan aplikasi sebagai Administrator
- Beberapa aplikasi memerlukan elevated privileges

### Bahasa tidak sesuai

- Aplikasi akan otomatis mendeteksi bahasa Windows
- Anda dapat mengubahnya secara manual di bagian Pengaturan
- Pilihan bahasa akan tersimpan dan digunakan di sesi berikutnya

## Requirements

- Windows 10/11
- Python 3.7+
- tkinter (biasanya sudah include di Python)
- psutil

## Tips

1. **Urutan Penting**: Letakkan aplikasi yang harus berjalan duluan di posisi paling atas
2. **Delay Cukup**: Berikan delay yang cukup antar aplikasi (3-5 detik recommended)
3. **Test Dulu**: Gunakan tombol "Mulai AutoStart" untuk testing sebelum mendaftarkan ke startup
4. **Path Absolut**: Pastikan path ke executable benar dan menggunakan full path
5. **Pilih Bahasa**: Gunakan dropdown bahasa di pengaturan untuk mengubah bahasa interface

## License

Free to use and modify.

## Author

Created with ❤️ for better Windows startup management
