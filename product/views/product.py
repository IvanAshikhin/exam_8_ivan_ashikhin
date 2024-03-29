from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Avg
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from product.forms import ProductForm
from product.models import Product, Review


class ProductDetail(DetailView):
    template_name = 'detail.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.filter(product=self.object)
        context['reviews'] = reviews
        context['average_rating'] = reviews.aggregate(Avg('rating')).get('rating__avg', 0) or 0
        return context


class ProductAddView(UserPassesTestMixin, CreateView):
    template_name = 'add.html'
    model = Product
    context_object_name = 'product'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('details', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.has_perm('product.add_product')


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('details', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.has_perm('product.change_product')


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'confirm_delete.html'
    context_object_name = 'product'
    model = Product
    success_url = reverse_lazy('index_page')

    def test_func(self):
        return self.request.user.has_perm('product.delete_product')
