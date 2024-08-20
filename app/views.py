from rest_framework import generics, mixins
from .models import Category, Group, Product, Comment
from .serializers import CategorySerializer, GroupSerializer, ProductSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from app.serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .permissions import CustomPermissions
from rest_framework.pagination import PageNumberPagination
class ListCreateRetrieveUpdateDestroyAPIView(mixins.ListModelMixin,
                                             mixins.CreateModelMixin,
                                             mixins.RetrieveModelMixin,
                                             mixins.UpdateModelMixin,
                                             mixins.DestroyModelMixin,
                                             generics.GenericAPIView):
    """
    A view that provides list, create, retrieve, update, and destroy actions.
    """
    queryset = None
    serializer_class = None
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        if 'slug' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CategoryView(ListCreateRetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class GroupView(ListCreateRetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProductPagination(PageNumberPagination):
    page_size = 1
class ProductView(ListCreateRetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().select_related('group__category').prefetch_related('is_liked', 'attributes', 'comment_set')
    serializer_class = ProductSerializer
    permission_classes = [CustomPermissions]
    pagination_class = ProductPagination




class CommentView(ListCreateRetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# Custom TokenObtainPairView to return extra data
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    # If you need to customize the returned token, do it here



class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=204)
        except Exception as e:
            return Response(status=400)
