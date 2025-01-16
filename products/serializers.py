from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)  # Display creator username

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        # Set the creator to the currently authenticated user
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name']