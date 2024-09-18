from django.urls import path
from main.views import show_main
from . import views

app_name = 'bookstore'

urlpatterns = [
    path('', show_main, name='show_main'),

    path('authors/', views.author_list, name='author_list'),
    path('authors/create/', views.create_author, name='create_author'),  
    
    path('publishers/', views.publisher_list, name='publisher_list'), 
    path('publishers/create/', views.create_publisher, name='create_publisher'),  
    
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.create_category, name='create_category'), 
    
    path('products/', views.product_list, name='product_list'), 
    path('products/create/', views.create_product, name='create_product'),
    
    path('customers/', views.customer_list, name='customer_list'), 
    path('customers/create/', views.create_customer, name='create_customer'), 

    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.create_order, name='create_order'), 
    
    path('order-items/', views.order_item_list, name='order_item_list'),  
    path('order-items/create/', views.create_order_item, name='create_order_item'),

    path('reviews/', views.review_list, name='review_list'),
    path('reviews/create/', views.create_review, name='create_review'),

    
    path('books/json/', views.book_list_json, name='book_list_json'),        # JSON for all books
    path('books/xml/', views.book_list_xml, name='book_list_xml'),           # XML for all books
    path('books/json/<uuid:id>/', views.book_detail_json, name='book_detail_json'),  # JSON for specific book
    path('books/xml/<uuid:id>/', views.book_detail_xml, name='book_detail_xml'),    # XML for specific book
]