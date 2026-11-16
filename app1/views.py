from django.shortcuts import render
from django.http import JsonResponse
from celery.result import AsyncResult
from app1.celery_tasks import add
from pj_celery import celery_app


# 前端task页面
def celery_page(request):
    return render(request, 'celery_result.html')


# 点击提交按钮，返回task_id
def submit_celery(request):
    result = add.apply_async((10, 20))
    # print(result.id)
    # result.id 是任务的唯一标识，异步提交任务后可以快速返回
    return JsonResponse({"task_id": result.id})


# 3. 基于task_id获得任务的执行状态和结果
def check_task_status(request):
    # 从客户端请求中获得task_id
    task_id = request.GET.get("task_id")
    task_result = AsyncResult(task_id, app=celery_app)

    # 如果任务完成，将任务执行的状态和结果返回给前端ajax的api请求：then(resData => {})
    # 任务未完成之间，任务状态是PENDING；任务完成之后，任务状态是SUCCESS或FAILURE
    response_data = {
        "state": task_result.state,
    }

    if task_result.ready():
        if task_result.state == 'SUCCESS':
            response_data["result"] = task_result.get()
        elif task_result.state == 'FAILURE':
            response_data["error"] = str(task_result.info)

    return JsonResponse({"code": 200, "data": response_data})