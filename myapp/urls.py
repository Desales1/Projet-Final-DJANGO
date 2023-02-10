from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

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
path("dashboard/", views.index1, name="dashboard"),
path("charts/", views.charts, name="charts"),
path("widgets/", views.widgets, name="widgets"),
path("tables/", views.tables, name="tables"),
path("grid/", views.grid, name="grid"),
path("form-basic/", views.form_basic, name="form-basic"),
path("form-wizard/", views.form_wizard, name="form-wizard"),
path("buttons/", views.buttons, name="buttons"),
path("icon-material/", views.icon_material, name="icon-material"),
path("icon-fontawesome/", views.icon_fontawesome, name="icon-fontawesome"),
path("elements/", views.elements, name="elements"),
path("gallery/", views.gallery, name="gallery"),
path("invoice/", views.invoice, name="invoice"),
path("chat/", views.chat, name="chat"),
]

