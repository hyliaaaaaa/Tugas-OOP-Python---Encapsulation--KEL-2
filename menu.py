from mahasiswa import Mahasiswa

# List untuk menyimpan data mahasiswa
daftar_mahasiswa = []


# Fitur untuk menambahkan data mahasiswa
def tambah_mahasiswa():
    nama = input("Nama: ")
    nim = input("NIM: ")
    daftar_mahasiswa.append(Mahasiswa(nama, nim))
    print("Data mahasiswa berhasil ditambahkan!")


# Fitur untuk menginput nilai mahasiswa berdasarkan NIM
def input_nilai():
    nim = input("NIM: ")
    ditemukan = False

    for mhs in daftar_mahasiswa:
        if mhs.get_nim() == nim:
            try:
                tugas = float(input("Tugas: "))
                uts = float(input("UTS: "))
                uas = float(input("UAS: "))

                mhs.set_nilai(tugas, uts, uas)
                print("Nilai berhasil disimpan!")

            except ValueError:
                print("Input harus berupa angka!")

            ditemukan = True
            break

    if not ditemukan:
        print("Mahasiswa tidak ditemukan!")


# Fitur untuk menampilkan seluruh data mahasiswa
def tampilkan():
    if not daftar_mahasiswa:
        print("Belum ada data mahasiswa!")
        return

    for mhs in daftar_mahasiswa:
        mhs.info()


# Fitur untuk mengupdate nilai mahasiswa berdasarkan jenis nilai
def update():
    nim = input("NIM: ")
    ditemukan = False

    for mhs in daftar_mahasiswa:
        if mhs.get_nim() == nim:
            jenis = input("Jenis (tugas/uts/uas): ").lower()

            try:
                nilai = float(input("Nilai: "))
                mhs.update_nilai(jenis, nilai)
                print("Nilai berhasil diupdate!")

            except ValueError:
                print("Input harus berupa angka!")

            ditemukan = True
            break

    if not ditemukan:
        print("Mahasiswa tidak ditemukan!")


# Bonus: Menampilkan mahasiswa dengan nilai tertinggi
def nilai_tertinggi():
    if not daftar_mahasiswa:
        print("Belum ada data mahasiswa!")
        return

    terbaik = max(daftar_mahasiswa, key=lambda m: m.get_nilai_akhir())

    print("\nMahasiswa dengan nilai tertinggi:")
    terbaik.info()


# Bonus: Mengurutkan mahasiswa berdasarkan nilai akhir
def urutkan_nilai():
    if not daftar_mahasiswa:
        print("Belum ada data mahasiswa!")
        return

    urut = sorted(
        daftar_mahasiswa,
        key=lambda m: m.get_nilai_akhir(),
        reverse=True
    )

    print("\nData mahasiswa berdasarkan nilai tertinggi:")
    for mhs in urut:
        mhs.info()