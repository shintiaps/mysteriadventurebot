import time
import random

def efek_teks(kalimat, jeda=0.5):
    """Fungsi untuk menampilkan teks dengan jeda dramatis"""
    for huruf in kalimat:
        print(huruf, end="", flush=True)
        time.sleep(jeda / len(kalimat))
    print()  # Pindah ke baris baru

def ascii_pedang():
    """ASCII Art: Pedang Kemenangan"""
    print("""
    ⚔️
     |
    / \\
    """)

def ascii_tengkorak():
    """ASCII Art: Tengkorak Kekalahan"""
    print("""
    ☠️
   /  \\
  |    |
   \\  /
    """)

def ascii_kastil():
    """ASCII Art: Kastil Misteri"""
    print("""
      🏰
     |  |
    _|__|_
    """)

def game_utama():
    efek_teks("--- MEMULAI PETUALANGAN DIGITAL ---", jeda=0.02)
    ascii_kastil()
    time.sleep(1)
    
    nama = input("\nSiapa namamu? ")
    
    efek_teks(f"\nSalam, {nama}! Kamu memasuki Kerajaan Misteri Digital.", jeda=0.02)
    efek_teks("Sebuah dunia penuh misteri dan tantangan menungguimu...\n", jeda=0.02)
    
    # STEP 2: SISTEM NYAWA
    nyawa = 100
    print(f"❤️ Nyawa Awalmu: {nyawa}\n")
    time.sleep(1)
    
    # STEP 1: ALUR CERITA - Dua Pilihan Jalur
    efek_teks("Kamu berada di perempatan jalan.", jeda=0.02)
    time.sleep(0.5)
    efek_teks("Di depanmu ada dua jalur yang berbeda:", jeda=0.02)
    time.sleep(0.3)
    print("1. Lembah Coding - jalur yang penuh dengan logika dan puzzle")
    print("2. Gunung Bug - jalur yang berbahaya dan penuh lawan\n")
    
    pilihan = input("Pilih jalur (1 atau 2): ")
    
    if pilihan == "1":
        efek_teks(f"\n{nama} memilih Lembah Coding...", jeda=0.02)
        time.sleep(0.5)
        efek_teks("Kamu turun ke lembah yang indah dengan pemandangan baris kode yang bersinar.", jeda=0.02)
        time.sleep(0.5)
        efek_teks("Namun tiba-tiba, error besar muncul dan menyerangmu!", jeda=0.02)
        time.sleep(0.5)
        print("\nApakah kamu menggunakan TRY-CATCH untuk bertahan?")
        print("1. Ya, aku tahu cara mengatasi error (PILIHAN BENAR)")
        print("2. Tidak, aku lari saja (PILIHAN SALAH)\n")
        
        pilihan_2 = input("Pilih (1 atau 2): ")
        
        # RANDOMNESS: Elemen keberuntungan
        keberuntungan = random.randint(1, 100)
        
        if pilihan_2 == "1":
            efek_teks("✨ Bagus! Kamu berhasil mengatasi error dengan TRY-CATCH!", jeda=0.02)
            # Bonus keberuntungan: ada 50% chance mendapat heal
            if keberuntungan > 50:
                bonus = random.randint(5, 15)
                nyawa += bonus
                efek_teks(f"🍀 Keberuntungan bersama! Nyawa +{bonus}!", jeda=0.02)
            time.sleep(0.5)
        else:
            nyawa -= 20
            efek_teks(f"❌ Kamu terluka! Nyawa berkurang 20.", jeda=0.02)
            time.sleep(0.3)
            print(f"Nyawa sekarang: {nyawa}\n")
            time.sleep(0.5)
            
    elif pilihan == "2":
        efek_teks(f"\n{nama} memilih Gunung Bug...", jeda=0.02)
        time.sleep(0.5)
        efek_teks("Kamu naik ke gunung yang gelap dengan terik panas yang menyengat.", jeda=0.02)
        time.sleep(0.5)
        efek_teks("Di tengah jalan, seekor Bug Monster muncul menghadang!", jeda=0.02)
        time.sleep(0.5)
        print("\nApakah kamu siap untuk melawannya?")
        print("1. Ya, aku siap! (PILIHAN BENAR)")
        print("2. Tidak, aku menyerah (PILIHAN SALAH)\n")
        
        pilihan_2 = input("Pilih (1 atau 2): ")
        
        # RANDOMNESS: Elemen keberuntungan dalam pertarungan
        kekuatan_serangan = random.randint(10, 50)
        
        if pilihan_2 == "1":
            efek_teks(f"🔥 Kamu melakukan serangan sengit dengan kekuatan {kekuatan_serangan}!", jeda=0.02)
            efek_teks("🎉 Hebat! Kamu mengalahkan Bug Monster!", jeda=0.02)
            ascii_pedang()
            # Bonus keberuntungan: ada 60% chance mendapat hadiah
            if kekuatan_serangan > 30:
                bonus = random.randint(10, 25)
                nyawa += bonus
                efek_teks(f"💎 Monster memberikan hadiah! Nyawa +{bonus}!", jeda=0.02)
            time.sleep(0.5)
        else:
            nyawa -= 20
            efek_teks(f"❌ Kamu kalah dalam pertarungan! Nyawa berkurang 20.", jeda=0.02)
            time.sleep(0.3)
            print(f"Nyawa sekarang: {nyawa}\n")
            ascii_tengkorak()
            time.sleep(0.5)
    else:
        print("Pilihan tidak valid! Cerita berakhir di sini.")
        return False
    
    # Pengecekan akhir
    time.sleep(1)
    if nyawa > 0:
        efek_teks(f"\n🏆 Selamat {nama}! Kamu menyelesaikan petualangan dengan nyawa {nyawa}!", jeda=0.02)
        ascii_pedang()
    else:
        efek_teks(f"\n💀 Game Over! Nyawa {nama} habis. Cerita berakhir tragis...", jeda=0.02)
        ascii_tengkorak()
    
    return True

# LOOPING: Main lagi?
def main_loop():
    while True:
        if game_utama():
            time.sleep(1)
            lanjut = input("\n🎮 Main lagi? (y/n): ").lower()
            if lanjut != 'y':
                efek_teks("\n👋 Terima kasih telah bermain! Sampai jumpa lagi di Kerajaan Misteri Digital.", jeda=0.02)
                break
        else:
            break
    
if __name__ == "__main__":
    main_loop()