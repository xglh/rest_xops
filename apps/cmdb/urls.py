from django.urls import path,include
from cmdb.views import dict
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'dicts', dict.DictViewSet, base_name="dicts")


urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'api/dict/tree/', dict.DictTreeView.as_view(), name='dict_tree')
]
