password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
	i = i-1 # 進入此迴圈，就用掉一次機會
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break
	else:
		if i >0:
			print('密碼錯誤!還有', i, '次機會')
		else:
			print('密碼錯誤! 帳號已鎖上')
			break
			