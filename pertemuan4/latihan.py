row1 = ['ㅤ', 'ㅤ', 'ㅤ'] 
row2 = ['ㅤ', 'ㅤ', 'ㅤ'] 
row3 = ['ㅤ', 'ㅤ', 'ㅤ']

map = [row1, row2, row3]
positions = input('Dimana posisi yang kamu mau\t : ') #23

"""
tulis code mu dibawah ini 
"""
horizontal = int(positions[0])
vertikal = int(positions[1])


pilih_row = map[vertikal - 1]
pilih_row[horizontal - 1] = "x"

# print(horizontal)



print(f'{row1}\n{row2}\n{row3}')
