#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime, timedelta

from airflow import DAG
from airflow.models import TaskInstance
from airflow.operators.dm_operator import DMOperator
from airflow.operators.oracle_operator import OracleOperator

TI = TaskInstance

default_args = {
    'owner': 'zhaoyu',
    'start_date': datetime.strptime("2020-06-17 00:00:00", "%Y-%m-%d %H:%M:%S"),
    'end_date': datetime.strptime("2020-06-18 00:00:00", "%Y-%m-%d %H:%M:%S"),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'depends_on_past': False,
    'pool': 'big_data',
    'queue': 'default',
}

dag = DAG(
    dag_id='test_dag_dm_oracle',  # dag_id
    catchup=True,
    default_args=default_args,  # 指定默认参数
    schedule_interval='5 * * * *',  # 执行周期，依次是分，时，天，月，年，此处表示每个整点执行
    concurrency=30,
    max_active_runs=3,
    description='',
)

sql = "select sysdate from dual"

dm_task = DMOperator(task_id='dm_task', sql=sql, dm_conn_id='x_dm', dag=dag)

oracle_task = OracleOperator(task_id='oracle_task', sql=sql, oracle_conn_id='x_oracle', dag=dag)