from rest_framework import generics, mixins
from .models import Category, Group, Product, Image, Comment
from .serializers import CategorySerializer, GroupSerializer, ProductSerializer, ImageSerializer, CommentSerializer

class ListCreateRetrieveUpdateDestroyAPIView(mixins.ListModelMixin,
                                             mixins.CreateModelMixin,
                                             mixins.RetrieveModelMixin,
                                             mixins.UpdateModelMixin,
                                             mixins.DestroyModelMixin,
                                             generics.GenericAPIView):
    """
    A view that provides `list`, `create`, `retrieve`, `update`, and `destroy` actions.
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

class ProductView(ListCreateRetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ImageView(ListCreateRetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class CommentView(ListCreateRetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
