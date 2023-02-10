from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from myapp.models import*
from .forms import ContactForm
from django.contrib import messages
  
def index(request):
	articles = Article.objects.all()

	datas = {
		articles:"articles"
	}
	return render(request, 'index4.html', datas)

def about_us(request):
    datas = {}
    return render(request, 'about_us.html', datas)




def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact-us.html', context)



def product_details(request):
	context = {}
	return render(request, 'product_details.html', context)

def category(request):
	category = Categorie.object.filter(statut = True)
	context = {
		'category': Categorie
	}
	return render(request, 'category.html', context)

def blog_list(request):
	context = {}
	return render(request, 'blog_list.html', context)

def blog_details(request):
	context = {}
	return render(request, 'blog_details.html', context)

def cart_page(request):
	context = {}
	return render(request, 'cart_page.html', context)

def checkout_page(request):
	context = {}
	return render(request, 'checkout_page.html', context)

def order_confirmation(request):
	context = {}
	return render(request, 'order-confirmation.html', context)

def product_grid(request):
	context = {}
	return render(request, 'product_grid.html', context)

def my_account(request):
	context = {}
	return render(request, 'my-account.html', context)

def index1(request):
	context = {}
	return render(request, 'dashboard/dashboard.html', context)


def charts(request):
    return render(request, 'dashboard/charts.html')


def widgets(request):
    return render(request, 'dashboard/widgets.html')




def tables(request):
    return render(request, "dashboard/tables.html")




def grid(request):
    return render(request, "dashboard/grid.html")




def form_basic(request):
    return render(request, "dashboard/form_basic.html")




def form_wizard(request):
    return render(request, "dashboard/form_wizard.html")




def buttons(request):
    return render(request, "dashboard/buttons.html")




def icon_material(request):
    return render(request, "dashboard/icon-material.html")




def icon_fontawesome(request):
    return render(request, "dashboard/icon-fontawesome.html")




def elements(request):
    return render(request, "dashboard/elements.html")




def gallery(request):
    return render(request, "dashboard/gallery.html")





def invoice(request):
    return render(request, "dashboard/invoice.html")



def chat(request):
    return render(request, "dashboard/chat.html")
