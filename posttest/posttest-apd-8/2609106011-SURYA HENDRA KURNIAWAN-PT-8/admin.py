import os
from data import tipe_kamar, status_kamar, kamar_hotel
from transisi import clear, jeda, cetak_error, cetak_sukses
from tabel import tampilkan_tabel

def input_harga():
    harga = input("Harga Kamar : ").strip()
    if not harga.isdigit():
        raise ValueError("Harga harus berupa angka!")
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
            cetak_error("Error: Pilihan menu tidak valid!")
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
        cetak_error(f"Error: {e}")
    else:
        kamar_hotel[nomor] = {
            "tipe": tipe_kamar[pilih_tipe],
            "harga": harga,
            "status": status_kamar[st]
        }
        cetak_sukses("Kamar berhasil ditambahkan!")
    finally:
        jeda()

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
        cetak_error("Error: Nomor kamar tidak ditemukan!")
    except ValueError as e:
        cetak_error(f"Error: {e}")
    else:
        if pilih_tipe != "":
            kamar_hotel[nomor]["tipe"] = tipe_kamar[pilih_tipe]
        if harga != "":
            kamar_hotel[nomor]["harga"] = int(harga)
        if st != "":
            kamar_hotel[nomor]["status"] = status_kamar[st]
        cetak_sukses("Kamar berhasil diperbarui!")
    finally:
        jeda()

def hapus_kamar():
    os.system(clear)
    print("=== HAPUS KAMAR ===")
    try:
        nomor = input("Nomor kamar yang dihapus: ").strip()
        del kamar_hotel[nomor]
    except KeyError:
        cetak_error("Error: Nomor kamar tidak ditemukan!")
    else:
        cetak_sukses(f"Kamar {nomor} berhasil dihapus!")
    finally:
        jeda()