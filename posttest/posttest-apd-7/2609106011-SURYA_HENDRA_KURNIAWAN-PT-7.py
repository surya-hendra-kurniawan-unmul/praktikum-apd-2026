import os

clear = 'cls' if os.name == 'nt' else 'clear'

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "SUHEKU": {"password": "SUHEKU83", "role": "admin"},
    "user": {"password": "user123", "role": "pengguna"},
    "test": {"password": "123456", "role": "pengguna"}
}

tipe_kamar = {"1": "Standard", "2": "Deluxe", "3": "Suite"}
status_kamar = {"1": "Tersedia", "2": "Terisi"}

kamar_hotel = {
    "101": {"tipe": "Standard", "harga": 300000, "status": "Tersedia"},
    "102": {"tipe": "Standard", "harga": 300000, "status": "Terisi"},
    "103": {"tipe": "Deluxe", "harga": 500000, "status": "Tersedia"},
    "104": {"tipe": "Deluxe", "harga": 500000, "status": "Terisi"},
    "105": {"tipe": "Suite", "harga": 1000000, "status": "Terisi"},
    "106": {"tipe": "Suite", "harga": 1000000, "status": "Tersedia"}
}

def jeda(pesan="Tekan Enter untuk melanjutkan..."):
    input(pesan)

def login():
    os.system(clear)
    print("=== LOGIN ===")
    username = input("Username : ")
    password = input("Password : ")

    role = cek_login(username, password)
    if role is None:
        jeda("Tekan Enter untuk kembali...")
    else:
        print(f"Login berhasil! Selamat datang, {username} ({role}).")
        jeda()
        if role == "admin":
            menu_admin()
        else:
            menu_pengguna()

def cek_login(username, password):
    try:
        akun = users[username]
        if akun["password"] != password:
            raise ValueError("Username atau password salah!")
    except KeyError:
        print("Error: Username atau password salah!")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    else:
        return akun["role"]

def register():
    os.system(clear)
    print("=== REGISTER ===")
    try:
        username = input("Username Baru : ").strip()
        if username == "":
            raise ValueError("Username tidak boleh kosong!")
        if username in users:
            raise ValueError("Username sudah digunakan!")

        password = input("Password Baru : ")
        if password.strip() == "":
            raise ValueError("Password tidak boleh kosong!")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        users[username] = {"password": password, "role": "pengguna"}
        print("Registrasi berhasil! Silakan login.")
    finally:
        jeda("Tekan Enter untuk kembali ke menu utama...")

def menu_utama():
    os.system(clear)
    print("=" * 40)
    print("   SISTEM MANAJEMEN KAMAR HOTEL")
    print("=" * 40)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("=" * 40)
    pilihan = input("Pilih menu (1-3): ")
    return pilihan

def input_harga():
    harga = input("Harga Kamar : ").strip()
    if not harga.isdigit():
        raise ValueError("Harga harus berupa angka!")
    if int(harga) <= 0:
        raise ValueError("Harga harus lebih dari 0!")
    return int(harga)

def menu_admin():
    while True:
        os.system(clear)
        print("=" * 40)
        print("   MENU ADMIN")
        print("=" * 40)
        print("1. Tambah Kamar")
        print("2. Lihat Kamar")
        print("3. Ubah Kamar")
        print("4. Hapus Kamar")
        print("5. Logout")
        print("=" * 40)
        menu = input("Pilih menu (1-5): ")

        if menu == "1":
            tambah_kamar()
        elif menu == "2":
            lihat_kamar()
        elif menu == "3":
            ubah_kamar()
        elif menu == "4":
            hapus_kamar()
        elif menu == "5":
            break
        else:
            print("Error: Pilihan menu tidak valid!")
            jeda()

def tambah_kamar():
    os.system(clear)
    print("=== TAMBAH KAMAR ===")
    try:
        nomor = input("Nomor Kamar : ").strip()
        if nomor == "":
            raise ValueError("Nomor kamar tidak boleh kosong!")
        if nomor in kamar_hotel:
            raise ValueError("Nomor kamar sudah ada!")

        print("Tipe Kamar:")
        for kode, nama in tipe_kamar.items():
            print(f"{kode}. {nama}")
        pilih_tipe = input("Pilih tipe (1-3) : ").strip()
        if pilih_tipe not in tipe_kamar:
            raise ValueError("Pilihan tipe tidak valid!")

        harga = input_harga()

        print("Status: 1. Tersedia  2. Terisi")
        st = input("Pilih status (1/2): ").strip()
        if st not in status_kamar:
            raise ValueError("Pilihan status tidak valid!")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        kamar_hotel[nomor] = {
            "tipe": tipe_kamar[pilih_tipe],
            "harga": harga,
            "status": status_kamar[st]
        }
        print("Kamar berhasil ditambahkan!")
    finally:
        jeda()

