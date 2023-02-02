# BMI calculate


# bmi = berat badan (kg) / (tinggi badan * tinggi badan(m))


berat = input("masukkan berat badan anda : ")
tinggi = input('masukkan tinggi anda : ')

n_berat = int(berat)
n_tinggi = float(tinggi)

bmi = n_berat / n_tinggi**2
print(bmi)