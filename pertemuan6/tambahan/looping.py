# membuat looping segitiga dengan input function dan input bercabang(nested)
baris = int(input("Masukkan jumlah baris: "))

for i in range(1, baris + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
