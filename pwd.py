x = 0
while True:
	password = input('請輸入密碼:')
	if password == 'a123456':
		print('登入成功')
		break
	else: 
		if x == 0:
			print('密碼錯誤 還有兩次機會')
		elif x == 1:
			print('密碼錯誤 還有一次機會')
		else:
			print('帳號鎖住')
			break
		x = x + 1

	