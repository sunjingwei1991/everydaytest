n = int(input('请输入学生数量:'))
data = {} #用来存储数据的字典变量
subjects = ('physics','maths','history')#所有科目
for i in range(0,n):
	name = input('请输入学生{}的姓名:'.format(i+1))#获得学生名称
	marks = []
	for x in subjects:
		marks.append(int(input('请输入{}成绩:'.format(x))))#获得学生每一科成绩
	data[name] =marks #将学生姓名和成绩对应存到data里面
for x ,y in data.items(): #x代表name，y代表markd，用sum进行求和 
	total = sum(y)
	print("{}的总得分是 {}".format(x,total))
	if total <120:
		print(x,"failed :( ")
	else:
		print(x,"passed :) ")
		