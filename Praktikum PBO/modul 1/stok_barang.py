class ManajerInventori:
    def __init__(self):
        # Menggunakan dictionary untuk menyimpan inventori (Nama Barang: Stok)
        self.inventori = {}

    def tambah_barang(self, nama_barang, jumlah):
        if jumlah > 0:
            if nama_barang in self.inventori:
                self.inventori[nama_barang] += jumlah
            else:
                self.inventori[nama_barang] = jumlah
            return f"Berhasil menambahkan {jumlah} stok untuk '{nama_barang}'."
        return "Jumlah penambahan barang harus positif."

    def hapus_barang(self, nama_barang, jumlah):
        if nama_barang in self.inventori:
            if 0 < jumlah <= self.inventori[nama_barang]:
                self.inventori[nama_barang] -= jumlah
                # Hapus barang dari dictionary jika stok habis
                if self.inventori[nama_barang] == 0:
                    del self.inventori[nama_barang]
                return f"Berhasil mengurangi {jumlah} stok dari '{nama_barang}'."
            return "Jumlah pengurangan melebihi stok yang tersedia atau tidak valid."
        return f"Barang '{nama_barang}' tidak ditemukan di inventori."

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori saat ini kosong."
        
        hasil = "Daftar Inventori Barang:\n"
        for barang, stok in self.inventori.items():
            hasil += f"- {barang}: {stok} pcs\n"
        return hasil.strip()

# --- Testing / Demontrasi ---
toko = ManajerInventori()

# Penambahan stok barang
print(toko.tambah_barang("Buku Tulis", 50))
print(toko.tambah_barang("Pulpen", 30))

# Pengurangan stok barang
print(toko.hapus_barang("Buku Tulis", 10))

# Menampilkan sisa inventori
print(toko.lihat_inventori())