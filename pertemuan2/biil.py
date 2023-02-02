total = float(input("Total bill anda (Rp.): "))
tip = float(input("Berapa persen tip yang akan anda berikan 5, 10 atau 15% pilih salah satu : "))
orang = int(input("Ada berapa orang yang akan membayar bill : "))

tip = tip/100
total_tip = total * tip
final = (total + total_tip)/orang
print("Total bill anda Rp.",total + total_tip)
print(f"Dan untuk pembagiannya per-orangnya membayar sekitar Rp.{final}")
