class Mobil:
    def __init__(self, nama, warna, merk, tahun, harga, tipe):
        self.__nama = nama
        self.__warna = warna
        self.__merk = merk
        self.__tahun = tahun
        self.__harga = harga
        self.__tipe = tipe
    def get_nama(self):
        return self.__nama
    def get_warna(self):
        return self.__warna
    def get_merk(self):
        return self.__merk
    def get_tahun(self):
        return self.__tahun
    def get_harga(self):
        return self.__harga
    def get_tipe(self):
        return self.__tipe
    
    def set_nama(self, nama):
        self.__nama = nama
    def set_warna(self, warna):
        self.__warna = warna
    def set_merk(self, merk):
        self.__merk = merk
    def set_tahun(self, tahun):
        self.__tahun = tahun
    def set_harga(self, harga):
        self.__harga = harga
    def set_tipe(self, tipe):
        self.__tipe = tipe
    
