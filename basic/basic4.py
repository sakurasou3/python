# 数値型
value = 1
print(value) # 1
value = -2
print(value) # -2
value += 4
print(value) # 2
value *= 3
print(value) # 6
value /= 2
print(value) # 3.0
value //= 3
print(value) # 1.0
value %= 3
print(value) # 1.0

value = 3
value **= 3# 冪乗
print(value) # 27

# 浮動小数点
value = 175.5
print(value + 1)
print(type(value)) # 型を表示

# 論理シフト
value = 8 # => 1000
print(value >> 2) # 2ビット右にずらす=> 0010 => 2
print(value << 3) # 3ビット左にずらす=> 100|0000 => 64

# ビット演算
print(12 & 21) # 1100 & 10101 => 00100 => 4
print(12 | 21) # 1100 | 10101 => 11101 => 29
