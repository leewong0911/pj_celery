from task1 import add
import time
from celery.result import AsyncResult
from task1 import app

if __name__ == '__main__':
    print("1. 正在提交异步计算任务...")
    start_time = time.time()

    # 主程序异步执行任务 （apply_async）：
    # 主程序将任务（函数名及参数）序列化成消息发送给 Broker（Redis/0）
    # broker（Redis/0）暂存这些任务指令
    # 后台worker进程执行从Broker（Redis/0）获取的任务指令，并执行
    # 后台worker进程把执行状态和结果存到Backend（Redis / 1），
    result = add.apply_async((10, 20))  # 或 result = add.delay(10, 20)
    print(f"2. 任务已提交 | 任务ID: {result.id}")

    # 主程序等待任务完成：
    # 主程序拿着 task_id 去向 Backend（Redis/1）轮训查询
    # 当查到task执行状态为ready，主程序停止轮训，从Backend（Redis/1）拿到执行结果30。
    print("--- 主程序等待任务完成 ---")
    task_result = AsyncResult(result.id, app=app)
    while not task_result.ready():
        print(f"主程序等待任务完成 ... 当前时间: {time.strftime('%H:%M:%S')}, 任务状态: {task_result.state}")
        time.sleep(0.5)

    total_elapsed = time.time() - start_time
    print(f"3. 异步任务执行完成！计算结果: {task_result.get()}, 端到端总耗时: {total_elapsed:.4f}s")
