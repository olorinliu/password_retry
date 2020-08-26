password = "a123456"
i = 3 #剩餘機會
while i > 0:
	password_key = input("請輸入密碼： ")
	if password_key == password:
		print("登入成功！") 
		break # 逃出迴圈
	else:
		i = i - 1
		print("密碼錯誤！ 還有", i, "次機會")
                					




