# Randy Hendriyawan
# 122140171
# PBO RF
# Fungsi untuk menghitung nilai akhir dan nilai huruf
def hitung_nilai_akhir(tugas, kuis, uts, uas):
    # Menghitung rata-rata dari nilai tugas, kuis, UTS, dan UAS
    nilai_akhir = (tugas + kuis + uts + uas) / 4
    
    # Menentukan nilai huruf berdasarkan rentang nilai akhir
    if nilai_akhir >= 85:
        nilai_huruf = 'A'
    elif nilai_akhir >= 70:
        nilai_huruf = 'B'
    elif nilai_akhir >= 60:
        nilai_huruf = 'C'
    elif nilai_akhir >= 50:
        nilai_huruf = 'D'
    else:
        nilai_huruf = 'E'
    
    # Mengembalikan nilai akhir dan nilai huruf
    return nilai_akhir, nilai_huruf

# Randy Hendriyawan
# 122140171

# Fungsi untuk login dengan maksimal 3 percobaan
def login():
    # Meminta input username dan password
    username = input("Masukkan NIM: ")
    password = input("Masukkan Tanggal Lahir (DDMMYYYY): ")
    attempts = 0  # Menghitung jumlah percobaan login
    
    while attempts < 3:
        # Jika username dan password benar
        if username == "1" and password == "1":  # Ini bisa diganti sesuai kebutuhan
            return True  # Login berhasil
        else:
            attempts += 1  # Menambah jumlah percobaan jika gagal
            print("Username atau password salah. Coba lagi.")
            username = input("Masukkan NIM: ")
            password = input("Masukkan Tanggal Lahir (DDMMYYYY): ")
    
    # Jika terlalu banyak percobaan gagal
    print("Terlalu banyak percobaan. Program keluar.")
    return False

# Randy Hendriyawan
# 122140171

# Program utama
def main():
    # Memeriksa apakah login berhasil
    if not login():
        return  # Keluar jika login gagal

    # Meminta jumlah mahasiswa yang akan dimasukkan
    N = int(input("Masukkan jumlah mahasiswa: "))
    data_mahasiswa = []  # List untuk menyimpan data mahasiswa

    # Loop untuk menginput data mahasiswa
    for i in range(N):
        print(f"\nMahasiswa {i + 1}")
        nim = input("NIM: ")
        nama = input("Nama: ")
        matakuliah = "Matematika"  # Contoh nama mata kuliah yang tetap
        
        # Memasukkan nilai dari masing-masing komponen
        tugas = float(input("Nilai Tugas: "))
        kuis = float(input("Nilai Kuis: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        
        # Menghitung nilai akhir dan nilai huruf
        nilai_akhir, nilai_huruf = hitung_nilai_akhir(tugas, kuis, uts, uas)
# Randy Hendriyawan
# 122140171        
        # Menyimpan data mahasiswa dalam bentuk dictionary
        data_mahasiswa.append({
            'NIM': nim,
            'Nama': nama,
            'Matakuliah': matakuliah,
            'Tugas': tugas,
            'Kuis': kuis,
            'UTS': uts,
            'UAS': uas,
            'Nilai Akhir': nilai_akhir,
            'Nilai Huruf': nilai_huruf
        })

    # Menampilkan data mahasiswa yang telah dimasukkan
    for i, mahasiswa in enumerate(data_mahasiswa):
        print(f"\nMahasiswa {i + 1}")
        print(f"NIM: {mahasiswa['NIM']}")
        print(f"Nama: {mahasiswa['Nama']}")
        print("-" * 80)
        print(f"{'No':<5} {'Matakuliah':<15} {'Tugas':<10} {'Kuis':<10} {'UTS':<10} {'UAS':<10} {'Nilai Akhir':<15} {'Nilai Huruf':<10}")
        print("-" * 80)
        print(f"{i + 1:<5} {mahasiswa['Matakuliah']:<15} {mahasiswa['Tugas']:<10} {mahasiswa['Kuis']:<10} {mahasiswa['UTS']:<10} {mahasiswa['UAS']:<10} {mahasiswa['Nilai Akhir']:<15.2f} {mahasiswa['Nilai Huruf']:<10}")
        print("-" * 80)

# Randy Hendriyawan
# 122140171

    # Menambahkan opsi untuk keluar atau melanjutkan
    while True:
        pilihan = input("\nApakah Anda ingin keluar dari program? (y/n): ").lower()
        if pilihan == 'y':
            print("Terima kasih! Program selesai.")
            break
        elif pilihan == 'n':
            print("Kembali ke menu utama...")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")

# Menjalankan program utama jika file ini dieksekusi langsung
if __name__ == "__main__":
    main()

# Randy Hendriyawan
# 122140171