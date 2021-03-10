# リスト宣言
list_a = [1, 2, 3, 4]
list_b = []
print(list_a)

print(list_a[0])
print(list_a[-2])# 後ろから2番目

# 多重リスト
list_a = [1, [1, 2, 'apple'], 3, 'banana']
print(list_a[1][2])
print(list_a)

# 書き換え
list_a[1][2] = 'lemon'
print(list_a)

# リストのスライス
list_a = [1, 2, 3, 4, 5]
list_b = list_a[:3]
print(list_b)
list_b = list_a[1:4]
print(list_b)
list_b = list_a[1:4:2] # 1つ飛ばしで取得
print(list_b)

# リストメソッド
list_a.append('apple')  # リストの末尾に追加する
print(list_a)

list_a.extend(['banana', 'melon']) # appendにすると多重リスト化されるが、extendするとlistとして結合される
print(list_a)

list_a.insert(1, 'grape')   # 追加する位置を指定する
print(list_a)

list_a.clear()
print(list_a)

list_a = [0,1,1,2,2,3,3,3,4]
print(list_a)
list_a.remove(3)    # 左から数えて一番初めの「3」を削除する
print(list_a)

value = list_a.pop() # 一番最後の値をpopする
print(list_a, value)
print(list_a.count(1)) # 1がリストの中に何個あるか
print(list_a.index(1)) # 1がリストの何番目にあるか

# copy
list_a = [0,1,1,2,2,3,3,3,4]
print(list_a)
list_b = list_a # 参照渡し！！
list_b[0] = 'AAAAA'
print(list_a) # list同志をただイコールで繋ぐだけでは、Aまで上書きされてしまう！

list_a = [0,1,1,2,2,3,3,3,4]
print(list_a)
list_b = list_a.copy() # リストの中身をコピーしている
list_b[0] = 'AAAAA'
print(list_a) # Aは上書きされない
print(list_b)

# ソート
list_a = ['banana', 'apple', 'lemon', 'grape']
print(list_a)
list_a.sort()   # 昇順に並べ替える
print(list_a)
list_a.reverse() # 降順に並べ替える
print(list_a)
