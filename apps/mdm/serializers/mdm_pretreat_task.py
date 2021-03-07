#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/5 21:38
# @Author : liuhui
# @desc :

from rest_framework import serializers
from mdm.models import MdmPretreatTask


# list序列化
class MdmPretreatTaskListSerializer(serializers.ListSerializer):
    # 继承Meta对象
    class Meta:
        model = MdmPretreatTask
        fields = '__all__'
        # exclude = ('id',)


# 实例序列化
class MdmPretreatTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MdmPretreatTask
        fields = '__all__'
        list_serializer_class = MdmPretreatTaskListSerializer