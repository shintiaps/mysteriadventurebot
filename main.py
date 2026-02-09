import time
import random

def efek_teks(kalimat, jeda=0.5):
    """Fungsi untuk menampilkan teks dengan jeda dramatis"""
    for huruf in kalimat:
        print(huruf, end="", flush=True)
        time.sleep(jeda / len(kalimat))
    print()  # Pindah ke baris baru

def ascii_pulau():
    """ASCII Art: Pulau Arunika"""
    print("""
         🏝️ PULAU ARUNIKA 🏝️
        /    \\
       /  ⛰️  \\
      /________\\
    """)

def ascii_peta_pulau():
    """ASCII Art: Peta Pulau Arunika menuju harta karun"""
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║          🗺️ PETA PULAU ARUNIKA 🗺️                         ║
    ╚════════════════════════════════════════════════════════════╝
    
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
    
    LEGENDA:
    🌲 = Hutan (Monster Muncul)
    ⛰️  = Gunung (Area Berbahaya, Makanan Sulit)
    🏛️  = Kuil (Berisi Puzzle Penting)
    💎 = Tujuan Akhir
    ⚔️  = Musuh Kuat
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

def tampilkan_status(nama, nyawa, makanan, inventory):
    """Menampilkan status pemain dengan format yang rapi"""
    print("\n" + "=" * 70)
    print(f"👤 PETUALANG: {nama.upper()}")
    print("=" * 70)
    
    # Status Nyawa
    print(f"❤️  NYAWA: {nyawa} HP", end="")
    if nyawa < 30:
        print(" ⚠️ KRITIS!")
    elif nyawa < 60:
        print(" ⚠️ TERLUKA")
    else:
        print(" ✅ SEHAT")
    
    # Status Makanan dengan kotak
    print(f"🍖 MAKANAN: ", end="")
    for i in range(makanan):
        print("■", end="")
    for i in range(5 - makanan):
        print("□", end="")
    print(f" ({makanan}/5)")
    
    # Inventory
    if inventory:
        items_str = ", ".join(inventory)
        print(f"🎒 INVENTORY: {items_str}")
    else:
        print(f"🎒 INVENTORY: Kosong")
    
    print("=" * 70 + "\n")

# ===== SISTEM MONSTER =====
MONSTER_LIST = {
    "Kelelawar Gelap": {"nyawa": 10, "reward_makanan": 1, "reward_item": "Daun Penyembuh"},
    "Arwah Gua": {"nyawa": 15, "reward_makanan": 2, "reward_item": "Tongkat Mistis"},
    "Serigala Hutan": {"nyawa": 20, "reward_makanan": 2, "reward_item": "Bulu Perak"},
    "Ogre Batu": {"nyawa": 25, "reward_makanan": 3, "reward_item": "Batu Kuat"},
    "Naga Kecil": {"nyawa": 30, "reward_makanan": 3, "reward_item": "Sisik Naga"},
}

