from django.db import models

from rest_xops.basic import BaseModel

task_choice = [(-1, '未执行'), (0, '执行中'), (1, '执行完毕')]


class MdmPretreatTask(BaseModel):
    table_name = models.CharField(max_length=255, verbose_name='询价单表', unique=True)
    total_num = models.IntegerField(default=-1, verbose_name='总数')
    task_status = models.IntegerField(choices=task_choice, default=-1, verbose_name='任务状态')

    class Meta:
        db_table = 'mdm_pretreat_task'
        verbose_name = '数据预处理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.table_name


class MdmPretreatInput(BaseModel):
    pretreat_task_id = models.ForeignKey(MdmPretreatTask, on_delete=models.CASCADE, db_column='pretreat_task_id',
                                         to_field='id', verbose_name='预处理任务id')
    car_brand = models.CharField(max_length=255, verbose_name='品牌')
    car_model = models.CharField(max_length=255, verbose_name='车型')
    vin = models.CharField(max_length=255, verbose_name='vin')
    user_input = models.CharField(max_length=255, verbose_name='用户输入')

    class Meta:
        db_table = 'mdm_pretreat_input'
        verbose_name = '用户输入'
        verbose_name_plural = verbose_name

        index_together = ('vin', 'user_input')
        unique_together = ('vin', 'user_input')

    def __str__(self):
        return f'{self.vin}:{self.user_input}'
