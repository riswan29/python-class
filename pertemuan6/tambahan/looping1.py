# membuat looping segitiga dengan input function dan while bercabang(nested)
baris = int(input("Masukkan jumlah baris: "))

i = 1
while i <= baris:
    j = 1
    while j <= i:
        print("*", end="")
        j = j + 1
    print()
    i = i + 1
