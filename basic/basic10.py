car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}

print(car['brand'])
print(car.get('bran', 'Does not exist'))

print(car.keys())
print(car.values())
print(car.items())

for k, v in car.items():
    print('key = {} value = {}'.format(k, v))

if 'brand' in car:
    print(car['brand'])