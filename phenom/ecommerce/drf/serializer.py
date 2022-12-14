from ecommerce.inventory.models import (
    Brand,
    Category,
    Media,
    Product,
    ProductAttributeValue,
    ProductAttributeValues,
    ProductInventory,
    ProductType,
)
from rest_framework import serializers

class CollectionSerializer(serializers.ModelSerializer):
    categoryImg = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ["name", "CollImg", "slug"]
        read_only = True
        
    def get_categoryImg(self, obj):
        return obj.categoryImg.url
class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        depth = 4
        exclude = ["id"]
        read_only = True


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]
        read_only = True


class CategorySerializer(serializers.ModelSerializer):
    categoryImg = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ["name", "categoryImg", "slug", "is_active"]
        read_only = True
        
    def get_categoryImg(self, obj):
        return obj.categoryImg.url

class ProductMediaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["img_url", "alt_text"]
        read_only = True
        editable = False

    def get_img_url(self, obj):
        return obj.img_url.url

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", 'name', 'slug', "web_id",  'description']
        # depth = 3
        # exclude = ["id"]
        read_only = True
        editable = False
        
class ProductInventorySerializer(serializers.ModelSerializer):

    product = ProductSerializer(many=False, read_only=True)
    media = ProductMediaSerializer(many=True, read_only=True)
    brand = BrandSerializer(read_only=True)
    attributes = ProductAttributeValueSerializer(
        source="attribute_values", many=True, read_only=True
    )

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "brand",
            "product",
            "is_on_sale",
            "weight",
            "media",
            "attributes",
            "product_type",
        ]
        read_only = True

        
class ProductInventorySearchSerializer(serializers.ModelSerializer):

    product = ProductSerializer(many=False, read_only=True)
    brand = BrandSerializer(many=False, read_only=True)

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "product",
            "brand",
        ]
