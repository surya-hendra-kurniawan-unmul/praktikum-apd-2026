import os
import pwinput
from data import users
from transisi import clear, jeda, cetak_error, cetak_sukses
from admin import menu_admin
from pengguna import menu_pengguna

def login():
    os.system(clear)
    print("=== LOGIN ===")
    username = input("Username : ")
    password = pwinput.pwinput("Password : ")

    role = cek_login(username, password)
    if role is None:
        jeda("Tekan Enter untuk kembali...")
    else:
        cetak_sukses(f"Login berhasil! Selamat datang, {username} ({role}).")
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
        cetak_error("Error: Username atau password salah!")
        return None
    except ValueError as e:
        cetak_error(f"Error: {e}")
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

        password = pwinput.pwinput("Password Baru : ")
        if password.strip() == "":
            raise ValueError("Password tidak boleh kosong!")
    except ValueError as e:
        cetak_error(f"Error: {e}")
    else:
        users[username] = {"password": password, "role": "pengguna"}
        cetak_sukses("Registrasi berhasil! Silakan login.")
    finally:
        jeda("Tekan Enter untuk kembali ke menu utama...")