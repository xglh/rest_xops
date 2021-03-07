import datetime
from django.utils import six
from rest_framework.response import Response
from rest_framework import serializers
from django.db import models
from rest_framework.viewsets import ModelViewSet


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BaseModelViewSet(ModelViewSet):
    pass


class BaseResponse(Response):
    def __init__(self, data=None, status=200, msg='成功',
                 template_name=None, headers=None,
                 exception=False, content_type=None):

        super(Response, self).__init__(None, status=status)

        if isinstance(data, serializers.Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)
        if status >= 400:
            msg = '失败'
        self.data = {
            'code': status,
            'message': msg,
            'detail': data
        }
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in six.iteritems(headers):
                self[name] = value
