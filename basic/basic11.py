# 辞書型メソッド
car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}
tmp_car = {'country': 'Japan', 'prefecture': 'Aichi', 'model': 'カローラ'}

# 追加更新（同一キーのものは上書きされる）
car.update(tmp_car)
print(car)

# updateの別パターン
car['city'] = 'Toyota-shi'
car['year'] = 2017
print(car)

# popitemは一番最後の値をタブル型で取り出す
value = car.popitem()
print(car)
print(value)

# popはvalueだけ返り、タプル型にはならない
value = car.pop('model')
print(car)
print(value)

car.clear()
print(car)

# delはオブジェクトそのものを削除する
del car
# print(car)  # not definedエラーになる
