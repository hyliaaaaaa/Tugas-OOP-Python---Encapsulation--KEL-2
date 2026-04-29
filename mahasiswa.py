class Mahasiswa: 
    def __init__(self, nama, nim):
        self.__nama = nama
        self.__nim = nim
        self.__nilai_tugas = 0
        self.__nilai_uts = 0
        self.__nilai_uas = 0
        self.__nilai_akhir = 0

    #ini bagian untuk memvalidasi nilainya ya
    def __validasi(self, nilai):
        return 0 <= nilai <= 100

    #Menghitung nilai akhirnya
    def menghitung_nilai_akhir(self):
        self.__nilai_akhir = (
            self.__nilai_tugas * 0.3 +   #nilai tugas nya diambil 30 % (kami menggunakan desimal (float))
            self.__nilai_uts * 0.3 +     #nilai uts nya diambil 30 %
            self.__nilai_uas * 0.4       #nilai uas nya diambil 30 %
        )
        
    def set_nilai(self, tugas, uts, uas):
        if self.__validasi(tugas) and self.__validasi(uts) and self.__validasi(uas):
            self.__nilai_tugas = tugas
            self.__nilai_uts = uts
            self.__nilai_uas = uas
            self.menghitung_nilai_akhir()
        else:
            print("Masukkan nilai dengan angka anatar 0 - 100")
            # Grade
    def get_grade(self):
        if self.__nilai_akhir >= 85:
            return "A"
        elif self.__nilai_akhir >= 70:
            return "B"
        elif self.__nilai_akhir >= 60:
            return "C"
        else:
            return "D"

    # Lulus / tidak
    def is_lulus(self):
        return self.__nilai_akhir >= 60
