from menu import *

while True:
    print("\n=== MENU SISTEM NILAI MAHASISWA ===")
    print("1. Tambah Mahasiswa")
    print("2. Input Nilai")
    print("3. Tampilkan Data")
    print("4. Update Nilai")
    print("5. Nilai Tertinggi")
    print("6. Urutkan Nilai")
    print("0. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_mahasiswa()

    elif pilih == "2":
        input_nilai()

    elif pilih == "3":
        tampilkan()

    elif pilih == "4":
        update()

    elif pilih == "5":
        nilai_tertinggi()

    elif pilih == "6":
        urutkan_nilai()

    elif pilih == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak adaa!")