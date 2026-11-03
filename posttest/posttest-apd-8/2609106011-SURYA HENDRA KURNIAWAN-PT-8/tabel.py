from prettytable import PrettyTable

def tampilkan_tabel(data_kamar):
    tabel = PrettyTable()
    tabel.field_names = ["No", "No Kamar", "Tipe", "Harga", "Status"]
    tabel.align["Tipe"] = "l"
    tabel.align["Status"] = "l"
    no = 1
    for nomor, data in data_kamar.items():
        tabel.add_row([no, nomor, data["tipe"], data["harga"], data["status"]])
        no += 1
    print(tabel)