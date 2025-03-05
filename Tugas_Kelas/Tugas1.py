# Fungsi untuk menghitung nilai akhir dari komponen penilaian
def hitung_nilai_akhir(tugas, kuis, uts, uas):
    return (tugas + kuis + uts + uas) / 4  # Menghitung rata-rata nilai

# Fungsi untuk menentukan nilai huruf berdasarkan nilai akhir
def tentukan_nilai_huruf(nilai_akhir):
    if nilai_akhir >= 85:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 60:
        return 'C'
    elif nilai_akhir >= 50:
        return 'D'
    else:
        return 'E'

# Fungsi untuk login dengan maksimal 3 percobaan
def login():
    username = input("Masukkan Username(NIM): ")
    password = input("Masukkan Password(Tanggal Lahir): ")
    attempts = 0  # Menghitung jumlah percobaan login
    
    while attempts < 3:
        if username == "122140171" and password == "25082004":  # Ini bisa diganti sesuai kebutuhan
            return True  # Login berhasil
        else:
            attempts += 1  # Menambah jumlah percobaan jika gagal
            print("Username atau password salah. Coba lagi.")
            username = input("Masukkan NIM: ")
            password = input("Masukkan Tanggal Lahir (DDMMYYYY): ")
    
    print("Terlalu banyak percobaan. Program keluar.")
    return False

# Program utama
def main():
    if not login():
        return  # Keluar jika login gagal

    # Meminta jumlah mahasiswa yang akan dimasukkan
    N = int(input("Masukkan jumlah mahasiswa: "))
    data_mahasiswa = []  # List untuk menyimpan data mahasiswa

    matakuliah_list = ["PBO", "DRPL", "OS"]  # Daftar matakuliah

    # Loop untuk menginput data mahasiswa
    for i in range(N):
        print(f"\nMahasiswa {i + 1}")
        nim = input("NIM: ")
        nama = input("Nama: ")
        nilai_matakuliah = {}  # Dictionary untuk menyimpan nilai setiap matakuliah

        # Memasukkan nilai untuk setiap mata kuliah
        for matakuliah in matakuliah_list:
            print(f"\nMasukkan nilai untuk matakuliah {matakuliah}")
            tugas = float(input("Nilai Tugas: "))
            kuis = float(input("Nilai Kuis: "))
            uts = float(input("Nilai UTS: "))
            uas = float(input("Nilai UAS: "))
            
            nilai_akhir = hitung_nilai_akhir(tugas, kuis, uts, uas)
            nilai_huruf = tentukan_nilai_huruf(nilai_akhir)
            
            nilai_matakuliah[matakuliah] = {
                'Tugas': tugas,
                'Kuis': kuis,
                'UTS': uts,
                'UAS': uas,
                'Nilai Akhir': nilai_akhir,
                'Nilai Huruf': nilai_huruf
            }
        
        data_mahasiswa.append({
            'NIM': nim,
            'Nama': nama,
            'Nilai Matakuliah': nilai_matakuliah
        })

    # Menampilkan data mahasiswa yang telah dimasukkan
    for i, mahasiswa in enumerate(data_mahasiswa):
        print(f"\nMahasiswa {i + 1}")
        print(f"NIM: {mahasiswa['NIM']}")
        print(f"Nama: {mahasiswa['Nama']}")
        print("-" * 80)
        print(f"{'No':<5} {'Matakuliah':<15} {'Tugas':<10} {'Kuis':<10} {'UTS':<10} {'UAS':<10} {'Nilai Akhir':<15} {'Nilai Huruf':<10}")
        print("-" * 80)
        
        for j, (matakuliah, nilai) in enumerate(mahasiswa['Nilai Matakuliah'].items()):
            print(f"{j + 1:<5} {matakuliah:<15} {nilai['Tugas']:<10} {nilai['Kuis']:<10} {nilai['UTS']:<10} {nilai['UAS']:<10} {nilai['Nilai Akhir']:<15.2f} {nilai['Nilai Huruf']:<10}")
        print("-" * 80)

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