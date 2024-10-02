from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import Product, Brand, Category, Customer, Order, OrderItem, Review
from .forms import BrandForm, CategoryForm, ProductForm, CustomerForm, OrderForm, OrderItemForm, ReviewForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# View to display all products
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'name': request.user.username,
    }
    return render(request, "main.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('bookstore:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("bookstore:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Your email or password is incorrect.')
            return redirect('bookstore:login')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('bookstore:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def create_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save()
            return JsonResponse({'success': True, 'brand': brand.name, 'id': brand.id})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = BrandForm()
        html = render_to_string('brand_form_partial.html', {'form': form}, request=request)
        return JsonResponse({'html': html})

@login_required(login_url='/login')
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return JsonResponse({'success': True, 'category': category.name, 'id': category.id})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = CategoryForm()
        html = render_to_string('category_form_partial.html', {'form': form}, request=request)
        return JsonResponse({'html': html})

@login_required(login_url='/login')
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES) 
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            form.save_m2m()  # Save the many-to-many field
            return redirect('bookstore:show_main') 
    else:
        form = ProductForm()

    # Fetch brands and categories for the dropdowns
    brands = Brand.objects.all()
    categories = Category.objects.all()

    return render(request, 'product_form.html', {'form': form, 'brands': brands, 'categories': categories})

@login_required(login_url='/login')
def edit_product(request, id):
    # Get the product entry based on id
    product = get_object_or_404(Product, pk=id)

    # Set the product as an instance of the form, pre-populating the form
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Save the form and redirect to the main product page
        form.save()
        return HttpResponseRedirect(reverse('bookstore:show_main'))

    context = {'form': form, 'product': product}
    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('bookstore:show_main'))

def brand_form_view(request):
    form = BrandForm()
    html = render_to_string('brand_form_partial.html', {'form': form})
    return JsonResponse({'html': html})

def category_form_view(request):
    form = CategoryForm()
    html = render_to_string('category_form_partial.html', {'form': form})
    return JsonResponse({'html': html})


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

# View for listing all brands
def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'brand_list.html', {'brands': brands})

# View for listing all categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

# View for listing all products
def product_list(request):
    products = Product.objects.all() 
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

# # JSON view for all products
# def product_list_json(request):
#     products = Product.objects.all()
#     data = list(products.values())  # Convert QuerySet to list of dictionaries
#     return JsonResponse(data, safe=False)

# # XML view for all products
# def product_list_xml(request):
#     products = Product.objects.all()
#     data = serializers.serialize("xml", products)
#     return HttpResponse(data, content_type="application/xml")

# # JSON view for a specific product by ID
# def product_detail_json(request, id):
#     product = get_object_or_404(Product, id=id)
#     data = {
#         "name": product.name,
#         "price": product.price,
#         "description": product.description,
#         "brand": str(product.brand),
#         "category": [str(cat) for cat in product.category.all()],
#         "sku": product.sku,
#         "stock_quantity": product.stock_quantity,
#     }
#     return JsonResponse(data)

# # XML view for a specific product by ID
# def product_detail_xml(request, id):
#     product = get_object_or_404(Product, id=id)
#     data = serializers.serialize("xml", [product])
#     return HttpResponse(data, content_type="application/xml")