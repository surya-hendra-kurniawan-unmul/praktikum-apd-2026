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

while True:
    os.system(clear)
    print("=" * 40)
    print("   SISTEM MANAJEMEN KAMAR HOTEL")
    print("=" * 40)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("=" * 40)
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        os.system(clear)
        print("=== LOGIN ===")
        username = input("Username : ")
        password = input("Password : ")

        akun = users.get(username)
        if akun is None or akun["password"] != password:
            print("Error: Username atau password salah!")
            input("Tekan Enter untuk kembali...")
            continue

        role = akun["role"]
        print(f"Login berhasil! Selamat datang, {username} ({role}).")
        input("Tekan Enter untuk melanjutkan...")

        while True:
            os.system(clear)
            print("=" * 40)
            print(f"   MENU {role.upper()}")
            print("=" * 40)

            if role == "admin":
                print("1. Tambah Kamar")
                print("2. Lihat Kamar")
                print("3. Ubah Kamar")
                print("4. Hapus Kamar")
                print("5. Logout")
                print("=" * 40)
                menu = input("Pilih menu (1-5): ")

                if menu == "1":
                    os.system(clear)
                    print("=== TAMBAH KAMAR ===")
                    nomor = input("Nomor Kamar : ").strip()

                    if nomor == "":
                        print("Error: Nomor kamar tidak boleh kosong!")
                    elif nomor in kamar_hotel:
                        print("Error: Nomor kamar sudah ada!")
                    else:
                        print("Tipe Kamar:")
                        for kode, nama in tipe_kamar.items():
                            print(f"{kode}. {nama}")
                        pilih_tipe = input("Pilih tipe (1-3) : ").strip()
                        harga = input("Harga Kamar : ")
                        if pilih_tipe not in tipe_kamar:
                            print("Error: Pilihan tipe tidak valid!")
                        elif not harga.isdigit():
                            print("Error: Harga harus berupa angka!")
                        else:
                            print("Status: 1. Tersedia  2. Terisi")
                            st = input("Pilih status (1/2): ")
                            if st in status_kamar:
                                kamar_hotel[nomor] = {
                                    "tipe": tipe_kamar[pilih_tipe],
                                    "harga": int(harga),
                                    "status": status_kamar[st]
                                }
                                print("Kamar berhasil ditambahkan!")
                            else:
                                print("Error: Pilihan status tidak valid!")
                    input("Tekan Enter untuk melanjutkan...")

                elif menu == "2":
                    os.system(clear)
                    print("=== DAFTAR KAMAR ===")
                    if len(kamar_hotel) == 0:
                        print("Belum ada data kamar.")
                    else:
                        print("-" * 55)
                        print(f"{'No':<4} | {'No Kamar':<10} | {'Tipe':<12} | {'Harga':<10} | {'Status':<10}")
                        print("-" * 55)
                        no = 1
                        for nomor, data in kamar_hotel.items():
                            print(f"{no:<4} | {nomor:<10} | {data['tipe']:<12} | {data['harga']:<10} | {data['status']:<10}")
                            no += 1
                        print("-" * 55)
                    input("Tekan Enter untuk melanjutkan...")

                elif menu == "3":
                    os.system(clear)
                    print("=== UBAH KAMAR ===")
                    nomor = input("Nomor kamar yang diubah: ").strip()

                    if nomor not in kamar_hotel:
                        print("Error: Nomor kamar tidak ditemukan!")
                    else:
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
                            print("Error: Pilihan tipe tidak valid!")
                        elif harga != "" and not harga.isdigit():
                            print("Error: Harga harus berupa angka!")
                        elif st != "" and st not in status_kamar:
                            print("Error: Pilihan status tidak valid!")
                        elif pilih_tipe == "" and harga == "" and st == "":
                            print("Tidak ada data yang diubah.")
                        else:
                            if pilih_tipe != "":
                                kamar_hotel[nomor]["tipe"] = tipe_kamar[pilih_tipe]
                            if harga != "":
                                kamar_hotel[nomor]["harga"] = int(harga)
                            if st != "":
                                kamar_hotel[nomor]["status"] = status_kamar[st]
                            print("Kamar berhasil diperbarui!")
                    input("Tekan Enter untuk melanjutkan...")

                elif menu == "4":
                    os.system(clear)
                    print("=== HAPUS KAMAR ===")
                    nomor = input("Nomor kamar yang dihapus: ").strip()

                    if nomor not in kamar_hotel:
                        print("Error: Nomor kamar tidak ditemukan!")
                    else:
                        del kamar_hotel[nomor]
                        print(f"Kamar {nomor} berhasil dihapus!")
                    input("Tekan Enter untuk melanjutkan...")

                elif menu == "5":
                    break

                else:
                    print("Error: Pilihan menu tidak valid!")
                    input("Tekan Enter untuk melanjutkan...")

            else:
                print("1. Pesan Kamar")
                print("2. Logout")
                print("=" * 40)
                menu = input("Pilih menu (1-2): ")

                if menu == "1":
                    os.system(clear)
                    print("=== PESAN KAMAR ===")
                    print("-" * 55)
                    print(f"{'No':<4} | {'No Kamar':<10} | {'Tipe':<12} | {'Harga':<10} | {'Status':<10}")
                    print("-" * 55)
                    no = 1
                    for nomor_kamar, data in kamar_hotel.items():
                        if data["status"] == "Tersedia":
                            print(f"{no:<4} | {nomor_kamar:<10} | {data['tipe']:<12} | {data['harga']:<10} | {data['status']:<10}")
                            no += 1
                    print("-" * 55)
                    if no == 1:
                        print("Saat ini tidak ada kamar yang tersedia.")
                    else:
                        nomor = input("Nomor kamar yang dipesan: ").strip()

                        kamar = kamar_hotel.get(nomor)

                        if kamar is None:
                            print("Error: Nomor kamar tidak ditemukan!")
                        elif kamar["status"] == "Terisi":
                            print("Error: Kamar sedang terisi!")
                        else:
                            kamar["status"] = "Terisi"
                            print(f"Kamar {nomor} ({kamar['tipe']}) berhasil dipesan!")
                    input("Tekan Enter untuk melanjutkan...")

                elif menu == "2":
                    break

                else:
                    print("Error: Pilihan menu tidak valid!")
                    input("Tekan Enter untuk melanjutkan...")

    elif pilihan == "2":
        os.system(clear)
        print("=== REGISTER ===")
        username = input("Username Baru : ").strip()

        if username == "":
            print("Error: Username tidak boleh kosong!")
        elif username in users:
            print("Error: Username sudah digunakan!")
        else:
            password = input("Password Baru : ")
            if password.strip() == "":
                print("Error: Password tidak boleh kosong!")
            else:
                users[username] = {"password": password, "role": "pengguna"}
                print("Registrasi berhasil! Silakan login.")
        input("Tekan Enter untuk kembali ke menu utama...")

    elif pilihan == "3":
        os.system(clear)
        print("Kula Diamond: Bye-bye! {-_-} play this: https://youtu.be/CNjqpg-G1xE?si=kP-hEZbBwV7O2qmL")
        break

    else:
        print("Error: Pilihan menu tidak valid!")
        input("Tekan Enter untuk mencoba lagi...")
