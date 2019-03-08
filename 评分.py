jscores = [10, 9, 1, 2, 4]
oneScore = 5
jscores.sort()
print(jscores)
jscores.pop()#去掉最后一个数字
jscores.pop(0)#去掉第一个数字，
print(jscores)

averScore = sum(jscores)/len(jscores)
print(averScore)

jscores.append(oneScore)
jscores.sort(reverse=1)
print(jscores)
averScore = sum(jscores)/len(jscores)
print(averScore)