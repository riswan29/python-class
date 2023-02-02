# tinggi = 170 180 190 160 200

tinggi_mhs = input("Input tinggi tiap mahasiswa : ").split(",")
# print(tinggi_mhs)

for i in range(len(tinggi_mhs)):
    tinggi_mhs[i] = int(tinggi_mhs[i])
print(tinggi_mhs)

panjang = len(tinggi_mhs)
total = sum(tinggi_mhs)
rata_rata = total / panjang
rt=(round(rata_rata))
print(f"rata rata = {rt}")

# # nentuin panjang alt_len

nomor_mhs = 0
for mhs in tinggi_mhs:
    nomor_mhs = nomor_mhs + 1
print(f"nomor mhs = {nomor_mhs}")
