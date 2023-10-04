from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):  # create a modle 
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', ) # order the categories Alphabetcaly
        verbose_name_plural = 'Categories'  # Corect the model name

    def __str__(self):
        return self.name    # show the value of the items on the admin site
    

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='items_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

