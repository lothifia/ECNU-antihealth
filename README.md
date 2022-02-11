# ECNU-antihealth

华东师范大学自动打卡

每天7:00至9:00内的随机时间打卡

## 如何使用

0. 需要Linux服务器
1. 执行 `cp config.py.example config.py`
2. 抓包一次，参考[woria的博客](https://www.woria.xyz/2021/11/02/ECNU%E6%89%93%E5%8D%A1/)，根据抓包结果填写 `config.py` (不是`.example`)
3. 执行 `./setup.sh`，激活crontab，每天00:00执行脚本，随机延迟一段时间后执行打卡。
4. 如果抓包得到的 `open_key` 过期（会有邮件提醒），只需重新抓包并修改 `config.py`，下次执行自动使用新配置

执行日志记录在 `anti-health.log` 中。

> 注：`./setup.sh`只能执行一次，若重复执行，可以有两种解决方案：
> 1. 执行 `crontab -r` 删除所有定时任务，然后再次执行 `./setup.sh`
> 2. 通过 `crontab -e` 手动修改定时任务，参考[crontab命令](https://www.runoob.com/linux/linux-comm-crontab.html)
