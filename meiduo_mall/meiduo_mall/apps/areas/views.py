<<<<<<< HEAD

=======
>>>>>>> origin/master
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from areas.models import Area
from areas.serializers import AreaSerializer, SubsSerializer


class AreaViewSet(CacheResponseMixin, ReadOnlyModelViewSet):
<<<<<<< HEAD

    # queryset = Area.objects.all()
    # 指定查询集
    def get_queryset(self):
        if self.action == 'list':
            return Area.objects.filter(parent=None)
        else:
            return Area.objects.all()

    # 指定序列化器
    # serializer_class =

=======
    """省市区三级联动列表和详情视图"""
    # 指定查询集
    def get_queryset(self):
        if self.action == 'list':
            return Area.objects.filter(parent=None) # 获取单一行政区
        else:
            return Area.objects.all() # 获取下级所有行政区

    # 获取指定序列化器
>>>>>>> origin/master
    def get_serializer_class(self):
        if self.action == 'list':
            return AreaSerializer
        else:
<<<<<<< HEAD
            return SubsSerializer
=======
            return SubsSerializer

>>>>>>> origin/master
