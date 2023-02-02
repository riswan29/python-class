# # prima
# # Bilangan prima adalah bilangan yang hanya bisa dibagi oleh angka 1 dan dirinya sendiri. Bilangan prima juga disebut sebagai bilangan asli. Contoh bilangan prima adalah 2, 3, 5, 7, 11, 13, 17, 19 dan seterusnya.

def prima(angka):
    # 3 = ini bilangan prima
    #  4 = ini bukan bilangan prima
    n_prima = True
    for i in range(2, angka):
        if angka % i == 0:
            n_prima = False
    if n_prima:
        print("Ini bilangan prima")
    else:
        print("Ini bukan bilangan prima")
n = int(input("masukkan angka : "))
prima(angka=n)
