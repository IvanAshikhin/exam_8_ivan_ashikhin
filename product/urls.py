from django.urls import path
from product.views.base import IndexView
from product.views.product import ProductDetail, ProductAddView, ProductUpdateView, ProductDeleteView
from product.views.reviews import create_review, ReviewUpdateView

urlpatterns = [
    path("", IndexView.as_view(), name="index_page"),
    path('products/<int:pk>', ProductDetail.as_view(), name='details'),
    path('products/add/', ProductAddView.as_view(), name="add_product"),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='delete_product'),
    path('products/<int:pk>/review', create_review, name='create_review'),
    path('products/<int:pk>/review/update', ReviewUpdateView.as_view(), name='review_update')
]
