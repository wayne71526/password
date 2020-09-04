# 密碼重試程式
# password = 'a123456'
# 讓使用者可以重複輸入密碼
# 最多輸入3次
# 如果正確就 印出 '登入成功'
# 如果不正確 就印出'密碼不正確! 還有_次機會!'
password = 'a123456'
i = 3
while True:
	pwd = input('請輸入密碼： ')
	if pwd == password:
		print('登入成功')
		break
	else:
		i = i - 1
		print('密碼不正確! 還有', i, '次機會!')
		if i == 0:
			break

