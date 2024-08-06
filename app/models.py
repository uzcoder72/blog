from typing import Any
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    title = models.CharField(max_length=70, unique=True)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to='media/images/category/')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'

class Group(BaseModel):
    title = models.CharField(max_length=90, unique=True)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to='media/images/group/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Product(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.IntegerField(default=0)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_liked = models.ManyToManyField(User, related_name='liked_products', blank=True)

    @property
    def discounted_price(self) -> Any:
        if self.discount > 0:
            return self.price * (1 - (self.discount / 100.0))
        return self.price

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

class Image(BaseModel):
    image = models.ImageField(upload_to='media/images/products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name

class Comment(BaseModel):
    class Rating(models.IntegerChoices):
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    message = models.TextField()
    rating = models.IntegerField(choices=Rating.choices, default=Rating.One.value)
    file = models.FileField(upload_to='comments/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


