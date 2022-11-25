from django.forms import TextInput, Textarea, DateTimeField, BooleanField,DateField
from rest_framework import serializers

from main.models import Juice, News


class JuiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juice
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'