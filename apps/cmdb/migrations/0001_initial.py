# Generated by Django 2.0.3 on 2021-03-04 13:49

import datetime
from django.db import migrations, models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='业务名称')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '业务',
                'verbose_name_plural': '业务',
            },
        ),
        migrations.CreateModel(
            name='ConnectionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('hostname', models.CharField(max_length=80, verbose_name='IP/域名')),
                ('auth_type', models.CharField(default='', max_length=30, verbose_name='认证类型')),
                ('port', models.IntegerField(blank=True, default=0, verbose_name='端口')),
                ('username', models.CharField(blank=True, default='', max_length=50, verbose_name='用户名/key')),
                ('password', models.CharField(blank=True, default='', max_length=80, verbose_name='密码')),
                ('is_public', models.BooleanField(default=False, verbose_name='是否公开')),
                ('desc', models.CharField(blank=True, max_length=150, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '连接信息',
                'verbose_name_plural': '连接信息',
            },
        ),
        migrations.CreateModel(
            name='DeviceFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('file_content', models.FileField(blank=True, null=True, upload_to='conf/asset_file/%Y/%m', verbose_name='资产文件')),
                ('upload_user', models.CharField(max_length=20, verbose_name='上传人')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='组名')),
                ('alias', models.CharField(default='', max_length=100, verbose_name='别名')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '设备组',
                'verbose_name_plural': '设备组',
            },
        ),
        migrations.CreateModel(
            name='DeviceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('status', models.CharField(blank=True, default='', max_length=10, verbose_name='状态')),
                ('sys_hostname', models.CharField(blank=True, default='', max_length=100, verbose_name='主机名')),
                ('mac_address', models.CharField(blank=True, default='', max_length=150, verbose_name='MAC地址')),
                ('sn_number', models.CharField(blank=True, default='', max_length=150, verbose_name='SN号码')),
                ('os_type', models.CharField(blank=True, default='', max_length=50, verbose_name='系统类型')),
                ('os_version', models.CharField(blank=True, default='', max_length=100, verbose_name='系统版本')),
                ('device_type', models.CharField(blank=True, default='', max_length=50, verbose_name='设备类型')),
                ('device_model', models.CharField(blank=True, default='', max_length=150, verbose_name='设备型号')),
                ('auth_type', models.CharField(default='', max_length=30, verbose_name='认证类型')),
                ('hostname', models.CharField(max_length=50, verbose_name='IP/域名')),
                ('network_type', models.IntegerField(blank=True, null=True, verbose_name='网络类型')),
                ('leader', models.CharField(blank=True, max_length=50, null=True, verbose_name='责任人')),
                ('buy_date', models.DateField(default=datetime.datetime.now, verbose_name='购买日期')),
                ('warranty_date', models.DateField(default=datetime.datetime.now, verbose_name='到保日期')),
                ('desc', models.TextField(blank=True, default='', verbose_name='备注信息')),
            ],
            options={
                'verbose_name': '设备信息',
                'verbose_name_plural': '设备信息',
            },
        ),
        migrations.CreateModel(
            name='DeviceScanInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('status', models.CharField(blank=True, default='', max_length=10, verbose_name='状态')),
                ('sys_hostname', models.CharField(blank=True, default='', max_length=100, verbose_name='主机名')),
                ('mac_address', models.CharField(blank=True, default='', max_length=150, verbose_name='MAC地址')),
                ('sn_number', models.CharField(blank=True, default='', max_length=150, verbose_name='SN号码')),
                ('os_type', models.CharField(blank=True, default='', max_length=50, verbose_name='系统类型')),
                ('os_version', models.CharField(blank=True, default='', max_length=100, verbose_name='系统版本')),
                ('device_type', models.CharField(blank=True, default='', max_length=50, verbose_name='设备类型')),
                ('device_model', models.CharField(blank=True, default='', max_length=150, verbose_name='设备型号')),
                ('hostname', models.CharField(max_length=80, verbose_name='IP/域名')),
                ('auth_type', models.CharField(default='', max_length=30, verbose_name='认证类型')),
                ('port', models.IntegerField(blank=True, default=0, verbose_name='端口')),
                ('username', models.CharField(blank=True, default='', max_length=50, verbose_name='用户名/key')),
                ('password', models.CharField(blank=True, default='', max_length=80, verbose_name='密码')),
                ('error_message', models.TextField(blank=True, default='', max_length=150, verbose_name='错误信息')),
            ],
            options={
                'verbose_name': '扫描信息',
                'verbose_name_plural': '扫描信息',
            },
        ),
        migrations.CreateModel(
            name='Dict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=80, verbose_name='键')),
                ('value', models.CharField(max_length=80, verbose_name='值')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '字典',
                'verbose_name_plural': '字典',
            },
        ),
        migrations.CreateModel(
            name='HistoricalDeviceInfo',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.CharField(blank=True, default='', max_length=10, verbose_name='状态')),
                ('sys_hostname', models.CharField(blank=True, default='', max_length=100, verbose_name='主机名')),
                ('mac_address', models.CharField(blank=True, default='', max_length=150, verbose_name='MAC地址')),
                ('sn_number', models.CharField(blank=True, default='', max_length=150, verbose_name='SN号码')),
                ('os_type', models.CharField(blank=True, default='', max_length=50, verbose_name='系统类型')),
                ('os_version', models.CharField(blank=True, default='', max_length=100, verbose_name='系统版本')),
                ('device_type', models.CharField(blank=True, default='', max_length=50, verbose_name='设备类型')),
                ('device_model', models.CharField(blank=True, default='', max_length=150, verbose_name='设备型号')),
                ('auth_type', models.CharField(default='', max_length=30, verbose_name='认证类型')),
                ('hostname', models.CharField(max_length=50, verbose_name='IP/域名')),
                ('network_type', models.IntegerField(blank=True, null=True, verbose_name='网络类型')),
                ('leader', models.CharField(blank=True, max_length=50, null=True, verbose_name='责任人')),
                ('buy_date', models.DateField(default=datetime.datetime.now, verbose_name='购买日期')),
                ('warranty_date', models.DateField(default=datetime.datetime.now, verbose_name='到保日期')),
                ('desc', models.TextField(blank=True, default='', verbose_name='备注信息')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical 设备信息',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='标签名')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
    ]