def tampilkan_tabel(data_kamar):
    print("-" * 55)
    print(f"{'No':<4} | {'No Kamar':<10} | {'Tipe':<12} | {'Harga':<10} | {'Status':<10}")
    print("-" * 55)
    no = 1
    for nomor, data in data_kamar.items():
        print(f"{no:<4} | {nomor:<10} | {data['tipe']:<12} | {data['harga']:<10} | {data['status']:<10}")
        no += 1
    print("-" * 55)

def lihat_kamar():
    os.system(clear)
    print("=== DAFTAR KAMAR ===")
    if len(kamar_hotel) == 0:
        print("Belum ada data kamar.")
    else:
        tampilkan_tabel(kamar_hotel)
    jeda()

def ubah_kamar():
    os.system(clear)
    print("=== UBAH KAMAR ===")
    try:
        nomor = input("Nomor kamar yang diubah: ").strip()
        lama = kamar_hotel[nomor]
        print(f"Data lama: {lama['tipe']}, Harga: {lama['harga']}, Status: {lama['status']}")
        print("Kosongkan (Enter) jika tidak ingin mengubah.")
        print("Tipe Kamar:")
        for kode, nama in tipe_kamar.items():
            print(f"{kode}. {nama}")
        pilih_tipe = input("Tipe Baru (1-3) : ").strip()
        harga = input("Harga Baru : ").strip()
        print("Status: 1. Tersedia  2. Terisi")
        st = input("Status Baru (1/2) : ").strip()

        if pilih_tipe != "" and pilih_tipe not in tipe_kamar:
            raise ValueError("Pilihan tipe tidak valid!")
        if harga != "" and not harga.isdigit():
            raise ValueError("Harga harus berupa angka!")
        if st != "" and st not in status_kamar:
            raise ValueError("Pilihan status tidak valid!")
        if pilih_tipe == "" and harga == "" and st == "":
            raise ValueError("Tidak ada data yang diubah!")
    except KeyError:
        print("Error: Nomor kamar tidak ditemukan!")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        if pilih_tipe != "":
            kamar_hotel[nomor]["tipe"] = tipe_kamar[pilih_tipe]
        if harga != "":
            kamar_hotel[nomor]["harga"] = int(harga)
        if st != "":
            kamar_hotel[nomor]["status"] = status_kamar[st]
        print("Kamar berhasil diperbarui!")
    finally:
        jeda()

def hapus_kamar():
    os.system(clear)
    print("=== HAPUS KAMAR ===")
    try:
        nomor = input("Nomor kamar yang dihapus: ").strip()
        del kamar_hotel[nomor]
    except KeyError:
        print("Error: Nomor kamar tidak ditemukan!")
    else:
        print(f"Kamar {nomor} berhasil dihapus!")
    finally:
        jeda()

def menu_pengguna():
    while True:
        os.system(clear)
        print("=" * 40)
        print("   MENU PENGGUNA")
        print("=" * 40)
        print("1. Pesan Kamar")
        print("2. Logout")
        print("=" * 40)
        menu = input("Pilih menu (1-2): ")

        if menu == "1":
            pesan_kamar()
        elif menu == "2":
            break
        else:
            print("Error: Pilihan menu tidak valid!")
            jeda()

def pesan_kamar():
    os.system(clear)
    print("=== PESAN KAMAR ===")

    tersedia = {}
    for nomor_kamar, data in kamar_hotel.items():
        if data["status"] == "Tersedia":
            tersedia[nomor_kamar] = data

    if len(tersedia) == 0:
        print("Saat ini tidak ada kamar yang tersedia.")
    else:
        tampilkan_tabel(tersedia)
        try:
            nomor = input("Nomor kamar yang dipesan: ").strip()
            if nomor not in kamar_hotel:
                raise KeyError("Nomor kamar tidak ditemukan!")
            
            kamar = kamar_hotel[nomor]
            if kamar["status"] == "Terisi":
                raise ValueError("Kamar sedang terisi!")
        except KeyError:
            print("Error: Nomor kamar tidak ditemukan!")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            kamar["status"] = "Terisi"
            print(f"Kamar {nomor} ({kamar['tipe']}) berhasil dipesan!")
    jeda()

if __name__ == "__main__":
    while True:
        pilihan = menu_utama()

        if pilihan == "1":
            login()
        elif pilihan == "2":
            register()
        elif pilihan == "3":
            os.system(clear)
            print("Kula Diamond: Bye-bye! {-_-} play this: https://youtu.be/CNjqpg-G1xE?si=kP-hEZbBwV7O2qmL")
            break
        else:
            print("Error: Pilihan menu tidak valid!")
            jeda("Tekan Enter untuk mencoba lagi...")