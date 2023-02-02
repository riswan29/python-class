# nilai tertinggi 

# nilai_siswa = input("masukkan semua nilai mahasiswa : ").split(',')

# # # mengubaha tipe data ke integer
# for nilai in range(0, len(nilai_siswa)):
#     nilai_siswa[nilai] = int(nilai_siswa[nilai])
# print(nilai_siswa)
nilai_siswa = [80,90,87,60,50]
nilai_tertinggi = 0
for nilai in nilai_siswa:
    if nilai > nilai_tertinggi :
        nilai_tertinggi = nilai
print(nilai_tertinggi)