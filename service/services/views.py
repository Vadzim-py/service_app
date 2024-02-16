from django.db.models import Prefetch
from rest_framework import serializers
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from services.models import Subscription, Plan
from services.serializers import SubscriptionSerializer


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client',
                 queryset=Client.objects.all().select_related('user').only('company_name',
                                                                           'user__email'))
    )
    serializer_class = SubscriptionSerializer
