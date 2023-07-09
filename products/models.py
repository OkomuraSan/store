from django.db import models

class prodCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField( null=True, blank=True)
    countProduct = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class prod(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products_images")
    category = models.ForeignKey(to=prodCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"Название: {self.name} | Категория: {self.category.name}"
