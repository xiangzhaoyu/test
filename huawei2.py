#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 下午5:11
# @Author  : zhaoyu
# @Site    : 
# @File    : huawei2.py
# @Software: PyCharm

import json

result_dict = {}
contents = []
results = []
with open('/Users/xiangzy/Desktop/huawei.log.1', 'r') as f:
    for line in f:
        if line is None or len(line) < 1:
            continue
        line = line.strip()
        if 'content:' in line:
            index = line.index('content:')
            content = line[index + len('content:'):]
            contents.append(content)
        if 'result:' in line:
            index = line.index('result:')
            result = line[index + len('result:'):]
            results.append(result)
            result_json = json.loads(result)
            audit = result_json.get('audit', [])

            current_content = contents[len(results) - 1]
            if len(audit) == 0:
                result_dict.setdefault(0, []).append({'content': current_content, 'result': result})
            for au in audit:
                result_dict.setdefault(au, []).append({'content': current_content, 'result': result})

print('huawei count:{}'.format(len(contents)))

for key, value in result_dict.items():
    print('current audit:{} \t count:{}'.format(key, len(value)))
    with open('{}.txt'.format(key), 'w') as f:
        for data in value:
            if data is None:
                continue
            content = data.get('content', '')
            result = data.get('result', '')
            f.write('content:{}\n'.format(content))
            f.write('result:{}\n'.format(result))


