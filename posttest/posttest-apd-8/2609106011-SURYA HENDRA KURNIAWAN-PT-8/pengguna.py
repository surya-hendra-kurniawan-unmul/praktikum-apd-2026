import os
from data import kamar_hotel
from transisi import clear, jeda, cetak_error, cetak_sukses
from tabel import tampilkan_tabel

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
            cetak_error("Error: Pilihan menu tidak valid!")
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
            cetak_error("Error: Nomor kamar tidak ditemukan!")
        except ValueError as e:
            cetak_error(f"Error: {e}")
        else:
            kamar["status"] = "Terisi"
            cetak_sukses(f"Kamar {nomor} ({kamar['tipe']}) berhasil dipesan!")
    jeda()