def battle_monster(nama, monster_name, nyawa, makanan, inventory):
    """Sistem pertarungan dengan monster"""
    
    print("\n" + "!" * 70)
    print(f"⚠️  MONSTER MUNCUL: {monster_name.upper()}!")
    print("!" * 70 + "\n")
    time.sleep(0.5)
    
    monster = MONSTER_LIST.get(monster_name, {"nyawa": 15, "reward_makanan": 1, "reward_item": "Item Biasa"})
    monster_hp = monster["nyawa"]
    
    while monster_hp > 0 and nyawa > 0:
        print(f"\n👹 {monster_name}: {monster_hp} HP")
        print(f"❤️  {nama}: {nyawa} HP\n")
        
        print("Pilihan Aksi:")
        print("1. 🤜 Serang dengan tangan kosong")
        
        # Tampilkan item yang ada di inventory
        action_num = 2
        item_actions = {}
        lari_action = None
        
        if "Tongkat Mistis" in inventory:
            print(f"{action_num}. 🪄 Serang dengan Tongkat Mistis (+5 DMG)")
            item_actions[str(action_num)] = ("Tongkat Mistis", 5, 12)
            action_num += 1
        if "Batu Kuat" in inventory:
            print(f"{action_num}. 🪨 Lempar Batu Kuat (+8 DMG)")
            item_actions[str(action_num)] = ("Batu Kuat", 6, 14)
            action_num += 1
        if "Daun Penyembuh" in inventory:
            print(f"{action_num}. 🌿 Gunakan Daun Penyembuh (+10 HP)")
            item_actions[str(action_num)] = ("Daun Penyembuh", "heal", 15)
            action_num += 1
        
        lari_action = str(action_num)
        print(f"{action_num}. 🏃 Coba Lari")
        
        while True:
            try:
                pilihan = input("\nPilihan: ").strip()
                if pilihan in ["1"] + list(item_actions.keys()) + [lari_action]:
                    break
                else:
                    print("❌ Pilihan tidak valid! Coba lagi.")
            except EOFError:
                efek_teks("\n⚠️ Input error! Pertarungan berakhir.", jeda=0.02)
                return nyawa, makanan, inventory, False
            except KeyboardInterrupt:
                print("\n\n⚠️ Permainan dibatalkan.")
                return nyawa, makanan, inventory, False
        
        damage = 0
        item_used = None
        
        if pilihan == "1":
            damage = random.randint(3, 8)
            efek_teks(f"💥 Kamu menyerang dengan tangan kosong! Damage: {damage}", jeda=0.02)
        elif pilihan in item_actions:
            item_info = item_actions[pilihan]
            item_name = item_info[0]
            
            if item_name == "Daun Penyembuh":
                heal = random.randint(8, 15)
                nyawa = min(nyawa + heal, 100)
                efek_teks(f"🌿 Kamu menggunakan Daun Penyembuh! +{heal} HP", jeda=0.02)
                inventory.remove(item_name)
                
                # Monster menyerang saat player healing
                monster_damage = random.randint(2, 6)
                nyawa -= monster_damage
                efek_teks(f"💢 {monster_name} menyerangmu! -{monster_damage} HP", jeda=0.02)
                continue
            else:
                damage = random.randint(item_info[1], item_info[2])
                efek_teks(f"💥 Kamu menyerang dengan {item_name}! Damage: {damage}", jeda=0.02)
                item_used = item_name
        elif pilihan == lari_action:
            if random.randint(1, 100) > 50:
                efek_teks(f"🏃 Kamu berhasil lari dari {monster_name}!", jeda=0.02)
                return nyawa, makanan, inventory, False
            else:
                efek_teks(f"💢 Kamu tidak bisa lari! {monster_name} menyerangmu!", jeda=0.02)
                monster_damage = random.randint(3, 8)
                nyawa -= monster_damage
                efek_teks(f"-{monster_damage} HP", jeda=0.02)
                continue
        else:
            # Default action - serangan tangan kosong
            damage = random.randint(2, 5)
            efek_teks(f"💥 Kamu menyerang! Damage: {damage}", jeda=0.02)
        
        # Monster menerima damage
        monster_hp -= damage
        
        # Hapus item jika sudah digunakan
        if item_used and item_used in inventory:
            inventory.remove(item_used)
        
        # Monster counterattack
        if monster_hp > 0:
            monster_damage = random.randint(2, 8)
            nyawa -= monster_damage
            efek_teks(f"💢 {monster_name} menyerangmu! -{monster_damage} HP", jeda=0.02)
        
        time.sleep(0.3)
    
    if monster_hp <= 0:
        efek_teks(f"\n🎉 Kamu berhasil mengalahkan {monster_name}!", jeda=0.02)
        
        # Reward makanan
        makanan_reward = monster["reward_makanan"]
        makanan = min(makanan + makanan_reward, 5)
        efek_teks(f"🍖 Kamu mendapat {makanan_reward} makanan! Total: {makanan}/5", jeda=0.02)
        
        # Reward item
        if random.randint(1, 100) > 40:  # 60% chance dapat item
            item_reward = monster["reward_item"]
            inventory.append(item_reward)
            efek_teks(f"📦 Kamu mendapat: {item_reward}", jeda=0.02)
        
        return nyawa, makanan, inventory, True
    else:
        efek_teks(f"\n💀 Kamu dikalahkan oleh {monster_name}!", jeda=0.02)
        return nyawa, makanan, inventory, False

