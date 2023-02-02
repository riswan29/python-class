"""soal 4. dalam sebuah kandang ada 1000 bebek setiap
   akhir bulan bebek tersebut serempak
   melahirkan satu bebek baru. namun sebelum melahirkan 20%
   dari bebek tersebut mati, buatlah suatu aplikasi untuk
   menghitung jumlah bebek setelah 10 bulan (latihan) """

# bebek = 1000
# lahiran = 0
# while lahiran <=10 :
#     bebek = bebek + (bebek * 0.1) - (bebek * 0.2)
#     lahiran+=1
#     print(f"Bulan ke {lahiran} jumlah bebek : {bebek}")

# def count_ducks(num_ducks, months, death_rate):
#     for i in range(months):
#         num_ducks = round(num_ducks - (num_ducks * death_rate) + num_ducks)
#         print(f"Bulan ke {i+1} jumlah bebek : {num_ducks}")
#     return int(num_ducks)

# count_ducks(1000, 10, 0.2)

# num_ducks = 1000
# months = 10
# death_rate = 0.2
# persen = 1 - death_rate


# for i in range(months):
#     yang_hidup = num_ducks * persen
#     total = yang_hidup * 2
#     print(f"bulan ke {i + 1} itu total nya {total}")


# for i in range(months):
#         num_duckss = round(num_ducks*death_rate)
#         num_duckss = num_duckss + num_duckss
#         print(f"Bulan ke {i+1} jumlah bebek : {num_duckss}")

import math
def count_ducks(num_ducks, months, death_rate):
    for i in range(months):
        death_ducks = num_ducks * death_rate
        num_ducks = math.ceil(num_ducks - death_ducks )* 2
        print(f"Bulan ke {i+1} jumlah bebek : {num_ducks}")
    return int(num_ducks)
count_ducks(1000, 10, 0.2)
