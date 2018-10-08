#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/09/30 10:00
# @Author  : dengchao
# @Site    :
# @File    : gitconfig.py
# @Software: vscode

from git import Repo
# # 创建版本库对象
# repo = Repo(r'C:\GitRepository\leetcode')
# # 获取默认版本库 origin
# remote = repo.remote()
# # 从远程版本库拉取分支
# remote.pull()
# # 推送本地分支到远程版本库
# remote.push()


from gitconfig import dist_lists, commit_lists

for url in dist_lists:
  # print(url)
  repo = Repo(url)
  remote = repo.remote()
  remote.pull()
