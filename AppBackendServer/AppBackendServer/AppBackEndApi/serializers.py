from rest_framework import serializers
from .models import PromotionAd

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionAd
        fields = '__all__'