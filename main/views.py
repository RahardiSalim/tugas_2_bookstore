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
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# View to display all products
@login_required(login_url='/login')
def show_main(request):
    brands = Brand.objects.all()  # Fetch all brands
    categories = Category.objects.all()  # Fetch all categories
    context = {
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'name': request.user.username,
        'brands': brands,  # Pass brands to the template
        'categories': categories,  # Pass categories to the template
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

# AJAX POST: Create a product via AJAX
@csrf_exempt
@require_POST
def create_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    brand_id = strip_tags(request.POST.get("brand"))
    sku = strip_tags(request.POST.get("sku"))
    stock_quantity = strip_tags(request.POST.get("stock_quantity"))
    user = request.user

    # Get the Brand instance
    brand = Brand.objects.get(pk=brand_id) if brand_id else None

    new_product = Product(
        name=name,
        price=price,
        description=description,
        brand=brand,
        sku=sku,
        stock_quantity=stock_quantity,
        user=user
    )
    new_product.save()

    # Handle categories (assuming it's a many-to-many field)
    category_ids = request.POST.getlist("category")
    for cat_id in category_ids:
        category = Category.objects.get(pk=cat_id)
        new_product.category.add(category)

    # Handle image upload
    if 'image' in request.FILES:
        new_product.image = request.FILES['image']
        new_product.save()

    return HttpResponse(b"CREATED", status=201)

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
def product_card(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'card_product.html', {'product': product})

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

@login_required(login_url='/login')
def product_list_json(request):
    """
    Returns a JSON response with all products for the logged-in user.
    """
    products = Product.objects.filter(user=request.user).select_related('brand').prefetch_related('category')
    data = [
        {
            "id": str(product.id),
            "name": product.name,
            "price": float(product.price),
            "description": product.description if product.description else "No description available",
            "brand": {
                "id": str(product.brand.id),
                "name": product.brand.name
            },
            "categories": [{"id": str(cat.id), "name": cat.name} for cat in product.category.all()],
            "sku": product.sku,
            "stock_quantity": product.stock_quantity,
            "image_url": product.image.url if product.image else ""
        }
        for product in products
    ]
    return JsonResponse(data, safe=False)

def brand_list_json(request):
    """
    Returns a JSON response with all brands.
    """
    brands = Brand.objects.all()
    data = [{"id": str(brand.id), "name": brand.name, "description": brand.description, "website": brand.website} for brand in brands]
    return JsonResponse(data, safe=False)

def category_list_json(request):
    """
    Returns a JSON response with all categories.
    """
    categories = Category.objects.all()
    data = [{"id": str(category.id), "name": category.name} for category in categories]
    return JsonResponse(data, safe=False)


@login_required(login_url='/login')
def product_list_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# JSON view for a specific product by ID
def product_detail_json(request, id):
    product = get_object_or_404(Product, id=id)
    data = {
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "brand": str(product.brand),
        "category": [str(cat) for cat in product.category.all()],
        "sku": product.sku,
        "stock_quantity": product.stock_quantity,
    }
    return JsonResponse(data)

# XML view for a specific product by ID
def product_detail_xml(request, id):
    product = get_object_or_404(Product, id=id)
    data = serializers.serialize("xml", [product])
    return HttpResponse(data, content_type="application/xml")

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Get or create brand
            brand, _ = Brand.objects.get_or_create(
                id=data["brand"]["id"],
                defaults={
                    "name": data["brand"]["name"],
                    "description": data.get("brand", {}).get("description"),
                    "website": data.get("brand", {}).get("website")
                }
            )

            # Get or create categories
            categories = []
            for cat_data in data["categories"]:
                category, _ = Category.objects.get_or_create(
                    id=cat_data["id"],
                    defaults={"name": cat_data["name"]}
                )
                categories.append(category)

            # Create the product
            new_product = Product.objects.create(
                id=data["id"],
                user_id=request.user.id if request.user.is_authenticated else None,
                name=data["name"],
                price=float(data["price"]),
                description=data.get("description"),
                brand=brand,
                sku=data["sku"],
                stock_quantity=int(data["stock_quantity"]),
            )

            # Add categories to the product
            new_product.category.set(categories)
            new_product.save()

            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
