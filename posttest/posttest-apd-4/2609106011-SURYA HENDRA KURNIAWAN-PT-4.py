username = "Hendra"
nim = "011"
pin = nim + nim

saldo = 5000000
kesempatan_login = 3

while kesempatan_login > 0:
    input_user = input("Masukkan username: ")
    input_pass = input("Masukkan password: ")

    if input_user == username and input_pass == nim:
        while True:
            print("--- MENU UTAMA ---")
            print("1. Transfer Uang")
            print("2. Logout")
            pilihan = input("Pilih menu (1/2): ")

            if pilihan == "1":
                lanjut_transfer = "y"
                while lanjut_transfer.lower() == "y":
                    print(f"Saldo saat ini: Rp{saldo:,}")
                    penerima = input("Masukkan username penerima: ")

                    while True:
                        nominal = int(input("Masukkan nominal transfer: "))
                        if nominal < 50000:
                            print("Nominal transfer minimal Rp 50.000")
                        elif nominal > 1000000:
                            print("Nominal transfer maksimal Rp 1.000.000")
                        elif nominal > saldo:
                            print("Saldo tidak mencukupi!")
                        else:
                            break

                    kesempatan_pin = 3
                    pin_valid = False
                    while kesempatan_pin > 0:
                        input_pin = input("Masukkan PIN: ")
                        if input_pin == pin:
                            pin_valid = True
                            break
                        else:
                            kesempatan_pin -= 1
                            print(
                                f"PIN salah! Sisa kesempatan: {kesempatan_pin}"
                            )

                    if pin_valid:
                        saldo -= nominal
                        print("BUKTI TRANSFER")
                        print(f"Pengirim : {username}")
                        print(f"Penerima : {penerima}")
                        print(f"Nominal  : Rp{nominal:,}")
                        print("===============================")
                        print("Transfer Berhasil!")

                        lanjut_transfer = input(
                            "Apakah pengguna ingin melakukan transfer lagi (y/n)? "
                        )
                    else:
                        print("Kesempatan PIN habis. Akun anda diblokir!")
                        break

                if not pin_valid:
                    break

            elif pilihan == "2":
                print("Logout berhasil. Terima kasih!")
                break
            else:
                print("Pilihan tidak valid!")

        break

    else:
        kesempatan_login -= 1
        if input_user != username and input_pass != nim:
            print("Username dan Password anda salah")
        elif input_user != username:
            print("Username anda salah")
        else:
            print("Password anda salah")

        print(f"Sisa kesempatan login: {kesempatan_login}")

if kesempatan_login == 0:
    print("Akun anda diblokir!")