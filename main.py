import time
import random

def efek_teks(kalimat, jeda=0.5):
    """Fungsi untuk menampilkan teks dengan jeda dramatis"""
    for huruf in kalimat:
        print(huruf, end="", flush=True)
        time.sleep(jeda / len(kalimat))
    print()  # Pindah ke baris baru

def ascii_pulau():
    """ASCII Art: Pulau Surtsey"""
    print("""
       🏝️ SURTSEY 🏝️
      /  \\
     /    \\
    /______\\
    """)

def ascii_harta_karun():
    """ASCII Art: Harta Karun"""
    print("""
     💎 HARTA KARUN! 💎
     ___________
    |  ✨ 👑 ✨  |
    |___________|
    """)

def ascii_korban():
    """ASCII Art: Kekalahan"""
    print("""
    ☠️ KEKALAHAN ☠️
   /  \\
  |    |
   \\  /
    """)

def ascii_kompas():
    """ASCII Art: Kompas"""
    print("""
       🧭
      / \\
     |   |
      \\ /
    """)


def tantangan_puzzle(nama, nyawa):
    """TANTANGAN 1: Puzzle Misteri Gua"""
    efek_teks("\n🌑 Memasuki Gua Misteri Surtsey...", jeda=0.02)
    time.sleep(0.5)
    efek_teks("Di dalam gua, kamu menemukan tulisan kuno di batu:", jeda=0.02)
    time.sleep(0.5)
    print(">" * 40)
    print("'Pertanyaan: Saya memiliki kota, tapi tidak ada rumah.'")
    print("'Saya memiliki gunung, tapi tidak ada pohon.'")
    print("'Saya memiliki air, tapi tidak ada ikan.'")
    print("'Apa saya?'")
    print(">" * 40)
    
    print("\nPilihan jawaban:")
    print("1. Peta")
    print("2. Langit")
    print("3. Permainan")
    
    jawaban = input("\nJawaban kamu (1, 2 atau 3): ")
    
    if jawaban == "1":
        efek_teks("\n✨ Benar! Kamu mengatasi puzzle gua!", jeda=0.02)
        nyawa += 15
        efek_teks(f"Nyawa +15! Total nyawa sekarang: {nyawa}❤️", jeda=0.02)
        return nyawa, True
    else:
        efek_teks(f"\n❌ Jawaban salah! Bayi kelelawar menyerangmu!", jeda=0.02)
        nyawa -= 15
        efek_teks(f"Nyawa -15! Total nyawa sekarang: {nyawa}❤️", jeda=0.02)
        return nyawa, False

def tantangan_labirin(nama, nyawa):
    """TANTANGAN 2: Labirin Hutan Belantara"""
    efek_teks("\n🌲 Memasuki hutan belantara yang gelap...", jeda=0.02)
    time.sleep(0.5)
    efek_teks("Kamu tersesat di sebuah labirin raksasa! Pilih jalur yang benar:", jeda=0.02)
    time.sleep(0.5)
    
    print("\nAda 3 pintu di depanmu:")
    print("🚪 PINTU 1: Membawa aroma buah beri (kemungkinan aman)")
    print("🚪 PINTU 2: Berasal dari kegelapan (misterius)")
    print("🚪 PINTU 3: Mengeluarkan suara hewan buas (berbahaya)")
    
    pilihan = input("\nPilih pintu (1, 2 atau 3): ")
    
    lokasi_aman = random.randint(1, 3)
    
    if pilihan == str(lokasi_aman):
        efek_teks(f"\n🎯 Tepat! Kamu memilih pintu yang benar!", jeda=0.02)
        efek_teks("Kamu keluar dari labirin dan menemukan peta harta karun!", jeda=0.02)
        nyawa += 20
        efek_teks(f"Bonus keberuntungan! Nyawa +20! Total: {nyawa}❤️", jeda=0.02)
        return nyawa, True
    else:
        efek_teks(f"\n⚠️ Kamu masuk ke jalur yang salah!", jeda=0.02)
        efek_teks("Terjebak dalam jebakan kuno di labirin!", jeda=0.02)
        nyawa -= 20
        efek_teks(f"Nyawa -20! Total nyawa sekarang: {nyawa}❤️", jeda=0.02)
        return nyawa, False

