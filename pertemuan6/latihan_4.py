"""soal 3. Buatlah sebuah aplikasi untuk menampilkan 
   bilangan fibonaci batasan di input oleh user """

# fibonaci -> 0 1 1 2 3 5 8 13 21..

batasnilai = int(input("masukkan batas Nilai : "))
a = 0
b = 1
c = 0
for i in range(1, batasnilai+1):
    print(a)
    c = b+a
    a = b
    b = c
    
