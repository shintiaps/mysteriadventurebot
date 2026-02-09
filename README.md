# 🏝️ Petualangan Pulau Arunika: Pencarian Harta Karun Legendaris 🏝️

Sebuah game petualangan berbasis text yang menceritakan kisah pencarian harta karun legendaris di **Pulau Arunika** yang misterius! Kelola makanan, hadapi monster, pecahkan puzzle, dan taklukkan penjaga terakhir!

## 📖 Cerita

**Selamat datang di Pulau Arunika**, sebuah pulau misterius yang konon menyimpan harta karun peninggalan pelaut legendaris. Selama bertahun-tahun, banyak orang mencoba menemukannya, tetapi tak satu pun yang berhasil. 

Hari ini, **kamulah yang terpilih** untuk memulai petualangan. Ikuti petunjuk, pecahkan teka-teki, dan temukan harta karun sebelum waktu habis!

Kamu harus:
1. **Menjelajahi Hutan Belantara** - Bertemu dan mengalahkan monster
2. **Mendaki Gunung Berbahaya** - Mengatasi kondisi ekstrim dan musuh lebih kuat
3. **Memecahkan Puzzle di Kuil Kuno** - Jawab teka-teki kuno untuk mendapatkan akses
4. **Pertarungan Final** - Menaklukkan Penjaga Abadi yang menjaga harta karun

## 🗺️ Peta Pulau Arunika

```
                🏝️ PANTAI UTARA 🏝️
                ↓
    ┌─────────────────────────┐
    │                         │
    │  🌲 HUTAN BELANTARA 🌲  │  
    │                         │
    │      ⛰️ GUNUNG ⛰️       │
    │    (AREA BERBAHAYA)     │
    │                         │
    └─────────────────────────┘
                ↓
          🏛️ KUIL KUNO 🏛️
          (Petunjuk Puzzle)
                ↓
       💎 HARTA KARUN TERSEMBUNYI 💎
     (Di gua bawah tanah dengan Penjaga)
```

## 🎮 Cara Bermain

1. Jalankan game dengan command:
   ```bash
   python main.py
   ```

2. Masukkan nama karakter kamu
3. Lihat peta untuk memahami rute perjalanan
4. Jelajahi setiap area dengan hati-hati
5. Kelola makanan, nyawa, dan inventory dengan bijak
6. Selesaikan semua area untuk mendapatkan harta karun!

## 💪 Sistem Game

### ❤️ Sistem Nyawa
- Mulai dengan **100 HP**
- Berkurang saat bertarungan atau kelaparan
- Jika mencapai 0, game berakhir
- Bisa di-recover dengan Daun Penyembuh

### 🍖 Sistem Makanan
- Mulai dengan **3/5 makanan**
- Status ditampilkan dengan kotak: `■□` (penuh) atau `□□□` (kosong)
- Berkurang setiap tahap perjalanan
- Jika **makanan 0**, nyawa berkurang drastis
- Makanan maksimal **5**, bisa didapat dari:
  - Membunuh monster
  - Istirahat dan cari makanan
  - Menemukan sumber makanan di area

### 🎒 Sistem Inventory
- Menyimpan item yang dikumpulkan
- Item didapat dari membunuh monster
- Digunakan dalam pertarungan untuk damage lebih tinggi

### ⚔️ Sistem Item
| Item | Source | Efek |
|------|--------|------|
| 🌿 Daun Penyembuh | Kelelawar Gelap | +8-15 HP |
| 🪄 Tongkat Mistis | Arwah Gua | +8-16 Damage |
| 🪨 Batu Kuat | Ogre Batu | +10-18 Damage |
| 🐉 Sisik Naga | Naga Kecil | +15-25 Damage (KUAT!) |
| 🪶 Bulu Perak | Serigala Hutan | Special Item |

## 🎯 Area & Tantangan

### 🌲 Hutan Belantara (Stage 1-3)
- **Monster**: Kelelawar Gelap, Arwah Gua, Serigala Hutan
- **Karakteristik**: 60% chance bertemu monster saat jelajah
- **Makanan**: Mudah didapat
- **Tujuan**: Temukan jalan ke gunung

