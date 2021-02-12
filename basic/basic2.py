# 変数の応用
animal = 'dog'
動物 = 'cat' # 日本語もできる…！
print(動物)

# 定数
age = 18
LEGAL_AGE = 20  # 定数はどこに書いてもいい？？可読性のこと考えると先頭に置いた方がいいかも

if age < LEGAL_AGE: 
    print('未成年')
else:
    print('成人')

# format文
print(f'age = {age}') # python 3.6
print(f'{age = }') # python 3.8