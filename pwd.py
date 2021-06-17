password = 'a12345'
x = 3
while True:
	pwd = input('請輸入密碼：')
	if pwd == password:
		print('登入成功')
	else:
		x = x - 1
		print('登入錯誤！ 還有', x, '次機會')
		if x == 0:
			break 