class Kalkulator:
    """contoh kelas kalkulator sederhana"""
    i = 12345
 
    def f(self):
        return 'Hello world!'

    @classmethod
    def tambah_angka(cls, angka1, angka2):
        return '{} + {} = {}'.format(angka1, angka2, angka1 + angka2)

    @staticmethod
    def kali_angka(angka1, angka2):
        return '{} x {} = {}'.format(angka1, angka2, angka1 * angka2)

print(Kalkulator.i)
Kalkulator.i = 1024
print(Kalkulator.i)

k = Kalkulator()  
print(Kalkulator.f(k))
print(k.f())
Kalkulator.tambah_angka(4,6)
print(Kalkulator.tambah_angka(5,5))
print(k.tambah_angka(2,2))

print(Kalkulator.kali_angka(5,5))
a = k.kali_angka(6,6)
print(a)

c = Kalkulator()
d = c.kali_angka(9,9)
print(d)