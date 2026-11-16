
import os
from celery import Celery

# 1. 告诉Django你正在使用哪些配置， 通过设置DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj_celery.settings')

# 2. 实例化 Celery， 'pj_celery'任意名字，通常为主项目文件名
celery_app = Celery('pj_celery')

# 3、让 celery_app从 django.conf:settings 这个对象中读取配置，并且只认前缀为 CELERY_ 的配置项。即读取'pj_celery.settings中以CELERY_为前缀的配置项
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# 4.自动发现celery任务
celery_app.autodiscover_tasks()



