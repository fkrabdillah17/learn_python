class Kalkulator:

    def __init__(self, nilai=0):
        self.nilai = nilai

    def tambahAngka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        if self.nilai > 9:
            print("Angka Kalkulator Sederhana Melebihi Batas Angka: {}".format(self.nilai))
        return self.nilai

class kaliKalkulator(Kalkulator):

    def kaliAngka(self, angka1, angka2):
        self.nilai = angka1 * angka2
        return self.nilai

    def tambahAngka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        return self.nilai

class KalkulatorTambah(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""
 
    def tambah_angka(self, angka1, angka2):
        if angka1 + angka2 <= 9:  # fitur ini sudah oke di kelas dasar, gunakan yang ada saja
            super().tambah_angka(angka1, angka2)  # panggil fungsi dari Kalkulator lalu isi nilai
        else:  # ini adalah fitur baru yang ingin diperbaiki dari keterbatasan kelas dasar
            self.nilai = angka1 + angka2
        return self.nilai

kk = kaliKalkulator()
a = kk.kaliAngka(2, 3)  # sesuai dengan definisi class memiliki fitur kali_angka
print(a)
 
b = kk.tambahAngka(5, 6)  # memiliki fitur tambah_angka karena mewarisi dari Kalkulator
print(b)

tk = KalkulatorTambah()
c = tk.tambah_angka(1,2)
print(c)