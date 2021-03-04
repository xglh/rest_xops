# Generated by Django 2.0.3 on 2021-03-04 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaldeviceinfo',
            name='changed_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldeviceinfo',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dict',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child', to='cmdb.Dict'),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='businesses',
            field=models.ManyToManyField(blank=True, to='cmdb.Business', verbose_name='业务'),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='changed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='groups',
            field=models.ManyToManyField(blank=True, to='cmdb.DeviceGroup', verbose_name='设备组'),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='labels',
            field=models.ManyToManyField(blank=True, to='cmdb.Label', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child', to='cmdb.DeviceInfo'),
        ),
        migrations.AddField(
            model_name='devicefile',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmdb.DeviceInfo', verbose_name='设备'),
        ),
        migrations.AddField(
            model_name='connectioninfo',
            name='uid',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='关联用户'),
        ),
    ]
