#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/5 21:38
# @Author : liuhui
# @desc :
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from common.custom import CommonPagination, RbacPermission
from mdm.models import MdmPretreatTask
from mdm.serializers.mdm_pretreat_task import MdmPretreatTaskListSerializer, MdmPretreatTaskSerializer
from rest_xops.basic import BaseModelViewSet, BaseResponse


class MdmPretreatTaskViewSet(BaseModelViewSet):
    '''译码任务管理：增删改查'''
    perms_map = ({'*': 'admin'},
                 {'*': 'pretreat_task_all'},
                 {'get': 'pretreat_task_list'},
                 {'post': 'pretreat_task_create'},
                 {'put': 'pretreat_task_edit'},
                 {'delete': 'pretreat_task_delete'})
    queryset = MdmPretreatTask.objects.all()
    serializer_class = MdmPretreatTaskSerializer
    pagination_class = CommonPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('table_name',)
    ordering_fields = ('id',)
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (RbacPermission,)


class MdmPretreatTaskListView(APIView):
    '''
    译码任务管理列表删除
    '''
    perms_map = ({'*': 'admin'},
                 {'*': 'pretreat_task_all'},
                 {'delete': 'pretreat_task_delete'})
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (RbacPermission,)

    def delete(self, request):
        response = BaseResponse()
        task_ids = request.data
        if type(task_ids) != list:
            response.set_error_response(code=400, message='参数校验失败')
        else:
            MdmPretreatTask.objects.filter(id__in=task_ids).delete()
        return response
