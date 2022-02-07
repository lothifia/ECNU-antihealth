# ECNU-antihealth

华东师范大学自动打卡

## 如何使用

0. 需要Linux服务器
1. 执行 `cp config.py.example config.py`
2. 抓包一次，参考[woria的博客](https://www.woria.xyz/2021/11/02/ECNU%E6%89%93%E5%8D%A1/)，根据抓包结果填写 `config.py` (不是`.example`)
3. 执行 `./setup.sh`，激活crontab，每天早上8:05执行打卡
4. 如果抓包得到的 `open_key` 过期（邮件提醒），重新抓包并修改 `config.py`，下次执行自动使用新配置

执行日志记录在 `anti-health.log` 中。
