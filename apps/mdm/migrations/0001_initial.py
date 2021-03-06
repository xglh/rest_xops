# Generated by Django 2.0.3 on 2021-03-07 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MdmPretreatInput',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('car_brand', models.CharField(max_length=255, verbose_name='品牌')),
                ('car_model', models.CharField(max_length=255, verbose_name='车型')),
                ('vin', models.CharField(max_length=255, verbose_name='vin')),
                ('user_input', models.CharField(max_length=255, verbose_name='用户输入')),
            ],
            options={
                'verbose_name': '用户输入',
                'verbose_name_plural': '用户输入',
                'db_table': 'mdm_pretreat_input',
            },
        ),
        migrations.CreateModel(
            name='MdmPretreatTask',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('table_name', models.CharField(max_length=255, unique=True, verbose_name='询价单表')),
                ('total_num', models.IntegerField(default=-1, verbose_name='总数')),
                ('task_status', models.IntegerField(choices=[(-1, '未执行'), (0, '执行中'), (1, '执行完毕')], default=-1, verbose_name='任务状态')),
            ],
            options={
                'verbose_name': '数据预处理',
                'verbose_name_plural': '数据预处理',
                'db_table': 'mdm_pretreat_task',
            },
        ),
        migrations.AddField(
            model_name='mdmpretreatinput',
            name='pretreat_task_id',
            field=models.ForeignKey(db_column='pretreat_task_id', on_delete=django.db.models.deletion.CASCADE, to='mdm.MdmPretreatTask', verbose_name='预处理任务id'),
        ),
        migrations.AlterUniqueTogether(
            name='mdmpretreatinput',
            unique_together={('vin', 'user_input')},
        ),
        migrations.AlterIndexTogether(
            name='mdmpretreatinput',
            index_together={('vin', 'user_input')},
        ),
    ]
