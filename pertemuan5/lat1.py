# tinggi = 170 180 190 160 200

tinggi_mhs = input("Input tinggi tiap mahasiswa : ").split(",")
# print(tinggi_mhs)

for mhs in range(0,len(tinggi_mhs)):
    tinggi_mhs[mhs] = int(tinggi_mhs[mhs])
# print(tinggi_mhs)

panjang = len(tinggi_mhs)
total = sum(tinggi_mhs)
rata_rata = total / panjang
print(round(rata_rata))

# nentuin panjang alt_len

nomor_mhs = 0
for mhs in tinggi_mhs:
    nomor_mhs = nomor_mhs + 1
print(nomor_mhs)