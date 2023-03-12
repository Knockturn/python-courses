# https://www.youtube.com/watch?v=rfscVS0vtbw&t=9680s

# Exponent Function (power function) (2 ** 3 = 2 * 2 * 2) (2 to the power of 3)

print(2 ** 3) # 2 to the power of 3 (2 * 2 * 2)

def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result

print(f"Raise: {raise_to_power(2, 3)}") # 2 to the power of 3 (2 * 2 * 2)