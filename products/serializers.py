from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
	image = serializers.ImageField(max_length=None, use_url=True, )
	class Meta:
		model = Product
		fields = ('id', 'name', 'mark', 'price', 'provider', 'image')