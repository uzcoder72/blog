from rest_framework import serializers
from app.models import Category, Group, Product, Comment
from rest_framework import serializers
from app.models import Product, Comment
from django.db.models import Avg
from app import models
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'




class ProductSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()
    comment_avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'price', 'discount', 'discounted_price',
                  'group', 'is_liked', 'comment_avg_rating', 'image']  # Include image field

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return user.is_authenticated and user in obj.is_liked.all()

    def get_comment_avg_rating(self, obj):
        average_rating = obj.comment_set.aggregate(Avg('rating'))['rating__avg']
        return round(average_rating, 1) if average_rating else None





class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