def tantangan_pertarungan(nama, nyawa):
    """TANTANGAN 3: Pertarungan dengan Penjaga Harta Karun"""
    efek_teks("\n⚔️ PERHATIAN!!! PENJAGA HARTA KARUN MUNCUL!", jeda=0.02)
    time.sleep(0.5)
    efek_teks("Seorang prajurit kuno yang misterius menghadang jalanmu!", jeda=0.02)
    time.sleep(0.5)
    
    print("\nPrajurit Kuno berkata: 'Harta ini bukan milikmu!'")
    print("\nStrategi apa yang akan kamu gunakan?")
    print("1. Menyerang dengan keberanian penuh")
    print("2. Menggunakan kecerdasan untuk berkelit")
    print("3. Menawarkan negosiasi damai")
    
    strategi = input("\nPilih strategi (1, 2 atau 3): ")
    
    kekuatan = random.randint(20, 80)
    
    if strategi == "1":
        if kekuatan > 50:
            efek_teks(f"\n🔥 Serangan ganas dengan kekuatan {kekuatan}!", jeda=0.02)
            efek_teks("💪 Kamu berhasil mengalahkan Penjaga!", jeda=0.02)
            ascii_harta_karun()
            nyawa += 25
            return nyawa, True
        else:
            efek_teks(f"\n⚔️ Serangan balasan yang fatal! Kekuatan: {kekuatan}", jeda=0.02)
            efek_teks("Penjaga marah dan menyerangmu!", jeda=0.02)
            nyawa -= 30
            return nyawa, False
    
    elif strategi == "2":
        if kekuatan > 40:
            efek_teks(f"\n🐱 Kamu menggunakan taktik jebakan cerdas!", jeda=0.02)
            efek_teks("Penjaga terjebak dan kamu lolos! Harta karun berhasil diambil!", jeda=0.02)
            ascii_harta_karun()
            nyawa += 30
            return nyawa, True
        else:
            efek_teks("Penjaga menyadari trikmu dan menyerang!", jeda=0.02)
            nyawa -= 25
            return nyawa, False
    
    else:  # strategi == "3"
        efek_teks(f"\n🤝 Kamu berbicara dengan tenang kepada Penjaga...", jeda=0.02)
        time.sleep(0.3)
        if kekuatan > 45:
            efek_teks("Penjaga terpesona dengan kebijaksanaanmu dan melangkah mundur!", jeda=0.02)
            efek_teks("Dia memberikan izin untuk mengambil sebagian dari harta karun!", jeda=0.02)
            ascii_harta_karun()
            nyawa += 35
            return nyawa, True
        else:
            efek_teks("Penjaga marah atas upaya negosiasi dan menyerangmu!", jeda=0.02)
            nyawa -= 20
            return nyawa, False

def tantangan_terakhir(nama, nyawa):
    """TANTANGAN 4: Memecahkan Kode Brankas Harta Karun"""
    efek_teks("\n💎 AKHIRNYA! Kamu sampai di ruang harta karun!", jeda=0.02)
    time.sleep(0.5)
    efek_teks("Sebuah brankas emas berkilau dengan kode rahasia di depanmu:", jeda=0.02)
    time.sleep(0.5)
    
    print("\n" + "=" * 50)
    print("BRANKAS BERLAPIS EMAS")
    print("Kode: 2, 4, 6, 8, ?")
    print("Apa angka selanjutnya?")
    print("=" * 50)
    
    print("\nPilihan:")
    print("1. 10 (Pola bilangan genap)")
    print("2. 12 (Perhitungan lain)")
    print("3. 9 (Urutan acak)")
    
    jawaban = input("\nJawaban kamu (1, 2 atau 3): ")
    
    if jawaban == "1":
        efek_teks("\n🔓 BENAR! Brankas terbuka!", jeda=0.02)
        time.sleep(0.5)
        efek_teks("GEMERLAP! Harta karun terbongkar penuh batu mulia dan koin emas!", jeda=0.02)
        ascii_harta_karun()
        nyawa += 50
        return nyawa, True
    else:
        efek_teks(f"\n❌ Kode salah! Sistem keamanan brankas aktif!", jeda=0.02)
        efek_teks("Peledak kuno meledak dan menyakitimu!", jeda=0.02)
        nyawa -= 40
        return nyawa, False

