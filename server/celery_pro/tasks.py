from __future__ import absolute_import

import logging
from celery.utils.log import get_task_logger
from celery_pro.celery import app

logger = logging.getLogger('admin_log')

@app.task
def test_add(num1, num2):
    return num1 + num2


@app.task(ignore_result=True)
def ignore_res(num1, num2):
    """ 结果不进行返回"""

    return num1 + num2


@app.task(bind=True)
def fail_restart(self, num1, num2):
    info = ('执行 任务 id:{0.id}, 参数：{0.args}, 关键字参数：{0.kwargs}'.
            format(self.request))
    logger.info(info)

    try:
        res = num1 / num2
    except ZeroDivisionError as erroe:
        # 任务失败会进行重试
        raise self.retry(exc=erroe, countdown=5, max_retries=3)
    return res
