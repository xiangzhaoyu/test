#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 上午11:49
# @Author  : zhaoyu
# @Site    : 
# @File    : get_huawei.py
# @Software: PyCharm

import datetime
import re
import json

contents = {}
results = {}
with open('/Users/xiangzy/Desktop/api.log', 'r') as f:
    result_t = None
    is_result = False
    temp_result = []
    for line in f:
        # print(line)
        if 'huawei nlp content:' in line:
            time_str = line[line.index('[') + 1:line.index(']')]
            t = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S,%f")
            index = line.index('huawei nlp content:')
            content = line[index + len('huawei nlp content:'):]
            if t not in contents.keys() and t is not None:
                contents[t] = content
        if 'huawei nlp result:' in line:
            time_str = line[line.index('[') + 1:line.index(']')]
            result_t = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S,%f")
            is_result = True
            index = line.index('huawei nlp result:')
            content = line[index + len('huawei nlp result:')]
            temp_result.append(content)
            continue
        if is_result and line != '\n':
            temp_result.append(line)
        if line == '\n':
            is_result = False
            if result_t not in results.keys() and result_t is not None:
                results[result_t] = temp_result
            temp_result = []
            result_t = None

print('content count:{}'.format(len(contents)))
print('results count:{}'.format(len(results)))

sorted(contents)
content_keys = list(contents.keys())
print('min:{}'.format(content_keys[0]))
print('max:{}'.format(content_keys[-1]))

# with open('/Users/xiangzy/Desktop/huawei.api', 'a+') as f:
#     content_length = len(contents)
#     result_length = len(results)
#     # length = min(content_length, result_length)
#     sorted(contents)
#     sorted(results)
#     result_keys = list(results.keys())
#     for i in range(content_length):
#         key = list(contents.keys())[i]
#         f.write('huawei nlp content:{}'.format(contents[key]))
#         result = None
#         for rk in result_keys:
#             if key > rk:
#                 break
#             # 结果时间在内容请求时间之后，且不超过2秒钟，否则认为无效
#             if key < rk and (rk-key).seconds < 3.0:
#                 result = results[rk]
#                 result_keys.remove(rk)
#                 break
#         if result is None:
#             f.write('huawei nlp result:{}'.format('超时！\n'))
#         else:
#             for j in range(len(result)):
#                 if j == 0:
#                     f.write('huawei nlp result:{}'.format(result[j]))
#                     continue
#                 f.write(result[j])

p = re.compile('\s+')
with open('/Users/xiangzy/Desktop/hw.api', 'a+') as f:
    for key, value in results.items():
        try:
            result = ''
            for v in value:
                result = result + v
            result = re.sub(p, '', result)
            result_json = json.loads(result)
            result_str = json.dumps(result_json, ensure_ascii=False)
            f.write(result_str + '\n')
        except Exception as e:
            print('have exception:{}'.format(str(repr(e))))

print('finished convert')
