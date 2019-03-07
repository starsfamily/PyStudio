# 身体质量指数（BMI，Body Mass Index）是国际上常用的衡量人体肥胖程度和是否健康的重要标准，
# 计算公式为：BMI=体重/身高的平方（国际单位kg/㎡）。中国的成年人BMI数值定义为：
# 过轻：低于18.5
#  正常：18.5-23.9
#  过重：24-27.9
#  肥胖：高于28
#  请输入体重和身高，输出相应的BMI值和体重肥胖程度判断结果（too thin、normal、overweight或fat)。
#  [输入样例]
#  60,1.6
#  [输出样例]
#  Your BMI is 23.4
#  normal
#  [提示]
#  程序中体重和身高的输入可用“weight, height = eval(input())”语句表示。
def main():
 w,h=eval(input('请输入你的身高和体重'))
 BMI(w,h)

def BMI(w,h):
 bmi = w / ( h **2)
 print(bmi)
 if bmi<18.5:
        print('too thin')
 elif bmi<23.9:
        print('normal')
 elif bmi < 27.9:
        print('overweight')
 elif bmi>28 :
        print('fat')

if __name__ == "__main__":
    main()
