from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import Product as Book, Author, Publisher, Category, Customer, Order, OrderItem, Review
from .forms import AuthorForm, PublisherForm, CategoryForm, ProductForm, CustomerForm, OrderForm, OrderItemForm, ReviewForm

# View to display all books
def show_main(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, "main.html", context)

# View for creating a new Author
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookstore:author_list')  
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})

# View for creating a new Publisher
def create_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookstore:publisher_list') 
    else:
        form = PublisherForm()
    return render(request, 'publisher_form.html', {'form': form})

# View for creating a new Category
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookstore:category_list') 
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

# View for creating a new Product (Book)
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('bookstore:product_list') 
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

# View for creating a new Customer
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookstore:customer_list') 
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

# View for creating a new Order
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookstore:order_list') 
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})

# View for creating a new Order Item
def create_order_item(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookstore:order_item_list') 
    else:
        form = OrderItemForm()
    return render(request, 'order_item_form.html', {'form': form})

# View for creating a new Review
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookstore:review_list') 
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form})



# View for listing all authors
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

# View for listing all publishers
def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publishers': publishers})

# View for listing all categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

# View for listing all products (books)
def product_list(request):
    products = Book.objects.all() 
    return render(request, 'product_list.html', {'products': products})

# View for listing all customers
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

# View for listing all orders
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

# View for listing all order items
def order_item_list(request):
    order_items = OrderItem.objects.all()
    return render(request, 'order_item_list.html', {'order_items': order_items})

# View for listing all reviews
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})





# JSON view for all books
def book_list_json(request):
    books = Book.objects.all()
    data = list(books.values())  # Convert QuerySet to list of dictionaries
    return JsonResponse(data, safe=False)

# XML view for all books
def book_list_xml(request):
    books = Book.objects.all()
    data = serializers.serialize("xml", books)
    return HttpResponse(data, content_type="application/xml")

# JSON view for a specific book by ID
def book_detail_json(request, id):
    book = get_object_or_404(Book, id=id)
    data = {
        "title": book.title,
        "price": book.price,
        "description": book.description,
        "author": str(book.author),
        "publisher": str(book.publisher),
        "category": str(book.category),
        "isbn": book.isbn,
        "stock_quantity": book.stock_quantity,
        "publication_year": book.publication_year,
    }
    return JsonResponse(data)

# XML view for a specific book by ID
def book_detail_xml(request, id):
    book = get_object_or_404(Book, id=id)
    data = serializers.serialize("xml", [book])
    return HttpResponse(data, content_type="application/xml")
