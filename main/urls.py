from django.urls import path
from main.views import show_main, login_user, logout_user, register, brand_form_view, category_form_view, edit_product, delete_product
from . import views

app_name = 'bookstore'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    
    # Brand URLs
    path('brands/create/', views.create_brand, name='create_brand'),
    
    # Category URLs
    path('categories/create/', views.create_category, name='create_category'), 

    path('brand-form/', brand_form_view, name='brand_form'),
    path('category-form/', category_form_view, name='category_form'),
    
    # Product URLs
    path('products/create/', views.create_product, name='create_product'),
    path('edit-product/<uuid:id>/', edit_product, name='edit_product'),
    path('delete-product/<uuid:id>/', delete_product, name='delete_product'),
    path('products/card/<uuid:id>/', views.product_card, name='product_card'),
    
    # AJAX Views for products
    path('products/json/', views.product_list_json, name='product_list_json'),  # AJAX GET
    path('products/create-ajax/', views.create_product_ajax, name='create_product_ajax'),  # AJAX POST


    # Customer URLs
    path('customers/create/', views.create_customer, name='create_customer'), 

    # Order URLs
    path('orders/create/', views.create_order, name='create_order'), 
    
    # Order Item URLs
    path('order-items/create/', views.create_order_item, name='create_order_item'),

    # Review URLs
    path('reviews/create/', views.create_review, name='create_review'),

    # Uncomment JSON/XML views if necessary
    path('products/json/', views.product_list_json, name='product_list_json'),        # JSON for all products
    path('products/xml/', views.product_list_xml, name='product_list_xml'),           # XML for all products
    # path('products/json/<uuid:id>/', views.product_detail_json, name='product_detail_json'),  # JSON for specific product
    # path('products/xml/<uuid:id>/', views.product_detail_xml, name='product_detail_xml'),    # XML for specific product
]
