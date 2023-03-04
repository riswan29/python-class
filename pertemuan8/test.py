import random
def main():
    score  = 0
    for i in range(3):
        print(f"Kesempatan ke-{i + 1}")
        kamu = int(input("Masukkan angka antar 1-10 : "))
        screet_nbr = random.randint(1,10)
        if kamu == screet_nbr :
            print("Kamu benar ")
            score = score + 10
        else :
            print("Kamu salah nilai dari komputer itu", screet_nbr)
        print("Skor kamu adalah", score)
main()
