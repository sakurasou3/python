# タプル
fruit = ('apple', 'banana', 'lemon')
print(fruit)
print(type(fruit))
print(fruit[1])

# タプルは値の更新ができない！
# fruit[1] = 'grape'

# 値の追加はできるけど、最後のコンマが大事らしい
fruit = fruit + ('grape',)
print(fruit)

# List => タプルへの変換
list = ['apple', 'banana']
fruit = tuple(list)
print(fruit)
print(fruit.count('apple'))
print(fruit.index('apple'))

# タプルをリストのキー名に指定する（よくやるらしい）
pos = (135, 35)
countries = {pos: 'Japan'}
print(countries)
print(countries.get((135, 35)))
