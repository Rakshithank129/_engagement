from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import EngagementPostSerializer, ProductSerializer, CollectionSerializer,        EngagementPostCollectionSerializer

def postlist(request):
    return render(request,'blaashapp/post_list.html')

class PostListView(generics.ListAPIView):
    serializer_class = EngagementPostSerializer

    def get_queryset(self):
        tenant_id = self.kwargs['tenant_id']
        return EngagementPost.objects.filter(tenant_id=tenant_id)

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CollectionCreateView(generics.CreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def create(self, request, *args, **kwargs):
        collection_data = request.data
        collection = Collection.objects.create(name=collection_data['name'])
        for post_id in collection_data['post_ids']:
            EngagementPostCollection.objects.create(
                post_id=post_id,
                collection=collection,
                duration_in_seconds=collection_data['duration_in_seconds']
            )
        return Response({'collection_id': collection.id})

class TopViewedPostsView(generics.ListAPIView):
    serializer_class = EngagementPostSerializer

    def get_queryset(self):
        tenant_id = self.kwargs['tenant_id']
        return EngagementPostCollection.objects.filter(post__tenant_id=tenant_id).order_by('-duration_in_seconds')[:5]

class TopViewedProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        tenant_id = self.kwargs['tenant_id']
        return Product.objects.filter(
            engagementpostproductmapping_post_tenant_id=tenant_id
        ).annotate(duration_watched=models.Sum('engagementpostcollection__duration_in_seconds')).order_by('-duration_watched')[:5]