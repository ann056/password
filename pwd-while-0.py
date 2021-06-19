password = 'a12345'
x = 3
while x > 0:
	pwd = input('請輸入密碼：')
	x = x - 1
	if pwd == password:
		print('登入成功')
		break
	elif x >= 1:
		print('登入錯誤！還有', x, '次機會')
	else:
		print('帳號鎖住')
	