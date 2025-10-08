from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["title", "price", "description", "category", "thumbnail", "is_featured"]

        def clean_title(self):
            title = self.cleaned_data["title"]
            return strip_tags(title)

        def clean_description(self):
            description = self.cleaned_data["description"]
            return strip_tags(description)