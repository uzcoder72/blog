from django.urls import path
from .views import (
    CategoryView, GroupView, ProductView, ImageView, CommentView
)

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='category-list-create'),
    path('categories/<slug:slug>/', CategoryView.as_view(), name='category-detail-update-destroy-retrieve'),
    path('groups/', GroupView.as_view(), name='group-list-create'),
    path('groups/<slug:slug>/', GroupView.as_view(), name='group-detail-update-destroy-retrieve'),
    path('products/', ProductView.as_view(), name='product-list-create'),
    path('products/<slug:slug>/', ProductView.as_view(), name='product-detail-update-destroy-retrieve'),
    path('images/', ImageView.as_view(), name='image-list-create'),
    path('images/<slug:slug>/', ImageView.as_view(), name='image-detail-update-destroy-retrieve'),
    path('comments/', CommentView.as_view(), name='comment-list-create'),
    path('comments/<slug:slug>/', CommentView.as_view(), name='comment-detail-update-destroy-retrieve'),
]
