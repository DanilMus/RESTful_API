from rest_framework import serializers
from products.models import product

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = product  
        fields = ('id','name','user')

class ProductDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default= serializers.CurrentUserDefault())

    class Meta:
        model = product  
        fields = '__all__'