from django.db import models

# Create your models here.


class Category(models.Model):

    # this will fix spelling issue and make it plural
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    # null in DB and blank in form, because each product requires a name,
    # description and a price, but null and blank will be optional
    # (that goes for all null and blank).
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # string method will return products name
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    # each product has sku, name and description
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    # they also have decimal field for price and rating
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    # and img url and img field
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
