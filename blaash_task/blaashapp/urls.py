from django.urls import path
from .views import PostListView, ProductCreateView, CollectionCreateView, TopViewedPostsView,postlist, TopViewedProductsView

urlpatterns = [
    path('',postlist,name='post_list'),
    path('posts/<int:tenant_id>/', PostListView.as_view(), name='post-list'),
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('collection/create/', CollectionCreateView.as_view(), name='collection-create'),
    path('top-viewed-posts/<int:tenant_id>/', TopViewedPostsView.as_view(), name='top-viewed-posts'),
    path('top-viewed-products/<int:tenant_id>/', TopViewedProductsView.as_view(), name='top-viewed-products'),
]