with open(r'D:\temp\PyStudio\file.txt', 'a+') as f:
 f.writelines("asdfnsdfjo\n"
                  "asfdjald\n"
                  "sfjasd\n")
 text = f.readlines()#z这里不能使用f.read(),因后续使用text[i]为元组类型
for i in range(0, len(text)):
        text[i] = str(i+1)+text[i]
        print(text[i])
p = open()
p.seek(0)
p.writelines("It is the very beginning\n")
print(p)