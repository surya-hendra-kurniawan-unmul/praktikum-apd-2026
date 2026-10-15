import os

clear = 'cls' if os.name == 'nt' else 'clear'

users = [
    ["admin", "admin123", "admin"],
    ["SUHEKU", "SUHEKU83", "admin"],
    ["user", "user123", "pengguna"],
    ["test", "123456", "pengguna"]
]

tipe_kamar = ["Standard", "Deluxe", "Suite"]

kamar_hotel = [
    ["101", "Standard", 300000, "Tersedia"],
    ["102", "Standard", 300000, "Terisi"],
    ["103", "Deluxe", 500000, "Tersedia"],
    ["104", "Deluxe", 500000, "Terisi"],
    ["105", "Suite", 1000000, "Terisi"],
    ["106", "Suite", 1000000, "Tersedia"]
]

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

        role = ""
        for akun in users:
            if akun[0] == username and akun[1] == password:
                role = akun[2]
                break

        if role == "":
            print("Error: Username atau password salah!")
            input("Tekan Enter untuk kembali...")
            continue

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

                    ada = False
                    for kamar in kamar_hotel:
                        if kamar[0] == nomor:
                            ada = True
                            break

                    if nomor == "":
                        print("Error: Nomor kamar tidak boleh kosong!")
                    elif ada:
                        print("Error: Nomor kamar sudah ada!")
                    else:
                        print("Tipe Kamar:")
                        for i in range(len(tipe_kamar)):
                            print(f"{i + 1}. {tipe_kamar[i]}")
                        pilih_tipe = input("Pilih tipe (1-3) : ").strip()
                        harga = input("Harga Kamar : ")
                        if pilih_tipe not in ["1", "2", "3"]:
                            print("Error: Pilihan tipe tidak valid!")
                        elif not harga.isdigit():
                            print("Error: Harga harus berupa angka!")
                        else:
                            print("Status: 1. Tersedia  2. Terisi")
                            st = input("Pilih status (1/2): ")
                            if st == "1":
                                kamar_hotel.append([nomor, tipe_kamar[int(pilih_tipe) - 1], int(harga), "Tersedia"])
                                print("Kamar berhasil ditambahkan!")
                            elif st == "2":
                                kamar_hotel.append([nomor, tipe_kamar[int(pilih_tipe) - 1], int(harga), "Terisi"])
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
                        for kamar in kamar_hotel:
                            print(f"{no:<4} | {kamar[0]:<10} | {kamar[1]:<12} | {kamar[2]:<10} | {kamar[3]:<10}")
                            no += 1
                        print("-" * 55)
                    input("Tekan Enter untuk melanjutkan...")

                elif menu == "3":
                    os.system(clear)
                    print("=== UBAH KAMAR ===")
                    nomor = input("Nomor kamar yang diubah: ").strip()

                    idx = -1
                    for i in range(len(kamar_hotel)):
                        if kamar_hotel[i][0] == nomor:
                            idx = i
                            break

                    if idx == -1:
                        print("Error: Nomor kamar tidak ditemukan!")
                    else:
                        lama = kamar_hotel[idx]
                        print(f"Data lama: {lama[1]}, Harga: {lama[2]}, Status: {lama[3]}")
                        print("Kosongkan (Enter) jika tidak ingin mengubah.")
                        print("Tipe Kamar:")
                        for i in range(len(tipe_kamar)):
                            print(f"{i + 1}. {tipe_kamar[i]}")
                        pilih_tipe = input("Tipe Baru (1-3) : ").strip()
                        harga = input("Harga Baru : ").strip()
                        print("Status: 1. Tersedia  2. Terisi")
                        st = input("Status Baru (1/2) : ").strip()

                        if pilih_tipe != "" and pilih_tipe not in ["1", "2", "3"]:
                            print("Error: Pilihan tipe tidak valid!")
                        elif harga != "" and not harga.isdigit():
                            print("Error: Harga harus berupa angka!")
                        elif st != "" and st != "1" and st != "2":
                            print("Error: Pilihan status tidak valid!")
                        elif pilih_tipe == "" and harga == "" and st == "":
                            print("Tidak ada data yang diubah.")
                        else:
                            if pilih_tipe != "":
                                kamar_hotel[idx][1] = tipe_kamar[int(pilih_tipe) - 1]
                            if harga != "":
                                kamar_hotel[idx][2] = int(harga)
                            if st == "1":
                                kamar_hotel[idx][3] = "Tersedia"
                            if st == "2":
                                kamar_hotel[idx][3] = "Terisi"
                            print("Kamar berhasil diperbarui!")
                    input("Tekan Enter untuk melanjutkan...")

                elif menu == "4":
                    os.system(clear)
                    print("=== HAPUS KAMAR ===")
                    nomor = input("Nomor kamar yang dihapus: ").strip()

                    idx = -1
                    for i in range(len(kamar_hotel)):
                        if kamar_hotel[i][0] == nomor:
                            idx = i
                            break

                    if idx == -1:
                        print("Error: Nomor kamar tidak ditemukan!")
                    else:
                        kamar_hotel.pop(idx)
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
                    for kamar in kamar_hotel:
                        if kamar[3] == "Tersedia":
                            print(f"{no:<4} | {kamar[0]:<10} | {kamar[1]:<12} | {kamar[2]:<10} | {kamar[3]:<10}")
                            no += 1
                    print("-" * 55)
                    if no == 1:
                        print("Saat ini tidak ada kamar yang tersedia.")
                    else:
                        nomor = input("Nomor kamar yang dipesan: ").strip()

                        idx = -1
                        for i in range(len(kamar_hotel)):
                            if kamar_hotel[i][0] == nomor:
                                idx = i
                                break

                        if idx == -1:
                            print("Error: Nomor kamar tidak ditemukan!")
                        elif kamar_hotel[idx][3] == "Terisi":
                            print("Error: Kamar sedang terisi!")
                        else:
                            kamar_hotel[idx][3] = "Terisi"
                            print(f"Kamar {nomor} ({kamar_hotel[idx][1]}) berhasil dipesan!")
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

        terpakai = False
        for akun in users:
            if akun[0] == username:
                terpakai = True
                break

        if username == "":
            print("Error: Username tidak boleh kosong!")
        elif terpakai:
            print("Error: Username sudah digunakan!")
        else:
            password = input("Password Baru : ")
            if password.strip() == "":
                print("Error: Password tidak boleh kosong!")
            else:
                users.append([username, password, "pengguna"])
                print("Registrasi berhasil! Silakan login.")
        input("Tekan Enter untuk kembali ke menu utama...")

    elif pilihan == "3":
        os.system(clear)
        print("Kula Diamond: Bye-bye! {-_-} play this: https://youtu.be/CNjqpg-G1xE?si=kP-hEZbBwV7O2qmL")
        break

    else:
        print("Error: Pilihan menu tidak valid!")
        input("Tekan Enter untuk mencoba lagi...")