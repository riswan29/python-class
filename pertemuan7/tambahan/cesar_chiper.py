# create alphabet a to z on list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v' , 'w' , 'x' , 'y' ,'z',' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v' , 'w' , 'x' , 'y' ,'z','']

# opsi encode atau decode
derection = input("Tulis 'encode' untuk enkripsi , tulis 'decode' untuk dekripsi:\n ")
# isi pesan yang akan di acak
text = input("Tulis pesan:\n")
# jumlah pergeseran
shift = int(input("Tulis berapa pergesaran yang akan dibuat\n"))

# def enkripsi(plain_text, jumlah_shift):
#     chiper_text = ""
#     for kata in plain_text:
#         posisi = alphabet.index(kata)
#         n_posisi = posisi + jumlah_shift
#         chiper_text += alphabet[n_posisi]
#     print(f"Text encode nya adalah {chiper_text}")

# def dekripsi(chiper_text, jumlah_shift):
#     plain_text = ""
#     for kata in chiper_text:
#         posisi = alphabet.index(kata)
#         n_posisi = posisi - jumlah_shift
#         plain_text += alphabet[n_posisi]
#     print(f"Text decode nya adalah {plain_text}")

# if derection == "encode":
#     enkripsi(plain_text=text, jumlah_shift=shift)
# elif dekripsi == "decode":
#     dekripsi(chiper_text=text, jumlah_shift=shift)


def caesar(text_awal , jumlah_shift, chiper_direction):
    akhir_text =""
    if chiper_direction == "decode":
        jumlah_shift *= -1
    for kata in text_awal:
        posisi = alphabet.index(kata)
        n_posisi = posisi + jumlah_shift
        akhir_text += alphabet[n_posisi]
    print(f"Text {derection} nya adalah {akhir_text}")

caesar(text_awal=text, jumlah_shift=shift, chiper_direction=derection)
