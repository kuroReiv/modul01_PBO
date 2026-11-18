class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} (NIDN: {self.nidn}) sedang mengajar mata kuliah {mata_kuliah}."

# Instansiasi object
dosen1 = Dosen("Rofiah", "676767")
dosen2 = Dosen("Fadiyah", "67676")

# Pemanggilan method dengan cetak (print)
print(dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))
print(dosen2.ajar_mata_kuliah("Struktur Data"))