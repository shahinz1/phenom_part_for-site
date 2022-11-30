from urllib import request
from django.shortcuts import render
from ecommerce.drf.serializer import (
    CategorySerializer,
    ProductInventorySerializer,
    ProductSerializer,
    CollectionSerializer,
)
from ecommerce.inventory.models import Category, Product, ProductInventory
from rest_framework.response import Response
from rest_framework.views import APIView


class CategoryList(APIView):
    """
    Return list of all categories
    """

    def get(self, request):
        queryset = Category.objects.all()[:8]
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
class CollectionList(APIView):
    """
    Return all collection
    """
    def get(self, request):
        queryset = Product.objects.all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    
class ProductList(APIView):
    """
    Return list of all products 
    """
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    

class ProductByCategory(APIView):
    """
    Return product by category
    """

    def get(self, request, query=None):
        queryset = Product.objects.filter(category__slug=query)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)



class ProductInventoryByWebId(APIView):
    """
    Return Sub Product by WebId
    """

    def get(self, request, query=None):
        queryset = ProductInventory.objects.filter(product__id=query)
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)

class ProductInventoryByWebSlug(APIView):
    """
    Return Sub Product by Slug
    """

    def get(self, request, query=None):
        queryset = ProductInventory.objects.filter(product__slug=query)
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)

class ProductInventoryById(APIView):
    """
    Return Sub Product by WebId
    """

    def get(self, request, query=None):
        queryset = ProductInventory.objects.filter(product__id=query)
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)
