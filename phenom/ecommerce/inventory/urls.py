
from django.urls import path
from ecommerce.inventory import views

app_name = 'inventory'

urlpatterns = [
    path("", views.home),
    path("about-us" , views.AboutUs),
    path("<slug:collection>/", views.Landing ,name="Landing" ),
    # path("categories/", views.category),
    path("x/<slug:slug>", views.singleProduct, name="single_product"),
    path("products/<slug:category>/", views.multiproduct),
    # path("categories/", views.category),
    # path("product-by-category/<slug:category>/", views.product_by_category, name="product_by_category"),
    # path("<slug:slug>", views.product_detail, name="product_detail"),
]

