# 确保 celery 的 app 在 Django 运行的时候被加载
from .celery import celery_app
__all__ = ('celery_app',)