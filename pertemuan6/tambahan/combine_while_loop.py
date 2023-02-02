# kita juga dapat mengkombinasikan code loop menggunakan while dan loop dalam satu program
baris = int(input("Masukkan jumlah baris: "))

i = 1
while i <= baris:
    for j in range(1, i + 1):
        print("*", end="")
    print()
    i = i + 1

