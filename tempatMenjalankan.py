from menu import *

while True:
    print("\n=== MENU ===")
    print("1. Tambah")
    print("2. Input Nilai")
    print("3. Tampilkan")
    print("4. Update")
    print("0. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        tambah_mahasiswa()
    elif pilih == "2":
        input_nilai()
    elif pilih == "3":
        tampilkan()
    elif pilih == "4":
        update()
    elif pilih == "0":
        break