class Kendaraan:
    # Class attribute (dibagi ke semua object)
    bahan_bakar = "Bensin"

    # Constructor untuk instance attributes (unik tiap object)
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"Kendaraan {self.merk}, Warna: {self.warna}, Tahun: {self.tahun}"

# Instansiasi object
kendaraan1 = Kendaraan("Toyota Avanza", "Hitam", 2022)
kendaraan2 = Kendaraan("Honda Civic", "Putih", 2023)

# Memanggil method
print(kendaraan1.info_kendaraan())
print(kendaraan2.info_kendaraan())

# Demonstrasi Akses Attribute
print(f"Merk Kendaraan 1 (Instance Attribute): {kendaraan1.merk}")
print(f"Bahan Bakar via Object (Class Attribute): {kendaraan1.bahan_bakar}")
print(f"Bahan Bakar via Class (Class Attribute): {Kendaraan.bahan_bakar}")