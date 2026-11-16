# pj_celery/urls.py
from django.contrib import admin
from django.urls import path
from app1.views import submit_celery  # 导入测试视图
from app1 import views
urlpatterns = [
    path('celery_page/', views.celery_page),  # 访问页面的地址
    path('api/celery_submit_task/', views.submit_celery),  # 提交任务的 API
    path('api/celery_task_status/', views.check_task_status),  # 查询状态的 API
]

