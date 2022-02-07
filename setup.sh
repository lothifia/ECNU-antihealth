#!/bin/bash
proj_path=$(realpath $0 | xargs dirname)

cmd="5 8 * * * /usr/bin/python ${proj_path}/main.py"
# cmd="* * * * * /usr/bin/python ${proj_path}/main.py"  # run every minute, for debug

# log, comment this line if you don't need it
cmd="${cmd} >> ${proj_path}/anti-health.log"

# This line of magic comes from: https://stackoverflow.com/a/9625233/17347885
(crontab -l 2>/dev/null; echo "${cmd}") | crontab -
