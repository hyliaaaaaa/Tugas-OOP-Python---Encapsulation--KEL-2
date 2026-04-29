class Mahasiswa: 
    def __init__(self, nama, nim):
        self.__nama = nama
        self.__nim = nim
        self.__nilai_tugas = 0
        self.__nilai_uts = 0
        self.__nilai_uas = 0
        self.__nilai_akhir = 0

    def get_nama(self):
        return self.__nama
    
    def get_nim(self):
        return self.__nim
    
    def get_nilai_akhir(self):
        return self.__nilai_akhir

    #ini bagian untuk memvalidasi nilainya ya
    def __validasi(self, nilai):
        return 0 <= nilai <= 100

    #Menghitung nilai akhirnya
    def hitung_nilai_akhir(self):
        self.__nilai_akhir = (
            self.__nilai_tugas * 0.3 +   #nilai tugas nya diambil 30 % (kami menggunakan desimal (float))
            self.__nilai_uts * 0.3 +     #nilai uts nya diambil 30 %
            self.__nilai_uas * 0.4       #nilai uas nya diambil 40 %
        )
        
    def set_nilai(self, tugas, uts, uas):
        if not self.__validasi(tugas):
            print("Nilai tugas tidak valid!")
            return
        if not self.__validasi(uts):
            print("Nilai UTS tidak valid!")
            return
        if not self.__validasi(uas):
            print("Nilai UAS tidak valid!")
            return

        self.__nilai_tugas = tugas
        self.__nilai_uts = uts
        self.__nilai_uas = uas


        self.hitung_nilai_akhir()

    # keterangan nilainya
    def get_grade(self):
        if self.__nilai_akhir >= 85:
            return "A"
        elif self.__nilai_akhir >= 70:
            return "B"
        elif self.__nilai_akhir >= 60:
            return "C"
        else:
            return "D"

    #Lulus / tidak
    def is_lulus(self):
        return self.__nilai_akhir >= 60 

    #Update nilai
    def update_nilai(self, jenis, nilai):
        if not self.__validasi(nilai):
            print("Nilai tidak valid")
            return

        if jenis == "tugas":
            self.__nilai_tugas = nilai
        elif jenis == "uts":
            self.__nilai_uts = nilai
        elif jenis == "uas":
            self.__nilai_uas = nilai
        else:
            print("Jenis nilai tidak dikenali")
            return

        self.hitung_nilai_akhir()

    # Info mahasiswa
    def info(self):
        print(f"Nama  : {self.__nama}")
        print(f"NIM   : {self.__nim}")
        print(f"Nilai Akhir : {self.__nilai_akhir:.2f}")
        print(f"Grade : {self.get_grade()}")
        print(f"Lulus : {'Ya' if self.is_lulus() else 'Tidak'}")
        print("-" * 30)