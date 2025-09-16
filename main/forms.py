from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["title", "price", "description", "category", "thumbnail", "is_featured"]