from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    weight = models.BigIntegerField(default=0)
    price = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

