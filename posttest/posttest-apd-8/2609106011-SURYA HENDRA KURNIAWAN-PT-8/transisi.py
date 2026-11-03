import os
from colorama import just_fix_windows_console, Fore, Style

just_fix_windows_console()

clear = 'cls' if os.name == 'nt' else 'clear'

def jeda(pesan="Tekan Enter untuk melanjutkan..."):
    input(pesan)

def cetak_error(pesan):
    print(Fore.RED + pesan + Style.RESET_ALL)

def cetak_sukses(pesan):
    print(Fore.GREEN + pesan + Style.RESET_ALL)