#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午4:47
# @Author  : zhaoyu
# @Site    :
# @File    : anti_device_play_count.py
# @Software: PyCharm


from pykafka import KafkaClient
from pykafka.simpleconsumer import OwnedPartition, OffsetType
from pykafka.balancedconsumer import BalancedConsumer
from pykafka.simpleconsumer import SimpleConsumer

import os
import json

import logging
logging.basicConfig(format='[%(asctime)s] [%(filename)s]:[line:%(lineno)d] [%(levelname)s] %(message)s', level=logging.INFO)


kafka_hosts = "10.26.12.200:9092,10.26.5.151:9092,10.26.1.47:9092,10.26.8.25:9092,10.26.10.19:9092,10.26.5.19:9092,10.26.6.220:9092,10.26.4.106:9092,10.26.15.241:9092,10.26.1.185:9092,10.26.0.203:9092,10.26.10.39:9092,10.26.12.155:9092,10.26.12.218:9092,10.26.0.185:9092,10.26.10.15:9092,10.26.2.3:9092,10.26.1.227:9092,10.26.5.73:9092,10.26.7.222:9092,10.26.10.52:9092,10.26.10.240:9092,10.26.15.246:9092,10.26.1.190:9092,10.26.4.159:9092,10.26.15.75:9092,10.26.11.237:9092,10.26.4.122:9092,10.26.7.94:9092,10.26.0.202:9092,10.26.9.96:9092,10.26.1.108:9092"

"""
设备5分钟内播放的次数
"""

client = KafkaClient(kafka_hosts)
print(client.topics)

topic = client.topics['anti_device_play_count']
partitions = topic.partitions
print(partitions)

partitions_list = []
for k, val in partitions.items():
    partitions_list.append(val)

pykafka_group = "anti_device_play_count_test_1022"
params = {"auto_commit_enable": True, "auto_commit_interval_ms": 60000, "auto_offset_reset": OffsetType.LATEST}
balanced_consumer = topic.get_balanced_consumer(consumer_group=pykafka_group, managed=True, **params)

log_data_path = "./data"
cache_file = os.path.join(log_data_path, "device_play_1022.txt")
outf = open(cache_file, 'a+')
count = 0
for msg in balanced_consumer:
    try:
        val = msg.value
        if isinstance(val, bytes):
            val = val.decode()
        print(val, file=outf)
    except Exception as e:
        logging.info(str(e))
        logging.info(f"error {val}")
        continue