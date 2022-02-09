# -*-coding:utf-8-*-
from record import HealthRecord
from send_gmail import send_gmail
import time
import datetime

if __name__ == '__main__':
    rc = 0
    print(datetime.datetime.now())  # log current time
    for t in range(3):
        rc, msg = HealthRecord()
        if rc == 0:
            print("Success!")
            break
        elif rc == -1 and msg == '今日已打卡':
            # send_gmail("打过了", "打过了)
            print("打过了！")
            break
        else:
            print(f"{rc=}, {msg=}")
            time.sleep(5)
    else:  # no break in for, HealthRecord failed
        send_gmail("打卡失败gggg！！！", "TOKEN坏掉了")
