import time

print('按下回车开始计时，按下 Ctrl + C 停止计时。')
while True:
    try:
        input()  # 如果是 python 2.x 版本请使用 raw_input()
        starttime = time.time()
        print('开始')
        while True:
          print('计时: ', round(time.time() - starttime, 0), '秒', end="\r")
          time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('总共的时间为:', round(endtime - starttime, 2), 'secs')
        break