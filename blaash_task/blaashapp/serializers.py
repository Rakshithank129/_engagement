from rest_framework import serializers
from .models import EngagementPost, EngagementPostContent, Product, EngagementPostProductMapping, Collection, EngagementPostCollection

class EngagementPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementPost
        fields = '_all_'

class EngagementPostContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementPostContent
        fields = '_all_'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '_all_'

class EngagementPostProductMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementPostProductMapping
        fields = '_all_'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '_all_'

class EngagementPostCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementPostCollection
        fields = '_all_'