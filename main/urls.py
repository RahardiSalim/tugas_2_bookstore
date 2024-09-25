from django.urls import path
from main.views import show_main, login_user, logout_user, register, brand_form_view, category_form_view
from . import views

app_name = 'bookstore'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    
    # Brand URLs
    path('brands/', views.brand_list, name='brand_list'), 
    path('brands/create/', views.create_brand, name='create_brand'),
    
    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.create_category, name='create_category'), 

    path('brand-form/', brand_form_view, name='brand_form'),
    path('category-form/', category_form_view, name='category_form'),
    
    # Product URLs
    path('products/', views.product_list, name='product_list'), 
    path('products/create/', views.create_product, name='create_product'),
    
    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'), 
    path('customers/create/', views.create_customer, name='create_customer'), 

    # Order URLs
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.create_order, name='create_order'), 
    
    # Order Item URLs
    path('order-items/', views.order_item_list, name='order_item_list'),  
    path('order-items/create/', views.create_order_item, name='create_order_item'),

    # Review URLs
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/create/', views.create_review, name='create_review'),

    # Uncomment JSON/XML views if necessary
    # path('products/json/', views.product_list_json, name='product_list_json'),        # JSON for all products
    # path('products/xml/', views.product_list_xml, name='product_list_xml'),           # XML for all products
    # path('products/json/<uuid:id>/', views.product_detail_json, name='product_detail_json'),  # JSON for specific product
    # path('products/xml/<uuid:id>/', views.product_detail_xml, name='product_detail_xml'),    # XML for specific product
]
