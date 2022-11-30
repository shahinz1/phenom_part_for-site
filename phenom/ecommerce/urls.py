from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from ecommerce.drf.views import (
    CategoryList,
    ProductList,
    ProductByCategory,
    ProductInventoryById,
    ProductInventoryByWebSlug
)
from ecommerce.search.views import SearchProductInventory

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/inventory/category/all/", CategoryList.as_view()),
    # path(
    #     "category/<str:query>/",
    #     ProductByCategory.as_view()),
        #  TemplateView.as_view(template_name="multiProduct.html")),
    # path("api/inventory/<int:query>/", ProductInventoryById.as_view()),
    # path("api/products/<str:query>/", ProductInventoryByWebSlug.as_view()),
    path("<slug:collection>/", ProductList.as_view()),
    # path("api/search/<str:query>/", SearchProductInventory.as_view()),
    path("", include("ecommerce.inventory.urls", namespace='inventory')),
    path("cart/" , include('ecommerce.basket.urls', namespace='basket')),
 ]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

