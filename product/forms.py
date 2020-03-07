from django import forms
from .models import Product

class ProductFrom(forms.ModelForm):
    name = forms.CharField(max_length=225)
    price = forms.IntegerField()
    cat_id = forms.IntegerField()
    image = forms.ImageField()

    class Meta:
        model = Product 
        fields = ['name','price','cat_id','image']
