nama = input("Masukkan nama pembeli: ")
umur = int(input("Masukkan umur pembeli: "))

if umur < 13:
    print("Mohon maaf, anda belum cukup umur untuk menonton.")
else:
    jenis_tiket = input("Masukkan jenis tiket (Reguler/Premium/VIP): ")
    status_member = input("Status member (Ya/Tidak): ")

    if jenis_tiket == "Reguler":
        harga_tiket = 50000
    elif jenis_tiket == "Premium":
        harga_tiket = 75000
    elif jenis_tiket == "VIP":
        harga_tiket = 100000
    else:
        harga_tiket = 0

    if harga_tiket == 0:
        print("Peringatan: Jenis tiket tidak valid!")
    else:
        persen_diskon = 0.20 if status_member == "Ya" else 0
        biaya_admin = 0 if status_member == "Ya" else 2000

        nominal_diskon = int(harga_tiket * persen_diskon)
        total_bayar = (harga_tiket - nominal_diskon) + biaya_admin

        uang_bayar = int(input("Masukkan nominal uang bayar: Rp "))

        if uang_bayar < total_bayar:
            print("Peringatan: Uang bayar kurang dari total bayar!")
        else:
            kembalian = uang_bayar - total_bayar

            print("STRUK PEMBELIAN")
            print("Nama Pembeli  :", nama)
            print("Umur Pembeli  :", umur, "tahun")
            print("Jenis Tiket   :", jenis_tiket)
            print("Status Member :", status_member)
            print("Biaya Admin   : Rp", biaya_admin)
            print("Total Bayar   : Rp", total_bayar)
            print("Kembalian     : Rp", kembalian)