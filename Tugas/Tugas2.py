# Randy Hendriyawan
# 122140171
# Praktikum PBO RF

# -*- coding: utf-8 -*-
import random  # Mengimpor modul random untuk menghasilkan angka acak

# Membuat kelas Robot yang merepresentasikan robot dalam permainan
class Robot:
    def __init__(self, name, hp, attack_power, attack_accuracy):
        self.name = name  # Nama robot
        self.hp = hp  # Jumlah kesehatan robot
        self.attack_power = attack_power  # Kekuatan serangan robot
        self.attack_accuracy = attack_accuracy  # Persentase akurasi serangan
        self.defense_mode = False  # Status apakah robot dalam mode bertahan

    # Metode untuk menyerang musuh
    def attack_enemy(self, enemy):
        # Jika angka acak dalam rentang 1-100 lebih kecil dari akurasi serangan, maka serangan berhasil
        if self.attack_accuracy >= random.randint(1, 100):
            enemy.hp -= self.attack_power  # Mengurangi HP musuh sesuai attack_power
            print(f"💥 {self.name} menyerang {enemy.name} dan menyebabkan {self.attack_power} damage!")
        else:
            print(f"❌ {self.name} gagal menyerang {enemy.name}!")  # Serangan meleset

    # Metode untuk bertahan dari serangan
    def defend(self):
        self.defense_mode = True  # Mengaktifkan mode pertahanan
        print(f"🛡️ {self.name} memilih untuk bertahan!")

    # Metode untuk menerima damage dari musuh
    def receive_damage(self, damage):
        if self.defense_mode:  
            damage //= 2  # Jika dalam mode pertahanan, damage yang diterima berkurang setengah
            self.defense_mode = False  # Mode pertahanan dinonaktifkan setelah menerima serangan
        self.hp -= damage  # Mengurangi HP sesuai damage yang diterima
        print(f"💔 {self.name} menerima {damage} damage! Kesehatan sekarang: {self.hp}")

    # Metode untuk mengecek apakah robot masih hidup
    def is_alive(self):
        return self.hp > 0  # Robot dianggap hidup jika HP-nya lebih dari 0

    # Metode untuk menampilkan informasi robot dalam bentuk string
    def __str__(self):
        return f"{self.name} [{self.hp} HP | {self.attack_power} ATK]"

# Kelas Game untuk mengatur jalannya permainan antara dua robot
class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1  # Robot pertama
        self.robot2 = robot2  # Robot kedua
        self.round = 1  # Menghitung jumlah ronde permainan

    # Metode untuk menjalankan permainan
    def play(self):
        while self.robot1.is_alive() and self.robot2.is_alive():  # Permainan berlangsung selama kedua robot masih hidup
            print(f"\n🌀 Round-{self.round} ==========================================================")
            print(self.robot1)  # Menampilkan status robot 1
            print(self.robot2)  # Menampilkan status robot 2

            # Giliran Robot 1
            action1 = self.get_action(self.robot1)  # Meminta input aksi untuk Robot 1
            self.perform_action(action1, self.robot1, self.robot2)  # Melakukan aksi berdasarkan input

            # Jika Robot 2 kalah setelah serangan Robot 1, permainan berakhir
            if not self.robot2.is_alive():
                print(f"🏆 {self.robot1.name} menang! janganlah kalian goyah dalam berpuasa!!!")
                break

            # Giliran Robot 2
            action2 = self.get_action(self.robot2)  # Meminta input aksi untuk Robot 2
            self.perform_action(action2, self.robot2, self.robot1)  # Melakukan aksi berdasarkan input

            # Jika Robot 1 kalah setelah serangan Robot 2, permainan berakhir
            if not self.robot1.is_alive():
                print(f"🏆 {self.robot2.name} menang! Katanya udah gede, kok mokel ngab?")
                break

            self.round += 1  # Meningkatkan jumlah ronde

    # Metode untuk meminta pemain memilih aksi
    def get_action(self, robot):
        print(f"\n🤖 {robot.name}, pilih aksi:")
        print("1. Attack 💥")  # Menyerang lawan
        print("2. Defense 🛡️")  # Bertahan dari serangan
        print("3. Giveup 🙅")  # Menyerah dan mengakhiri permainan
        action = input("Pilih aksi (1/2/3): ")  # Meminta input dari pemain
        return action

    # Metode untuk menjalankan aksi yang dipilih oleh pemain
    def perform_action(self, action, robot, enemy):
        if action == '1':  # Jika memilih menyerang
            robot.attack_enemy(enemy)  # Robot menyerang musuh
            enemy.receive_damage(robot.attack_power)  # Musuh menerima damage setelah serangan
        elif action == '2':  # Jika memilih bertahan
            robot.defend()
        elif action == '3':  # Jika memilih menyerah
            print(f"🙅 {robot.name} menyerah!")
            enemy.hp = 0  # HP musuh diatur menjadi 0 agar permainan berakhir
        else:
            print("⚠️ Aksi tidak valid! Silakan pilih 1, 2, atau 3.")  # Jika input tidak valid

# Contoh penggunaan kelas Robot dan Game
robot1 = Robot("Iman Puasa", 500, 375, 80)  # Membuat robot pertama dengan HP 500, serangan 10, akurasi 80%
robot2 = Robot("Mokel", 750, 8, 70)  # Membuat robot kedua dengan HP 750, serangan 8, akurasi 70%

# Memulai permainan dengan dua robot yang telah dibuat
game = Game(robot1, robot2)
game.play()
