from django import forms
from .models import Brand, Category, Product, Customer, Order, OrderItem, Review

# Brand Form
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description', 'website']

# Category Form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

# Product Form (formerly Book Form)
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'brand', 'category', 'sku', 'stock_quantity', 'image']
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
        }

# Customer Form
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']

# Order Form
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'total_amount']

# Order Item Form
class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'price_at_order'] 

# Review Form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'customer', 'rating', 'comment']
