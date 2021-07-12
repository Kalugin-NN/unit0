a = list(range(1,10))#поле

def doska(a):#рисуем поле
	print (' ', '  0', '|', '1','|', '2')
	print ('-' * 15)
	for i in range(3):
		print(i, '|', a[0+i*3], '|', a[1+i*3], '|', a[2+i*3], '|')
		print ('-' * 15)

def vvod(x_o):#ввод значений
	valid = False
	while not valid:
		vopros = input('kuda postavim ' + x_o + '?')
		try:
			vopros = int(vopros)
		except:
			print('ne korektnii vvod')
			continue
		if 1<=vopros <=9:
			if (str(a[vopros-1]) not in 'XO'):
				a[vopros-1] = x_o
				valid = True
			else:
				print('ZANYATO!')
		else:
			print('vvod ot 0 do 9')
			
def pobeda(a):#проверка победы
	kombinacia = ((0, 1, 2),(3, 4 ,5),(6,7,8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6))
	for i in kombinacia:
		if a[i[0]] == a[i[1]] == a[i[2]]:
			return a[i[0]]
	return False

def igra(a):#игра
	count = 0
	victory = False
	while not victory:
		doska(a)
		if count % 2 ==0:
			vvod('X')
		else:
			vvod('O')
		count +=1
		if count >4:
			rezult = pobeda(a)
			if rezult:
				print(rezult, ' pobedil')
				victory = True
			break
		if count == 9:
			print('nichya')
			break
	doska(a)
						
igra(a)# запуск игры
