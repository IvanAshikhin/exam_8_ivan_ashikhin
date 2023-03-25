from django.contrib.auth.models import User
from django.db import models

CATEGORY = (('Laptop', 'laptop'),
            ('Headphones', 'Headphones'),
            ('Mouses', 'Mouses'),
            ('Keyboards', 'Keyboards'),
            ('Other', 'Other'))


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name', blank=True, null=False)
    category = models.CharField(max_length=500, null=False, blank=False, verbose_name='Category', choices=CATEGORY)
    description = models.TextField(max_length=2000, null=True, blank=False, verbose_name='Description')
    image = models.CharField(max_length=10000, null=True, verbose_name='Image',
                             default="https://tastystore.ru/design/no-photo.png?design=THEMENAME")

    def __str__(self):
        return f'{self.name} - {self.description}'


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    review_text = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Review Text')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name='Rating')

    def __str__(self):
        return f'{self.author} - {self.product} - {self.rating}'
