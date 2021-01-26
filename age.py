driving = input('請問你有沒有開過車？')
if driving != '有' and driving != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit
age = input('請輸入年齡')
if driving == '有':
	if int(age) < 18:
		print('你怎麼有開過車？')
	else:
		print('你通過測驗了')
elif driving == '沒有':
	if int(age) < 18:
		print('再過幾年就可以考駕照了')
	else:
		print('怎麼沒有考駕照？')