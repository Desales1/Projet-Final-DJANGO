from django.urls import path
from . import views 

app_name="myapp"

urlpatterns = [
   
path('', views.index, name="index4" ),
path('about-us', views.about_us, name='about_us'),
path('contact-us/', views.contact_us, name='contact-us'),
path('category', views.category, name='category'),
path('my-account', views.my_account, name='my-account'),
path('checkout_page', views.checkout_page, name='checkout_page'),
path('product_grid', views.product_grid, name='product_grid'),
path('cart-page', views.cart_page, name='cart_page'),
path('blog_list', views.blog_list, name='blog_list'),
path('blog_details', views.blog_details, name='blog_details'),
path('order_confirmation', views.contact_us, name='order-confirmation'),
path('product_details', views.product_details, name='product_details'),
path('Register', views.RegisterView, name='register'),
 path('login', views.login, name='login'),
path('logout', views.deconnexion, name='deconnexion'),



    
]