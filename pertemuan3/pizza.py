# kecil = S
# sedang = M
# besar = L

# harga S = 50rb
# harga M = 70rb
# harga S = 100rb

# ukuran 

print("Halo selamat datang di pizza order ...")
print("Kami menyediakan beberapa size pizza yang tersedia mulai dari\nS=small\nM=medium\nL=Large")
ukuran = input("Silakan pilih ukuran ..? S, M atau L : ")

if ukuran == "S":
    print("Baik pesanan pizza anda dengan ukuran Small akan segera diproses , total harga yang perlu anda bayar = Rp.50.000")
elif ukuran == "M":
    print("Baik pesanan pizza anda dengan ukuran Small akan segera diproses , total harga yang perlu anda bayar = Rp.70.000")
else :
    print("Baik pesanan pizza anda dengan ukuran Small akan segera diproses , total harga yang perlu anda bayar = Rp.100.000")
