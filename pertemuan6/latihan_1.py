""" Membuat Segita dari looping"""

# mengunakan for loop 
sisi = 10

angka = 1 
for i in range(sisi):
    print("*"*angka)
    angka+=1

# menggunakan while loop 
while True: 
    print("*"*angka)
    angka+=1
    if angka > sisi:
        break

#membuat segitiga tetapi hanya sisi yang  ganjil  saja 

while True: 
    if (angka%2):
         print("*"*angka)
         angka+=1
    else : 
         angka+=1     
         continue
    if angka > sisi:
        break