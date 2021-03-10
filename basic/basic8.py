# int str変換
int_num = 12
str_num = str(int_num)
print(str_num)
print(type(str_num))
print('num = ' + str_num)

float_num = -20.5
print(f'num = {str(float_num)}')

# str => int, float
msg = '12'
int_msg = int(msg)
float_msg = float(msg)

print('value = {}, type = {}'.format(int_msg, type(int_msg)))
print('value = {}, type = {}'.format(float_msg, type(float_msg)))