from django import forms

from product.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'image']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Find')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']
        labels = {
            'review_text': 'Your review',
            'rating': 'Your rating',
        }

