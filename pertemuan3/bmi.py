# kalkulator BMI

# input data 
# input()

tinggi = input("Masukkan tinggi anda : ")
berat = input("Masukkan berat anda : ")

# convert tipe data
n_tinggi = int(tinggi)
n_berat = int(berat)

bmi = n_berat/n_tinggi ** 2
print(bmi)

