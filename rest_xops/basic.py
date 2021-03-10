import datetime
from django.utils import six
from rest_framework.response import Response
from rest_framework import serializers, status
from django.db import models
from rest_framework.viewsets import ModelViewSet


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModelViewSet(ModelViewSet):

    def create(self, request, *args, **kwargs):
        user_id = request.user.id
        request.data["creator"] = user_id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        results = dict()
        results["code"] = status.HTTP_201_CREATED
        results["detail"] = serializer.data
        results["message"] = "创建成功"
        results["success"] = True
        return Response(results, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        results = dict()
        results["code"] = status.HTTP_200_OK
        results["detail"] = serializer.data
        results["message"] = "检索成功"
        results["success"] = True
        return Response(results, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        user_id = request.user.id
        request.data["editor"] = user_id
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        results = dict()
        results["code"] = status.HTTP_200_OK
        results["detail"] = serializer.data
        results["message"] = "更新成功"
        results["success"] = True
        return Response(results, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if hasattr(instance, 'is_delete'):
            instance.is_delete = 1
            instance.save()
        else:
            instance.delete()
        results = dict()
        results["code"] = status.HTTP_204_NO_CONTENT
        results["detail"] = ""
        results["message"] = "删除成功"
        results["success"] = True
        return Response(results)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        results = dict()
        results["code"] = status.HTTP_200_OK
        results["detail"] = serializer.data
        results["message"] = "查询成功"
        results["success"] = True
        return Response(results, status=status.HTTP_200_OK)


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

        success = True
        if status >= 400:
            msg = msg if msg else '失败'
            success = False
        self.data = {
            'code': status,
            'message': msg,
            'detail': data,
            'success': success
        }
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in six.iteritems(headers):
                self[name] = value

    def set_error_response(self, code=-100, message='error', detail={}):
        self.data = {
            'code': code,
            'message': message,
            'detail': detail,
            'success': False
        }

    def set_http_500_response(self, message='error', detail={}):
        self.set_error_response(500, message, detail)
