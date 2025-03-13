#tes
# Randy Hendriyawan
# 122140171
# PBO RF

# Inisialisasi dictionary untuk menyimpan data mahasiswa
mahasiswa = {}  # Dictionary kosong untuk menyimpan data mahasiswa dengan NIM sebagai kunci

# Fungsi untuk menambah mahasiswa
def tambah_mahasiswa(nim, nama, nilai):
    mahasiswa[nim] = {'nama': nama, 'nilai': nilai}  # Menambahkan data mahasiswa ke dictionary
    print("Mahasiswa berhasil ditambahkan!")

# Fungsi untuk menampilkan semua mahasiswa
def tampilkan_mahasiswa():
    print("==== DATA MAHASISWA ====")
    print("NIM      | Nama  | Nilai")
    print("-------------------------")
    for nim, data in mahasiswa.items():  # Iterasi untuk menampilkan seluruh data mahasiswa
        print(f"{nim}  | {data['nama']}   | {data['nilai']}")

# Fungsi untuk mencari mahasiswa berdasarkan NIM
def cari_mahasiswa(nim):
    if nim in mahasiswa:  # Mengecek apakah NIM ada dalam dictionary
        data = mahasiswa[nim]
        print(f"Data Mahasiswa:\nNIM: {nim}\nNama: {data['nama']}\nNilai: {data['nilai']}")
    else:
        print("Mahasiswa tidak ditemukan.")

# Randy Hendriyawan
# 122140171

# Fungsi untuk mengedit data mahasiswa
def edit_mahasiswa(nim, nama_baru=None, nilai_baru=None):
    if nim in mahasiswa:
        if nama_baru:
            mahasiswa[nim]['nama'] = nama_baru  # Mengubah nama jika diberikan input dari user
        if nilai_baru:
            mahasiswa[nim]['nilai'] = nilai_baru  # Mengubah nilai jika diberikan input dari user
        print("Data berhasil diperbarui!")
    else:
        print("Mahasiswa tidak ditemukan.")

# Fungsi untuk menghapus data mahasiswa
def hapus_mahasiswa(nim):
    if nim in mahasiswa:
        del mahasiswa[nim]  # Menghapus mahasiswa berdasarkan NIM yang dibuat sebelumnya
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("Mahasiswa tidak ditemukan.")

# Fungsi untuk menyimpan data ke file
def simpan_ke_file(nama_file='mahasiswa.txt'):
    file = open(nama_file, 'w')  # Membuka file untuk menulis
    for nim, data in mahasiswa.items():
        file.write(f"{nim},{data['nama']},{data['nilai']}\n")  # Menulis setiap mahasiswa ke file
    file.close()
    print(f"Data mahasiswa telah disimpan dalam file '{nama_file}'")

# Randy Hendriyawan
# 122140171

# Fungsi untuk membaca data dari file
def baca_dari_file(nama_file='mahasiswa.txt'):
    global mahasiswa  # Menggunakan variabel global mahasiswa
    try:
        file = open(nama_file, 'r')  # Membuka file untuk membaca
        for line in file:
            nim, nama, nilai = line.strip().split(',')  # Memisahkan data berdasarkan koma
            mahasiswa[nim] = {'nama': nama, 'nilai': nilai}  # Menambahkan data ke dictionary
        file.close()
        print(f"Data mahasiswa telah dimuat dari file '{nama_file}'")
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
# Randy Hendriyawan
# 122140171

# Menu utama
def menu():
    while True:
        print("\n==== SISTEM PENGELOLAAN DATA MAHASISWA ====")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Mahasiswa Berdasarkan NIM")
        print("4. Edit Data Mahasiswa")
        print("5. Hapus Data Mahasiswa")
        print("6. Simpan ke File")
        print("7. Baca dari File")
        print("8. Keluar")
        pilihan = input("Pilihan: ")
# Randy Hendriyawan
# 122140171
        if pilihan == '1':
            nim = input("Masukkan NIM: ")
            nama = input("Masukkan Nama: ")
            nilai = input("Masukkan Nilai: ")
            tambah_mahasiswa(nim, nama, nilai)
        elif pilihan == '2':
            tampilkan_mahasiswa()
        elif pilihan == '3':
            nim = input("Masukkan NIM yang ingin dicari: ")
            cari_mahasiswa(nim)
        elif pilihan == '4':
            nim = input("Masukkan NIM yang ingin diedit: ")
            nama_baru = input("Nama baru (kosongkan jika tidak ingin mengubah): ")
            nilai_baru = input("Nilai baru (kosongkan jika tidak ingin mengubah): ")
            edit_mahasiswa(nim, nama_baru if nama_baru else None, nilai_baru if nilai_baru else None)
        elif pilihan == '5':
            nim = input("Masukkan NIM yang ingin dihapus: ")
            hapus_mahasiswa(nim)
        elif pilihan == '6':
            simpan_ke_file()
        elif pilihan == '7':
            baca_dari_file()
        elif pilihan == '8':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    menu()  # Memulai program dengan menampilkan menu utama
# Randy Hendriyawan
# 122140171
