#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 下午2:40
# @Author  : zhaoyu
# @Site    : 通用数据请求
# @File    : common_requests.py
# @Software: PyCharm


import requests
import json
import logging as logger


def get_request(url, params=None):
    """
    get 请求
    :param url: 请求地址
    :param params: get参数
    :return: 字典
    """
    logger.info('get 请求：{}'.format(url))
    resp = requests.get(url, params=params)
    if resp is not None and len(resp.text) > 300:
        logger.info('get 请求返回：{}'.format(resp.text[:300]))
    else:
        logger.info('get 请求返回：{}'.format(resp.text))
    result = json.loads(resp.content)
    return result


def post_request(url, request, request_obj):
    """
    post 请求
    :param url: 请求地址
    :param request: 请求对象
    :param request_obj: 请求对象类型
    :return:
    """
    logger.info('post 请求：{} {}'.format(url, request))
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(url, data=json.dumps(request, ensure_ascii=False).encode('utf-8'), headers=headers)
    if resp is not None and len(resp.text) > 300:
        logger.info('post 请求返回：{}'.format(resp.text[:300]))
    else:
        logger.info('post 请求返回：{}'.format(resp.text))
    result = json.loads(resp.content)
    return result
