a = input("Выберите режим('Математика'/'Сравнение'):")
b = int(input('Выберите первое число:'))
c = int(input('Выберите второе число:'))
if a ==  'Математика':
 d =input("Выберите операцию('+', '-', '*', '/', '//', '**', '%' )")
 if d == '+':
    print(b + c)
 elif d == '-':
    print(b - c)
 elif d == '*':
    print(b * c)
 elif d == '/':
    print(b / c)
 elif d == '//':
    print(b // c)
 elif d == '**':
    print(b ** c)
 else:
    print(b % c)

if a == 'Сравнение':
    if b > c:
        print(b,'>', c)
    else:
        print(b, '<', c)