# rollercoaster tiket

tinggi = 130
umur = 18

if tinggi >= 130 :
    print("Silahkan masuk")
    if umur ==  12 : 
        print("Anak anak : Harga tiket = 10.000")
    elif umur >= 12 and umur <= 20: #range nya itu ada di umur 12 - 20 
        print("Remaja : Harga tiket = 20.000")
    elif umur > 20 and umur <= 29:
        print("Dewasa : harga tiket = 30.000")
    else :
        print("Orang Tua : Harga tiket : 35.000")
else :
    print("Anda belum sesuai dengan kriteria")