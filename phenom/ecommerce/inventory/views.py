from django.shortcuts import render
from ecommerce.inventory import models
from django.contrib.postgres.aggregates import ArrayAgg 
from django.db.models import Count
from django.contrib.sessions.models import Session


# def Landing (request,category):
    
#     y = models.Product.objects.filter(category__name=category).values(
#          "id","description", "name", "slug", "created_at", "category__name", "product__store_price", "product__media__img_url"  )

#     return render (request , "landing.html", {"data": y})

def Landing (request,collection):
    
    y = models.Category.objects.filter(name=collection).values(
         "id","name", "slug" )

    return render (request , "landing.html", {"data": y})

def multiproduct (request, category):
    y = models.Product.objects.filter(category__name=category).values(
         "id", "name", "slug")

    return render (request, 'multiProduct.html' , {"data": y})

def AboutUs (request, collection):
    y = models.Category.objects.filter(name=collection).values(
         "id", "name", "slug")
    return render (request, "about us.html", {'data': y})

def home(request):
    
    data = models.Collection.objects.all
    
    return render(request, "index.html" , {"data": data})

def category(request):

    data = models.Category.objects.all()

    return render(request, "categories.html", {"data": data})


def product_by_category(request, category):

    # x = models.Product.objects.filter(category__name="fashion")
    # print(models.Product.objects.filter(category__name="fashion").explain(verbose=True, analyze=True))

    y = models.Product.objects.filter(category__name=category).values(
         "id", "name", "slug", "created_at", "category__name", "product__store_price","description" , "media__img_url" )

    # data = serializers.serialize("json", x, indent=4)

    return render(request, "product_by_category.html", {"data": y})


def singleProduct(request, slug):
    
    filter_arguments = []
    
    if request.GET:
        for value in request.GET.values():
            filter_arguments.append(value)
    
        product = models.ProductInventory.objects.filter(product__slug=slug).filter(attribute_values__attribute_value__in=filter_arguments
            ).annotate(num_tags=Count('attribute_values')).filter(num_tags=len(filter_arguments)).values("id", 
            "product__name", "product__description","web_id", "sku" , "store_price", "media__img_url" ,"product_inventory__units").annotate(field_a =ArrayAgg(
                "attribute_values__attribute_value")).get()
            
    else:
         
        product = models.ProductInventory.objects.filter(product__slug=slug).filter(is_default=True).values("id", 
            "product__name", "product__description", "sku" , "store_price", "weight" ,"media__img_url", "product_inventory__units").annotate(field_a =ArrayAgg(
                "attribute_values__attribute_value", )).get()
        
        
    y = models.ProductInventory.objects.filter(product__slug=slug).distinct().values(
        "attribute_values__product_attribute__name", "attribute_values__attribute_value")
    
    z = models.ProductTypeAttribute.objects.filter(product_type__product_type__product__slug= slug).values("product_attribute__name").distinct()

    return render(request , "singleProduct.html", {"product": product , "y": y ,"z": z })
    

