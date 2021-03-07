#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/5 21:20
# @Author : liuhui
# @desc :
from django.urls import path,include
from rest_framework import routers

from mdm.views.mdm_pretreat_task import MdmPretreatTaskViewSet

router = routers.SimpleRouter()
router.register(r'pretreat_tasks', MdmPretreatTaskViewSet, base_name="pretreat_tasks")


urlpatterns = [
    path(r'api/', include(router.urls))
]
