#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/30 10:00
# @Author  : dengchao
# @Site    : 
# @File    : svnconfig.py
# @Software: vscode
 
import time
import os
from svnconfig import setting, dist_lists
 
# 全局变量
 
# 用于存放每次运行update_all_dists期间的logs
logs = []
 
# 运行命令行需先进入SVN所在的路径
os.chdir(setting['svn'])
 
# 执行更新并记录更新成功或失败的logs


def update_all_dists():
    # 遍历所有需要更新的SVN floders，将更新的cmd拼出来
    for dist in dist_lists:
        cmd = 'TortoiseProc.exe /command:update /path:"' + dist + '"' + setting['closeOption']
        # print(cmd)
        
    # 记录下更新的时间
        log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        log = 'Execute ' + cmd + " --- Time " + log_time + '\n'
        logs.append(log)
 
    #   执行更新   （这里后面还需要加上对更新失败的处理）
        update_result = os.system(cmd)
 
    #  更新完毕，添加成功与否的log
        if update_result == 0:
            log = 'SUCCESS: update ' + dist + ' success' + '\n'
        else:
            log = 'FAIL: update ' + dist + ' fail' + '\n'
        logs.append(log)
 
    # 将log写入给定的log file
    with open(setting['logFile'], 'a') as f:
        logs.append("******************************************************** next update /n")
        for l in logs:
            f.write(l)
 
    # 将logs[]清空，为下次循环做准备
    logs.clear()
 
 
if __name__ == "__main__":
    # 每隔一段时间运行一次更新
    while True:
        update_all_dists()
        time.sleep(setting['interval'])
 