def game_utama():
    """GAME UTAMA: PETUALANGAN HARTA KARUN SURTSEY"""
    efek_teks("=" * 60, jeda=0.02)
    efek_teks("🏝️ SELAMAT DATANG DI PETUALANGAN SURTSEY 🏝️", jeda=0.02)
    efek_teks("🗺️ PENCARIAN HARTA KARUN YANG LEGENDARIS 🗺️", jeda=0.02)
    efek_teks("=" * 60, jeda=0.02)
    
    ascii_pulau()
    time.sleep(1)
    
    nama = input("\n🏴 Siapa nama petualang pemberani? ")
    
    efek_teks(f"\n👋 Selamat datang, {nama}!", jeda=0.02)
    efek_teks(f"Kamu adalah petualang legendaris yang mencari harta karun di pulau Surtsey.", jeda=0.02)
    ascii_kompas()
    time.sleep(1)
    
    # INISIALISASI GAME
    nyawa = 100
    harta_ditemukan = 0
    tantangan_selesai = 0
    
    print(f"\n" + "=" * 50)
    print(f"❤️ NYAWA AWAL: {nyawa}")
    print(f"💎 HARTA DITEMUKAN: {harta_ditemukan}/4")
    print("=" * 50)
    time.sleep(1)
    
    efek_teks(f"\nBersiaplah {nama}! Ada 4 tantangan menungguimu:\n", jeda=0.02)
    
    # ===== TANTANGAN 1: PUZZLE GUA =====
    print("\n📍 TANTANGAN 1: PUZZLE GUA MISTERI")
    print("Sebelum mencapai harta karun, kamu harus memecahkan puzzle kuno...")
    input("Tekan ENTER untuk lanjut...")
    
    nyawa, berhasil1 = tantangan_puzzle(nama, nyawa)
    if berhasil1:
        harta_ditemukan += 1
        tantangan_selesai += 1
    
    if nyawa <= 0:
        efek_teks(f"\n💀 {nama} telah gugur dalam perjalanan!", jeda=0.02)
        ascii_korban()
        return False
    
    time.sleep(1)
    
    # ===== TANTANGAN 2: LABIRIN =====
    print("\n📍 TANTANGAN 2: LABIRIN HUTAN BELANTARA")
    print("Untuk melanjutkan, kamu harus keluar dari hutan yang mengerikan...")
    input("Tekan ENTER untuk lanjut...")
    
    nyawa, berhasil2 = tantangan_labirin(nama, nyawa)
    if berhasil2:
        harta_ditemukan += 1
        tantangan_selesai += 1
    
    if nyawa <= 0:
        efek_teks(f"\n💀 {nama} hilang dalam hutan!", jeda=0.02)
        ascii_korban()
        return False
    
    time.sleep(1)
    
    # ===== TANTANGAN 3: PERTARUNGAN =====
    print("\n📍 TANTANGAN 3: PERTARUNGAN PENJAGA HARTA")
    print("Ada makhluk penjaga yang mau mengalahkanmu...")
    input("Tekan ENTER untuk lanjut...")
    
    nyawa, berhasil3 = tantangan_pertarungan(nama, nyawa)
    if berhasil3:
        harta_ditemukan += 1
        tantangan_selesai += 1
    
    if nyawa <= 0:
        efek_teks(f"\n💀 {nama} tewas dalam pertarungan epik!", jeda=0.02)
        ascii_korban()
        return False
    
    time.sleep(1)
    
    # ===== TANTANGAN 4: MEMBUKA HARTA =====
    print("\n📍 TANTANGAN 4: MEMBUKA BRANKAS HARTA KARUN")
    print("Langkah terakhir menuju kejayaan...")
    input("Tekan ENTER untuk lanjut...")
    
    nyawa, berhasil4 = tantangan_terakhir(nama, nyawa)
    if berhasil4:
        harta_ditemukan += 1
        tantangan_selesai += 1
    
    time.sleep(1)
    
    # ===== HASIL AKHIR =====
    print("\n" + "=" * 50)
    print(f"📊 HASIL AKHIR PERJALANAN {nama.upper()}")
    print("=" * 50)
    print(f"❤️ Nyawa Akhir: {nyawa}")
    print(f"💎 Tantangan Berhasil: {tantangan_selesai}/4")
    
    if tantangan_selesai == 4 and nyawa > 0:
        efek_teks(f"\n🏆 LUAR BIASA {nama}! KAMU ADALAH PENAKLUK SURTSEY! 🏆", jeda=0.02)
        efek_teks("Kamu berhasil menyelesaikan SEMUA tantangan dan menemukan HARTA KARUN SEJATI!", jeda=0.02)
        ascii_harta_karun()
        efek_teks("Legenda tentang keberanianmu akan dikenang selamanya di pulau Surtsey!", jeda=0.02)
    elif tantangan_selesai >= 2:
        efek_teks(f"\n👍 Bagus {nama}! Kamu berhasil mengatasi beberapa tantangan!", jeda=0.02)
        efek_teks(f"Kamu menemukan {tantangan_selesai} dari 4 harta karun. Coba lagi untuk mencapai sempurna!", jeda=0.02)
    else:
        efek_teks(f"\n⚠️ Sayang sekali {nama}! Kamu menemukan sedikit harta karun.", jeda=0.02)
        efek_teks("Coba lagi dengan strategi yang lebih baik!", jeda=0.02)
        ascii_korban()
    
    return True


# ===== MAIN LOOP =====
def main_loop():
    while True:
        if game_utama():
            time.sleep(1)
            lanjut = input("\n🎮 Mau mencoba petualangan baru? (y/n): ").lower()
            if lanjut != 'y':
                efek_teks("\n👋 Terima kasih telah bermain Petualangan Surtsey!", jeda=0.02)
                efek_teks("Sampai jumpa di petualangan berikutnya!", jeda=0.02)
                break
        else:
            break
    
if __name__ == "__main__":
    main_loop()