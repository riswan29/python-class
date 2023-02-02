import random
nama = input("Masukkan nama petugas\t : ")

nama_split = nama.split(",")

# print(nama_split)

# latihan membuat random petugas nyapu ruangan 
panjang = len(nama_split)
# print(panjang)

acak_nama = random.randint(0, ( panjang- 1) )
# print(acak_nama)
nama_final = nama_split[acak_nama]

print(f"Petugas nyapu sekarang itu adalah.... {nama_final}")