### ⛰️ Gunung Arunika (Stage 1-2)
- **Monster**: Lebih kuat (75% chance bertemu)
- **Karakteristik**: Makanan sulit didapat, damage lebih besar
- **Perhatian**: Makanan berkurang 2x lebih cepat!
- **Tujuan**: Menemukan lintasan menuju kuil

### 🏛️ Kuil Kuno
- **Tantangan**: Jawab teka-teki kuno
- **Soal**: "Aku adalah awal dari akhir, dan akhir dari waktu..."
- **Reward**: Akses ke ruang harta karun

### 🏰 Ruang Harta Karun
- **Boss**: Prajurit Penjaga Abadi (60 HP)
- **Pertarungan**: Full battle system dengan semua item
- **Reward**: Harta karun legendaris jika menang!

## 🔥 Monster dalam Permainan

| Monster | HP | Makanan | Item Drop |
|---------|----|----|---------|
| 🦇 Kelelawar Gelap | 10 | 1 | Daun Penyembuh |
| 👻 Arwah Gua | 15 | 2 | Tongkat Mistis |
| 🐺 Serigala Hutan | 20 | 2 | Bulu Perak |
| 💪 Ogre Batu | 25 | 3 | Batu Kuat |
| 🐉 Naga Kecil | 30 | 3 | Sisik Naga |

## 📊 Sistem Penilaian

- **🏆 Sempurna**: Menang pertarungan final + Nyawa > 0 = **JUARA!** 
- **👍 Bagus**: Melewati area tapi kalah di final = Coba lagi
- **⚠️ Gagal**: Kehabisan nyawa atau kelaparan = Game Over

## 🎨 Fitur Game

- ✨ **Cerita Pembuka Keren** - Intro yang engaging dengan deskripsi detail
- 🗺️ **Peta Interaktif** - Visualisasi jalur perjalanan yang jelas
- 💥 **Pertarungan Real-time** - HP tracking untuk player dan enemy
- 🍖 **Status Food Bar** - Tampilan makanan dengan kotak visual `■□`
- 🎲 **Elemen Keberuntungan** - Hasil acak membuat setiap permainan unik
- ✨ **Efek Teks Dramatis** - Teks muncul bertahap untuk kesan yang seru
- 🎪 **ASCII Art & Emoji** - Visualisasi yang menarik

## 💡 Tips & Strategi Bermain

### 🍖 Manajemen Makanan
- Jangan sampai makanan 0! Lebih baik istirahat lebih awal
- Di gunung, makanan berkurang 2x lebih cepat - bawa ekstra!
- Prioritaskan membunuh monster untuk mendapat makanan bonus

### ⚔️ Strategi Pertarungan
- **Tangan Kosong**: Basic attack (3-8 damage), aman untuk early game
- **Tongkat Mistis**: Damage medium (8-16), cocok untuk mid-game
- **Batu Kuat**: Damage tinggi (10-18), untuk late game
- **Sisik Naga**: DAMAGE EKSTRIM (15-25), gunakan saat critical!
- **Daun Penyembuh**: JANGAN gunakan di awal, simpan untuk situasi darurat

### 🏃 Escape System
- Lari berhasil 50% tapi tidak mendapat reward
- Lebih baik hadapi monster jika nyawa cukup tinggi
- Lari berguna saat nyawa kritis

### 🧠 Puzzle Kuil
- Pikirkan setiap kata dengan hati-hati
- Jawabannya adalah huruf yang ada di awal dan akhir sesuatu
- Petunjuk: "awal dari akhir" = huruf pertama dari "end" = E

## 🛠️ Teknologi

- **Bahasa**: Python 3.x
- **Libraries**: `time`, `random`
- **File**: `main.py`

## 📋 Requirements

```
Python 3.6+
Tidak ada dependency eksternal
```

## 👤 Developer

Game ini dibuat sebagai contoh game petualangan interaktif dengan sistem yang kompleks dan storytelling yang menarik!

---

### 🎮 Ready to Play?

```bash
python main.py
```

**Semoga kamu menjadi penakluk Pulau Arunika dan menemukan harta karun legendaris!** 💎✨

*"Perjalanan seribu langkah dimulai dengan satu langkah..."* - Konfusius