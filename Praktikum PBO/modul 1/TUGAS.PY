class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    def __init__(self, nama, nim, jurusan, ipk=0.0):
        # Instance attributes
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def perkenalan_diri(self):
        return f"Halo, nama saya {self.nama} dengan NIM {self.nim}, jurusan {self.jurusan} dari {Mahasiswa.universitas}. IPK saya saat ini {self.ipk}."

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        return f"IPK {self.nama} berhasil diperbarui menjadi {self.ipk}."

    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            predikat = "Cum Laude"
        elif self.ipk >= 3.0:
            predikat = "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            predikat = "Memuaskan"
        elif self.ipk >= 2.0:
            predikat = "Lulus"
        else:
            predikat = "Belum Memenuhi Syarat Kelulusan"
        
        return f"Predikat kelulusan {self.nama} (IPK: {self.ipk}): {predikat}"

# --- Instansiasi 3 Object Mahasiswa dengan Data Berbeda ---
mhs1 = Mahasiswa("Ahmad Fauzi", "202301001", "Teknik Informatika", 3.75)
mhs2 = Mahasiswa("Siti Aminah", "202301002", "Sistem Informasi", 3.20)
mhs3 = Mahasiswa("Budi Santoso", "202301003", "Teknik Informatika", 2.65)

# --- Demonstrasi Semua Method ---
print("=== DEMONSTRASI OBJECT 1 ===")
print(mhs1.perkenalan_diri())
print(mhs1.predikat_kelulusan())
print()

print("=== DEMONSTRASI OBJECT 2 ===")
print(mhs2.perkenalan_diri())
print(mhs2.update_ipk(3.60)) # Menguji update IPK
print(mhs2.predikat_kelulusan()) # Cek predikat setelah update
print()

print("=== DEMONSTRASI OBJECT 3 ===")
print(mhs3.perkenalan_diri())
print(mhs3.predikat_kelulusan())