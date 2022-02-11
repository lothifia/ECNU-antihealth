# -*-coding:utf-8-*-
import random
import time
from datetime import timedelta as td

import config


def delay():
    begin, end = config.time_range['begin'], config.time_range['end']
    record_time = random.uniform(begin, end)
    print(f"choose random time {td(hours=record_time)} in [{td(hours=begin)}, {td(hours=end)}]")
    time.sleep(record_time * 3600)

if __name__ == '__main__':
    delay()
