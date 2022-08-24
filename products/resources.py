from import_export import resources

from .models import Product, Category, IPAddress, Comments


class ProductsResources(resources.ModelResource):
    class Meta:
        model = Product
