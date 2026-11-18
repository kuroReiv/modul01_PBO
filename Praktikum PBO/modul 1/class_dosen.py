class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def perkenalan(self):
        return f"Hai, saya {self.nama} dengan NIDN {self.nidn}"

# Instansiasi object harus berada di luar class (sejajar dengan posisi 'class Dosen')
dosen1 = Dosen("Rofiah", "676767")
dosen2 = Dosen("Fadiyah", "67676")

print(dosen1.perkenalan())
print(dosen2.perkenalan())