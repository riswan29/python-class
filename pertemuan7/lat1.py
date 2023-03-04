# 1 ember cat = 5m^2
# panjang = 5
# lebar = 6
# luas = 30 m^2
from math import ceil
pjg = int(input('Masukkan panjang rumah: '))
lbr = int(input('Masukkan lebar rumah : '))
cat = 5

def total_cat(panjang, lebar, jlh_cat):
    luas = panjang * lebar
    t_cat = ceil(luas / jlh_cat)
    print(t_cat)
total_cat(panjang=pjg, lebar=lbr, jlh_cat=cat)
