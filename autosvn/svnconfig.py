#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/30 10:00
# @Author  : dengchao
# @Site    : 
# @File    : svnconfig.py
# @Software: vscode
 
setting={
    'svn':'D:/application/svn1.7/bin/',#svn的程序所在路径
    'interval':36000, # 更新时间，单位秒  这里设置6个小时更新一次
    'logFile': 'C:/GitRepository/auto/autosvn/logFile.txt', #　log文件放置位置
    'closeOption': ' /closeonend:2'
}
# /closeonend:0 不自动关闭对话框
# /closeonend:1 如果没发生错误则自动关闭对话框
# /closeonend:2 如果没发生错误和冲突则自动关闭对话框
# /closeonend:3如果没有错误、冲突和合并，会自动关闭
# /closeonend:4如果没有错误、冲突和合并，会自动关闭

 
dist_lists = [  # 需要更新的folder路径列表
 "D: /kitandtool/workspace/idea-3jba/nw",
 "D: /kitandtool/workspace/idea-3jba/ww",
 "D: /kitandtool/workspace/normal/文档",
 "D: /kitandtool/workspace/idea-blsp-nw",
 "D: /kitandtool/workspace/normal/plate"
]

# distforcommit = [  # 需要提交的的folder路径列表
#  # "D: /kitandtool/workspace/idea-3jba/nw",
#  "D: /kitandtool/workspace/idea-3jba/ww"
# ]
