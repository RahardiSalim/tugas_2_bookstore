from django import forms
from .models import Author, Publisher, Category, Product, Customer, Order, OrderItem, Review

# Author Form
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']

# Publisher Form
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'website']

# Category Form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

# Product (Book) Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'author', 'publisher', 'category', 'isbn', 'stock_quantity', 'publication_year', 'image']
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
        fields = ['order', 'book', 'quantity', 'price_at_order']

# Review Form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'customer', 'rating', 'comment']
