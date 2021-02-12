# 文字列型
fruit = 'apple'
print(fruit)
print(type(fruit))
print(fruit * 10) # 文字列を10回表示　※ +にするとstr + numberでエラーになる
print(fruit[3]) # 文字列の3(4)番目の文字列を取得
print(fruit[-1]) # 文字列の末尾の文字列を取得

# 文字連結
new_fruit = fruit + ' banana'
print(new_fruit)

# 改行
fruits = """apple
banana
grape
"""
print(fruits)

# encode、decode => bytes[]
fruit = 'banana'
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))

# count関数(対象の文字列に何個含まれているか)
msg = 'ABCDEABC'
print(msg.count('ABCD')) # 1
print(msg.count('ABC')) # 2
print(msg.count('ABCDEF')) # 0

# startswith, endswith
print(msg.startswith('ABCD')) # 対象の文字列で始まるかどうか => True
print(msg.endswith('ABCD')) # False

# strip, rstrip, lstrip
msg = ' ABC '
print(msg)
print(msg.strip()) # 両端のスペースを削除して表示
print(msg.rstrip()) # 右端のスペースを削除して表示
print(msg.lstrip()) # 左端のスペースを削除して表示

msg = 'ABCDEFABC'
print(msg.strip('C')) # 右端がCなのでこれだけ削除 =>  ABCDEFAB
print(msg.strip('CBA')) # 両端からAがあるから削除、Bがあるから削除、… => DEF　orでつながってるイメージ
print(msg.lstrip('CBA')) # DEFABC
print(msg.rstrip('CBA')) # ABCDEF

# upper, lower, swapcase, replace, capitalize
msg = 'abcABC'
print(msg.upper()) # 全て大文字に
print(msg.lower()) # 全て小文字に
print(msg.swapcase()) # 大文字、小文字の入れ替え

msg = 'ABCDEABC'
print(msg.replace('ABC', 'FFF'))
print(msg.replace('ABC', 'FFF', 1)) # 左から数えて1こだけ置換

msg = 'hello world'
print(msg.capitalize()) # 先頭文字だけを大文字に
msg = 'hello WoRld. helLo world'
print(msg.capitalize())

# 文字列取りだし、format、islower, isupper
msg = 'hello, my name is taro'
print(msg[:6]) # 6文字めまで取り出す => hello,　※indexじゃない！！
print(msg[6:]) # 6文字目以降を取り出す =>  my name is taro
print(msg[1:6]) # indexの1〜6までを取り出す =>  ello,
print(msg[1:10:2]) # indexの1〜10までを1文字飛ばしで取り出す =>  el,m

msg = 'Taro'
print('hello {}'.format(msg))
msg = 'Jiro'
print(f'hello {msg}') # python 3.6以上
print(f'{msg=}') # python 3.8以上

print('apple'.islower())
print('appLe'.islower()) # 1文字でも大文字が入ってるとFalse
print('BANANa'.isupper())
print('BANANA'.isupper())

# find, index, rfind, rindex
msg = 'ABCDEABC'
print(msg.find('BC')) # はじめに出現する文字列の先頭indexを返す => 1
print(msg.rfind('ABC')) # 右から検索 => 5
print(msg.index('BC'))
print(msg.rindex('ABC'))

print(msg.find('ABCE')) # 見つからない時-1を返す => -1
print(msg.index('ABCE')) # 見つからない時ValueErrorを返す
