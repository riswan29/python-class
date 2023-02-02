#input nama 

nama1 = input("Masukkan nama mu : ")
nama2 = input("Masukkan nama cruch mu : ")


combine = nama1 + nama2

#lowercase
cbn = combine


#true love

t = cbn.count("t")
r = cbn.count("r")
u = cbn.count("u")
e = cbn.count("e")

true = t + r + u + e

l = cbn.count("l")
o = cbn.count("o")
v = cbn.count("v")
e = cbn.count("e")

love = l + o + v + e

#ubah ke string
total = str(true) + str(love)

print(f'{total}%')
