from django.db import models
from django.contrib.auth.models import User
import uuid

# Brand Model
class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# Category Model
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', blank=True)
    sku = models.CharField(max_length=100, unique=True) 
    stock_quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

# Customer Model
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Order Model
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order {self.id} by {self.customer}'

# Order Item Model
class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity = models.IntegerField()
    price_at_order = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'  

# Review Model
class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.customer} on {self.product.name}' 