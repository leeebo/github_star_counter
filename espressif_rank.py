#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'guofei9987;libo'

import sys, json, os, requests, datetime

today = datetime.date.today()
print('Espressif Systems Github Star Rank ',end = "")
print(today)
github_id = "espressif"
url = 'https://api.github.com/users/{github_id}/repos?page={page_id}'
repo_list = []
page_id = 1
while True:
    r = requests.get(url.format(github_id=github_id, page_id=page_id))
    if r.status_code != 200:
        print('check your network connections')
        exit()

    repo_array = json.loads(r.content.decode('utf-8'))
    if len(repo_array) == 0:
        break

    for repo in repo_array:
        if not repo['fork']:
            repo_list.append([repo['name'], repo['stargazers_count'], repo['forks_count'], repo['description']])
    page_id += 1

# sort by number of stars
repo_list = sorted(repo_list, key=lambda x: x[1], reverse=True)

print('=' * 100)
print('\n'.join(['{: <30}★{: <10}\tfork {: <10}\t\t{} '.format(*repo) for repo in repo_list]))
print('=' * 100)
print('{: <30}★{: <10}\tfork {} '.format('total', sum([i[1] for i in repo_list]), sum([i[2] for i in repo_list])))
