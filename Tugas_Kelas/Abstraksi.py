from abc import ABC, abstractmethod

# Abstraksi dasar
class ProdukVape(ABC):
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    @abstractmethod
    def tampilkan_info(self):
        pass

# Subclass untuk Mod
class Mod(ProdukVape):
    def __init__(self, nama, harga, watt):
        super().__init__(nama, harga)
        self.watt = watt

    def tampilkan_info(self):
        print(f"MOD: {self.nama} | Harga: Rp{self.harga} | Watt: {self.watt}W")

# Subclass untuk Pod
class Pod(ProdukVape):
    def __init__(self, nama, harga, kapasitas_baterai):
        super().__init__(nama, harga)
        self.kapasitas_baterai = kapasitas_baterai

    def tampilkan_info(self):
        print(f"POD: {self.nama} | Harga: Rp{self.harga} | Baterai: {self.kapasitas_baterai}mAh")

# Subclass untuk Liquid
class Liquid(ProdukVape):
    def __init__(self, nama, harga, rasa):
        super().__init__(nama, harga)
        self.rasa = rasa

    def tampilkan_info(self):
        print(f"LIQUID: {self.nama} | Harga: Rp{self.harga} | Rasa: {self.rasa}")

# Simulasi penggunaan di toko
daftar_produk = [
    Mod("Hexohm V3 Vapezoo Polos", 2950000, 250),
    Pod("Oxva Xlim Pro Treasure Hunt One Piece", 310000, 1300),
    Liquid("Foom Ice Cream - Strawberry", 98000, " Ice Cream Strawberry")
]

for produk in daftar_produk:
    produk.tampilkan_info()
