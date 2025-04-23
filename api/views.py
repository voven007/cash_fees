from djoser.views import UserViewSet
from rest_framework import viewsets

from collect.models import User

class CollectUserViewSet(UserViewSet):
    pass

class PaymentViewSet(viewsets.ModelViewSet):
    pass

class CollectViewSet(viewsets.ModelViewSet):
    pass
