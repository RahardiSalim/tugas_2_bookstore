from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()

    # Additional Attributes
    author = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    condition = models.CharField(max_length=50)
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)

    def __str__(self):
        return self.title
