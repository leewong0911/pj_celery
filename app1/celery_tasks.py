# app1/task.py
from celery import shared_task
import time

@shared_task
def add(x, y):
    print("任务开始执行")
    time.sleep(5)
    print("任务执行完毕")
    return x + y