from mahasiswa import Mahasiswa

daftar_mahasiswa = []

#fitur tambahan
def tambah_mahasiswa():
    nama = input("Nama: ")
    nim = input("NIM: ")
    daftar_mahasiswa.append(Mahasiswa(nama, nim))

def input_nilai():
    nim = input("NIM: ")
    for mhs in daftar_mahasiswa:
        if mhs.get_nim() == nim:
            tugas = float(input("Tugas: "))
            uts = float(input("UTS: "))
            uas = float(input("UAS: "))
            mhs.set_nilai(tugas, uts, uas)

def tampilkan():
    for mhs in daftar_mahasiswa:
        mhs.info()

def update():
    nim = input("NIM: ")
    for mhs in daftar_mahasiswa:
        if mhs.get_nim() == nim:
            jenis = input("Jenis: ")
            nilai = float(input("Nilai: "))
            mhs.update_nilai(jenis, nilai)