def cerita_pembuka():
    """Menampilkan cerita pembuka yang menarik"""
    print("\n")
    efek_teks("╔" + "═" * 68 + "╗", jeda=0.01)
    efek_teks("║" + " " * 68 + "║", jeda=0.01)
    efek_teks("║" + "  🏝️ SELAMAT DATANG DI PULAU ARUNIKA 🏝️".center(68) + "║", jeda=0.01)
    efek_teks("║" + "  PENCARIAN HARTA KARUN LEGENDARIS".center(68) + "║", jeda=0.01)
    efek_teks("║" + " " * 68 + "║", jeda=0.01)
    efek_teks("╚" + "═" * 68 + "╝", jeda=0.01)
    
    ascii_pulau()
    time.sleep(1.5)
    
    efek_teks("\n" + "▓" * 70, jeda=0.01)
    efek_teks("📖 CERITA DIMULAI...", jeda=0.02)
    efek_teks("▓" * 70 + "\n", jeda=0.01)
    time.sleep(0.8)
    
    efek_teks("Selamat datang di Pulau Arunika, sebuah pulau misterius yang konon", jeda=0.02)
    time.sleep(0.3)
    efek_teks("menyimpan harta karun peninggalan pelaut legendaris.", jeda=0.02)
    time.sleep(0.5)
    
    efek_teks("\nSelama bertahun-tahun, banyak orang mencoba menemukannya,", jeda=0.02)
    time.sleep(0.3)
    efek_teks("tetapi tak satu pun yang berhasil kembali dengan harta.",jeda=0.02)
    time.sleep(0.5)
    
    efek_teks("\n⚡ Hari ini, kamulah yang terpilih untuk memulai petualangan ini!", jeda=0.02)
    time.sleep(0.8)
    
    efek_teks("\n✦ Ikuti petunjuk dengan cermat...", jeda=0.02)
    time.sleep(0.3)
    efek_teks("✦ Pecahkan teka-teki yang tersebar...", jeda=0.02)
    time.sleep(0.3)
    efek_teks("✦ Hadapi makhluk-makhluk berbahaya...", jeda=0.02)
    time.sleep(0.3)
    efek_teks("✦ Temukan harta karun sebelum waktu habis!", jeda=0.02)
    time.sleep(1)
    
    efek_teks("\n🔴 Perhatian: Perjalanan ini penuh dengan bahaya.", jeda=0.02)
    time.sleep(0.3)
    efek_teks("Kelola makananmu, jaga nyawamu, dan kumpulkan item berharga", jeda=0.02)
    time.sleep(0.3)
    efek_teks("untuk mengalahkan musuh-musuh yang menghadang!", jeda=0.02)
    time.sleep(1)
    
    efek_teks("\n💪 Apakah kamu siap untuk menerima tantangan? Mari kita lihat peta!", jeda=0.02)
    time.sleep(1)
    
    print("\n")

def tampilkan_peta():
    """Menampilkan peta pulau"""
    ascii_peta_pulau()
    time.sleep(2)
    efek_teks("\nIkuti jalur yang ditandai untuk mencapai harta karun legendaris!", jeda=0.02)
    time.sleep(0.5)

