from  rest_framework import serializers

from canteen_managemant_system.models import FoodItem


class CookSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'