# menentukan nilai tertinggi pakai tuple
def max_tuple(numbers):
    mx_num = numbers[0]
    for num in numbers :
        if num > mx_num:
            mx_num = num
    return mx_num
my_tuple = (3, 8, 2, 10, 5)
result = max_tuple(my_tuple)
print("Nilai tertinggi dalam tuple adalah", result)
