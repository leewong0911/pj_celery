from celery import Celery
import time

# 初始化 Celery 实例，指定 Broker(消息代理) 和 Backend(结果存储)
app = Celery(broker='redis://127.0.0.1:6379/2', backend='redis://127.0.0.1:6379/3')


# 定义一个简单的加法任务
@app.task
def add(x, y):
    print("任务开始执行")
    # 模拟任务耗时
    time.sleep(5)
    print("任务执行完毕")
    return x + y