def eksplorasi_hutan(nama, nyawa, makanan, inventory):
    """Adventure exploration dengan random monster encounter"""
    print("\n" + "=" * 70)
    print("🌲 MEMASUKI HUTAN BELANTARA ARUNIKA 🌲")
    print("=" * 70)
    
    efek_teks(f"\nKamu melangkah masuk ke hutan yang gelap dan berbahaya...", jeda=0.02)
    time.sleep(0.5)
    
    stage_hutan = 0
    monster_dikalahkan = 0
    
    while stage_hutan < 3:  # 3 stage eksplorasi
        stage_hutan += 1
        tampilkan_status(nama, nyawa, makanan, inventory)
        
        print(f"📍 STAGE {stage_hutan}/3 - Eksplorasi Hutan")
        print("\nApa yang akan kamu lakukan?")
        print("1. 🔍 Jelajahi lebih dalam (kemungkinan bertemu monster)")
        print("2. 🏕️ Istirahat dan cari makanan")
        print("3. 📍 Cari jalan ke gunung")
        
        while True:
            pilihan = input("\nPilihan (1-3): ").strip()
            if pilihan in ["1", "2", "3"]:
                break
            else:
                print("❌ Pilihan tidak valid! Masukkan 1, 2, atau 3.")
        
        if pilihan == "1":
            # Kemungkinan bertemu monster
            if random.randint(1, 100) > 40:  # 60% chance bertemu monster
                monster_name = random.choice(list(MONSTER_LIST.keys()))
                print()
                nyawa, makanan, inventory, menang = battle_monster(nama, monster_name, nyawa, makanan, inventory)
                
                if not menang:
                    return nyawa, makanan, inventory, False, monster_dikalahkan
                
                if menang:
                    monster_dikalahkan += 1
            else:
                efek_teks("\n✨ Kamu berjalan tanpa bertemu makhluk berbahaya.", jeda=0.02)
                efek_teks("Tapi kamu menemukan beberapa buah dan binatang buruan!", jeda=0.02)
                makanan = min(makanan + 1, 5)
                efek_teks(f"🍖 Makanan: {makanan}/5", jeda=0.02)
        
        elif pilihan == "2":
            efek_teks("\n🏕️ Kamu berhenti untuk istirahat...", jeda=0.02)
            
            # Cek makanan
            if makanan >= 5:
                efek_teks("Perutmu sudah penuh, tidak perlu makan lagi!", jeda=0.02)
            else:
                makanan = min(makanan + 2, 5)
                efek_teks(f"😋 Kamu makan dan merasa segar kembali! Makanan: {makanan}/5", jeda=0.02)
            
            # Ada kemungkinan monster muncul saat istirahat
            if random.randint(1, 100) > 70:  # 30% chance
                efek_teks("\n⚠️ Saat kamu istirahat, ada suara mendekat!", jeda=0.02)
                monster_name = random.choice(list(MONSTER_LIST.keys()))
                print()
                nyawa, makanan, inventory, menang = battle_monster(nama, monster_name, nyawa, makanan, inventory)
                
                if not menang:
                    return nyawa, makanan, inventory, False, monster_dikalahkan
                
                if menang:
                    monster_dikalahkan += 1
        
        elif pilihan == "3":
            efek_teks("\n🗺️ Kamu mengikuti jejak ke arah gunung...", jeda=0.02)
            efek_teks("Setelah perjalanan yang cukup jauh, kamu berhasil keluar dari hutan!", jeda=0.02)
            break
        
        # Cek kesehatan
        if nyawa <= 0:
            return nyawa, makanan, inventory, False, monster_dikalahkan
        
        # Kurangi makanan setiap stage (hunger system)
        makanan = max(makanan - 1, 0)
        
        if makanan == 0:
            efek_teks("\n⚠️ Kamu kelaparan! Nyawa berkurang!", jeda=0.02)
            nyawa -= 10
            if nyawa <= 0:
                efek_teks("💀 Kamu meninggal kelaparan!", jeda=0.02)
                return nyawa, makanan, inventory, False, monster_dikalahkan
        
        time.sleep(0.5)
    
    return nyawa, makanan, inventory, True, monster_dikalahkan

