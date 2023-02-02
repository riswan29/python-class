# tampilkan nilai tertinggi
n_tinggi = input("Input masukkan nilai tertinggi : ").split()
# print(n_tinggi)

for nilai in range(0,len(n_tinggi)):
    n_tinggi[nilai] = int(n_tinggi[nilai])
print(n_tinggi)

nilai_tinggi = 0
for nilai in n_tinggi:
    if nilai > nilai_tinggi:
        nilai_tinggi = nilai
print(nilai_tinggi)

