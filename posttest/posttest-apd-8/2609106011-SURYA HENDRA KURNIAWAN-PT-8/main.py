import os
from transisi import clear, jeda, cetak_error
from auth import login, register

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

if __name__ == "__main__":
    while True:
        pilihan = menu_utama()

        if pilihan == "1":
            login()
        elif pilihan == "2":
            register()
        elif pilihan == "3":
            os.system(clear)
            print("Kula Diamond: Bye-bye! {-_-} play this: https://youtu.be/CNjqpg-G1xE?si=kP-hEZbBwV7O2qmL", flush=True)
            break
        else:
            cetak_error("Error: Pilihan menu tidak valid!")
            jeda("Tekan Enter untuk mencoba lagi...")