def eksplorasi_gunung(nama, nyawa, makanan, inventory):
    """Eksplorasi gunung berbahaya"""
    print("\n" + "=" * 70)
    print("⛰️ MENDAKI GUNUNG ARUNIKA (AREA BERBAHAYA) ⛰️")
    print("=" * 70)
    
    efek_teks(f"\nKamu mulai mendaki gunung yang curam dan berbatuan...", jeda=0.02)
    time.sleep(0.5)
    
    stage_gunung = 0
    monster_dikalahkan = 0
    
    while stage_gunung < 2:  # 2 stage di gunung (lebih sulit)
        stage_gunung += 1
        tampilkan_status(nama, nyawa, makanan, inventory)
        
        print(f"📍 STAGE {stage_gunung}/2 - Pendakian Gunung")
        print("\nApa yang akan kamu lakukan?")
        print("1. ⛰️ Terus mendaki (makanan susah didapat, monster muncul lebih sering)")
        print("2. 🏕️ Istirahat sebentar")
        print("3. 📍 Cari lintasan menuju kuil kuno")
        
        while True:
            pilihan = input("\nPilihan (1-3): ").strip()
            if pilihan in ["1", "2", "3"]:
                break
            else:
                print("❌ Pilihan tidak valid! Masukkan 1, 2, atau 3.")
        
        if pilihan == "1":
            # Gunung lebih berbahaya - 75% chance bertemu monster
            if random.randint(1, 100) > 25:
                monster_name = random.choice(list(MONSTER_LIST.keys()))
                print()
                nyawa, makanan, inventory, menang = battle_monster(nama, monster_name, nyawa, makanan, inventory)
                
                if not menang:
                    return nyawa, makanan, inventory, False, monster_dikalahkan
                
                if menang:
                    monster_dikalahkan += 1
            else:
                efek_teks("\n✨ Kamu menemukan beberapa kristal yang bisa ditukar dengan makanan!", jeda=0.02)
                makanan = min(makanan + 1, 5)
                efek_teks(f"🍖 Makanan: {makanan}/5", jeda=0.02)
        
        elif pilihan == "2":
            efek_teks("\n🏕️ Kamu beristirahat di tebing gunung...", jeda=0.02)
            
            if makanan >= 5:
                efek_teks("Perutmu sudah penuh!", jeda=0.02)
            else:
                makanan = min(makanan + 1, 5)
                efek_teks(f"😋 Kamu makan dan recovery! Makanan: {makanan}/5", jeda=0.02)
            
            # 40% chance monster muncul saat istirahat di gunung
            if random.randint(1, 100) > 60:
                efek_teks("\n⚠️ Ada suara batu yang bergesekan!", jeda=0.02)
                monster_name = random.choice(list(MONSTER_LIST.keys()))
                print()
                nyawa, makanan, inventory, menang = battle_monster(nama, monster_name, nyawa, makanan, inventory)
                
                if not menang:
                    return nyawa, makanan, inventory, False, monster_dikalahkan
                
                if menang:
                    monster_dikalahkan += 1
        
        elif pilihan == "3":
            efek_teks("\n🗺️ Kamu menemukan jalan setapak menuju kuil kuno!", jeda=0.02)
            efek_teks("Cahaya keemasan terlihat di jauh hari!", jeda=0.02)
            break
        
        if nyawa <= 0:
            return nyawa, makanan, inventory, False, monster_dikalahkan
        
        # Makanan berkurang lebih cepat di gunung
        makanan = max(makanan - 2, 0)
        
        if makanan == 0:
            efek_teks("\n⚠️ Kamu sangat kelaparan! Nyawa berkurang drastis!", jeda=0.02)
            nyawa -= 15
            if nyawa <= 0:
                efek_teks("💀 Kamu jatuh dari gunung karena kelemahan!", jeda=0.02)
                return nyawa, makanan, inventory, False, monster_dikalahkan
        
        time.sleep(0.5)
    
    return nyawa, makanan, inventory, True, monster_dikalahkan

def puzzle_kuil(nama):
    """Puzzle di kuil kuno"""
    print("\n" + "=" * 70)
    print("🏛️ KUIL KUNO ARUNIKA 🏛️")
    print("=" * 70)
    
    efek_teks("\nKamu memasuki kuil yang indah dengan ukiran-ukiran kuno...", jeda=0.02)
    time.sleep(0.5)
    efek_teks("Di dinding kuil terdapat tiga pintu, dan di depannya ada nisan batu", jeda=0.02)
    time.sleep(0.3)
    efek_teks("dengan tulisan misterius:", jeda=0.02)
    time.sleep(0.5)
    
    print("\n" + ">" * 70)
    print("""
    "Aku adalah awal dari akhir, dan akhir dari waktu.
    Aku ada di tengah alam semesta, tetapi tak di bumi.
    Aku hadir dalam malam, tetapi tidak di siang hari.
    Apa aku?"
    """)
    print(">" * 70)
    
    print("\nPilihan Jawaban:")
    print("1. GELAP")
    print("2. HURUF 'E'")
    print("3. MATAHARI")
    
    while True:
        try:
            jawaban = input("\nJawaban kamu (1, 2 atau 3): ").strip()
            if jawaban in ["1", "2", "3"]:
                break
            else:
                print("❌ Jawaban tidak valid! Masukkan 1, 2, atau 3.")
        except EOFError:
            print("\n⚠️ Input error! Game berakhir.")
            return False
        except KeyboardInterrupt:
            print("\n⚠️ Game dibatalkan.")
            return False
    
    if jawaban == "2":
        efek_teks("\n✨ BENAR! Huruf 'E' adalah awal dan akhir! 🎯", jeda=0.02)
        efek_teks("Pintu tengah terbuka dan menunjukkan jalan ke bawah tanah!", jeda=0.02)
        ascii_harta_karun()
        return True
    else:
        efek_teks("\n❌ Jawaban salah! Pintu menutup dan kamu terjebak sejenak...", jeda=0.02)
        time.sleep(0.5)
        efek_teks("Namun kamu menemukan cara keluar alternatif melalui jendela samping.", jeda=0.02)
        return False

