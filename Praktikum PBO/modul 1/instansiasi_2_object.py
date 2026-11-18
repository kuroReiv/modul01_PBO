class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} (NIDN: {self.nidn}) sedang mengajar mata kuliah {mata_kuliah}."

# Membuat 2 object dari class Dosen
dosen1 = Dosen("Dr. Ahmad Fauzi", "1101018501")
dosen2 = Dosen("Ir. Rina Wijaya, M.Kom", "1102029002")

# Memanggil method ajar_mata_kuliah()
print(dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))
print(dosen2.ajar_mata_kuliah("Struktur Data"))