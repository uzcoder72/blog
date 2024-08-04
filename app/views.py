from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import *
from rest_framework.permissions import AllowAny

# Create your views here.
# class BooklistApiView(APIView):
#     permission_classes = [AllowAny]
#
#     def get(self, request):
#         book_data=[
#             'name': book.name,
#             'description': book.description,
#
#         ]
class Category_list(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        categories = [category.title for category in Category.objects.all()]
        return Response(categories)