def pertarungan_final(nama, nyawa, makanan, inventory):
    """Pertarungan final melawan penjaga harta karun"""
    print("\n" + "=" * 70)
    print("🏰 RUANG HARTA KARUN LEGENDARIS 🏰")
    print("=" * 70)
    
    tampilkan_status(nama, nyawa, makanan, inventory)
    
    efek_teks("\nKamu masuk ke ruangan besar dengan cahaya emas yang membutakan...", jeda=0.02)
    time.sleep(0.5)
    efek_teks("Di tengah ruangan, terdapat prajurit kuno berjaket emas yang berkilau!", jeda=0.02)
    time.sleep(0.5)
    
    print("\n" + "!" * 70)
    print("👹 PENJAGA ABADI HARTA KARUN ARUNIKA")
    print("!" * 70)
    
    efek_teks("\nPrajurit berkata dengan suara menggelegar:", jeda=0.02)
    efek_teks("'Siapa berani mengambil harta warisan Raja Arunika?", jeda=0.02)
    efek_teks("Kamu harus melewatiku terlebih dahulu!'", jeda=0.02)
    time.sleep(1)
    
    # Battle dengan penjaga
    penjaga_hp = 60
    
    while penjaga_hp > 0 and nyawa > 0:
        print(f"\n👹 Prajurit Penjaga: {penjaga_hp} HP")
        print(f"❤️  {nama}: {nyawa} HP\n")
        
        print("Pilihan Aksi:")
        print("1. 🤜 Serang dengan tangan kosong")
        
        action_num = 2
        item_actions = {}
        mundur_action = None
        
        if "Tongkat Mistis" in inventory:
            print(f"{action_num}. 🪄 Serang dengan Tongkat Mistis")
            item_actions[str(action_num)] = "Tongkat Mistis"
            action_num += 1
        if "Batu Kuat" in inventory:
            print(f"{action_num}. 🪨 Lempar Batu Kuat")
            item_actions[str(action_num)] = "Batu Kuat"
            action_num += 1
        if "Sisik Naga" in inventory:
            print(f"{action_num}. 🐉 Gunakan Sisik Naga")
            item_actions[str(action_num)] = "Sisik Naga"
            action_num += 1
        if "Daun Penyembuh" in inventory:
            print(f"{action_num}. 🌿 Gunakan Daun Penyembuh")
            item_actions[str(action_num)] = "Daun Penyembuh"
            action_num += 1
        
        mundur_action = str(action_num)
        print(f"{action_num}. 🏃 Mundur dan coba lagi")
        
        while True:
            try:
                pilihan = input("\nPilihan: ").strip()
                if pilihan in ["1"] + list(item_actions.keys()) + [mundur_action]:
                    break
                else:
                    print("❌ Pilihan tidak valid! Coba lagi.")
            except EOFError:
                efek_teks("\n⚠️ Input error! Pertarungan berakhir.", jeda=0.02)
                return nyawa, makanan, inventory, False
            except KeyboardInterrupt:
                print("\n\n⚠️ Permainan dibatalkan.")
                return nyawa, makanan, inventory, False
        
        damage = 0
        item_used = None
        
        if pilihan == "1":
            damage = random.randint(5, 12)
            efek_teks(f"💥 Kamu menyerang Prajurit! Damage: {damage}", jeda=0.02)
        elif pilihan in item_actions:
            item_name = item_actions[pilihan]
            
            if item_name == "Daun Penyembuh":
                heal = random.randint(10, 20)
                nyawa = min(nyawa + heal, 100)
                efek_teks(f"🌿 Daun menyembuhimu! +{heal} HP", jeda=0.02)
                inventory.remove(item_name)
                
                # Penjaga menyerang
                penjaga_damage = random.randint(8, 15)
                nyawa -= penjaga_damage
                efek_teks(f"⚔️ Prajurit menyerangmu! -{penjaga_damage} HP", jeda=0.02)
                continue
            elif item_name == "Tongkat Mistis":
                damage = random.randint(8, 16)
                efek_teks(f"✨ Tongkat Mistis bersinar! Damage: {damage}", jeda=0.02)
                item_used = item_name
            elif item_name == "Batu Kuat":
                damage = random.randint(10, 18)
                efek_teks(f"🪨 Batu Kuat terbang! Damage: {damage}", jeda=0.02)
                item_used = item_name
            elif item_name == "Sisik Naga":
                damage = random.randint(15, 25)
                efek_teks(f"🐉 Kekuatan Naga meledak! Damage: {damage}", jeda=0.02)
                item_used = item_name
        elif pilihan == mundur_action:
            efek_teks("\nKamu mundur untuk merancang strategi lagi...", jeda=0.02)
            return nyawa, makanan, inventory, False
        else:
            damage = random.randint(3, 8)
            efek_teks(f"💥 Serangan biasa! Damage: {damage}", jeda=0.02)
        
        penjaga_hp -= damage
        
        if item_used and item_used in inventory:
            inventory.remove(item_used)
        
        if penjaga_hp > 0:
            penjaga_damage = random.randint(8, 15)
            nyawa -= penjaga_damage
            efek_teks(f"⚔️ Prajurit membalas! -{penjaga_damage} HP", jeda=0.02)
        
        time.sleep(0.3)
    
    if penjaga_hp <= 0:
        efek_teks("\n🎉 KEMENANGAN! Prajurit akhirnya jatuh dan lenyap!", jeda=0.02)
        time.sleep(1)
        return nyawa, makanan, inventory, True
    else:
        efek_teks("\n💀 Kamu dikalahkan oleh Prajurit!", jeda=0.02)
        return nyawa, makanan, inventory, False

