from django.contrib import admin
from .models import Category, Group, Product, Image, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category')
    search_fields = ('title', 'category__title')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'discounted_price', 'group')
    search_fields = ('name', 'group__title')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('group', 'price', 'discount')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'is_primary')
    list_filter = ('is_primary', 'product__name')
    search_fields = ('product__name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating')
    search_fields = ('product__name', 'rating')
    list_filter = ('product', 'rating')

