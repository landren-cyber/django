from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='categories/', blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name="children", on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        unique_together = ('slug', 'parent',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('test_app:product_list_by_category',
                        args=[self.slug])

    def get_sub_categories(self):
        return Category.object.filter(parent=self)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    #image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField()
    product_information = models.TextField(blank=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('test_app:product_detail',
                    args=[self.id, self.slug])

    def get_title_image(self):
        if ProductImage.objects.filter(product=self).count() > 0:
            return ProductImage.objects.filter(product=self)[0]

    def get_images(self):
        return ProductImage.objects.filter(product=self)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
