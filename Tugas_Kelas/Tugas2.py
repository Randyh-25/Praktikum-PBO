class Mahasiswa:
    # Konstruktor untuk inisialisasi objek Mahasiswa dengan atribut nama dan daftar nilai mata kuliah
    def __init__(self, nama):
        self.nama = nama  # Menyimpan nama mahasiswa
        self.nilai_matakuliah = []  # List untuk menyimpan nilai dari berbagai mata kuliah

    # Metode untuk menambahkan nilai mata kuliah
    def tambah_nilai(self, matakuliah, uts, uas, tugas):
        nilai = {
            'matakuliah': matakuliah,  # Nama mata kuliah
            'UTS': uts,  # Nilai UTS
            'UAS': uas,  # Nilai UAS
            'Tugas': tugas  # Nilai tugas
        }
        self.nilai_matakuliah.append(nilai)  # Menambahkan nilai ke dalam daftar

    # Metode untuk mendapatkan daftar nilai mata kuliah
    def get_nilai(self):
        return self.nilai_matakuliah  # Mengembalikan daftar nilai

    # Metode untuk mengubah nilai berdasarkan indeks dalam daftar
    def set_nilai(self, index, uts=None, uas=None, tugas=None):
        if index < len(self.nilai_matakuliah):  # Mengecek apakah indeks valid
            if uts is not None:
                self.nilai_matakuliah[index]['UTS'] = uts  # Mengupdate nilai UTS jika diberikan
            if uas is not None:
                self.nilai_matakuliah[index]['UAS'] = uas  # Mengupdate nilai UAS jika diberikan
            if tugas is not None:
                self.nilai_matakuliah[index]['Tugas'] = tugas  # Mengupdate nilai tugas jika diberikan
        else:
            print("Index tidak valid.")  # Menampilkan pesan jika indeks tidak valid

    # Metode untuk mengonversi nilai angka ke huruf
    def konversi_nilai(self, nilai_angka):
        if nilai_angka >= 85:
            return 'A' # Mengembalikan nilai huruf berdasarkan rentang nilai
        elif nilai_angka >= 70:
            return 'B'
        elif nilai_angka >= 56:
            return 'C'
        elif nilai_angka >= 40:
            return 'D'
        else:
            return 'E'

    # Metode statis untuk menghitung IP berdasarkan daftar nilai mata kuliah
    @staticmethod # Dekorator untuk menandakan metode statis
    def hitung_ip(nilai_matakuliah):
        total_ip = 0  # Inisialisasi total IP
        for nilai in nilai_matakuliah:
            rata_rata = (nilai['UTS'] + nilai['UAS'] + nilai['Tugas']) / 3  # Menghitung rata-rata nilai
            total_ip += Mahasiswa.konversi_nilai_static(rata_rata)  # Menambahkan nilai IP berdasarkan rata-rata
        return total_ip / len(nilai_matakuliah) if nilai_matakuliah else 0  # Mengembalikan IP rata-rata

    # Metode statis untuk mengonversi nilai angka ke skala 4.0
    @staticmethod # Dekorator untuk menandakan metode statis
    def konversi_nilai_static(nilai_angka):
        if nilai_angka >= 85:
            return 4.0
        elif nilai_angka >= 70:
            return 3.0
        elif nilai_angka >= 56:
            return 2.0
        elif nilai_angka >= 40:
            return 1.0
        else:
            return 0.0

    # Metode untuk menampilkan informasi mahasiswa dan nilai mata kuliah
    def tampilkan_informasi(self):
        print(f"Nama Mahasiswa: {self.nama}")  # Menampilkan nama mahasiswa
        for nilai in self.nilai_matakuliah:
            rata_rata = (nilai['UTS'] + nilai['UAS'] + nilai['Tugas']) / 3  # Menghitung rata-rata nilai
            nilai_huruf = self.konversi_nilai(rata_rata)  # Mengonversi nilai ke huruf
            print(f"Matakuliah: {nilai['matakuliah']}, UTS: {nilai['UTS']}, UAS: {nilai['UAS']}, "
                  f"Tugas: {nilai['Tugas']}, Rata-rata: {rata_rata:.2f}, Nilai Huruf: {nilai_huruf}")
        ip = self.hitung_ip(self.nilai_matakuliah)  # Menghitung IP mahasiswa
        print(f"IP: {ip:.2f}")  # Menampilkan IP

# Contoh penggunaan kelas Mahasiswa
mahasiswa1 = Mahasiswa("Ujang")  # Membuat objek Mahasiswa dengan nama Ujang
mahasiswa1.tambah_nilai("PBO", 80, 90, 85)  # Menambahkan nilai untuk mata kuliah PBO
mahasiswa1.tambah_nilai("Basdat", 70, 75, 80)  # Menambahkan nilai untuk mata kuliah Basis Data
mahasiswa1.tampilkan_informasi()  # Menampilkan informasi mahasiswa
