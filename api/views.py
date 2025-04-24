from djoser.views import UserViewSet
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.serializers import UserSerializer

from collect.models import Collect, Event, Payment, User


class CollectUserViewSet(UserViewSet):
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination


class PaymentViewSet(viewsets.ModelViewSet):
    pass


class CollectViewSet(viewsets.ModelViewSet):
    pass
