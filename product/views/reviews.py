from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView
from product.forms import ReviewForm
from product.models import Product, Review


@login_required
def create_review(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.author = request.user
            review.save()
            return redirect('details', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'create_review.html', {'form': form, 'product': product})


class ReviewUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'update_review.html'
    form_class = ReviewForm
    model = Review
    context_object_name = 'review'

    def get_success_url(self):
        return reverse_lazy('index_page')

    def test_func(self):
        return self.request.user.has_perm('review.change_product') or self.request.user == self.model


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'delete_review.html'
    success_url = reverse_lazy('index_page')
    context_object_name = 'review'

    def test_func(self):
        return self.request.user.has_perm('review.delete_product') or self.request.user == self.model
