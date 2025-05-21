from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Deal(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.URLField()
    image_url = models.URLField(default='https://example.com/default-image.jpg')

    def __str__(self):
        return f"{self.product.name} - {self.store} - ${self.price}"
# Create your models here.
