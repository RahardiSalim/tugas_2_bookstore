from django import forms
from .models import Brand, Category, Product, Customer, Order, OrderItem, Review
from django.utils.html import strip_tags

# Brand Form
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description', 'website']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'name': 'Brand Name',
            'website': 'Website (Optional)',
        }

        def clean_name(self):
            name = self.cleaned_data['name']
            return strip_tags(name)

        def clean_description(self):
            description = self.cleaned_data['description']
            return strip_tags(description)

# Category Form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Category Name',
        }


    def clean_name(self):
        name = self.cleaned_data['name']
        return strip_tags(name)

# Product Form (formerly Book Form)
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'brand', 'category', 'sku', 'stock_quantity', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'category': forms.SelectMultiple(attrs={'class': 'select2-multiple'}),  # Multi-select dropdown for categories
            'brand': forms.Select(attrs={'class': 'select2-single'}),  # Single-select dropdown for brand
        }
        labels = {
            'name': 'Product Name',
            'price': 'Price ($)',
            'description': 'Description',
            'sku': 'Stock Keeping Unit (SKU)',
            'stock_quantity': 'Stock Quantity',
            'image': 'Product Image',
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data['description']
        return strip_tags(description)

    def clean_sku(self):
        sku = self.cleaned_data['sku']
        return strip_tags(sku)

    def clean_stock_quantity(self):
        stock_quantity = self.cleaned_data['stock_quantity']
        if stock_quantity < 0:
            raise forms.ValidationError("Stock quantity cannot be negative.")
        return stock_quantity

# Customer Form
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'address': 'Shipping Address',
        }

# Order Form
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'total_amount']
        widgets = {
            'customer': forms.Select(attrs={'class': 'select2-single'}),  # Dropdown for selecting a customer
        }
        labels = {
            'total_amount': 'Total Amount ($)',
        }

# Order Item Form
class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'price_at_order']
        widgets = {
            'order': forms.Select(attrs={'class': 'select2-single'}),  # Dropdown for selecting an order
            'product': forms.Select(attrs={'class': 'select2-single'}),  # Dropdown for selecting a product
        }
        labels = {
            'quantity': 'Quantity Ordered',
            'price_at_order': 'Price at Order ($)',
        }

# Review Form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'customer', 'rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),  # Limit rating between 1 and 5
        }
        labels = {
            'rating': 'Rating (1-5)',
            'comment': 'Your Review',
        }
