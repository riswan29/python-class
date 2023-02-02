"""
Rumus = berat badan/(tinggi * tinggi)

Kurus, Kekurangan berat badan berat         = < 17,0
Kurus, Kekurangan berat badan ringan        = 17,0 – 18,4
Normal                                      = 18,5 – 25,0
Gemuk, Kelebihan berat badan tingkat ringan = 25,1 – 27,0
Gemuk, Kelebihan berat badan tingkat berat  = > 27

"""

tinggi = float(input("Masukkan tinggi anda : "))
berat  = float(input("Masukkan berat badan anda : "))

bmi = berat / (tinggi * tinggi)

if bmi < 17.0 :
    print("Kurus, Kekurangan berat badan berat ")
elif bmi >= 17.0 and bmi <=18.4 :
    print("Kurus, Kekurangan berat badan ringan")
elif bmi >= 18.5 and bmi <=25.0 :
    print("Normal")
elif bmi >= 25.1 and bmi <=27.0 :
    print("Kurus, Kekurangan berat badan berat")
else:
    print("Anda obesitas")

