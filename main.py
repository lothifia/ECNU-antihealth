from login import Login
from send_gmail import send_gmail
import time

if __name__ == '__main__':
    rc = 0
    for t in range(10):
        rc, msg = Login('101xxxxxxxx', 'xxxxxxxxx')
        if rc == 0:
            print("Success!")
            break
        elif rc == -1 and msg == '今日已打卡':
            # send_gmail("打过了", "打过了)
            print("打过了！")
            break
        else:
            time.sleep(5)

    if rc != 0 and msg != '今日已打卡':
        send_gmail("打卡失败gggg！！！", "TOKEN坏掉了")