def game_utama():
    """GAME UTAMA: PETUALANGAN PULAU ARUNIKA"""
    cerita_pembuka()
    
    while True:
        try:
            nama = input("\n🏴 Siapa nama petualangmu? ").strip()
            if len(nama) > 0:
                break
            else:
                print("❌ Nama tidak boleh kosong! Coba lagi.")
        except EOFError:
            print("\n⚠️ Input error! Game berakhir.")
            return False
        except KeyboardInterrupt:
            print("\n⚠️ Game dibatalkan.")
            return False
    
    efek_teks(f"\n👋 Selamat datang, {nama}!", jeda=0.02)
    efek_teks(f"Kamu adalah petualang terpilih yang akan mencari harta karun legendaris!", jeda=0.02)
    ascii_kompas()
    time.sleep(1)
    
    # Tampilkan peta
    print("\nSalah satu langkah pertama adalah melihat peta:")
    tampilkan_peta()
    
    # INISIALISASI GAME
    nyawa = 100
    makanan = 3  # Mulai dengan 3 makanan
    inventory = []
    monster_dikalahkan_total = 0
    
    tampilkan_status(nama, nyawa, makanan, inventory)
    
    efek_teks(f"\nPerjalananmu dimulai sekarang, {nama}. Semoga berhasil!\n", jeda=0.02)
    time.sleep(0.5)
    
    # ===== EKSPLORASI HUTAN =====
    nyawa, makanan, inventory, berhasil, monster_hutan = eksplorasi_hutan(nama, nyawa, makanan, inventory)
    monster_dikalahkan_total += monster_hutan
    
    if nyawa <= 0:
        efek_teks(f"\n💀 {nama} telah gugur dalam hutan Arunika!", jeda=0.02)
        ascii_korban()
        return False
    
    if not berhasil:
        efek_teks(f"\n⚠️ Kamu tidak berhasil melalui hutan dengan selamat!", jeda=0.02)
        return False
    
    time.sleep(1)
    
    # ===== EKSPLORASI GUNUNG =====
    nyawa, makanan, inventory, berhasil, monster_gunung = eksplorasi_gunung(nama, nyawa, makanan, inventory)
    monster_dikalahkan_total += monster_gunung
    
    if nyawa <= 0:
        efek_teks(f"\n💀 {nama} jatuh dari gunung Arunika!", jeda=0.02)
        ascii_korban()
        return False
    
    if not berhasil:
        efek_teks(f"\n⚠️ Kamu gagal mendaki gunung!", jeda=0.02)
        return False
    
    time.sleep(1)
    
    # ===== PUZZLE KUIL =====
    puzzle_benar = puzzle_kuil(nama)
    time.sleep(1)
    
    # ===== PERTARUNGAN FINAL =====
    nyawa, makanan, inventory, menang_final = pertarungan_final(nama, nyawa, makanan, inventory)
    
    if nyawa <= 0:
        efek_teks(f"\n💀 {nama} tewas dalam pertarungan terakhir!", jeda=0.02)
        ascii_korban()
        return False
    
    time.sleep(1)
    
    # ===== HASIL AKHIR =====
    print("\n" + "=" * 70)
    print(f"📊 HASIL AKHIR PETUALANGAN {nama.upper()}")
    print("=" * 70)
    print(f"❤️ Nyawa Akhir: {nyawa} HP")
    print(f"🍖 Makanan Sisa: {makanan}/5")
    print(f"⚔️ Monster Dikalahkan: {monster_dikalahkan_total}")
    print(f"🧩 Puzzle Terpecahkan: {'YA ✅' if puzzle_benar else 'TIDAK ❌'}")
    print(f"🏆 Pertarungan Final: {'MENANG ✅' if menang_final else 'KALAH ❌'}")
    
    if menang_final and nyawa > 0:
        efek_teks(f"\n🏆 LUAR BIASA {nama}! KAMU ADALAH PENAKLUK PULAU ARUNIKA! 🏆", jeda=0.02)
        time.sleep(0.5)
        efek_teks("Kamu berhasil mendapatkan HARTA KARUN LEGENDARIS!", jeda=0.02)
        time.sleep(0.5)
        ascii_harta_karun()
        time.sleep(0.5)
        efek_teks("Batu mulia, koin emas, dan perhiasan langka bersinar membawamu kaya raya!", jeda=0.02)
        time.sleep(0.5)
        efek_teks("Legenda tentang keberanianmu akan dikenang selamanya di Pulau Arunika!", jeda=0.02)
        return True
    elif nyawa > 0:
        efek_teks(f"\n👍 Bagus {nama}! Kamu berhasil melewati banyak tantangan!", jeda=0.02)
        efek_teks(f"Namun, Prajurit Penjaga masih menjaga harta karun. Coba lagi!", jeda=0.02)
        return False
    else:
        efek_teks(f"\n⚠️ Sayang sekali {nama}! Petualanganmu berakhir tragis.", jeda=0.02)
        ascii_korban()
        return False

def main_loop():
    """Main loop untuk permainan"""
    while True:
        if game_utama():
            time.sleep(1)
            lanjut = input("\n🎮 Mau mencoba petualangan baru? (y/n): ").lower()
            if lanjut != 'y':
                efek_teks("\n👋 Terima kasih telah bermain di Pulau Arunika!", jeda=0.02)
                efek_teks("Sampai jumpa di petualangan berikutnya!", jeda=0.02)
                break
        else:
            time.sleep(1)
            lanjut = input("\n🎮 Mau mencoba lagi? (y/n): ").lower()
            if lanjut != 'y':
                efek_teks("\n👋 Terima kasih telah bermain di Pulau Arunika!", jeda=0.02)
                efek_teks("Sampai jumpa di petualangan berikutnya!", jeda=0.02)
                break

if __name__ == "__main__":
    main_loop()
