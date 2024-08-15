from django.urls import path
from app.views import CategoryView, GroupView, ProductView, CommentView
from django.urls import path
from app.views import RegisterView, CustomTokenObtainPairView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='category-list-create'),
    path('categories/<slug:slug>/', CategoryView.as_view(), name='category-detail-update-destroy-retrieve'),
    path('groups/', GroupView.as_view(), name='group-list-create'),
    path('groups/<slug:slug>/', GroupView.as_view(), name='group-detail-update-destroy-retrieve'),
    path('products/', ProductView.as_view(), name='product-list-create'),
    path('products/<slug:slug>/', ProductView.as_view(), name='product-detail-update-destroy-retrieve'),
    path('comments/', CommentView.as_view(), name='comment-list-create'),
    path('comments/<slug:slug>/', CommentView.as_view(), name='comment-detail-update-destroy-retrieve'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
